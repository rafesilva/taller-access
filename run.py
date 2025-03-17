import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))  

from app.minivenmo import MiniVenmo
from app.models.credit_card import CreditCard

def main():
    app = MiniVenmo()

    bobby = app.create_user("Bobby", initial_balance=20, credit_card=CreditCard("Bobby", limit=100))
    carol = app.create_user("Carol", initial_balance=30, credit_card=CreditCard("Carol", limit=100))

    print("Users created successfully!")

    
    print("Transactions:")
    print(bobby.pay(carol, 25, "Coffee"))  
    print(carol.pay(bobby, 10, "Lunch"))

    
    print("Friendships:")
    print(carol.add_friend(bobby))
    print(bobby.add_friend(carol))

    
    print("MiniVenmo Feed:")
    feed = app.render_feed()
    for entry in feed:
        print(entry)


if __name__ == "__main__":
    main()
