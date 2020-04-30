import komand
from .schema import ReleaseMessageInput, ReleaseMessageOutput, Input, Output, Component
# Custom imports below
from komand_mimecast.util import util
from komand.exceptions import PluginException


class ReleaseMessage(komand.Action):
    # URI for Decode URL
    _URI = '/api/gateway/hold-release'

    def __init__(self):
        super(self.__class__, self).__init__(
                name='release_message',
                description=Component.DESCRIPTION,
                input=ReleaseMessageInput(),
                output=ReleaseMessageOutput())

    def run(self, params={}):
        # Import variables from connection
        url = self.connection.url
        access_key = self.connection.access_key
        secret_key = self.connection.secret_key
        app_id = self.connection.app_id
        app_key = self.connection.app_key

        # Generate payload dictionary
        data = {}
        if params.get(Input.ID):
            data["id"] = params.get(Input.ID)

        mimecast_request = util.MimecastRequests()
        response = mimecast_request.mimecast_post(url=url, uri=ReleaseMessage._URI,
                                                  access_key=access_key, secret_key=secret_key,
                                                  app_id=app_id, app_key=app_key, data=data)

        try:
            data_id = response["data"][0]["id"]
            data_release = response["data"][0]["release"]
        except KeyError:
            raise PluginException(preset=PluginException.Preset.UNKNOWN,
                                  data=response)
        except IndexError:
            raise PluginException(preset=PluginException.Preset.UNKNOWN,
                                  data=response)

        return {
            Output.ID: data_id,
            Output.RELEASE: data_release
        }
