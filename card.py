import random
import replit

dealer = []
you = []
bust = 21
cards= [11,2,3,4,5,6,7,8,9,10,10,10,10]

points = {'dealer':0,'you':0}

cards_dealer = cards[:]
cards_user = cards[:]
 
def choose(round):
    if round < 2:
        dealer.append(random.choice(cards_dealer))
        cards_dealer.remove(dealer[round-1])
    you.append(random.choice(cards_user))
    cards_user.remove(you[round-1])
    round=round+1
    return round

def main():
    round= 1
    round = choose(round)
    print(f'1st round your card{you} , dealer{dealer}')
    choice_str = input('Make A draw Y or N')
    if choice_str == 'y' or 'Y':
        choice = True
    else:
        choice = False
    replit.clear()
    while (choice and round < 4):
        round = choose(round)
        print(f'{round} round your card{you}')
        choice = input('Make Another draw Y or N')
        if choice_str == 'y' or 'Y':
            choice = True
        else:
            choice = False
        replit.clear()
    
    print(f'{round} round your card{you} , dealer{dealer}')
    dealer_sum = sum(dealer)
    you_sum = sum(you)
    print(f'{round} round your card total{you_sum} , dealer total{dealer_sum}')
    
    if you_sum > 21 and dealer_sum < 21 :
        print("dealer won")
    elif you_sum < 21 and dealer > 21 :
        print("you won")
    elif you_sum > 21 and dealer >21 or you_sum == dealer_sum:
        print('draw')
    else:
        if you_sum > dealer_sum:
             print("you won")
        else:
            print("dealer won")
  
  
main()