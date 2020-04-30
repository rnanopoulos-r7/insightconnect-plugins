import komand
from .schema import MessageFinderSearchInput, MessageFinderSearchOutput, Input, Output, Component
# Custom imports below
from komand_mimecast.util import util
from komand.exceptions import PluginException


class MessageFinderSearch(komand.Action):
    # URI for Decode URL
    _URI = '/api/message-finder/search'

    def __init__(self):
        super(self.__class__, self).__init__(
            name='message_finder_search',
            description=Component.DESCRIPTION,
            input=MessageFinderSearchInput(),
            output=MessageFinderSearchOutput())

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
        response = mimecast_request.mimecast_post(url=url, uri=MessageFinderSearch._URI,
                                                  access_key=access_key, secret_key=secret_key,
                                                  app_id=app_id, app_key=app_key, data=data)

        try:
            data = response["data"][0]["trackedEmails"]
        except KeyError:
            raise PluginException(preset=PluginException.Preset.UNKNOWN,
                                  data=response)
        except IndexError:
            raise PluginException(preset=PluginException.Preset.UNKNOWN,
                                  data=response)

        return {
            Output.TRACKED_EMAILS: data,
        }

    @staticmethod
    def get_data(params):
        data = {}
        if params.get(Input.START_DATE):
            data["start"] = params.get(Input.START_DATE)
        if params.get(Input.END_DATE):
            data["end"] = params.get(Input.END_DATE)
        if params.get(Input.SEARCH_REASON):
            data["searchReason"] = params.get(Input.SEARCH_REASON)
        if params.get(Input.ADVANCED_OPTIONS):
            data["advancedTrackAndTraceOptions"] = params.get(Input.ADVANCED_OPTIONS)
        if params.get(Input.MESSAGE_ID):
            data["messageId"] = params.get(Input.MESSAGE_ID)

        return data
