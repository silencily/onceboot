# -*- coding: utf-8 -*-
__author__ = 'silencily'
import booter.booters
import logging

if __name__ == '__main__':
    #存储所有启动器的标识键值用于检测用户输入的键值是否正确
    symbols = []
    booters = booter.booters.loadBooters()
    welcome = '===============================\n'
    for bt in booters:
        welcome += "%12s: '%s'\n" % (bt.name, bt.symbol)
        symbols.append(bt.symbol)
    welcome += '===============================\n'
    choice = raw_input(welcome + 'Please choose the once booter:')
    logging.debug("Your choice is '" + choice + "'")
    if choice not in symbols:
        #若用户输入键值不存在启动器运行默认的启动器
        logging.info('Your choice is not existed in the booters.')
        choice = ''
    for bt1 in booters:
        if bt1.symbol == choice:
            bt1.boot()
            break
    logging.info('Please wait your programs booting...')



