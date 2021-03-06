# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Sets the specified fields to their respective values in the hash stored at key"


class Input:
    EXPIRE = "expire"
    KEY = "key"
    VALUES = "values"
    

class Output:
    REPLY = "reply"
    

class HmsetInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "expire": {
      "type": "integer",
      "title": "Expire",
      "description": "Expiration in seconds",
      "order": 3
    },
    "key": {
      "type": "string",
      "title": "Key",
      "description": "Key",
      "order": 1
    },
    "values": {
      "type": "object",
      "title": "Values",
      "description": "Object hash field:value to set",
      "order": 2
    }
  },
  "required": [
    "key",
    "values"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class HmsetOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "reply": {
      "type": "boolean",
      "title": "Reply",
      "description": "Reply (usually OK)",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
