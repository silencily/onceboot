# -*- coding: utf-8 -*-
__author__ = 'silencily'
__all__ = ['Booter', 'Program', 'loadBooters']

import yaml
import logging
import os
import win32api

#常量
_BOOT_YAML = 'boot.yaml'
_NODE_BOOTERS = 'booters'
_NODE_NAME = 'name'
_NODE_SYMBOL = 'symbol'
_NODE_PROGRAMS = 'programs'
_NODE_PATH = 'path'
#日志logger
_logger = logging.getLogger('booters')


class Booter:
    """
    The booter bean.
    The structure is->name:string;symbol:string;programs:list(Program)
    """

    def __init__(self):
        self.name = 'Default'
        self.symbol = '0'
        self.programs = []

    def boot(self):
        """
        Boot the programs.
        """
        for program in self.programs:
            _logger.info('Booting the program:' + program.name)
            win32api.ShellExecute(0, 'open', program.path, '', '', 1)


class Program:
    """
    The program bean.
    The structure is->name:string;path:string
    """

    def __init__(self, name, path):
        self.name = name
        self.path = path


def loadBooters():
    """
    Load the booters from boot.yaml. Return the list of booters.

    The boot.yaml must exist in current work path.
    """
    #装配的启动器列表
    booterlist = [Booter()]
    cwp = os.getcwd()
    _logger.debug('current work path:' + cwp)
    stream = open(os.path.abspath(os.path.join(cwp, _BOOT_YAML)), 'r')
    content = yaml.load(stream)
    _logger.debug(content)
    booters = content.get(_NODE_BOOTERS)
    _logger.debug(booters)
    for booter in booters:
        bt = Booter()
        bt.name = booter.get(_NODE_NAME)
        bt.symbol = booter.get(_NODE_SYMBOL)
        programs = booter.get(_NODE_PROGRAMS)
        ps = []
        for program in programs:
            ps.append(Program(program.get(_NODE_NAME), program.get(_NODE_PATH)))
        bt.programs = ps
        booterlist.append(bt)

    return booterlist









