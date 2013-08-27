from Handler import *

class KidsHandler(Handler):
	def get(self):
		self.render('kids.html')

	def post(self):
		first_name = self.request.get('first_name')
		last_name = self.request.get('last_name')
		attending_service = self.request.get('attending_service')
		attending_party = self.request.get('attending_party')
		attending_friday = self.request.get('attending_friday')
		attending_sunday = self.request.get('attending_sunday')
		# error check form
		if first_name == '' or last_name == '' or attending_service == '' or attending_party == '' or attending_friday == '' or attending_sunday == '':
			self.render('kids.html', error=True)
		else:
			UserDatabase.addUser(first_name, last_name, attending_service, attending_party, attending_friday, attending_sunday)
			self.render('submitted.html')