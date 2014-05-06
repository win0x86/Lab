# coding: utf-8

from common.utility import cmd
from common.base import CmdBase

CMD = "-four"


@cmd(CMD, "4", "help four")
class Four(CmdBase):
    pass
