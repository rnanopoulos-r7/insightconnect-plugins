# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Add an address object (host object) to a group"


class Input:
    ADDRESS_OBJECT = "address_object"
    GROUP = "group"
    

class Output:
    SUCCESS = "success"
    

class AddAddressObjectToGroupInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "address_object": {
      "type": "string",
      "title": "Host Name",
      "description": "The name of the host object to add",
      "order": 2
    },
    "group": {
      "type": "string",
      "title": "Group",
      "description": "Name of the group to add this object to",
      "order": 1
    }
  },
  "required": [
    "address_object",
    "group"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AddAddressObjectToGroupOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Success",
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
