import settings


class BaseLogger(object):
    """
    This is the base logger object.
    """

    def log(self, data):
        """
        Prints to std out
        """
        print data

class FileLogger(BaseLogger):
    """
    Logs our requests to a file in a CSV format
    """
    pass

class SqliteLogger(BaseLogger):
    """
    Logs our requests to a Sqlite database
    """
    pass
