# Description

[Confluence](https://atlassian.com/software/confluence) is an open and shared workspace for managing documents and
files within an organization. Using the Confluence plugin for Rapid7 InsightConnect, users can view and update pages
dynamically within automation workflows.

# Key Features

* Update pages
* View pages

# Requirements

* Confluence URL
* Confluence username and password

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|credentials|credential_username_password|None|True|Username and password|None|
|url|string|None|True|Connection URL|None|

## Technical Details

### Actions

#### Store Page Contents

This action is used to store page contents.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|contents|string|None|True|Contents to store|None|
|page|string|None|True|Page name|None|
|space|string|None|True|Space|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|page|page|False|Page stored|

Example output:

```
```

#### Get Page Contents

This action is used to get page contents.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|page|string|None|True|Page name|None|
|space|string|None|True|Space|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|contents|string|False|Contents|
|found|boolean|False|True if found|

Example output:

```
```

#### Get Page

This action is used to retrieve a Wiki page.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|page|string|None|True|Page name|None|
|space|string|None|True|Space|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|found|boolean|False|True if found|
|page|page|False|Page|

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

Make sure the credentials are valid and the Confluence URL is correct.

# Version History

* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.3 - Pin Confluence python library at 0.2
* 0.1.2 - SSL bug fix in SDK
* 0.1.1 - Fix bug dumping credentials to log
* 0.1.0 - Initial plugin

# Links

## References

* [Confluence](https://www.atlassian.com/software/confluence)
* [Confluence API URL](https://docs.atlassian.com/confluence/REST/latest/)
* [Confluence Python Documentation](https://pythonhosted.org/confluence/)

