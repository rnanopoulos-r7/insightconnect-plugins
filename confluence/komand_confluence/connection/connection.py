import komand
from .schema import ConnectionSchema, Input
# Custom imports below
from confluence import Confluence


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        """
        Connect to Confluence
        """
        self.logger.info("Connecting to Confluence: %s", params.get(Input.URL))
        self.client = Confluence(
            url=params.get(Input.URL),
            username=params.get(Input.CREDENTIALS).get('username'),
            password=params.get(Input.CREDENTIALS).get('password'))
