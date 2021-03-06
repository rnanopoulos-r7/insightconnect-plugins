# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Fetch details for the agent with the given ID"


class Input:
    AGENT_ID = "agent_id"
    APP_ID = "app_id"
    

class Output:
    AGENT = "agent"
    

class GetAgentDetailsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "agent_id": {
      "type": "string",
      "title": "Agent ID",
      "description": "Agent ID",
      "order": 2
    },
    "app_id": {
      "type": "string",
      "title": "App ID",
      "description": "App ID",
      "order": 1
    }
  },
  "required": [
    "agent_id",
    "app_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetAgentDetailsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "agent": {
      "$ref": "#/definitions/agent",
      "title": "Agent",
      "description": "Details for the provided agent, including the agent type (ApacheAgent, JVMAgent, etc), version string, earliest and most recent time seen, and whether the agent is currently known to be actively sending data to the tCell service",
      "order": 1
    }
  },
  "definitions": {
    "agent": {
      "type": "object",
      "title": "agent",
      "properties": {
        "active": {
          "type": "boolean",
          "title": "Active",
          "description": "Whether or not the agent is currently active",
          "order": 7
        },
        "from": {
          "type": "integer",
          "title": "From",
          "description": "The Unix timestamp (in milliseconds) when the agent was first seen",
          "order": 4
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "The agent ID",
          "order": 1
        },
        "last_process_id": {
          "type": "string",
          "title": "Last Process ID",
          "description": "The most recent process ID associated with the agent",
          "order": 6
        },
        "to": {
          "type": "integer",
          "title": "To",
          "description": "The Unix timestamp (in milliseconds) when the agent was last seen",
          "order": 5
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "The agent type",
          "order": 2
        },
        "version": {
          "type": "string",
          "title": "Version",
          "description": "The version of the agent",
          "order": 3
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
