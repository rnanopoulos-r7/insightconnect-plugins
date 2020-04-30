import komand
from .schema import GetThreatIntelFeedInput, GetThreatIntelFeedOutput, Input, Output, Component
# Custom imports below
from komand_mimecast.util import util
from komand.exceptions import PluginException


class GetThreatIntelFeed(komand.Action):
    # URI for Decode URL
    _URI = '/api/ttp/threat-intel/get-feed'

    def __init__(self):
        super(self.__class__, self).__init__(
            name='get_threat_intel_feed',
            description=Component.DESCRIPTION,
            input=GetThreatIntelFeedInput(),
            output=GetThreatIntelFeedOutput())

    def run(self, params={}):
        # Import variables from connection
        url = self.connection.url
        access_key = self.connection.access_key
        secret_key = self.connection.secret_key
        app_id = self.connection.app_id
        app_key = self.connection.app_key

        # Generate payload dictionary
        data = self.get_data(params)
        mimecast_request = util.MimecastRequests()
        response = mimecast_request.mimecast_post(url=url, uri=GetThreatIntelFeed._URI,
                                                  access_key=access_key, secret_key=secret_key,
                                                  app_id=app_id, app_key=app_key, data=data)

        stix_objects = None
        csv_lines = None

        if Input.FILE_TYPE == "csv":
            csv_lines = response
        else:
            stix_objects = response

        return {
            Output.STIX_OBJECTS: stix_objects,
            Output.CSV_LINES: csv_lines
        }

    @staticmethod
    def get_data(params):
        data = {}
        if params.get(Input.END_DATE):
            data["end"] = params.get(Input.END_DATE)
        if params.get(Input.FILE_TYPE):
            data["fileType"] = params.get(Input.FILE_TYPE)
        if params.get(Input.COMPRESS):
            data["compress"] = params.get(Input.COMPRESS)
        if params.get(Input.START_DATE):
            data["start"] = params.get(Input.START_DATE)
        if params.get(Input.TOKEN):
            data["token"] = params.get(Input.TOKEN)
        if params.get(Input.FEED_TYPE):
            data["feedType"] = params.get(Input.FEED_TYPE)

        return data
