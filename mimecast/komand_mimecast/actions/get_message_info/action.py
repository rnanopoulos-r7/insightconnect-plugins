import komand
from .schema import GetMessageInfoInput, GetMessageInfoOutput, Input, Output, Component
# Custom imports below
from komand_mimecast.util import util
from komand.exceptions import PluginException


class GetMessageInfo(komand.Action):
    # URI for Decode URL
    _URI = '/api/message-finder/get-message-info'

    def __init__(self):
        super(self.__class__, self).__init__(
            name='get_message_info',
            description=Component.DESCRIPTION,
            input=GetMessageInfoInput(),
            output=GetMessageInfoOutput())

    def run(self, params={}):
        # Import variables from connection
        url = self.connection.url
        access_key = self.connection.access_key
        secret_key = self.connection.secret_key
        app_id = self.connection.app_id
        app_key = self.connection.app_key

        # Generate payload dictionary
        data = {
            "id": params.get(Input.ID)
        }

        mimecast_request = util.MimecastRequests()
        response = mimecast_request.mimecast_post(url=url, uri=GetMessageInfo._URI,
                                                  access_key=access_key, secret_key=secret_key,
                                                  app_id=app_id, app_key=app_key, data=data)

        try:
            if not response['data'][0]['success'] or not response['data'][0]['success'] == 200:
                raise PluginException(cause=f'Problem with input parameters',
                                      assistance='Please ensure that it is a Mimecast parameters.',
                                      data=response['fail'])

            return {
                Output.STATUS: response["data"][0]["status"],
                Output.RETENTIONINFO: response["data"][0]["retentionInfo"],
                Output.RECIPIENTINFO: response["data"][0]["recipientInfo"],
                Output.DELIVEREDMESSAGE: response["data"][0]["deliveredMessage"],
                Output.ID: response["data"][0]["id"],
            }
        except KeyError:
            raise PluginException(preset=PluginException.Preset.UNKNOWN,
                                  data=response)
        except IndexError:
            raise PluginException(preset=PluginException.Preset.UNKNOWN,
                                  data=response)
