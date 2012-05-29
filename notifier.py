import sys
import os
import os.path



from twisted.internet import task
from twisted.internet import reactor
from twapi import TwitterApi
from sets import Set


timeout = 20.00 # Sixty seconds

def doWork():
    #do work here
    twapi.main('1')
    pass
def mention_notifier(self):
	s = Set([])
	A = TwitterApi()
	stat_new = A.get_replies()
	for status in stat_new:
		#print '%s: %s' % (status['user']['screen_name'], status['text'])
		s.update({status['user']['screen_name'], status['text']})
	if s - self.stat_old != None:
		self.stat_new = s - self.stat_old
		self.stat_old = s
		s = None
		print "hi"
	print self.stat_new
	#if list(set(stat_new) - set(stat_old)) != None:
	#	print stat_new - stat_old
	#	stat_old = stat_new
	#	stat_new = ""
	#	print "hello"
	#statuses_new = set(status_new) - set(statuses_old)
	#print statuses_new 
	pass
#l = task.LoopingCall(mention_notifier).start(timeout)


class Namespace(object): pass

if __name__ == "__main__":
    import sys
    self=Namespace()
    self.stat_old = Set([])
    self.stat_new = Set([])
    l = task.LoopingCall(mention_notifier,self).start(timeout)
    reactor.run()
#l.start(timeout) # call every sixty seconds

#reactor.run()
#A = TwitterApi()
#A.say_hi()