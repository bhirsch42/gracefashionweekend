from Handler import *

class User(ndb.Model):
	first_name = ndb.StringProperty(required=True)
	last_name = ndb.StringProperty(required=True)
	attending_service = ndb.StringProperty(required=True)
	attending_party = ndb.StringProperty(required=True)
	attending_sunday = ndb.StringProperty(required=True)
	attending_friday = ndb.StringProperty(required=True)

def addUser(fname, lname, attendings, attendingp, attendingf, attendingsu):
	user = User(first_name=fname, last_name=lname, attending_service=attendings, attending_party=attendingp, attending_friday=attendingf, attending_sunday=attendingsu)
	user.put()