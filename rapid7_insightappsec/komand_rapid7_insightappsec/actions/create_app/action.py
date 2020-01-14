import komand
from .schema import CreateAppInput, CreateAppOutput, Input, Output, Component
# Custom imports below
from komand_rapid7_insightappsec.util.endpoints import Apps
from komand_rapid7_insightappsec.util.resource_helper import ResourceHelper
import json


class CreateApp(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_app',
                description=Component.DESCRIPTION,
                input=CreateAppInput(),
                output=CreateAppOutput())

    def run(self, params={}):
        request = ResourceHelper(self.connection.session, self.logger)
        url = Apps.create_app(self.connection.url)
        app_name = params.get(Input.APP_NAME, "")
        app_description = params.get(Input.APP_DESCRIPTION, "")
        payload = {
            "name": app_name,
            "description": app_description
        }
        response = request.resource_request(url, 'post', payload=payload)

        try:
            if response["resource"]:
                data = json.loads(response["resource"])
                return {Output.APP_ID: "",
                        Output.ERROR_CODE: data['error_code'],
                        Output.MESSAGE: data['message'],
                        Output.STATUS: data['status']}

            header = response.get("headers")
            appID = header['Location'].split('/')[-1]

        except json.decoder.JSONDecodeError:
            self.logger.error(f'InsightAppSec response: {response}')
            raise Exception('The response from InsightAppSec was not in JSON format. Contact support for help.'
                            ' See log for more details')

        return {Output.APP_ID: appID,
                Output.ERROR_CODE: "",
                Output.MESSAGE: "",
                Output.STATUS: 0}
