import random

print(''' █     █░▓█████  ██▓     ▄████▄   ▒█████   ███▄ ▄███▓▓█████ 
▓█░ █ ░█░▓█   ▀ ▓██▒    ▒██▀ ▀█  ▒██▒  ██▒▓██▒▀█▀ ██▒▓█   ▀ 
▒█░ █ ░█ ▒███   ▒██░    ▒▓█    ▄ ▒██░  ██▒▓██    ▓██░▒███   
░█░ █ ░█ ▒▓█  ▄ ▒██░    ▒▓▓▄ ▄██▒▒██   ██░▒██    ▒██ ▒▓█  ▄ 
░░██▒██▓ ░▒████▒░██████▒▒ ▓███▀ ░░ ████▓▒░▒██▒   ░██▒░▒████▒
░ ▓░▒ ▒  ░░ ▒░ ░░ ▒░▓  ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ░  ░░░ ▒░ ░
  ▒ ░ ░   ░ ░  ░░ ░ ▒  ░  ░  ▒     ░ ▒ ▒░ ░  ░      ░ ░ ░  ░
  ░   ░     ░     ░ ░   ░        ░ ░ ░ ▒  ░      ░      ░   
    ░       ░  ░    ░  ░░ ░          ░ ░         ░      ░  ░
                        ░                                   ''')

papper = '''                                           
    ____   ____ _ ____   ____   ___   _____
   / __ \ / __ `// __ \ / __ \ / _ \ / ___/
  / /_/ // /_/ // /_/ // /_/ //  __// /    
 / .___/ \__,_// .___// .___/ \___//_/     
/_/           /_/    /_/                   '''

pencil='''                               _  __
    ____   ___   ____   _____ (_)/ /
   / __ \ / _ \ / __ \ / ___// // / 
  / /_/ //  __// / / // /__ / // /  
 / .___/ \___//_/ /_/ \___//_//_/   
/_/                                 '''
scissor = '''   _____        _                               
  / ___/ _____ (_)_____ _____ ____   _____ _____
  \__ \ / ___// // ___// ___// __ \ / ___// ___/
 ___/ // /__ / /(__  )(__  )/ /_/ // /   (__  ) 
/____/ \___//_//____//____/ \____//_/   /____/  
                                                '''

stone = '''          __                    
   _____ / /_ ____   ____   ___ 
  / ___// __// __ \ / __ \ / _ |
 (__  )/ /_ / /_/ // / / //  __/
/____/ \__/ \____//_/ /_/ \___/ 
                                '''   

score = '_______________________________________________________________________'
score1= '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
comp_score = 0
your_score = 0                     
while(True):
    print(score)
    print(score1)
    print(score)
    comp_choice = random.randint(0,3)
    option = [papper,pencil,scissor,stone]
    print("1 papper\t2 pencil\t3 scissor\t4 stone")
    print(score)

    your_opt=int(input('Enter Your option : '))
    your_opt-=1     
    print ('You choosed \n',option[your_opt])
    print ('computer choosed \n',option[comp_choice]) 
                              
    if comp_choice > your_opt :
        if comp_choice !=3:
            print(score)
            print('computer won')
            print(score)
            comp_score+=1
        else :
            if your_opt !=0:
                print(score)
                print('computer won')
                print(score)
                comp_score+=1
            else :
                print(score)
                print('you won')
                print(score)  
                your_score+=1                                                         
    elif comp_choice < your_opt :
            if your_opt != 3:
                print(score)
                print('You won')  
                your_score+=1
                print(score)
            else :
                if comp_choice != 0 :
                    print(score)
                    print('You won')
                    print(score)
                    your_score+=1
                else :
                    print(score)
                    print('computer won')
                    comp_score+=1
                    print(score)
    else:
        print(score)
        print(f"tie")
        print(score)
    print(score)
    print(f'COMPUTER {comp_score}\nYOU {your_score}')
    print(score)
    
        
                

