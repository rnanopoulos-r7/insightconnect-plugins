# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Delete analysis by ID and malware SHA256 hash"


class Input:
    ID = "id"
    MALWARE_SHA256 = "malware_sha256"
    PROJECT_NAME = "project_name"
    

class Output:
    pass

class DeleteAnalysisInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "integer",
      "title": "Analysis ID",
      "order": 3
    },
    "malware_sha256": {
      "type": "string",
      "title": "Malware SHA256 Hash",
      "order": 2
    },
    "project_name": {
      "type": "string",
      "title": "Project Name",
      "order": 1
    }
  },
  "required": [
    "id",
    "malware_sha256",
    "project_name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DeleteAnalysisOutput(komand.Output):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)