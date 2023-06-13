############### Blackjack Project #####################
from art import logo
from replit import clear
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Calculate sum of a list`s all element
def sum_of_list(list):
  sum = 0
  for n in range(len(list)):
    sum += list[n]
  return sum


# Draw one card
def draw(cards):
  n = random.randint(0, len(cards) - 1)
  return cards[n]


# Filter Ace to be 11 or 1, for other cards, there`s no change
def filter_card(my_cards, card):
  if card == 11:
    if sum_of_list(my_cards) + card <= 21:
      return card
    else:
      return 1
  else:
    return card


# Computer draw cards
def computer_draw(my_cards):
  while sum_of_list(my_cards) < 17:
    card = draw(cards)
    card = filter_card(my_cards, card)
    my_cards.append(card)

def print_current_cards(player_cards, computer_cards):
  print(f"Your cards: {player_cards}, current score: {sum_of_list(player_cards)}")
  print(f"Computer`s first card: {computer_cards[0]}")

def print_final_cards(player_cards, computer_cards):
  print(f"Your final cards: {player_cards}, final score: {sum_of_list(player_cards)}")
  print(f"Computer`s final cards: {computer_cards}, final score: {sum_of_list(computer_cards)}")
  
def blackjack():
  play_or_not = input("Do you want to play Blackjack or not? Type 'y' or 'n': ").lower()
  # Exit game
  if play_or_not != 'y':
    return
  # Play the game
  else:
    clear()
    player_cards = []
    computer_cards = []
    result_from_player = False
    print(logo)
       
    # At beginning, draw two cards respectively for both player and computer
    card = draw(cards)
    player_cards.append(card)
    card = draw(cards)
    card = filter_card(player_cards, card)
    player_cards.append(card)
    card = draw(cards)
    computer_cards.append(card)
    card = draw(cards)
    card = filter_card(computer_cards, card)
    computer_cards.append(card)

    # Main game loop
    if sum_of_list(player_cards) == 21:
      print_final_cards(player_cards, computer_cards)
      print("Congratulation! You win! 😊")
    elif sum_of_list(computer_cards) == 21:
      print_final_cards(player_cards, computer_cards)
      print("Oops! You lose! 😭")
    else:
      print_current_cards(player_cards, computer_cards)
      
      # Player turn to decide who wins
      player_to_draw = input("Type 'y' to get another card, type 'n' to pass: ").lower()
      while player_to_draw == "y":
        card = draw(cards)
        card = filter_card(player_cards, card)
        player_cards.append(card)

        if sum_of_list(player_cards) > 21:
          computer_draw(computer_cards)
          print_final_cards(player_cards, computer_cards)
          print("Oops! You lose! 😭")
          player_to_draw = "n"
          result_from_player = True
        elif sum_of_list(player_cards) == 21:
          computer_draw(computer_cards)
          print_final_cards(player_cards, computer_cards)
          print("Congratulation! You win! 😊")
          player_to_draw = "n"
          result_from_player = True
        elif sum_of_list(player_cards) < 21:
          print_current_cards(player_cards, computer_cards)
          player_to_draw = input("Type 'y' to get another card, type 'n' to pass: ").lower()

      # Computer turn to decide who win
      if not result_from_player:
        computer_draw(computer_cards)
        if sum_of_list(computer_cards) > 21:
          print_final_cards(player_cards, computer_cards)
          print("Congratulation! You win! 😊")
        elif sum_of_list(computer_cards) == 21:
          print_final_cards(player_cards, computer_cards)
          print("Oops! You lose! 😭")
        else:
          if sum_of_list(computer_cards) > sum_of_list(player_cards):
            print_final_cards(player_cards, computer_cards)
            print("Oops! You lose! 😭")
          elif sum_of_list(computer_cards) == sum_of_list(player_cards):
            print_final_cards(player_cards, computer_cards)
            print("Draw!")
          else:
            print_final_cards(player_cards, computer_cards)
            print("Congratulation! You win! 😊")

    blackjack()


# Run the game
blackjack()