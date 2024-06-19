class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    CYAN = "\033[36m"

def banner():
    font=print(bcolors.CYAN + """"

    
  /$$$$$$  /$$   /$$ /$$$$$$$$  /$$$$$$   /$$$$$$              
 /$$__  $$| $$  | $$| $$_____/ /$$__  $$ /$$__  $$             
| $$  \__/| $$  | $$| $$      | $$  \__/| $$  \__/             
| $$ /$$$$| $$  | $$| $$$$$   |  $$$$$$ |  $$$$$$              
| $$|_  $$| $$  | $$| $$__/    \____  $$ \____  $$             
| $$  \ $$| $$  | $$| $$       /$$  \ $$ /$$  \ $$             
|  $$$$$$/|  $$$$$$/| $$$$$$$$|  $$$$$$/|  $$$$$$/             
 \______/  \______/ |________/ \______/  \______/              
                                                               
                                                               
                                                               
 /$$$$$$$$ /$$   /$$ /$$$$$$$$                                 
|__  $$__/| $$  | $$| $$_____/                                 
   | $$   | $$  | $$| $$                                       
   | $$   | $$$$$$$$| $$$$$                                    
   | $$   | $$__  $$| $$__/                                    
   | $$   | $$  | $$| $$                                       
   | $$   | $$  | $$| $$$$$$$$                                 
   |__/   |__/  |__/|________/                                 
                                                               
                                                               
                                                               
 /$$   /$$ /$$   /$$ /$$      /$$ /$$$$$$$  /$$$$$$$$ /$$$$$$$ 
| $$$ | $$| $$  | $$| $$$    /$$$| $$__  $$| $$_____/| $$__  $$
| $$$$| $$| $$  | $$| $$$$  /$$$$| $$  \ $$| $$      | $$  \ $$
| $$ $$ $$| $$  | $$| $$ $$/$$ $$| $$$$$$$ | $$$$$   | $$$$$$$/
| $$  $$$$| $$  | $$| $$  $$$| $$| $$__  $$| $$__/   | $$__  $$
| $$\  $$$| $$  | $$| $$\  $ | $$| $$  \ $$| $$      | $$  \ $$
| $$ \  $$|  $$$$$$/| $$ \/  | $$| $$$$$$$/| $$$$$$$$| $$  | $$
|__/  \__/ \______/ |__/     |__/|_______/ |________/|__/  |__/
                                                               
                                                               
                                                               

    
    
    
    """)
    print(font)
if __name__ == "__main__":
    banner()



import random
import math





users_name = input(bcolors.GREEN + "What is your name >")
print("Hello " + users_name)

print(bcolors.GREEN + "You will pick an upper bound number and a lower bound number.")
print(bcolors.GREEN + "Then i will choose a random number between those numbers and your job is to figure out which number it is.")



lower = input(bcolors.YELLOW + "Pick a lower bound number>")
print(bcolors.YELLOW + "OK " + users_name)
upper = input(bcolors.YELLOW + "Pick an upper bound>")


correct_number = random.randrange(int(lower), int(upper))


number_of_guessess =  round(math.log(correct_number)) + 1


print(bcolors.YELLOW + "\n\tYouv'e only got ", number_of_guessess, "turns to guess the number!Begin!")

count = 0

while count < number_of_guessess:
    count += 1
    users_guess = float(input(bcolors.RED + "Guess the number>"))

    if users_guess == correct_number:
        print(bcolors.GREEN + "Correct!You guessed the number in your " + str(count) + " try.")
    elif count >= number_of_guessess:
        print(bcolors.RED + "Ooops!Youv'e run out of guesses.")
        print(bcolors.RED + "The number is ", correct_number)
        break


    elif users_guess >= correct_number:
        print(bcolors.YELLOW + "You guessed too high!")
    elif users_guess <= correct_number:
        print(bcolors.YELLOW + "You guessed too low")
    else:
        continue


    









