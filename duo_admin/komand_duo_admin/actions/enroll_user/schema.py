# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Enrolls a user and sends an enrollment email to the specified email address"


class Input:
    EMAIL = "email"
    TIME_TO_EXPIRATION = "time_to_expiration"
    USERNAME = "username"
    

class Output:
    SUCCESS = "success"
    

class EnrollUserInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "email": {
      "type": "string",
      "title": "Email Address",
      "description": "Email address to send enrollment email to",
      "order": 2
    },
    "time_to_expiration": {
      "type": "number",
      "title": "Time to Expiration",
      "description": "Amount of time in seconds until enrollment email expires. Use '0' for no expiration",
      "default": 0,
      "order": 3
    },
    "username": {
      "type": "string",
      "title": "Username",
      "description": "Username for user to enroll",
      "order": 1
    }
  },
  "required": [
    "email",
    "time_to_expiration",
    "username"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class EnrollUserOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Whether or not the enrollment was successful",
      "order": 1
    }
  },
  "required": [
    "success"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
