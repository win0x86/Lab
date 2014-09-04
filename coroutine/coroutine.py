#!/usr/bin/env python
# coding: utf-8

import time
import types
import select
import collections
from log import get_logger

log = get_logger()


class Task(object):
    def __init__(self, target):
        self.target = target
        self.sendval = None
        self.stack = []

    def run(self):
        try:
            log.d("send target:%s", self.target)
            result = self.target.send(self.sendval)
            log.d("result: %s", result)
            if isinstance(result, SystemCall):
                return result

            if isinstance(result, types.GeneratorType):
                self.stack.append(self.target)
                self.sendval = None
                self.target = result
            else:
                if not self.stack: return
                self.sendval = result
                self.target = self.stack.pop()
        except StopIteration:
            log.d("Except stack: %s", self.stack)
            if not self.stack: raise
            self.sendval = None
            self.target = self.stack.pop()


class SystemCall(object):
    def handle(self, sched, task):
        pass


class Scheduler(object):
    def __init__(self):
        self.task_queue = collections.deque()
        self.read_waiting = {}
        self.write_waiting = {}
        self.numtasks = 0

    def new(self, target):
        newtask = Task(target)
        self.schedule(newtask)
        self.numtasks += 1

    def schedule(self, task):
        self.task_queue.append(task)

    def readwait(self, task, fd):
        self.read_waiting[fd] = task

    def writewait(self, task, fd):
        self.write_waiting[fd] = task

    def mainloop(self, count=-1, timeout=None):
        while self.numtasks:
            if self.read_waiting or self.write_waiting:
                log.d("mainloop select event.")
                wait = 0 if self.task_queue else timeout
                r, w, e = select.select(self.read_waiting,
                                        self.write_waiting,
                                        [], wait)
                for fileno in r:
                    self.schedule(self.read_waiting.pop(fileno))

                for fileno in w:
                    self.schedule(self.write_waiting.pop(fileno))

            while self.task_queue:
                task = self.task_queue.popleft()
                try:
                    # time.sleep(0.2)
                    result = task.run()
                    if isinstance(result, SystemCall):
                        result.handle(self, task)
                    else:
                        self.schedule(task)
                except StopIteration:
                    self.numtasks -= 1
            else:
                log.d("numtasks: %d", self.numtasks)
                log.d("count: %d", count)
                if count > 0: count -= 1
                if count == 0: return


class ReadWait(SystemCall):
    def __init__(self, f):
        self.f = f

    def handle(self, sched, task):
        fileno = self.f.fileno()
        sched.readwait(task, fileno)


class WriteWait(SystemCall):
    def __init__(self, f):
        self.f = f

    def handle(self, sched, task):
        fileno = self.f.fileno()
        sched.writewait(task, fileno)


class NewTask(SystemCall):
    def __init__(self, target):
        self.target = target

    def handle(self, sched, task):
        log.d("new task")
        sched.new(self.target)
        sched.schedule(task)
