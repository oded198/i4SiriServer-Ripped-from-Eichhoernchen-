import urllib2
import json

from plugin import *
class chucknorrisjoke(Plugin):

	@register ("en-US", ".*tell.*joke.*")
	@register ("en-GB", ".*tell.*joke.*")
	@register ("en-AU", ".*tell.*joke.*")
	def st_chucknorris(self, speech, language):
		if language == 'en-US' or language != 'en-US':
			req = urllib2.Request("http://jokes.tfound.org/jokebot/?format=json")
		full_json = urllib2.urlopen(req).read()
		load = json.loads(full_json)
		store = load['text']
		store = store.replace('&quot;','\"')
		store = store.replace('<br>',' ')
		store = store.replace('<br/>',' ')
		self.say(store)
		self.complete_request()