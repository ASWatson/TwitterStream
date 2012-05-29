import os
import shelve
import urllib
import urlparse
import sys
import shelve
import oauth2 as oauth

consumer_key = ''
consumer_secret = ''

request_token_url = 'https://api.twitter.com/oauth/request_token'
access_token_url = 'https://api.twitter.com/oauth/access_token'
authorize_url = 'https://api.twitter.com/oauth/authorize'

class Config():

	#Initial configuration with the consumer key and consumer script. 
	def __init__(self):
		#Check if consumer key and consumer secret are not null.

		if consumer_key == None:
			enter_config("1")
		if consumer_secret == None:
			enter_config("2")

		self._consumer_key = consumer_key
		self._consumer_secret = consumer_secret
		


	def get_access_token(self,consumer):

  		client = oauth.Client(consumer)

  		#Now, let's get the access token.
  		resp, content = client.request(request_token_url, "GET")
  		if resp['status'] != '200':
  			raise Exception("Invalid response %s." % resp['status'])

  		request_token = dict(urlparse.parse_qsl(content))

		print "Request Token:"
		print "    - oauth_token        = %s" % request_token['oauth_token']
		print "    - oauth_token_secret = %s" % request_token['oauth_token_secret']
	

		#Post the url on the command line. If this is being deployed in django then redirect the user to the link below.  

  		print "Go to the following link in your browser:"
  		print "%s?oauth_token=%s" % (authorize_url, request_token['oauth_token'])
  	


  		accepted = 'n'
  		while accepted.lower() == 'n':
  			accepted = raw_input('Have you authorized me? (y/n) ')
  		oauth_verifier = raw_input('What is the PIN? ')


  		token = oauth.Token(request_token['oauth_token'],
    	request_token['oauth_token_secret'])
  		token.set_verifier(oauth_verifier)
  		client = oauth.Client(consumer, token)

  		resp, content = client.request(access_token_url, "POST")
  		access_token = dict(urlparse.parse_qsl(content))

  		print "Access Token:"
  		print "    - oauth_token        = %s" % access_token['oauth_token']
  		print "    - oauth_token_secret = %s" % access_token['oauth_token_secret']
  		print
  		print "You may now access protected resources using the access tokens above." 
  		print

  		return access_token
  	
  	def enter_config(choice):
  		if choice == "1":
  				cosumer_key = raw_input('Consumer key missing. Enter here:')
  		if choice == "2":
  				consumer_secret = raw_input('Consumer secret missing. Enter here')

  	def oauth_call(self):
  		self._consumer = oauth.Consumer(self._consumer_key, self._consumer_secret)
  		self._access_token = self.get_access_token(self._consumer)
		self._token = oauth.Token(self._access_token['oauth_token'],self._access_token['oauth_token_secret'])
		self._client = oauth.Client(self._consumer, self._token)
		self.key_storage()
		


	def key_storage(self):
		key_storage = shelve.open('newconfig') #This will create a configurations file that will store the consumer key, consumer secret and access token. This file can be used across the system thus improving the API. 
		key_storage['consumer_key'] = self._consumer_key
		key_storage['consumer_secret'] = self._consumer_secret

		key_storage['client'] = self._client
		key_storage['oauth_token'] = self._access_token['oauth_token']
		key_storage['oauth_token_secret'] = self._access_token['oauth_token_secret'] 
		key_storage.close()


A = Config()
A.oauth_call()


