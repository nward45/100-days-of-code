from art import logo
import random
from replit import clear


cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

start_game = input("Would you like to play Blackjack? type 'y'or 'n' to cancel: ")

def deal_cards():
  card = random.choice(cards)
  return card

def calculate_score(player):
  #calculate who wins
  total = sum(player)
  if total > 21 and 11 in player:
    player[player.index(11)] = 1
    print(player)
    return sum(player)
  else:
    return total

def hit_card(player):
  player.append(deal_cards())

def compare(user, dealer):
  user_score = calculate_score(user)
  dealer_score = calculate_score(dealer)
  if user_score == 21:
    return "User wins!"
  elif dealer_score == 21:
    return "Dealer wins."
  elif user_score == dealer_score:
    return "Draw"
  elif user_score > 21:
    return "User busts. Dealer wins."
  elif dealer_score > 21:
    return "Dealer busts. User wins!"
  elif user_score > dealer_score:
    return "User wins!"
  elif user_score < dealer_score:
    return "Dealer wins!"
  else:
    return 'error'
    
def play_again():
  play_new_game = input("Would you like to play again? (y/n) ")
  if play_new_game == 'y':
    clear()
    play_game()
  

def play_game():
  print(logo)
  user = []
  dealer = []
  end_game = False
  
  for i in range(2):
    user.append(deal_cards())
    dealer.append(deal_cards())
  
  
  print(f"User cards {user}. User has {calculate_score(user)}")
  
  dealer_cards_shown = [dealer[0], " "]
  print(f"Dealer cards: {dealer_cards_shown}. Dealer has {dealer[0]}")

  if calculate_score(user) == 21 and calculate_score(dealer) != 21:
    print('Blackjack! User wins!')
    play_again()
    
  if calculate_score(user) != 21 and calculate_score(dealer) == 21:
    print('Blackjack! Dealer wins!')
    play_again()
  
  
  another_card = True
  
  while another_card:
    if calculate_score(user) > 21:
      print("User busts. Dealer wins.")
      another_card = False
    elif input("Would you like to hit? type 'y' for another card or 'n' to stay: ")=='y':
      user.append(deal_cards())
      print(f"User cards {user}. User has {calculate_score(user)}")
    else:
      another_card = False
  
  dealer_plays = True
  
  while dealer_plays:
    print(f"Dealer cards: {dealer}. Dealer has {calculate_score(dealer)}")
    if calculate_score(dealer) < 17:
      hit_card(dealer)
    else:
      dealer_plays = False
  
  winner = compare(user, dealer)
  print(winner)

  play_again()
    
play_game()