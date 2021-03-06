# Description

[Twitter](https://twitter.com) is a microblogging and social networking service. With the Twitter plugin for
Rapid7 InsightConnect, users can monitor tweets, post, and block users. This plugin can be effective in discovering
social media campaigns, threat intelligence, and more.

# Key Features

* Monitor tweets
* Post tweet
* Block users

# Requirements

* Consume key and secret
* Access token and secret
* OAuth token registered to a Twitter account (see: https://apps.twitter.com/)

# Documentation

## Setup

Using the plugin will require a valid Twitter OAuth token, by creating an "App" registered to use your Twitter account.
You can find the page to do so at [Twitter Apps](https://apps.twitter.com/)
Note - you must be logged in to access this page properly.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|consumer_credentials|credential_username_password|None|True|Consumer Key and Consumer Secret|None|
|access_token_credentials|credential_username_password|None|True|Access Token and Access Token Secret|None|

## Technical Details

### Actions

#### Destroy

This action can be used to destroy a direct message from the Twitter account linked via the connection.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|message_id|string|None|True|ID of direct message to destroy|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|destroyed|boolean|False|Destroyed|

#### Post

This action can be used to issue a tweet from the Twitter account linked via the connection.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|msg|string|None|True|Text to tweet|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|url|string|False|URL|

#### Block

This action can be used to block a user from the Twitter account linked via the connection.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user|string|None|True|User to block|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|blocked|boolean|False|Blocked|

### Triggers

All of the below triggers utilize the plugin cache to track a history of the last message received.
This means they will not replay messages that already were pulled via the API.

#### Tweets

The Tweets trigger will fire off a job for every Tweet that matches the supplied pattern you give to the Trigger. For example, you could monitor for "BBQ" to get BBQ related tweets.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|interval|integer|300|False|Poll interval in seconds|None|
|pattern|string|None|True|Pattern to match|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|msg|string|False|Tweet message|
|url|string|False|URL of tweet|
|user|string|False|Posting user|

#### Mentions

The Mentions trigger will off a job for every Mention that matches the supplied pattern, and involves the linked account in the connection.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|interval|integer|300|False|Poll interval in seconds|None|
|pattern|string|None|False|Pattern to Match|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|msg|string|False|Twitter message|
|url|string|False|URL of tweet|
|user|string|False|Posting user|

#### Messages

This trigger will fire off a job for every direct message received by the linked account in the connection.
Note that to use this trigger "Read, Write and Access direct messages" must be selected in your Twitter App's permissions tab.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|interval|integer|300|False|Poll interval in seconds|None|
|pattern|string|None|False|Pattern to Match|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|created_at|string|False|Creation date|
|id|string|False|Twitter message ID|
|msg|string|False|Twitter Message|
|recipient_id|integer|False|Recipient ID|
|sender_created_at|string|False|Sender account creation date|
|sender_default_profile|boolean|False|Sender uses the default profile|
|sender_default_profile_image|boolean|False|Sender uses the default profile image|
|sender_description|string|False|Sender profile description|
|sender_followers_count|integer|False|Sender's follower count|
|sender_friends_count|integer|False|Sender's friend count|
|sender_id|integer|False|Sender ID|
|sender_lang|string|False|Sender's language|
|sender_location|string|False|Sender's geographic location|
|sender_name|string|False|Sender's profile name|
|user|string|False|Posting user|

#### User

The user trigger will allow you to follow a given user and receive any tweets from their timeline.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|interval|integer|300|False|Poll interval in seconds|None|
|screen_name|string|None|True|Screen Name (no @)|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|msg|string|False|Message|
|url|string|False|URL of tweet|
|user|string|False|Posting user|

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

Refer to the Jobs page to inspect any jobs which have failed due to issues with this plugin.
If you suspect the failures are caused by a bug in the plugin, please contact Komand.

# Version History

* 2.0.1 - New spec and help.md format for the Extension Library
* 2.0.0 - Support web server mode | Update to new credential types
* 1.0.1 - Fix long integer bug for `message_id` in Destroy action and `id` in Messages trigger
* 1.0.0 - Update to v2 Python plugin architecture
* 0.3.5 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Twitter Apps](https://apps.twitter.com/)
* [python-twitter](https://github.com/bear/python-twitter/wiki)

