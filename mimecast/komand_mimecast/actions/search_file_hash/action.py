import komand
from .schema import SearchFileHashInput, SearchFileHashOutput, Input, Output, Component
# Custom imports below
from komand_mimecast.util import util
from komand.exceptions import PluginException


class SearchFileHash(komand.Action):
    # URI for Decode URL
    _URI = '/api/ttp/remediation/search-hash'

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search_file_hash',
                description=Component.DESCRIPTION,
                input=SearchFileHashInput(),
                output=SearchFileHashOutput())

    def run(self, params={}):
        # Import variables from connection
        url = self.connection.url
        access_key = self.connection.access_key
        secret_key = self.connection.secret_key
        app_id = self.connection.app_id
        app_key = self.connection.app_key

        # Generate payload dictionary
        data = {}
        if params.get(Input.HASHES):
            data["hashes"] = params.get(Input.HASHES)

        mimecast_request = util.MimecastRequests()
        response = mimecast_request.mimecast_post(url=url, uri=SearchFileHash._URI,
                                                  access_key=access_key, secret_key=secret_key,
                                                  app_id=app_id, app_key=app_key, data=data)

        try:
            failed_hashes = response["data"][0]["failedHashes"]
            hash_status = response["data"][0]["hashStatus"]
        except KeyError:
            raise PluginException(preset=PluginException.Preset.UNKNOWN,
                                  data=response)
        except IndexError:
            raise PluginException(preset=PluginException.Preset.UNKNOWN,
                                  data=response)

        return {
            Output.FAILED_HASHES: failed_hashes,
            Output.HASH_STATUS: hash_status
        }
