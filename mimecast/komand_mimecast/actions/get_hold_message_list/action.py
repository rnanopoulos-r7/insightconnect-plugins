import komand
from .schema import GetHoldMessageListInput, GetHoldMessageListOutput, Input, Output, Component
# Custom imports below
from komand_mimecast.util import util
from komand.exceptions import PluginException


class GetHoldMessageList(komand.Action):
    # URI for Decode URL
    _URI = '/api/gateway/get-hold-message-list'

    def __init__(self):
        super(self.__class__, self).__init__(
            name='get_hold_message_list',
            description=Component.DESCRIPTION,
            input=GetHoldMessageListInput(),
            output=GetHoldMessageListOutput())

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
        response = mimecast_request.mimecast_post(url=url, uri=GetHoldMessageList._URI,
                                                  access_key=access_key, secret_key=secret_key,
                                                  app_id=app_id, app_key=app_key, data=data)

        if len(response["data"]) == 0:
            output = []
        else:
            output = response["data"][0]["heldEmails"]

        return {
            Output.HELD_EMAILS: output
        }

    @staticmethod
    def get_data(params):
        data = {}
        if params.get(Input.ADMIN):
            data["admin"] = params.get(Input.ADMIN)
        if params.get(Input.START_DATE):
            data["start"] = params.get(Input.START_DATE)
        if params.get(Input.SEARCH_BY):
            data["searchBy"] = params.get(Input.SEARCH_BY)
        if params.get(Input.END_DATE):
            data["end"] = params.get(Input.END_DATE)
        if params.get(Input.FILTER_BY):
            data["filterBy"] = params.get(Input.FILTER_BY)

        return data
