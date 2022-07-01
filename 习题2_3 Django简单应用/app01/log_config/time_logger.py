import os
import logging
import sys
from logging.handlers import TimedRotatingFileHandler
import time

LOG_PATH = "../../logs"


def create_mylogger(name="test"):
    logger = logging.getLogger(name)
    if os.path.exists(LOG_PATH):
        pass
    else:
        os.mkdir(LOG_PATH)
    # 设置日志基础级别
    logger.setLevel(logging.DEBUG)
    # 日志格式
    formatter = '%(asctime)s | %(levelname)s | %(thread)d | %(filename)s - %(funcName)s : %(message)s'

    log_formatter = logging.Formatter(formatter)
    # 控制台日志
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(log_formatter)
    # info日志文件名
    info_file_name = 'info-' + time.strftime(
        '%Y-%m-%d', time.localtime(time.time())) + '.log'
    # info日志处理器
    # filename：日志文件名
    # when：日志文件按什么维度切分。'S'-秒；'M'-分钟；'H'-小时；'D'-天；'W'-周
    #       这里需要注意，如果选择 D-天，那么这个不是严格意义上的'天'，而是从你
    #       项目启动开始，过了24小时，才会从新创建一个新的日志文件，
    #       如果项目重启，这个时间就会重置。所以这里选择'MIDNIGHT'-是指过了午夜
    #       12点，就会创建新的日志。
    # interval：是指等待多少个单位 when 的时间后，Logger会自动重建文件。
    # backupCount：是保留日志个数。默认的0是不会自动删除掉日志。
    info_handler = TimedRotatingFileHandler(filename='logs/info/' +
                                                     info_file_name,
                                            when='MIDNIGHT',
                                            interval=1,
                                            backupCount=7,
                                            encoding='utf-8')
    info_handler.setFormatter(log_formatter)
    info_handler.setLevel(logging.INFO)
    # error日志文件名
    error_file_name = 'error-' + time.strftime(
        '%Y-%m-%d', time.localtime(time.time())) + '.log'
    # 错误日志处理器
    err_handler = TimedRotatingFileHandler(filename='logs/error/' +
                                                    error_file_name,
                                           when='MIDNIGHT',
                                           interval=1,
                                           backupCount=7,
                                           encoding='utf-8')
    err_handler.setFormatter(log_formatter)
    err_handler.setLevel(logging.ERROR)
    # 添加日志处理器
    logger.addHandler(info_handler)
    logger.addHandler(err_handler)
    logger.addHandler(console_handler)
    return logger
