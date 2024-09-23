from logger.domain import Logger,LoggerManager

def main(name):
    logger1 = LoggerManager.get_logger(type_logger = "console")
    logger1.log("test")
    logger1.info("test")
    logger1.error("test")

    logger2 = LoggerManager.get_logger(type_logger = "file")
    logger2.info("test2")

if __name__ == '__main__':
    main('PyCharm')
