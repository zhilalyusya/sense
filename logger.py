import logging.handlers

FORMATTER_STRING = '%(asctime)s - %(levelname)s: %(message)s'
LOG_LVL = logging.INFO

# basic logging config
logging.basicConfig(format=FORMATTER_STRING, datefmt='%d-%m-%Y:%H:%M:%S', level=LOG_LVL)
logger = logging.getLogger()

# configure timed rotating handler to rotate log files every midnight
# trh = logging.handlers.TimedRotatingFileHandler(LOG_FILE, when='midnight', backupCount=30)
# formatter = logging.Formatter(FORMATTER_STRING)
# trh.setFormatter(formatter)
# trh.setLevel(LOG_LVL)
# logger.addHandler(trh)
LOG = logger