import komand
from .schema import DownloadLogsInput, DownloadLogsOutput, Input, Output, Component
import requests
# Custom imports below


class DownloadLogs(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='download_logs',
                description=Component.DESCRIPTION,
                input=DownloadLogsInput(),
                output=DownloadLogsOutput())

    def run(self, params={}):
        logs = params.get("logs")
        if logs:
            logs = ":".join(logs)
        query = params.get("query", "")
        from_millis = params.get("from_millis")
        to_millis = params.get("to_millis")
        limit = params.get("limit")
        service_url = '/download/logs/'
        url = self.connection.insighturl + service_url + logs + '?from=' + from_millis + '&to=' + to_millis
        if limit:
        	url += '&limit=' + limit
        if query:
            url += '&query=' + query
        headers = {'x-api-key': self.connection.api_key}
        try:
            resp = requests.get(url, headers=headers)
            cleaned_resp = komand.helper.clean(resp.json())
            return cleaned_resp
        except Exception:
            self.logger.info(Exception)
            raise

    def test(self):
        service_url = "/download/logs/"
        url = self.connection.insighturl + service_url
        headers = {'x-api-key': self.connection.api_key}
        try:
            resp = requests.get(url, headers=headers)
            cleaned_resp = komand.helper.clean(resp.json())
            return cleaned_resp
        except Exception:
            self.logger.info(Exception)
            raise
