class CreditCard:
	def __init__(self, owner, limit):
		self.owner = owner
		self.limit = limit
		self.user_credit = 0.0

	def charge(self, amount):

		if self.used_credit + amount > self.limit:
			return "Credit exceeded."

		self.used_credit += amount
		return f"Charged {amount} to {self.owner}'s credit card"

