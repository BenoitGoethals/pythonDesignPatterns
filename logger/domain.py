from jupyter_core.version import pattern


class logger_manager:

    @staticmethod
    def get_logger(type_logger):
        pattern = console_pattern()
        if type_logger == 'console':
            pattern = console_pattern()
        elif type_logger == 'file':
            pattern = file_pattern()

        return logger(pattern)


class logger:
    def __init__(self, pattern):
        self.pattern = pattern


    def log(self,message):
        self.pattern.write(message)



class console_pattern:
    def __init__(self):
        pass

    def write(self,msg):
        print(msg)

class file_pattern:
    def __init__(self):
        pass

    def write(self,msg):
        with open('log.txt','a') as f:
            f.write(msg)
            f.close()

