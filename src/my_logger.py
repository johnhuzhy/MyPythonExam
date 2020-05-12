import logging

# loggerを新規する
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# handleを新規し、ログ出力ため
logfile = './log/test.log'
fh = logging.FileHandler(logfile)
fh.setLevel(logging.DEBUG)

# handleを新規し、コンソール出力ため
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# formatterを生成する
formatter = logging.Formatter(
    "%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
formatter.datefmt = "%Y-%m-%d %a %H:%M:%S"
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# loggerはhandleに追加する
logger.addHandler(fh)
logger.addHandler(ch)


def debug(msg):
    """ logging.debug """
    logger.debug(msg)


def info(msg):
    """ logging.info """
    logger.info(msg)


def warning(msg):
    """ logging.warning """
    logger.warning(msg)


def error(msg):
    """ logging.error """
    logger.error(msg)


def critical(msg):
    """ logging.critical """
    logger.critical(msg)
