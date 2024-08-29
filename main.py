import random
import requests
import colorama
from colorama import *
colorama.init(autoreset=True)





print(Style.BRIGHT + Fore.YELLOW + "\nWelcome to Battle Pokemon! This is a combat simulator where there can only be one winner.\n\nHow to play:\n\n1) Players will be asked to choose the number of rounds they would like to play.\n2) Each round the player will be randomly assigned a Pokemon. \n3) The player will be asked to compete with a choice of stat: id, height or weight.\n4) The player with the highest pokemon stat will win each round. \n5) At the end of the game, the game will show who the final winner is. \nThat's it! Good luck and let the battle begin.\n")



def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()

    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
    }

def set_rounds():
    default_rounds = 10
    while True:
        try:
            rounds = input(Fore.CYAN + "How many rounds would you like to play? (default: 10 rounds): ")
            # default case
            if (rounds == ""):
                return default_rounds

            # Validations
            if (not rounds.isdigit()):
                print(Fore.RED + "\nInvalid input! Try again!\n")
                continue
            rounds = int(rounds)
            if rounds < 1:
                print(Fore.RED + "\nYou cannot have less than 1 round. Please try again\n")
                continue
            else:
                print(Fore.GREEN +"\nLet's get started!\n")
                return rounds

        except:
            print(Fore.RED +"\nSomething went wrong.\n")
            continue
        
def pick_a_stat():
  while True:
    try:
      my_pokemon = random_pokemon()
      print(Fore.GREEN + '\nYou were given {}'.format(my_pokemon['name']))
      print(Fore.MAGENTA +'\nHere are the stats:')
      print(Fore.GREEN +'id: {}'.format(my_pokemon['id']))
      print(Fore.GREEN +'height: {}'.format(my_pokemon['height']))
      print(Fore.GREEN +'weight: {}'.format(my_pokemon['weight']))
      stat_choice = input(Fore.CYAN+'\nwhich stat would you like to use? (id, height, weight): ').lower()
      if (stat_choice != "id" and stat_choice != "height" and stat_choice != "weight"):
        print(Fore.RED +"\nThis is not a valid response. Please pick 'id', 'height' or weight'\n")
        continue
    except:
        print(Fore.RED + "\nSomething went wrong. Please pick 'id', 'height' or weight'\n")
    return stat_choice, my_pokemon 

def wins(rounds):
        round_number = 1
        counter = 0
        user_wins = 0
        computer_wins = 0
        draw = 0
        while True:
            if (counter == rounds):
               print(Fore.MAGENTA +"\nGame Over!")
               print(Fore.GREEN +f"\nYou won {user_wins} times.")
               print(Fore.RED +f"\nThe computer won {computer_wins} times.")
               print(Fore.YELLOW +f"\nYou both drew {draw} times! \n")
               break
            print(Fore.MAGENTA +'\nRound {}'.format(round_number))
            try:
               stat_choice, my_pokemon = pick_a_stat() 
               opponent_pokemon = random_pokemon()
               my_stat = my_pokemon[stat_choice]
               opponent_stat = opponent_pokemon[stat_choice]
               print(Fore.RED +"\nThe opponent's pokemon is {}\n".format(opponent_pokemon['name']))
               print(Fore.GREEN +stat_choice + ' of your pokemon ' + my_pokemon['name'] + ' is ' + str(my_stat))
               print(Fore.RED + stat_choice + ' of the opponent pokemon ' +    opponent_pokemon['name'] + ' is ' + str(opponent_stat))
               if (my_pokemon[stat_choice] > opponent_pokemon[stat_choice]):
                  print(Fore.GREEN +"\nYou Win!")
                  counter += 1
                  user_wins +=1
                  round_number +=1
               elif (my_pokemon[stat_choice] < opponent_pokemon[stat_choice]):
                  print(Fore.RED +"\nYou Lose!") 
                  counter += 1  
                  computer_wins +=1    
                  round_number +=1   
               else:
                  print(Fore.YELLOW +"\nDraw!")
                  counter += 1 
                  draw +=1
                  round_number +=1
            except:
                print(Fore.RED +"Something went wrong.")
                
        if user_wins > computer_wins:
            print (Fore.GREEN +"You won the game, Goodbye!")
        elif computer_wins > user_wins:
            print (Fore.RED +"You lost the game, Goodbye")
        else:
            print(Fore.YELLOW +"It's a draw! Goodbye")
    
        

def main():
    rounds = set_rounds()
    wins(rounds)
    


if __name__ == '__main__':
    main()
