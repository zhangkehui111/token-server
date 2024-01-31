# @Project : token
# @Time : 2022/12/23 11:08
# @Author : Alan
# @File : logger.py

from loguru import logger
from setting import LOG_DIR

log_file = LOG_DIR / "run.log"
# 路径，每日分割时间，是否异步记录，日志是否序列化，编码格式，最长保存日志时间
logger.add(log_file, rotation='0:00', enqueue=True, serialize=False, encoding="utf-8", retention="10 days")