# _*_coding:utf-8_*_
"""
@Author:  Javen Yan
@File: logger.py
@Software: PyCharm
@Time :    2020/4/18 下午3:07
"""
import inspect
import os
import logging
import time
from logging.handlers import RotatingFileHandler

loggerList = dict()
logLevelHandlers = dict()
Level = logging.DEBUG
color = False

for level in [logging.DEBUG, logging.INFO, logging.WARNING, logging.FATAL, logging.ERROR]:
    logger = logging.getLogger(str(level))
    console = logging.StreamHandler()
    logger.addHandler(console)
    logger.setLevel(level)
    logger.propagate = False
    loggerList[level] = logger


def remove_handler():
    for k, v in loggerList.items():
        log = logging.getLogger(str(k))
        log.removeHandler(v)


def InitLogConfig(loglevel: int = logging.DEBUG, dev: bool = True):
    return InitLogConfigWithPrefix(loglevel, "", dev)


def InitLogConfigWithPrefix(loglevel: int = logging.DEBUG, filePrefix: str = "", dev: bool = True):
    global loggerList, logLevelHandlers, Level
    isDebug = dev
    Level = loglevel
    if not isDebug:
        if filePrefix:
            logFilePrefix = os.getcwd() + "/logfile/" + filePrefix + "_"
        else:
            logFilePrefix = os.getcwd() + "/logfile/"
        if not os.path.isdir(logFilePrefix):
            os.mkdir(logFilePrefix)
        remove_handler()
        logLevelHandlers[logging.INFO] = RotatingFileHandler(
            filename=logFilePrefix + "info.log",
            maxBytes=102400,
            backupCount=3,
            encoding='utf-8'
        )
        logLevelHandlers[logging.DEBUG] = RotatingFileHandler(
            filename=logFilePrefix + "debug.log",
            maxBytes=102400,
            backupCount=3,
            encoding='utf-8'
        )
        logLevelHandlers[logging.ERROR] = RotatingFileHandler(
            filename=logFilePrefix + "error.log",
            maxBytes=102400,
            backupCount=3,
            encoding='utf-8'
        )
        logLevelHandlers[logging.WARNING] = RotatingFileHandler(
            filename=logFilePrefix + "warn.log",
            maxBytes=102400,
            backupCount=3,
            encoding='utf-8'
        )
        logLevelHandlers[logging.FATAL] = RotatingFileHandler(
            filename=logFilePrefix + "fatal.log",
            maxBytes=102400,
            backupCount=3,
            encoding='utf-8'
        )
        for lv, handle in logLevelHandlers.items():
            temp = logging.getLogger(str(lv))
            temp.setLevel(lv)
            remove_stream(temp)
            temp.addHandler(handle)
            temp.propagate = False
            loggerList[lv] = temp


def remove_stream(log):
    new_handler = []
    for i in log.handlers:
        if not isinstance(i, logging.StreamHandler):
            new_handler.append(i)
    log.handlers = new_handler


def onTime():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())


def getLogger(lv, message):
    frame, filename, lineNo, functionName, code, unknownField = inspect.stack()[2]
    pyName = filename.split("/")[-1]
    msg = "[%s] %s [%s] %s %s:%s" % (lv, onTime(), functionName, message, pyName, lineNo)
    if color:
        colorDict = {
            "INFO": "\033[32m%s\033[0m",
            "DEBUG": "\033[37m%s\033[0m",
            "ERROR": "\033[31m%s\033[0m",
            "FATAL": "\033[36m%s\033[0m",
            "WARN": "\033[33m%s\033[0m",
        }
        return colorDict[lv] % msg
    else:
        return msg


def info(msg, *args, **kwargs):
    if Level in [logging.INFO, logging.DEBUG]:
        message = getLogger("INFO", msg)
        loggerList[logging.INFO].info(message, *args, **kwargs)


def debug(msg, *args, **kwargs):
    if Level == logging.DEBUG:
        message = getLogger("DEBUG", msg)
        loggerList[logging.DEBUG].debug(message, *args, **kwargs)


def error(msg, *args, **kwargs):
    if Level in [logging.ERROR, logging.DEBUG]:
        message = getLogger("ERROR", msg)
        loggerList[logging.ERROR].error(message, *args, **kwargs)


def fatal(msg, *args, **kwargs):
    if Level in [logging.FATAL, logging.DEBUG]:
        message = getLogger("FATAL", msg)
        loggerList[logging.FATAL].fatal(message, *args, **kwargs)


def warning(msg, *args, **kwargs):
    if Level in [logging.WARNING, logging.DEBUG]:
        message = getLogger("WARN", msg)
        loggerList[logging.WARNING].fatal(message, *args, **kwargs)
