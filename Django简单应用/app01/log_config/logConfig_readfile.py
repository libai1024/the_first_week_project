
#导入 logging.config 不能用logging调用
import logging.config
import sys
# 读取日志配置文件内容
from os import path


def create_mylogger():
    log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
    logging.config.fileConfig(log_file_path)
    logger = logging.getLogger("test")
# 创建一个日志器logger
    return logger

if __name__ == '__main__':
    # 日志输出
    logger = create_mylogger()
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')