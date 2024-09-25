#input history

his = []
his_length = len(his)
correct_guess = '''
                       
┏┏┓┏┓┏┓┏┓┏╋    ┏┓┓┏┏┓┏┏
┗┗┛┛ ┛ ┗ ┗┗    ┗┫┗┻┗ ┛┛
                ┛      

'''
wrong ='''
                       
┓┏┏┏┓┏┓┏┓┏┓    ┏┓┓┏┏┓┏┏
┗┻┛┛ ┗┛┛┗┗┫    ┗┫┗┻┗ ┛┛
          ┛     ┛      

'''
game_over ='''
  ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                     ░                   

'''
won ='''
                 _,.---._                                ,-.-.    _,.---._    .-._         
 ,--.-.  .-,--.,-.' , -  `.  .--.-. .-.-.       ,-..-.-./  \==\ ,-.' , -  `. /==/ \  .-._  
/==/- / /=/_ //==/_,  ,  - \/==/ -|/=/  |       |, \=/\=|- |==|/==/_,  ,  - \|==|, \/ /, / 
\==\, \/=/. /|==|   .=.     |==| ,||=| -|       |- |/ |/ , /==/==|   .=.     |==|-  \|  |  
 \==\  \/ -/ |==|_ : ;=:  - |==|- | =/  |        \, ,     _|==|==|_ : ;=:  - |==| ,  | -|  
  |==|  ,_/  |==| , '='     |==|,  \/ - |        | -  -  , |==|==| , '='     |==| -   _ |  
  \==\-, /    \==\ -    ,_ /|==|-   ,   /         \  ,  - /==/ \==\ -    ,_ /|==|  /\ , |  
  /==/._/      '.='. -   .' /==/ , _  .'          |-  /\ /==/   '.='. -   .' /==/, | |- |  
  `--`-`         `--`--''   `--`..---'            `--`  `--`      `--`--''   `--`./  `--`  

'''
title = '''
 .----------------.  .----------------.  .-----------------. .----------------.  .----------------.  .----------------.  .-----------------.
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  ____  ____  | || |      __      | || | ____  _____  | || |    ______    | || | ____    ____ | || |      __      | || | ____  _____  | |
| | |_   ||   _| | || |     /  \     | || ||_   \|_   _| | || |  .' ___  |   | || ||_   \  /   _|| || |     /  \     | || ||_   \|_   _| | |
| |   | |__| |   | || |    / /\ \    | || |  |   \ | |   | || | / .'   \_|   | || |  |   \/   |  | || |    / /\ \    | || |  |   \ | |   | |
| |   |  __  |   | || |   / ____ \   | || |  | |\ \| |   | || | | |    ____  | || |  | |\  /| |  | || |   / ____ \   | || |  | |\ \| |   | |
| |  _| |  | |_  | || | _/ /    \ \_ | || | _| |_\   |_  | || | \ `.___]  _| | || | _| |_\/_| |_ | || | _/ /    \ \_ | || | _| |_\   |_  | |
| | |____||____| | || ||____|  |____|| || ||_____|\____| | || |  `._____.'   | || ||_____||_____|| || ||____|  |____|| || ||_____|\____| | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 

'''
HangMan = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
current_hangman = 0 
welcome = '''
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| | _____  _____ | || |  _________   | || |   _____      | || |     ______   | || |     ____     | || | ____    ____ | || |  _________   | |
| ||_   _||_   _|| || | |_   ___  |  | || |  |_   _|     | || |   .' ___  |  | || |   .'    `.   | || ||_   \  /   _|| || | |_   ___  |  | |
| |  | | /\ | |  | || |   | |_  \_|  | || |    | |       | || |  / .'   \_|  | || |  /  .--.  \  | || |  |   \/   |  | || |   | |_  \_|  | |
| |  | |/  \| |  | || |   |  _|  _   | || |    | |   _   | || |  | |         | || |  | |    | |  | || |  | |\  /| |  | || |   |  _|  _   | |
| |  |   /\   |  | || |  _| |___/ |  | || |   _| |__/ |  | || |  \ `.___.'\  | || |  \  `--'  /  | || | _| |_\/_| |_ | || |  _| |___/ |  | |
| |  |__/  \__|  | || | |_________|  | || |  |________|  | || |   `._____.'  | || |   `.____.'   | || ||_____||_____|| || | |_________|  | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 


'''

