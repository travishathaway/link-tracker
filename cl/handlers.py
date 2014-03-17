import SocketServer
import re
import datetime

# Our module imports
import loggers
import settings


class ClTcpHandler(SocketServer.BaseRequestHandler):
    """
    This is a TCP Request Handler that listens specifically for
    HTTP requests. In these request is a special header called
    "link-tracker".  This essentially tells us which link we have
    just clicked, so we can record it to a file or database
    """

    def handle(self):
        self.data = self.request.recv(1024).strip()
        for line in self.data.split('\n'):
            # We are looking for our "link-tracker" header
            if 'link-tracker' in line:
                match = re.search('http(s)?://.+', line)
                if match:
                    data = {}
                    data['url'] = match.group().replace('\r', '')
                    data['timestamp'] = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

                    self.log(data)

    def log(self, data):
        logger = getattr(loggers, settings.LOGGER_CLASS)
        logger = logger()
        logger.log(data)
