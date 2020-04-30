import komand
from .schema import FileUploadInput, FileUploadOutput, Input, Output, Component
# Custom imports below
from komand_mimecast.util import util
from komand.exceptions import PluginException
import base64
import hashlib


class FileUpload(komand.Action):
    # URI for Decode URL
    _URI = '/api/file/file-upload'

    def __init__(self):
        super(self.__class__, self).__init__(
            name='file_upload',
            description=Component.DESCRIPTION,
            input=FileUploadInput(),
            output=FileUploadOutput())

    def run(self, params={}):
        # Import variables from connection
        url = self.connection.url
        access_key = self.connection.access_key
        secret_key = self.connection.secret_key
        app_id = self.connection.app_id
        app_key = self.connection.app_key

        # Generate payload dictionary
        file_bytes = base64.b64decode(params.get(Input.FILE).get("content"))

        sha256 = hashlib.sha256()
        sha256.update(file_bytes)
        data = {
            'sha256': sha256.hexdigest(),
            'fileSize': len(file_bytes)
        }

        mimecast_request = util.MimecastRequests()
        response = mimecast_request.mimecast_post(url=url, uri=FileUpload._URI,
                                                  access_key=access_key, secret_key=secret_key,
                                                  app_id=app_id, app_key=app_key, file_bytes=file_bytes, data=data)

        try:
            data_id = response["id"]
        except KeyError:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response)
        except IndexError:
            raise PluginException(preset=PluginException.Preset.UNKNOWN, data=response)

        return {
            Output.ID: data_id,
        }
