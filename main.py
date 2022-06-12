#LOAD MODULES
from art import logo, vs
from game_data import data
import random
from replit import clear
def format_data(account):
  """format the account in a printable format NAME, A DESCRIPTION, FROM WHERE"""
  account_name = account["name"]
  account_desc = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_desc}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
  """Use if statement to check if user is correct"""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

#PRINT HIGHER LOWER LOGO
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)
# Generate random accounts from the game data
while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
      account_b = random.choice(data)
    
    
    print(f"Compare A: {format_data(account_a)}.")
    
    #PRINT VS LOGO
    print(vs)
    #LOAD B: NAME, A DESCRIPTION, FROM WHERE
    print(f"Against B: {format_data(account_b)}.\n")
    
    
    #ASK USER WHO HAS MORE FOLLOWERS A OR B
    guess = input("Who has more follows? A or B? ").lower()
    # Score keeping
     #CLEAR THE SCREEN BETWEEN ROUNDS
    clear()
    
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    ## Get follower count of each account
    
    ## use if statement to check if user is corret
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    
    # Give user feedback on guesses
    if is_correct:
      score+=1
      print(f"You're right! Current score: {score}")
      
    else: 
      print(f"Sorry, you're wrong. Final score: {score}")
      game_should_continue = False
   
