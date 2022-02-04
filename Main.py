from cmath import log
import logging
from pythonjsonlogger import jsonlogger

logger = logging.getLogger()

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)

for i in range(0, 5000):
    location = ("127.0.0.1", i)
    result_of_check = a_socket.connect_ex(location)

    if result_of_check == 0:
        logger.log("Port is open", i)
    else:
        logger.log("Port is not open", i)
