import logging

log_format = "%(asctime)-15s [%(process)d] [%(levelname)s] %(name)s:%(lineno)d - %(threadName)s - %(message)s"
datefmt = "[%Y-%m-%d %H:%M:%S %z]"
logging.basicConfig(level=logging.DEBUG, format=log_format, datefmt=datefmt)
