
'''
Python Wrapper for getdrip https://www.getdrip.com/
Nishant Nawarkhede
nishant.nawarkhede@gmail.com
'''

import requests
import json


class TokenNotFoundException(Exception):
    pass


class AccountIDNotFound(Exception):
    pass


class GetDripAPI(object):
    def __init__(self, **kwrds):

        if not 'token' in kwrds.keys():
            raise TokenNotFoundException('Please provide token.')

        if not 'account_id' in kwrds.keys():
            raise AccountIDNotFound('Please provide account id')

        self.token = kwrds['token']
        self.account_id = kwrds['account_id']
        self.api_url = 'https://api.getdrip.com/v2/'
        self.headers = {'Authorization': 'Bearer %s' % (self.token), 'Content-Type': 'application/vnd.api+json'}

    def fetch_all_campaign(self):
        url = self.api_url + '%s/campaigns/' % (self.account_id)
        response = requests.get(url, headers=self.headers)
        return response.status_code, response.json()

    def fetch_campaign(self, campaign_id):
        url = self.api_url + '%s/campaigns/%s' % (self.account_id, campaign_id)
        response = requests.get(url, headers=self.headers)
        return response.status_code, response.json()

    def fetch_accounts(self):
        url = self.api_url + 'accounts'
        response = requests.get(url, headers=self.headers)
        return response.status_code, response.json()

    def create_or_update_subscriber(self, payload):
        url = self.api_url + '%s/subscribers' % (self.account_id)
        response = requests.post(url, headers=self.headers, data=json.dumps(payload))
        return response.status_code, response.json()

    def create_or_update_subscriber_batch(self, payload):
        url = self.api_url + '%s/subscribers/batches' % (self.account_id)
        response = requests.post(url, headers=self.headers, data=json.dumps(payload))
        return response.status_code, response.json()

    def fetch_subscriber(self, subscriber_id):
        url = self.api_url + '%s/subscribers/%s' % (self.account_id, subscriber_id)
        response = requests.get(url, headers=self.headers)
        return response.status_code, response.json()

    def subscribe_subscriber(self, campaign_id, payload):
        url = self.api_url + '%s/campaigns/%s/subscribers' % (self.account_id, campaign_id)
        response = requests.post(url, headers=self.headers, data=json.dumps(payload))
        return response.status_code, response.json()

    def list_of_all_subscribers(self):
        url = self.api_url + '%s/subscribers' % (self.account_id)
        response = requests.get(url, headers=self.headers)
        return response.status_code, response.json()

    def delete_subscriber(self, subscriber_id):
        url = self.api_url + '%s/subscribers/%s' % (self.account_id, subscriber_id)
        response = requests.delete(url, headers=self.headers)
        return response.status_code

    def activate_campaign(self, campaign_id):
        url = self.api_url + '%s/campaigns/%s/activate' % (self.account_id, campaign_id)
        response = requests.post(url, headers=self.headers)
        return response.status_code

    def pause_campaign(self, campaign_id):
        url = self.api_url + '%s/campaigns/%s/pause' % (self.account_id, campaign_id)
        response = requests.post(url, headers=self.headers)
        return response.status_code

    def fetch_everyone_sucbscribed_to_campaign(self, campaign_id):
        url = self.api_url + '%s/campaigns/%s/subscribers' % (self.account_id, campaign_id)
        response = requests.get(url, headers=self.headers)
        return response.status_code, response.json()

    def tag_a_subscriber(self, payload):
        url = self.api_url + '%s/tags' % (self.account_id)
        response = requests.post(url, headers=self.headers, data=json.dumps(payload))
        return response.status_code, response.json()

    def untag_a_subscriber(self, email, tag):
        url = self.api_url + '%s/subscribers/%s/tags/%s' % (self.account_id, email, tag)
        response = requests.delete(url, headers=self.headers)
        return response.status_code

    def fetch_a_form(self, form_id):
        url = self.api_url + '%s/forms/%s' % (self.account_id, form_id)
        response = requests.get(url, headers=self.headers)
        return response.status_code, response.json()

    def fetch_list_of_goals(self):
        url = self.api_url + '%s/goals' % (self.account_id)
        response = requests.get(url, headers=self.headers)
        return response.status_code, response.json()

    def fetch_goal(self, goal_id):
        url = self.api_url + '%s/goals/%s' % (self.account_id, goal_id)
        response = requests.get(url, headers=self.headers)
        return response.status_code, response.json()
