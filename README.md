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

| Method                                 | Description                                       |
| -------------------------------------- | ------------------------------------------------- |
| fetch_all_campaign                     | returns all campaigns                             |
| fetch_campaign                         | returns specific campaign                         |
| fetch_campaign                         | return all accounts accociated                    |
| create_or_update_subscriber            | create new or update existing subscriber          |
| create_or_update_subscriber_batch      | create new or update existing batch of subscriber |
| fetch_subscriber                       | returns specific subscriber                       |
| subscribe_subscriber                   | subscribe a subscriber                            |
| list_of_all_subscribers                | return list of all subscriber                     |
| delete_subscriber                      | deletes existing subscriber                       |
| unsubscribe_from_all                   | remove a subscriber from all mailings             |
| activate_campaign                      | activates campaign                                |
| pause_campaign                         | pauses campaign                                   |
| remove_subscriber_from_campaign        | remove a subscriber from one or all campaigns     |
| fetch_everyone_sucbscribed_to_campaign | returns everyone who is subscribed to campaign    |
| tag_a_subscriber                       | tags a subscriber                                 |
| untag_a_subscriber                     | untags a subscriber                               |
| fetch_a_form                           | returns a form                                    |
| fetch_list_of_goals                    | returns list of goals                             |
| fetch_goal                             | returns specific goal                             |
| record_event                           | sends a custom event                              |
| record_purchase                        | records a purchase                                |
| create_or_update_cart                  | create new or update existing cart                |
| create_or_update_order                 | create new or update existing order               |
| create_or_update_product               | create new or update existing product             |

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

**Unsubscribe from all mailings**

```
drip.unsubscribe_from_all(subscriber_id)
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

**Remove subscriber from campaign**

```
drip.remove_subscriber_from_campaign(id_or_email, campaign_id=campaign_id)
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

**Create new or update existing cart**

```
drip.create_or_update_cart(payload)
payload = {
    "provider": "my_custom_platform",
    "email": "user@gmail.com",
    "action": "created",
    "cart_id": "456445746",
    "occurred_at": "2019-01-17T20:50:00Z",
    "cart_public_id": "#5",
    "grand_total": 16.99,
    "total_discounts": 5.34,
    "currency": "USD",
    "cart_url": "https://mysuperstore.com/cart/456445746",
    "items": [
      {
        "product_id": "B01J4SWO1G",
        "product_variant_id": "B01J4SWO1G-CW-BOTT",
        "sku": "XHB-1234",
        "name": "The Coolest Water Bottle",
        "brand": "Drip",
        "categories": [
          "Accessories"
        ],
        "price": 11.16,
        "quantity": 2,
        "discounts": 5.34,
        "total": 16.99,
        "product_url": "https://mysuperstore.com/dp/B01J4SWO1G",
        "image_url": "https://www.getdrip.com/images/example_products/water_bottle.png",
        "product_tag": "Best Seller"
      }
    ]
  }
```

**Create new or update existing order**

```
drip.create_or_update_order(payload)
payload = {
    "provider": "my_custom_platform",
    "email": "user@gmail.com",
    "action": "placed",
    "occurred_at": "2019-01-17T20:50:00Z",
    "order_id": "456445746",
    "order_public_id": "#5",
    "grand_total": 22.99,
    "total_discounts": 5.34,
    "total_taxes": 1.00,
    "total_fees": 2.00,
    "total_shipping": 5.00,
    "currency": "USD",
    "order_url": "https://mysuperstore.com/order/456445746",
    "items": [
      {
        "product_id": "B01J4SWO1G",
        "product_variant_id": "B01J4SWO1G-CW-BOTT",
        "sku": "XHB-1234",
        "name": "The Coolest Water Bottle",
        "brand": "Drip",
        "categories": [
          "Accessories"
        ],
        "price": 11.16,
        "sale_price": 10.16,
        "quantity": 2,
        "discounts": 5.34,
        "taxes": 1.00,
        "fees": 0.50,
        "shipping": 5.00,
        "total": 23.99,
        "product_url": "https://mysuperstore.com/dp/B01J4SWO1G",
        "image_url": "https://www.getdrip.com/images/example_products/water_bottle.png",
        "product_tag": "Best Seller"
      }
    ],
    "billing_address": {
      "label": "Primary Billing",
      "first_name": "Bill",
      "last_name": "Billington",
      "company": "Bills R US",
      "address_1": "123 Bill St.",
      "address_2": "Apt. B",
      "city": "Billtown",
      "state": "CA",
      "postal_code": "01234",
      "country": "United States",
      "phone": "555-555-5555"
    },
    "shipping_address": {
      "label": "Downtown Office",
      "first_name": "Ship",
      "last_name": "Shipington",
      "company": "Shipping 4 Less",
      "address_1": "123 Ship St.",
      "city": "Shipville",
      "state": "CA",
      "postal_code": "01234",
      "country": "United States",
      "phone": "555-555-5555"
    }
  }
```

**Create new or update existing product**

```
drip.create_or_update_product(payload)
payload = {
    "provider": "my_custom_platform",
    "action": "created",
    "occurred_at": "2019-01-28T12:15:23Z",
    "product_id": "B01J4SWO1G",
    "product_variant_id": "B01J4SWO1G-CW-BOTT",
    "sku": "XHB-1234",
    "name": "The Coolest Water Bottle",
    "brand": "Drip",
    "categories": [
      "Accessories"
    ],
    "price": 11.16,
    "inventory": 42,
    "product_url": "https://mysuperstore.com/dp/B01J4SWO1G",
    "image_url": "https://www.getdrip.com/images/example_products/water_bottle.png"
  }
```

## Contributing

1. Fork it ( https://github.com/nawarkhede/getdrip/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request

## Contributors

1. Iqbal Abdullah (https://github.com/iq8al)
