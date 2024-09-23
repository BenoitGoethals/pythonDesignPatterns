# This is a sample Python script.

from logger.domain import logger, logger_manager


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    logger1 = logger_manager.get_logger(type_logger = "console")
    logger1.log("test")

    logger2 = logger_manager.get_logger(type_logger = "file")
    logger2.log("test2")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
