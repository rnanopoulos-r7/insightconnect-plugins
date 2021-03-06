# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Get account status of a user"


class Input:
    USER = "user"
    

class Output:
    STATUS = "status"
    USER_ID = "user_id"
    

class GetUserStatusInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "user": {
      "type": "string",
      "title": "User",
      "description": "The user account to check status, e.g. jdoe",
      "order": 1
    }
  },
  "required": [
    "user"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetUserStatusOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "status": {
      "type": "string",
      "title": "Status",
      "description": "Status",
      "order": 1
    },
    "user_id": {
      "type": "string",
      "title": "User ID",
      "description": "User ID",
      "order": 2
    }
  },
  "required": [
    "status",
    "user_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
