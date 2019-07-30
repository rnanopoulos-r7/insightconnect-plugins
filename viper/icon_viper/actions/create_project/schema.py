# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Create a new project with a given name"


class Input:
    NAME = "name"
    

class Output:
    PROJECT = "project"
    

class CreateProjectInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "name": {
      "type": "string",
      "title": "New Project",
      "order": 1
    }
  },
  "required": [
    "name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateProjectOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "project": {
      "$ref": "#/definitions/Project",
      "title": "Project",
      "order": 1
    }
  },
  "required": [
    "project"
  ],
  "definitions": {
    "Project": {
      "type": "object",
      "title": "Project",
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Project name",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)