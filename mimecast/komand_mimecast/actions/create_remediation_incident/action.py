import komand
from .schema import CreateRemediationIncidentInput, CreateRemediationIncidentOutput, Input, Output, Component
# Custom imports below
from komand_mimecast.util import util
from komand.exceptions import PluginException


class CreateRemediationIncident(komand.Action):
    # URI for Decode URL
    _URI = '/api/ttp/remediation/create'

    def __init__(self):
        super(self.__class__, self).__init__(
            name='create_remediation_incident',
            description=Component.DESCRIPTION,
            input=CreateRemediationIncidentInput(),
            output=CreateRemediationIncidentOutput())

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
        response = mimecast_request.mimecast_post(url=url, uri=CreateRemediationIncident._URI,
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

    @staticmethod
    def get_data(params):
        data = {}
        if params.get(Input.END_DATE):
            data["end"] = params.get(Input.END_DATE)
        if params.get(Input.START_DATE):
            data["start"] = params.get(Input.START_DATE)
        if params.get(Input.REASON):
            data["reason"] = params.get(Input.REASON)
        if params.get(Input.SEARCH_BY):
            data["searchBy"] = params.get(Input.SEARCH_BY)
        if params.get(Input.HASHORMESSAGEID):
            data["hashOrMessageId"] = params.get(Input.HASHORMESSAGEID)

        return data
