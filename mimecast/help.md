# Description

[Mimecast](https://www.mimecast.com) is a set of cloud services designed to provide next generation protection against
advanced email-borne threats such as malicious URLs, malware, impersonation attacks, as well as internally generated
threats, with a focus on email security.
This plugin utilizes the [Mimecast API](https://www.mimecast.com/developer/documentation).

# Key Features

* Email security
* Malicious URL and attachment detection

# Requirements

* Access API Key
* Secret Key
* Mimecast server
* API Username and Password

# Documentation

* https://www.mimecast.com/tech-connect/documentation/api-overview

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|access_key|credential_secret_key|None|True|The application access key|None|eWtOL3XZCOwG96BOiFTZRiC5rdvDmP4FFdwU2Y1DC1Us-gh7KyL5trUrZ9aEuzQMV7pPWWxTnPVtsJ6x3fajAh3cRskP0w8hNjaFFVkZB6G9dOytLM2ssQ7HY-p7gJoi|
|app_id|string|None|True|Application ID|None|78d2e4b1-8cc2-4806-nt79-6ef332a47374|
|app_key|credential_secret_key|None|True|The application key|None|475x54c6-4f61-4fab-8be7-a0710f3859e3|
|secret_key|credential_secret_key|None|True|The application secret key|None|FgHrtydiP4TynI+rTZF42Qu0FtGuhJtuNM5bDh82goJQHed9kJZ5t/ORwGnI5r2hkl/bzCosZ+KVapJFeaf3Yw==|
|url|string|None|True|The URL for the Mimecast server|None|https://api.mimecast.com|

## Technical Details

### Actions

#### Send Email

This action is used to send Email.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|attachments|[]attachments|None|False|An attachment object describing any attachments on the message|None|None|
|bcc|[]email_address|None|False|An array of recipient objects describing the "bcc" recipient(s) of the message|None|None|
|cc|[]email_address|None|False|An array of recipient objects describing the "cc" recipient(s) of the message|None|None|
|extra_headers|[]extra_headers|None|False|An array of header objects describing any custom message headers to be included on the message|None|None|
|from|email_address|None|False|An object describing the sender of the message. If not included, the details of the authorized user are used|None|None|
|html_body|html_body|None|False|A body object describing the html body of the message|None|None|
|plain_body|html_body|None|False|A body object describing the plain text body of the message|None|None|
|subject|string|None|True|The message subject|None|None|
|to|[]email_address|None|True|An array of recipient objects describing the "to" recipient(s) of the message|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message_date_header|string|False|The date that the message was sent via the API|
|message_id|string|False|The internet message id that the API automatically generates for the message|

Example output:

```

```

#### Search File Hash

This action is used to identify if an account has seen a specific file hash within mesasges over the last year. A maximum of 100 hashes can be submitted in a single call. Currently this action does not support image file hashes.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|hashes|[]string|None|True|List of file hashes to determine if they have been seen within an account|None|TODO|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|failed_hashes|[]string|True|List of hashses that failed verification|
|hash_status|[]hash_status|True|List of hashes that were deteced within account|

Example output:

```
```

#### Release Message

This action is used to release a currently held message.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|The Mimecast secure ID of a message|None|TODO|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|False|The Mimecast secure ID of the message hold|
|release|boolean|False|Returns true if the message was released|

Example output:

```
```

#### Reject Message

This action is used to reject a currently held message based.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|ids|[]string|None|True|An array of Mimecast secure ids for messages to be rejected|None|TODO|
|message|string|None|False|Rejection message to be returned to sender|None|TODO|
|notify|boolean|False|False|Deliever a rejection notification to the sender|None|False|
|reason_type|string|None|False|The reason code for rejecting the message|['MESSAGE CONTAINS UNDESIRABLE CONTENT', 'MESSAGE CONTAINS CONFIDENTIAL INFORMATION', 'REVIEWER DISAPPROVES OF CONTENT', 'INAPPROPRIATE COMMUNICATION', 'MESSAGE GOES AGAINST EMAIL POLICIES']|MESSAGE CONTAINS UNDESIRABLE CONTENT|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|False|The Mimecast secure ID of the message hold|
|reject|boolean|False|Returns true if the message was rejected|

Example output:

```
```

#### Message Finder Search

This action is used to return tracked email objects.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|advanced_options|advanced_options|None|False|An object describing the advanced filters to use in the tracking query|None|None|
|end_date|string|None|False|The date and time of the latest message to track, in the following format, 2011-12-03T10:15:30+0000|None|2011-12-03T10:15:30+0000|
|message_id|string|None|False|The internet message ID of the message to track|None|TODO|
|search_reason|string|None|False|Reason for Tracking a email, used for activity tracking puposes|None|TODO|
|start_date|string|None|False|The date and time of the earliest message to track, in the following format, 2011-12-03T10:15:30+0000|None|2011-12-03T10:15:30+0000|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|tracked_emails|[]tracked_emails|False|An array of tracked email objects|

Example output:

```

```

#### Get Threat Intel Feed

This action is used to return identified malware threats at a customer or regional grid level.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|compress|string|False|False|Compress multiple feed files|None|False|
|end_date|string|None|False|End Date in the ISO 8601 date time format (e.g. 2011-12-03T10:15:30+0000). Default is current date|None|2011-12-03T10:15:30+0000|
|feed_type|string|malware_customer|False|The scope of data to return, either for the account, or for the regions grid|['malware_customer', 'malware_grid']|malware_customer|
|file_type|string|csv|False|File type of respective feed|['csv', 'stix']|csv|
|start_date|string|None|False|Start Date in the ISO 8601 date time format (e.g. 2011-12-03T10:15:30+0000). Default is 7 days before current date|None|2011-12-03T10:15:30+0000|
|token|string|None|False|Secure ID of the threat feed file that was previously downloaded. The Secure ID is included in every response|None|TODO|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|csv_lines|[]string|False|List of csv lines|
|stix_objects|stix_object|False|Stix object|

Example output:

```
```

#### Get Remediation Incident

This action is used to get information about an exisiting incident.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|The Mimecast ID for a remediation incident, provided when an incident is created|None|TODO|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|incident|True|Incident information|

Example output:

```
```

#### Get Message Info

This action is used to return message info.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|The Mimecast ID of the message to load. This is returned by the message_finder_search action|None|TODO|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|deliveredMessage|object|False|If rewriting of this URL in emails is disabled|
|id|string|False|The Mimecast ID of the message|
|recipientInfo|recipientInfo|False|An object describing the recipient information applied to the message|
|retentionInfo|retentionInfo|False|An object describing the retention information applied to the message|
|status|string|False|The message status|

Example output:

```

```

#### Get Message Hold Summary List

This action is used to get counts of currenlty held messages for each hold reason.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|number_of_items|integer|False|The number of messages currenlty held for this reason|
|policy_info|string|False|The name of the policy or definition that held a message|

Example output:

```

```

#### Get Hold Message List

This action is used to get information about held messages.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|admin|boolean|False|False|Level of results to return|None|False|
|end_date|string|None|False|The date and time of the latest message to return, in the following format, 2011-12-03T10:15:30+0000|None|2011-12-03T10:15:30+0000|
|filter_by|[]filter_by|None|False|Filter options to narrow results|None|2011-12-03T10:15:30+0000|
|search_by|search_by|None|False|Object data used to filter results|None|None|
|start_date|string|None|False|The date and time of the earliest message to return, in the following format, 2011-12-03T10:15:30+0000|None|2011-12-03T10:15:30+0000|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|held_emails|[]held_emails|True|An array of held messages|

Example output:

```

```

#### File Upload

This action is used to file Upload.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|file|file|None|True|The file to upload|None|{"filename": "file.txt", "content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="}|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|False|The Mimecast ID of the file|

Example output:

```

```

#### Hold Release

This action is used to release a currently held message.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|end_date|string|None|False|The most recent date of messages to remediate. Default value is the end of the current day|None|2015-11-16T14:49:18+0000|
|hashOrMessageId|string|None|True|The file hash or messageId value|None|2015-11-16T14:49:18+0000|
|reason|string|None|True|The reason for creating the remediation incident|None|2015-11-16T14:49:18+0000|
|search_by|string|hash|False|The message component in which to search by. When using messageId, the "<" ">" delimiters are required|['hash', 'messageId']|hash|
|start_date|string|None|False|The earliest date of messages to remediate. Default value is one month back|None|2015-11-16T14:49:18+0000|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|incident|True|Incident information|

Example output:

```
```

#### Create Managed URL

This action is used to create a managed URL.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|action|string|block|True|Set to 'block' to blacklist the URL, 'permit' to whitelist it|['block', 'permit']|block|
|comment|string|None|False|A comment about the why the URL is managed; for tracking purposes|None|i'm blocking this because virustotal said it was malicious|
|disable_log_click|boolean|None|True|Disable logging of user clicks on the URL|None|Flase|
|disable_rewrite|boolean|None|True|Disable rewriting of this URL in emails. Applies only if action = 'permit'|None|True|
|disable_user_awareness|boolean|None|True|Disable User Awareness challenges for this URL. Applies only if action = 'permit'|None|False|
|match_type|string|explicit|True|Set to 'explicit' to block or permit only instances of the full URL. Set to 'domain' to block or permit any URL with the same domain|['explicit', 'domain']|explicit|
|url|string|None|True|The URL to block or permit. Do not include a fragment|None|https://rapid7.com|

Example input:

```
{
  "action": "block",
  "comment": "test",
  "disable_log_click": false,
  "disable_rewrite": false,
  "disable_user_awareness": false,
  "match_type": "explicit",
  "url": "http://rapid7.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|[]managed_url|False|Managed URL that was created|

Example output:

```
{
  "response": [
    {
      "id": "wOi3MCwjYFYhZfkYlp2RMAhvN30QSmqOT7D-I9Abwlmy7ZH7eCwvY3ImP7QVjTLhQT4SWBA3wB_E-UNk-s0gc6iZeMRZzgizv28dIpyFWXw",
      "scheme": "http",
      "domain": "youtube.com",
      "port": -1,
      "matchType": "explicit",
      "action": "block",
      "comment": "test",
      "disableUserAwareness": false,
      "disableRewrite": false,
      "disableLogClick": false
    }
  ]
}
```

#### Get Managed URL

This action is used to get information on a managed URL.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|action|string|none|False|Filter on whether or not the action is 'block' or 'permit'|['none', 'block', 'permit']|block|
|disable_log_click|string|none|False|Filter on whether or not clicks are logged for this URL|['none', 'false', 'true']|True|
|disable_rewrite|string|none|False|Filter on whether or not rewriting of this URL in emails is enabled|['none', 'false', 'true']|False|
|disable_user_awareness|string|none|False|Filter on whether or not User Awareness challenges for this URL|['none', 'false', 'true']|False|
|domain|string|None|False|The managed domain|None|rapid7.com|
|id|string|None|False|Filter on the Mimecast secure ID of the managed URL|None|None|
|match_type|string|none|False|Filter on whether or not the match type is 'explicit' or 'domain'|['none', 'explicit', 'domain']|domain|
|scheme|string|None|False|Filter on whether or not the protocol is HTTP or HTTPS|None|http|

Example input:

```
{
  "action": "none",
  "disable_log_click": "true",
  "disable_rewrite": "false",
  "disable_user_awareness": "ture",
  "domain": "rapid7.com",
  "id": "",
  "match_type": "explicit",
  "scheme": "http"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|[]managed_url|False|Managed URLs matching |

Example output:

```
{
  "response": [
    {
      "id": "wOi3MCwjYFYhZfkYlp2RMAhvN30QSmqOT7D-I9Abwlmy7ZH7eCwvY3ImP7QVjTLho3KMtTMfYm2C21vDPXvKC5vmEJWDAcvTHtH4L4Kw20c",
      "scheme": "https",
      "domain": "steam.com",
      "port": -1,
      "matchType": "explicit",
      "action": "block",
      "comment": "ui test",
      "disableUserAwareness": true,
      "disableRewrite": true,
      "disableLogClick": false
    }
  ]
}
```

#### Delete Managed URL

This action is used to remove a Managed URL from the blocked list.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|The Mimecast secure ID of the managed URL|None|wOi3MCwjYFYhZfkYlp2RMAhvN30QSmqOT7D-I9Abwlmy7ZH7eCwvY3ImP7QVjTLhHMy6V8J3VOvTNMW2G-txx3o4zL0YXqWxuCVlGQ-1viE|

Example input:

```
{
  "id": "wOi3MCwjYFYhZfkYlp2RMAhvN30QSmqOT7D-I9Abwlmy7ZH7eCwvY3ImP7QVjTLhHMy6V8J3VOvTNMW2G-txx3o4zL0YXqWxuCVlGQ-1viE"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Success status of delete request|

Example output:

```
{
  "response": [
    {
      "success": True
    }
  ]
}
```

#### Permit or Block Sender

This action is used to permit or block a sender.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|action|string|block|True|Either 'permit' (to bypass spam checks) or 'block' (to reject the email)|['block', 'permit']|block|
|sender|string|None|True|The email address of the external sender|None|user@example.com|
|to|string|None|True|The email address of the internal recipient|None|user@example.com|

Example input:

```
{
  "action": "block",
  "sender": "user@example.com",
  "to": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|[]managed_sender|False|The Managed Sender that was created|

Example output:

```
{
  "response": [
    {
      "id": "MTOKEN:eNoVzbEOgjAUQNF_eTMDGArK1oC2GARFjTpi-zQQ28ZWDGr8d3G-ybkfcCh6i62EBM4MB5Z2hpIiWlM_n0tecYv8nkXLBVH8WOvVTb_Kfcze-ZWefDUUzWHXVeYS1jHdgAeidw-j0AojcRTTbZkFNJ6RcGxPtK41GpLAA9Voh1r-t5OATL8_1zIraQ",
      "sender": "user@example.com",
      "to": "user@example.com",
      "type": "Block"
    }
  ]
}
```

#### Create Blocked Sender Policy

This action is used to create a blocked sender policy.

##### Input

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|description|string|None|True|A description for the policy which is kept with the email in the archive for future reference|None|A description|
|from_part|string|envelope_from|True|Must be: envelope_from, header_from or both|['envelope_from', 'header_from', 'both']|envelope_from|
|from_type|string|everyone|True|Can be one of: everyone, internal_addresses, external_addresses, email_domain, profile_group or individual_email_address|['everyone', 'internal_addresses', 'external_addresses', 'email_domain', 'profile_group', 'individual_email_address']|internal_addresses|
|from_value|string|None|False|Required if `From Type` is one of email_domain, profile_group, individual_email_address. Expected values: If `From Type` is email_domain, a domain name without the @ symbol. If `From Type` is profile_group, the ID of the profile group. If `From Type` is individual_email_address, an email address|None|user@example.com|
|option|string|block_sender|True|The block, option must be: no_action or block_sender|['block_sender', 'no_action']|block_sender|
|source_ips|string|None|False|A comma separated list of IP addresses using CIDR notation (X.X.X.X/XX). When set the policy only applies for connections from matching addresses|None|198.51.100.0/24|
|to_type|string|everyone|True|Can be one of: everyone, internal_addresses, external_addresses, email_domain, profile_group or individual_email_address|['everyone', 'internal_addresses', 'external_addresses', 'email_domain', 'profile_group', 'individual_email_address']|everyone|
|to_value|string|None|False|Required if `To Type` is one of email_domain, profile_group, individual_email_address. Expected values: If `To Type` is email_domain, a domain name without the @ symbol. If `To Type` is profile_group, the ID of the profile group. If `To Type` is individual_email_address, an email address|None|user@example.com|

Example input:

```
{
  "description": "komand test",
  "from_part": "envelope_from",
  "from_type": "email_domain",
  "from_value": "rapid7.com",
  "option": "block_sender",
  "source_ips": "198.51.100.0/24",
  "to_type": "everyone",
  "to_value": "example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|sender_policy|[]sender_policy|False|The policy that was created|

Example output:

```
{
  "response": [
    {
      "option": "block_sender",
      "id": "eNo1jU0LgjAYgP_LrgpusZl2EzWwUoaKJHibb7W-pk4tif57euj-fHyQBjF0IGu0QW0c20cSFkXgKt_Z2Zz6nNN8wjqU5aqyEuOcRmP6arfgGXl_Si_X_UE0-p0pGFhl6RsyUaPuUkxLjzDiONREYtC9ekAnVA3zxc-SgHhrl9GZHqHTUj1n-G_mUwPRYmNM8fcHIHEysg",
      "policy": {
        "description": "komand test",
        "fromPart": "envelope_from",
        "from": {
          "type": "email_domain",
          "emailDomain": "example.com"
        },
        "to": {
          "type": "everyone"
        },
        "fromType": "email_domain",
        "fromValue": "example.com",
        "toType": "everyone",
        "fromEternal": true,
        "toEternal": true,
        "fromDate": "1900-01-01T00:00:00+0000",
        "toDate": "2100-01-01T23:59:59+0000",
        "override": false,
        "bidirectional": false,
        "conditions": {},
        "createTime": "2019-01-28T17:09:01+0000",
        "lastUpdated": "2019-01-28T17:09:01+0000"
      }
    }
  ]
}
```

#### Add Group Member

This action is used to add an email address or domain to a group.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|domain|string|None|False|A domain to add to a group. Use either email address or domain|None|rapid7.com|
|email_address|string|None|False|The email address of a user to add to a group. Use either email address or domain|None|user@example.com|
|id|string|None|True|The Mimecast ID of the group to add to|None|eNoVzssKgkAUgOF3OWuhvDHlTjMqgjIilWgzN0UdHZnjBBK9e7b_-fg_gJJbIxsBEdB2Dl-r1HDCMLeHuufXTZyt8_Gou3l_i21JWeK3TOgJizrBvFM0ez5EaDwcytO5AAeUoCNEFVUoHeAWJ91Lw7WQi7-7X1I3JtswWMK3NNjoASLXgUorIc3_ISA-8b4_Gl8xjA|

Example input:

```
{
  "domain": "rapid7.com",
  "email_address": "user@example.com",
  "id": "eNoVzssKgkAUgOF3OWuhvDHlTjMqgjIilWgzN0UdHZnjBBK9e7b_-fg_gJJbIxsBEdB2Dl-r1HDCMLeHuufXTZyt8_Gou3l_i21JWeK3TOgJizrBvFM0ez5EaDwcytO5AAeUoCNEFVUoHeAWJ91Lw7WQi7-7X1I3JtswWMK3NNjoASLXgUorIc3_ISA-8b4_Gl8xjA"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|email_address|string|False|The email address of the user that was added to the group|
|folder_id|string|False|The Mimecast ID of the group that the user / domain was added to|
|id|string|False|The Mimecast ID of the user / domain that was added to the group|
|internal|boolean|False|Whether or not the user or domain is internal|

Example output:

```
{
  "id": "eNqrVipOTS4tSs1MUbJSctdOd43RNy3K9klKdA038M4xq8otcfIMqTQods2MNIrR99NOD_IsCyovdEt11A4pSQvKyPL2SS4orgjOTy01jdEvzlbSUUouLS7Jz00tSs5PSQUa6hzs52LoaG5pagKUK0stKs7Mz1OyMtRRSsvPSUktysnMywZZbmxgYmFRCwBatS7G",
  "folder_id": "eNoVzrkOgkAUQNF_eTWFIIjQEdk0OEaUgCUyD8HMojNiROO_i_3Nyf2AxmZQ2FPwgUgRxWbnzZOxKwsyiCjP-BnTe7jYxA5Pq1xsmRhJ4Sbv9SU4zfgrq8vjdSdbO3eDPRjAaH0Dv62ZRgOaQT8kR9VIihO_OpDQDFzPsafwiUr3UoBvGtBKRlH9F-ylZXnfH3hjMBs",
  "email_address": "user@example.com",
  "internal": true
}
```

#### Delete Group Member

This action is used to remove an email address or domain from a group.
Delete on an email or domain that does not exist will result in no operation performed.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|domain|string|None|False|A domain to remove from group. Use either email address or domain|None|rapid7.com|
|email_address|string|None|False|The email address to remove from group. Use either email address or domain|None|user@example.com|
|id|string|None|True|The Mimecast ID of the group to remove from|None|eNoVzssKgkAUgOF3OWuhvDHlTjMqgjIilWgzN0UdHZnjBBK9e7b_-fg_gJJbIxsBEdB2Dl-r1HDCMLeHuufXTZyt8_Gou3l_i21JWeK3TOgJizrBvFM0ez5EaDwcytO5AAeUoCNEFVUoHeAWJ91Lw7WQi7-7X1I3JtswWMK3NNjoASLXgUorIc3_ISA-8b4_Gl8xjA|

Example input:

```
{
  "domain": "rapid7.com",
  "email_address": "user@example.com",
  "id": "eNoVzssKgkAUgOF3OWuhvDHlTjMqgjIilWgzN0UdHZnjBBK9e7b_-fg_gJJbIxsBEdB2Dl-r1HDCMLeHuufXTZyt8_Gou3l_i21JWeK3TOgJizrBvFM0ez5EaDwcytO5AAeUoCNEFVUoHeAWJ91Lw7WQi7-7X1I3JtswWMK3NNjoASLXgUorIc3_ISA-8b4_Gl8xjA"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Status of success of the delete operation|

Example output:

```
{
  "success": true
}
```

#### Decode URL

This action is used to decode a Mimecast encoded URL.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|encoded_url|string|None|True|The Mimecast encoded URL|None|https://protect-xx.mimecast.com/TXH7fhe|

Example input:

```
{
  "encoded_url": "https://protect-xx.mimecast.com/TXH7fhe"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|decoded_url|string|True|Original decoded URL|

Example output:

```
{
  "decoded_url": "https://example.com"
}
```

#### Find Groups

This action is used to find groups that match a given query.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|query|string|None|False|A string to query for|None|mygroup|
|source|string|cloud|True|A group source to filter on, either "cloud" or "ldap"|['cloud', 'ldap']|cloud|

Example input:

```
{

  "query": "exam.*",
  "source": "cloud"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|groups|[]group|False|A list of groups that mach the query|

Example output:

```
{
  "groups": [
    {
      "id": "eNoVzrEOgjAUQNF_eTMDaLGBDSUCBjAWjDqS9qGYlmorRjH-u7jfnNwPWOSDwU5ACJkbXJLZklWJ5nlBajWyFaeY3uPFZu2r9Mj6Qvbvck-TMTtHJ1e98uZQX7e6JYxGO3BAiuYGYdtIiw7wwT60QsO1wIlfVWXsRTTwyRQ-0dhO9xB6DrRaCjT_BULn1Pv-ACT0L3A",
      "description": "Relay",
      "source": "cloud",
      "parentId": "eNoVzr0OgjAUQOF3uasMkFAq3RqJ4h8E1IAjaS8EU6i2oqLx3cX95Mv5gEUxGGwlMHgWzUgCvk2t0HbI5iFXM0kxvkXBZkm6uMz7verH5ERX73XDz2732lXF8ZLq2s8pz8ABJasrsLpSFh0Qg73rDo3QEid-cUgij9OQ-FP4QGNb3QPzHKi1kmj-C-73B7L7LyY",
      "userCount": 0,
      "folderCount": 0
    },
    {
      "id": "eNoVzssOgjAQQNF_mTWJoGAjOwIqGkVFQUnc1HYgaKHaCvER_x3c35zcL2hkjcKSgwsqbWlmJmx6Hmz9NNAXJymam8LwEYyXM6cKT3G9FvU7Ssj8syi8zKxeK3o8XDcyt2Pi7cAAwekd3JwKjQawRj9lhYpJjr3v76PA8sjEsfuwRaVLWYNrGZBLwVH9H2wyIsNfB8G2MJw",
      "description": "Permitted senders",
      "source": "cloud",
      "parentId": "eNoVzr0OgjAUQOF3uasMkFAq3RqJ4h8E1IAjaS8EU6i2oqLx3cX95Mv5gEUxGGwlMHgWzUgCvk2t0HbI5iFXM0kxvkXBZkm6uMz7verH5ERX73XDz2732lXF8ZLq2s8pz8ABJasrsLpSFh0Qg73rDo3QEid-cUgij9OQ-FP4QGNb3QPzHKi1kmj-C-73B7L7LyY",
      "userCount": 0,
      "folderCount": 0
    }
  ]
}
```

#### Get TTP URL Logs

This action is used to get TTP URL logs.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|from|string|None|False|Start date of logs to return in the following format 2015-11-16T14:49:18+0000. Default is the start of the current day|None|2018-11-22T14:49:18+0000|
|max_pages|integer|100|False|Max pages returned, default 100|None|10|
|page_size|integer|10|False|The number of logs returned per page, default value is 10|None|10|
|route|string|all|True|Filters logs by route, must be one of inbound, outbound, internal, or all|['all', 'inbound', 'outbound', 'internal']|inbound|
|scan_result|string|all|True|Filters logs by scan result, must be one of clean, malicious, or all|['clean', 'malicious', 'all']|malicious|
|to|string|None|False|End date of logs to return in the following format 2015-11-16T14:49:18+0000. Default is time of request|None|2018-11-22T14:49:18+0000|
|url_to_filter|string|None|False|Regular expression to filter on. e.g. `examp` will return only URLs with the letters examp in them|None|exam.*|

Example input:

```
{
  "from": "2019-04-23T11:00:00+0000",
  "route": "all",
  "scan_result": "all",
  "to": "2019-04-28T11:00:00+0000"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|click_logs|[]click_logs|False|Click Logs|

Example output:

```
{
  [
    {
       "userEmailAddress": "user@example.com",
       "url": "https://www.dummy-mimecast-blacklist.com",
       "ttpDefinition": "Default URL Protection Definition",
       "action": "warn",
       "adminOverride": "N/A",
       "userOverride": "None",
       "scanResult": "malicious",
       "category": "Compromised",
       "userAwarenessAction": "N/A",
       "date": "2019-04-23T19:50:28+0000",
       "route": "inbound"
    }
  ]
}
```

### Triggers

_This plugin does not contain any triggers._

## Troubleshooting

For the Create Managed URL action, the URL must include `http://` or `https://` e.g. `http://google.com`
Most common cloud [URLs](https://www.mimecast.com/tech-connect/documentation/api-overview/global-base-urls/)

### Custom Output Types

#### click_logs

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Action|string|False|The action that was taken for the click|
|Admin Override|string|False|The action defined by the administrator for the URL|
|Category|string|False|The category of the URL clicked|
|Date|string|False|The date that the URL was clicked|
|Route|string|False|The route of the email that contained the link|
|Scan Result|string|False|The result of the URL scan|
|TTP Definition|string|False|The description of the definition that triggered the URL to be rewritten by Mimecast|
|URL|string|False|The URL clicked|
|User Awareness Action|string|False|The action taken by the user if user awareness was applied|
|User Email Address|string|False|The email address of the user who clicked the link|
|User Override|string|False|The action requested by the user|

#### group

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Description|string|False|The name of the group|
|Folder Count|integer|False|None|
|Id|string|False|None|
|Parent Id|string|False|None|
|Source|string|False|None|
|User Count|integer|False|None|

#### managed_sender

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|The Mimecast secure ID of the managed sender object|
|Sender|string|False|The email address of the external sender|
|To|string|False|The email address of the internal recipient|
|Type|string|False|Either 'permit' (to bypass spam checks) or 'block' (to reject the email)|

#### managed_url

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Action|string|False|Either block or permit|
|Comment|string|False|The comment that was posted in the request|
|Click Logging|boolean|False|If logging of user clicks on the URL is disabled|
|URL Rewriting|boolean|False|If rewriting of this URL in emails is disabled|
|User Awareness|boolean|False|If User Awareness challenges for this URL are disabled|
|Domain|string|False|The managed domain|
|ID|string|False|The Mimecast secure ID of the managed URL|
|Match Type|string|False|Either 'explicit' or 'domain'|
|Port|integer|False|Port|
|Scheme|string|False|The protocol to apply for the managed URL. Either HTTP or HTTPS|

#### policy

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Bidirectional|boolean|False|If the policy is also applied in the reverse of the email flow, i.e. where the specified recipient in the policy becomes the sender, and the specified sender in the policy becomes the recipient|
|Conditions|object|False|An object with fields describing additional conditions that should affect when the policy is applied|
|Description|string|False|The description for the policy which is kept with the email in the archive for future reference|
|From|object|False|An object containing type and value fields defining which sender addresses the policy applies to|
|From Date|string|False|The date that the policy will apply from|
|From Eternal|boolean|False|If the policy is always applied or if there is a specific start date|
|From Part|string|False|Which from address is used in the policy. Can be any of envelope_from, header_from, both|
|From Type|string|False|Which sender addresses the policy applies to. CCan be one of everyone, internal_addresses, external_addresses, email_domain, profile_group, address_attribute_value, individual_email_address, free_mail_domains, header_display_name|
|From Value|string|False|A value defining which senders the policy applies to|
|Override|boolean|False|If true, this option overrides the order in which the policy is applied, and forces it to be applied first if there are multiple applicable policies, unless more specific policies of the same type have been configured with an override as well|
|To|object|False|An object containing type and value fields defining which recipient addresses the policy applies to|
|To Date|string|False|The date that the policy will apply until|
|To Eternal|boolean|False|If the policy should always be applied or if there is an end date|
|To Type|string|False|Which recipient addresses the policy applies to. Can be one of everyone, internal_addresses, external_addresses, email_domain, profile_group, address_attribute_value, individual_email_address, free_mail_domains, header_display_name|

#### sender_policy

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|The Mimecast ID of the policy. Used when updating the policy|
|Option|string|False|The option set for the policy. Will be one of no_action, block_sender|
|Policy|policy|False|The policy that was created|

# Version History

* 4.2.0 - New action Get Hold Message List | New action Get Message Hold Summary List | New action Reject Message | New action Release Message | New action Create Remediation Incident | New action Get Remediation Incident | New action Search File Hash | New action Get Threat Intel Feed | New action Message Finder Search | New action Get Message Info | New action File Upload | New action Send Email
* 4.1.0 - Update Get TTP URL Logs action to use pagination
* 4.0.1 - Add example inputs
* 4.0.0 - Update Get TTP URL Logs to allow for better URL filtering
* 3.1.0 - New action Delete Managed URL and Delete Group Member
* 3.0.1 - New spec and help.md format for the Extension Library
* 3.0.0 - Add URL in Get TTP URL Logs action to filter output | Update connection settings to the proper authentication supported by the Mimecast API
* 2.5.0 - New action Decode URL
* 2.4.0 - New action Get TTP URL Logs
* 2.3.0 - New actions Add Group Member and Find Group
* 2.2.0 - New action Create Blocked Sender Policy
* 2.1.0 - New action Permit or Block Sender
* 2.0.0 - Add Get Managed URL Action | Update descriptions and output titles
* 1.0.0 - Initial plugin

# Links

## References

* [Mimecast API](https://www.mimecast.com/developer/documentation)
