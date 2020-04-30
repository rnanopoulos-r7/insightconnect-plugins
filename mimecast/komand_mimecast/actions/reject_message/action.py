import komand
from .schema import RejectMessageInput, RejectMessageOutput, Input, Output, Component
# Custom imports below
from komand_mimecast.util import util
from komand.exceptions import PluginException


class RejectMessage(komand.Action):
    # URI for Decode URL
    _URI = '/api/gateway/hold-reject'

    def __init__(self):
        super(self.__class__, self).__init__(
            name='reject_message',
            description=Component.DESCRIPTION,
            input=RejectMessageInput(),
            output=RejectMessageOutput())

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
        response = mimecast_request.mimecast_post(url=url, uri=RejectMessage._URI,
                                                  access_key=access_key, secret_key=secret_key,
                                                  app_id=app_id, app_key=app_key, data=data)

        try:
            data_id = response["data"][0]["id"]
            data_reject = response["data"][0]["reject"]
        except KeyError:
            raise PluginException(preset=PluginException.Preset.UNKNOWN,
                                  data=response)
        except IndexError:
            raise PluginException(preset=PluginException.Preset.UNKNOWN,
                                  data=response)

        return {
            Output.ID: data_id,
            Output.REJECT: data_reject
        }

    @staticmethod
    def get_data(params):
        data = {}
        if params.get(Input.MESSAGE):
            data["message"] = params.get(Input.MESSAGE)
        if params.get(Input.IDS):
            data["ids"] = params.get(Input.IDS)
        if params.get(Input.REASON_TYPE):
            data["reasonType"] = params.get(Input.REASON_TYPE)
        if params.get(Input.NOTIFY):
            data["notify"] = params.get(Input.NOTIFY)

        return data
