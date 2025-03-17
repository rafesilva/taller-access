from app.models.user import User
from app.models.credit_card import CreditCard

class MiniVenmo:

	def __init__(self):
		self.users = {}


	def create_user(self, name, initial_balance=0.0, credit_card=None):
		if name in self.users:
			return "User already exists"
		user = User(name, initial_balance)
		self.users[name] = user
		return user


	def render_feed(self):
		feed = []
		for user in self.users.values():
			feed.extend(user.retrieve_activity())

		return sorted(feed, reverse=True)



