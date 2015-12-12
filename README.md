# python getdrip

A python wrapper for getdrip https://www.getdrip.com/ .

Installation    

```
pip install getdrip
```

Usage

```
>>> from getdrip import GetDripAPI
>>> drip = GetDripAPI(token="<token>", account_id="<account_id>")
```


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


# Examples
```
drip.fetch_all_campaign()
```

```
drip.fetch_campaign(campaign_id)
```

```
drip.fetch_accounts()
```

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

```
drip.fetch_subscriber(subscriber_id)
```

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

```
drip.list_of_all_subscribers()
```

```
drip.delete_subscriber(subscriber_id)
```

```
drip.activate_campaign(ampaign_id)
```

```
drip.pause_campaign(campaign_id)
```

```
drip.etch_everyone_sucbscribed_to_campaign(self, campaign_id):
```

```
drip.tag_a_subscriber(payload)
payload= { 
          "tags": [{ 
            "email": "nawarkhede@live.com", 
            "tag": "SEO-123" 
          }] 
        }
```
```
drip. untag_a_subscriber(email, tag)
```

```
drip.fetch_a_form(form_id)
```

```
drip.fetch_list_of_goals()
```

```
drip.fetch_goal(goal_id)

```


