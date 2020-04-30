import komand
from .schema import SendEmailInput, SendEmailOutput, Input, Output, Component
# Custom imports below
from komand_mimecast.util import util
from komand.exceptions import PluginException


class SendEmail(komand.Action):
    # URI for Decode URL
    _URI = '/api/email/send-email'

    def __init__(self):
        super(self.__class__, self).__init__(
            name='send_email',
            description=Component.DESCRIPTION,
            input=SendEmailInput(),
            output=SendEmailOutput())

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
        response = mimecast_request.mimecast_post(url=url, uri=SendEmail._URI,
                                                  access_key=access_key, secret_key=secret_key,
                                                  app_id=app_id, app_key=app_key, data=data)

        try:
            return {
                Output.MESSAGE_ID: response["data"][0]["messageId"],
                Output.MESSAGE_DATE_HEADER: response["data"][0]["messageDateHeader"]
            }
        except KeyError:
            raise PluginException(preset=PluginException.Preset.UNKNOWN,
                                  data=response)
        except IndexError:
            raise PluginException(preset=PluginException.Preset.UNKNOWN,
                                  data=response)

    @staticmethod
    def get_data(params):
        data = {}
        if params.get(Input.TO):
            data["to"] = params.get(Input.TO)
        if params.get(Input.FROM):
            data["from"] = params.get(Input.FROM)
        if params.get(Input.ATTACHMENTS):
            data["attachments"] = params.get(Input.ATTACHMENTS)
        if params.get(Input.HTML_BODY):
            data["htmlBody"] = params.get(Input.HTML_BODY)
        if params.get(Input.CC):
            data["cc"] = params.get(Input.CC)
        if params.get(Input.PLAIN_BODY):
            data["plainBody"] = params.get(Input.PLAIN_BODY)
        if params.get(Input.SUBJECT):
            data["subject"] = params.get(Input.SUBJECT)
        if params.get(Input.EXTRA_HEADERS):
            data["extraHeaders"] = params.get(Input.EXTRA_HEADERS)
        if params.get(Input.BCC):
            data["bcc"] = params.get(Input.BCC)

        return data
