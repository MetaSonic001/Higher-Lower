import random
from art import logo,vs
from game_data import data
from replit import clear

print(logo)

def fetch_data():
  return random.choice(data)

def detail_specific(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f" {name}, a {description}, from {country}"

def logic(acc1,acc2):
  global value
  if acc1>acc2:
    value="a"
    return value
  elif acc1<acc2:
    value ="b"
    return value
  else:
    print("error")

def play_game():
  score=0
  is_correct = True
  account1 = fetch_data()
  account2 = fetch_data()
  while is_correct:
    account1 = account2
    account2 = fetch_data()
    
    while account1 == account2:
      account2 = fetch_data()
      
    print(f"Compare A: {detail_specific(account1)}")
    print(vs)
    print(f"Against B: {detail_specific(account2)}")
    logic(account1["follower_count"],account2["follower_count"])
    print(account1["follower_count"],account2["follower_count"])
    
    print("Who do you think has more followers?")
    guess = input("Enter A or B: ").lower()
    
      
    if guess==value:
      print("You Win")
      score +=1
      clear()
      print(logo)
      print(f"You're right! Current score: {score}.")
      is_correct = True
      
    else:
      print("You Lose")
      is_correct = False
      print(f"Sorry, that's wrong. Final score: {score}")


play_game()



