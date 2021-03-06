# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Provision new user or change exisiting user"


class Input:
    FULL_NAME = "full_name"
    GROUPS = "groups"
    PASSWORD = "password"
    PASSWORD_RESET_REQUIRED = "password_reset_required"
    USER_NAME = "user_name"
    

class Output:
    STATUS = "status"
    

class ProvisionUserInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "full_name": {
      "type": "string",
      "title": "Full Name",
      "description": "Full name of user to add",
      "order": 2
    },
    "groups": {
      "type": "array",
      "title": "Groups",
      "description": "Array of groups",
      "items": {
        "type": "string"
      },
      "order": 5
    },
    "password": {
      "type": "string",
      "title": "Password",
      "description": "Password for the user",
      "order": 3
    },
    "password_reset_required": {
      "type": "boolean",
      "title": "Password Reset Required",
      "description": "Password reset required",
      "order": 4
    },
    "user_name": {
      "type": "string",
      "title": "User Name",
      "description": "User name to add",
      "order": 1
    }
  },
  "required": [
    "user_name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ProvisionUserOutput(komand.Output):
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
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
