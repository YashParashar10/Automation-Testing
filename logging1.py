import logging
import time

logging.basicConfig(filename="C://seleniumpractice//test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)

logging.debug("This is debug msg")
logging.warning("This is warning msg")
logging.info("This is info msg")
logging.error("This is error msg")
logging.critical("This is critical msg")
