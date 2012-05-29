import json
import urllib
import urlparse
import sys
import os
import os.path
import shelve
import oauth2 as oauth




#URLS
status_update_url = "https://api.twitter.com/1/statuses/update.json"
get_replies_url  = "https://api.twitter.com/1/statuses/replies/ids.json"


class TwitterApi():


    def __init__(self):

      self._get_keys()
      self._client = self._key_storage['client']
      user=dict()
    def update_status(self):
      data = {'status': raw_input("Enter status update:")}
      resp, content = self._client.request(status_update_url,'POST',urllib.urlencode(data))
      if resp['status'] != '200':
        print repr(resp)
      elif resp['status'] == 200:
        print repr(resp)

    def get_replies(self):
      username = list()
      resp,content = self._client.request(get_replies_url,'GET')
      if resp['status'] != '200':
        print repr(resp)
      else:
        statuses = json.loads(content)
       
      return statuses



    def _get_keys(self):
      self._key_storage = shelve.open('newconfig')

    def say_hi(self):
      print "hi"

class User():

    def __init__(self):
      pass



