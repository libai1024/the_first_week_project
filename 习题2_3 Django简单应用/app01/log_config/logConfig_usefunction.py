import logging
import sys

def create_mylogger():
    # 创建一个日志器logger并设置其日志级别为DEBUG
    logger = logging.getLogger('simple_logger')
    logger.setLevel(logging.DEBUG)

    # 创建一个流处理器handler并设置其日志级别为DEBUG
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)

    # 创建一个格式器formatter并将其添加到处理器handler
    formatter = logging.Formatter("%(asctime)s - [%(levelname)s]-%(message)s")
    handler.setFormatter(formatter)
    # 为日志器logger添加上面创建的处理器handler
    logger.addHandler(handler)
    return logger

# 日志输出
if __name__ == '__main__':
    logger = create_mylogger()
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')