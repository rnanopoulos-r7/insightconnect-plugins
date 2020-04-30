import komand
from .schema import GetMessageHoldSummaryListInput, GetMessageHoldSummaryListOutput, Input, Output, Component
# Custom imports below
from komand_mimecast.util import util
from komand.exceptions import PluginException


class GetMessageHoldSummaryList(komand.Action):
    # URI for Decode URL
    _URI = '/api/gateway/get-hold-summary-list'

    def __init__(self):
        super(self.__class__, self).__init__(
            name='get_message_hold_summary_list',
            description=Component.DESCRIPTION,
            input=GetMessageHoldSummaryListInput(),
            output=GetMessageHoldSummaryListOutput())

    def run(self, params={}):
        # Import variables from connection
        url = self.connection.url
        access_key = self.connection.access_key
        secret_key = self.connection.secret_key
        app_id = self.connection.app_id
        app_key = self.connection.app_key

        mimecast_request = util.MimecastRequests()
        response = mimecast_request.mimecast_post(url=url, uri=GetMessageHoldSummaryList._URI,
                                                  access_key=access_key, secret_key=secret_key,
                                                  app_id=app_id, app_key=app_key, data=None)

        if len(response["data"]) == 0:
            return {}

        return {
            Output.NUMBER_OF_ITEMS: response["data"][0]["numberOfItems"],
            Output.POLICY_INFO: response["data"][0]["policyInfo"]
        }
