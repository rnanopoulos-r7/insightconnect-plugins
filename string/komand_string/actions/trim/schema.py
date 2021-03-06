# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Trim a string of leading and trailing whitespace"


class Input:
    STRING = "string"
    

class Output:
    TRIMMED = "trimmed"
    

class TrimInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "string": {
      "type": "string",
      "title": "String Input",
      "description": "String to trim",
      "order": 1
    }
  },
  "required": [
    "string"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class TrimOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "trimmed": {
      "type": "string",
      "title": "Trimmed",
      "description": "Trimmed string",
      "order": 1
    }
  },
  "required": [
    "trimmed"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