line = '____________________________________________________________________________________________________________________________________________'
line2 = '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
print (welcome)
print(line)
print(title)
import random
from replit import clear

meaningful_words = [

    'apple', 'banana', 'orange', 'grape', 'strawberry', 'watermelon', 'kiwi', 'pineapple', 'mango', 'pear',
    'carrot', 'broccoli', 'spinach', 'tomato', 'cucumber', 'lettuce', 'bell pepper', 'onion', 'potato', 'zucchini',
    'car', 'truck', 'bus', 'motorcycle', 'bicycle', 'scooter', 'van', 'train', 'boat', 'plane',
    'lemon', 'lime', 'blueberry', 'cherry', 'avocado', 'pumpkin', 'eggplant', 'celery', 'cabbage', 'cauliflower',
    'jeep', 'ambulance', 'firetruck', 'helicopter', 'submarine', 'rocket', 'hovercraft', 'tractor', 'skateboard', 'segway'
]

#random selection and assigning
seleceted_word = random.choice(meaningful_words)
#seleceted_word ='cherry'
#print(seleceted_word)
guess_length=len(seleceted_word)
guess_list=[]
for i in range(guess_length):
    guess_list.append('_')

print('Welcome to Hangman')



#initial Input
print(line)
print(line)

initial_choice = input('Enter a letter : ')
initial_choice = initial_choice.lower()
his.append(initial_choice)
check = False



#intial check
while check == False:
    for i in range(guess_length):
        if seleceted_word[i] == initial_choice:
            guess_list[i] = initial_choice
            check = True
            
    if check == False:
        print('letter not present in the word ! Guess again')
        initial_choice = input('Enter a letter')
print(line2)



        
#printing the current status
def print_status():
    clear()       
    guess_str=''
    for i in range(guess_length):
        guess_str += str(guess_list[i])+' '
    
    guess_str = guess_str.upper()  
    print(guess_str)
    
    
    
    
print_status()


#findin check lenth or no of char should be guessed
def check_lenthOf():
    check_lenth = 0
    for i in range(guess_length):
        if guess_list[i]== '_':
            check_lenth+=1
    
    return check_lenth
        
#no ofchances
trials = 6

def check_word(guess,trials,check_length):
    isPresent = False
    for i in range(guess_length):
        if guess == seleceted_word[i]:
             guess_list[i] = guess
             isPresent=True

            
    if isPresent==True:
        print(correct_guess)
        his.append(guess)
        print_status()
    else:
        print_status()
        trials-=1
        print(wrong)
        his.append(guess)
        print(f'You have {trials} left')
        
    return isPresent  

    
#history checking 
def CheckHistory(item,l):
    for i in range(l):
        if his[i] == item:
            return True
    return False
            
NotPresent = False    

check_lenth = check_lenthOf()
while check_lenth != 0 and trials != 0:
    guess = input("Enter your guess : ")
    guess = guess.lower()
    his_length=len(his)
    NotPresent = CheckHistory(guess,his_length)
    if not NotPresent :
        isPresent = check_word(guess,trials,check_lenth)
        if isPresent:
            check_lenth = check_lenthOf()
        else:
            trials-=1
            current_hangman+=1
            
    else:
        print('You have already Guessed this guess Another')
        
    #print(check_lenth)
    print(HangMan[current_hangman])
    print(line2)
    
    
    
    
if check_lenth==0:
    print(won)
elif trials == 0:
    print(f'Correct word is {seleceted_word}')
    print(game_over)
else:
    print('Error')


