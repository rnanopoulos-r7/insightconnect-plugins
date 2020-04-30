import komand
from .schema import GetRemediationIncidentInput, GetRemediationIncidentOutput, Input, Output, Component
# Custom imports below
from komand_mimecast.util import util
from komand.exceptions import PluginException


class GetRemediationIncident(komand.Action):
    # URI for Decode URL
    _URI = '/api/ttp/remediation/get-incident'

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_remediation_incident',
                description=Component.DESCRIPTION,
                input=GetRemediationIncidentInput(),
                output=GetRemediationIncidentOutput())

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
        response = mimecast_request.mimecast_post(url=url, uri=GetRemediationIncident._URI,
                                                  access_key=access_key, secret_key=secret_key,
                                                  app_id=app_id, app_key=app_key, data=data)

        try:
            data = response["data"][0]
        except KeyError:
            raise PluginException(preset=PluginException.Preset.UNKNOWN,
                                  data=response)
        except IndexError:
            raise PluginException(preset=PluginException.Preset.UNKNOWN,
                                  data=response)

        return {
            Output.DATA: data,
        }
