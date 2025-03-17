class User:
	def __init__(self, name, balance=0.0, credit_card=None):
		self.name = name
		self.balance = balance
		self.credit_card = credit_card 
		self.friends = set()
		self.activity_log = []

	def pay(self, payee, amount, reason=""):
		if amount <= 0:
			return "Amount not enough"

		if self.balance >= amount:
			self.balance -= amount
		elif self.credit_card:
			self.credit_card.charge(amount)
		else:
			"Insuficient funds"

		payee.balance += amount
		transaction = f"{self.name} paid {payee.name}"
		self.activity_log.append(transaction)
		payee.activity_log.append(transaction)
		return transaction

	def add_friend(self, friend):
	
		if friend not in self.friends:

			self.friends.add(friend)
			friend.friends.add(self)
			log = f"Friend added successfully"
			self.activity_log.append(log)
			friend.activity_log.append(log)

		return "Already a friend"



	def retrieve_activity(self):
		return self.activity_log	


		