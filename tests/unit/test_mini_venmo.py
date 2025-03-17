
import unittes
from app.mini_venmo import MiniVenmo
from models.credit_card import CreditCard


class TestMiniVenmo(unittest.TestCase):
	def setUp(self):
		self.app = MiniVenmo()
		self.bobby = self.create_user("Bobby", 50)
		self.carol = self.create_user("Carol", 35)

	def test_user_creation(self):
		self.assertEqual(self.bobby.name, "Bobby")
		self.assertEqual(self.bobby.balance, 50)
		self.assertIsNone(self.booby.credit_card)

	def test_payment_balance_sufficient(self):
		transaction = self.bobby.pay(self.bobby, 5, "Coffee")
		self.assertEqual(self.bobby.balance, 45)
		self.assertEqual(self.carol.balance, 35)
		self.assertIn("Bobby paid $5 for Coffee", self.bobby.activity_log)

	def test_payment_insufficient_balance_with_card(self):
		transaction = self.bobby.pay(self.bobby, 5, "Coffee")
		self.assertEqual(self.bobby.balance, 1)
		self.assertEqual(self.bobby.credit_card.used_credit, 5)
		self.assertIn("Bobby paid $5 for Coffee", self.bobby.activity_log)



	def test_add_friend(self):
		log = self.carol.add_friend(self.bobby)
		self.assertIn(self.bobby, self.carol.friends)
		self.assertIn(self.carol, self.bobby.friends)

	def test_render_feed(self):
		pass


if __name__ == "__main__":
	unittest.main()








