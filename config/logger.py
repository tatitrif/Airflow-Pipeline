import logging

from config.settings import PATH_LOG

FORMAT = "%(asctime)s %(levelname)s {%(message)s} {%(pathname)s:%(lineno)d} "
DATE_FMT = "%y-%m-%d %H:%M"
# set up logging to file - see previous section for more details
logging.basicConfig(
    level=logging.DEBUG,
    format=FORMAT,
    datefmt=DATE_FMT,
    filename=f"{PATH_LOG}",
    filemode="w",
)
# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
formatter = logging.Formatter(
    FORMAT,
    datefmt=DATE_FMT,
)
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger("").addHandler(console)
