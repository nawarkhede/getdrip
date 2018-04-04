# python getdrip

A python wrapper for getdrip https://www.getdrip.com/ .

**Installation**

```
pip install getdrip
```

**Usage**

```
>>> from getdrip import GetDripAPI
>>> drip = GetDripAPI(token="<token>", account_id="<account_id>", application_name="<application_name>")
```

The application name is optional, and is sent as the User-Agent in the request to Drip if provided.


Method  | Description
------------- | -------------
fetch_all_campaign  | returns all campaigns
fetch_campaign  | returns specific campaign
fetch_campaign | return all accounts accociated
create_or_update_subscriber  | create new or update existing subscriber
create_or_update_subscriber_batch  | create new or update existing batch of subscriber
fetch_subscriber  | returns specific subscriber
subscribe_subscriber  | subscribe a subscriber
list_of_all_subscribers  | return list of all subscriber
delete_subscriber  | deletes existing subscriber
activate_campaign  | activates campaign
pause_campaign | pauses campaign
fetch_everyone_sucbscribed_to_campaign | returns everyone who is subscribed to campaign
tag_a_subscriber | tags a subscriber
untag_a_subscriber | untags a subscriber
fetch_a_form | returns a form
fetch_list_of_goals |  returns list of goals
fetch_goal | returns specific goal
record_event | sends a custom event
record_purchase | records a purchase


# Examples

**Returns all campaigns**
```
drip.fetch_all_campaign()
```

**Returns specific campaign**
```
drip.fetch_campaign(campaign_id)
```

**Return all accounts accociated**
```
drip.fetch_accounts()
```

**Create new or update existing subscriber**
```
drip.create_or_update_subscriber(payload)
payload = {
    'subscribers': [{
        'email': 'nishant.n@coverfox.com',
        'custom_fields': {
            'name': 'Nishant Nawarkhede'
        },
        'time_zone': 'America/Los_Angeles'
    }]
}
```

**Create new or update existing batch of subscriber**
```
drip.create_or_update_subscriber_batch(payload)
payload = {
    'batches': [{
        'subscribers': [{
            'tags': ['Customer', 'SEO'],
            'email': 'nawarkhede@live.com',
            'custom_fields': {
                'name': 'Nishant D. Nawarkhede'
            },
            'time_zone': 'America/Los_Angeles'
        }, {
            'tags': ['Prospect'],
            'email': 'nishant.nawarkhede@gmail.com',
            'custom_fields': {
                'name': 'Nishant N.'
            },
            'time_zone': 'America/Los_Angeles'
        }]
    }]
}
```

**Returns specific subscriber**
```
drip.fetch_subscriber(subscriber_id)
```

**Subscribe a subscriber**
```
drip.subscribe_subscriber(campign_id, payload)
payload = { 
    'subscribers': 

        [{ 
        'email': 'nawarkhede@live.com', 
        'custom_fields': { 
            'name': 'Nishant Nawarkhede' 
        } 
        }] 
}
```

**Return list of all subscriber**
```
drip.list_of_all_subscribers()
```

**Deletes existing subscriber**
```
drip.delete_subscriber(subscriber_id)
```

**Activates campaign**
```
drip.activate_campaign(ampaign_id)
```

**Pauses campaign**
```
drip.pause_campaign(campaign_id)
```

**Returns everyone who is subscribed to campaign**
```
drip.etch_everyone_sucbscribed_to_campaign(self, campaign_id):
```

**Tags a subscriber**
```
drip.tag_a_subscriber(payload)
payload= { 
          "tags": [{ 
            "email": "nawarkhede@live.com", 
            "tag": "SEO-123" 
          }] 
        }
```

**Untags a subscriber**
```
drip. untag_a_subscriber(email, tag)
```

**Returns a form**
```
drip.fetch_a_form(form_id)
```

**Returns list of goals**
```
drip.fetch_list_of_goals()
```

**Returns specific goal**
```
drip.fetch_goal(goal_id)

```

## Contributing

1. Fork it ( https://github.com/nawarkhede/getdrip/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request


## Contributors

1. Iqbal Abdullah (https://github.com/iq8al)
