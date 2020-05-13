import logging
import datetime

# loggerを新規する
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# handleを新規し、ログ出力ため
today = datetime.date.today()
logfile = './log/'+str(today)+'.log'
fh = logging.FileHandler(logfile, encoding='utf-8')
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
