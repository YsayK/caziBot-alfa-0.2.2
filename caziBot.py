#----------------------For-all--------------------------
#import
from random import randint as randint
from random import uniform as randfloat
import time

from colorama import Fore
from colorama import init
init()

#int
give_money = 0
max_coins_take = 100
account_coins = 0

bid_amount = 0

#float
spin_drop1 = 0.0
spin_drop2 = 0.0

#str
message = None
bid = None
help = ('''
    Commands:
!c help (!h) - for help
!c give coins (!gc) - for more coins (has cool down)
!c account balance (!ab) - to see an account balance
!c spinning weel (!sw) - to bid and spin weel
!c roll dice (!rd)- to bid and roll dice
!c save (!s) - for saving your statistic
!c exit (!e) - to exit from game
!c delite (!d) - to make you account balance 0 cazi-coins
''')
    #array-str
help_words = ("!c", "!ch", "!chelp", "!h", "!help")
give_coins = ("!cgc", "!gc", "!cgivecoin", "!cgivecoins")
account_balance = ("!cab", "!ab", "!caccountbalance", "!caccountcoins")
roll_dice = ("!crd", "!rd", "!crolldice", "!rolldice")
exit_words = ("!exit", "!e", "!cexit")
save_words = ("!save", "!s", "!csave")
delite_words = ("!d", "!cd", "!delite", "!del", "delitetheprogress", "!cdelite", "!cdel", "cdelitetheprogress")

        #spinning-weel
spinning_weel = ("!csw", "!sw", "!cspinningweel", "!cspinweel")

bid_spinning_weel_2x = ("2", "x2")
bid_spinning_weel_3x = ("3", "x3")
bid_spinning_weel_5x = ("5", "x5")
bid_spinning_weel_14x = ("14", "x14")

#bool
god_mode = False

#def

#-gives-money-from-1-to-max_coins_take-------
def give_some_money():
    global give_money
    global account_coins

    try:
        give_money = int(input("how much? : "))
    except ValueError:
        print("\n" + Fore.RED + "Error" + Fore.WHITE +": you didn't put the "+ Fore.CYAN + "integer" + Fore.WHITE)
        main_menu()

    if int(give_money) <= max_coins_take and god_mode == False:
        account_coins += int(give_money)
        print('\nok, ' + Fore.GREEN + "done!" + Fore.WHITE +' \nYour balance: ' + Fore.YELLOW + str(account_coins) +" cc" + Fore.WHITE)
        main_menu()

    elif god_mode == True:
        account_coins += int(give_money)
        print('\nok, ' + Fore.GREEN + "done!" + Fore.WHITE +' \nYour balance: ' + Fore.YELLOW + str(account_coins) +" cc" + Fore.WHITE)
        main_menu()

    else:
        print("\n"+ Fore.GREEN + "Sorry" + Fore.WHITE +', but the max amount of ' + Fore.YELLOW + 'cazi-coins' + Fore.WHITE + ' you can take is: ' + Fore.RED + str(max_coins_take) + Fore.WHITE)
        main_menu()


#----bid-for-the-weel-----
def spin_weel():
    global account_coins
    global bid_amount
    global bid
#---which-x-?-
    bid = input("\nX2-(42.5%), X3-(30%), X5-(20%), or X14-(7.5%)? : ")

    if bid not in bid_spinning_weel_2x and bid not in bid_spinning_weel_3x and bid not in bid_spinning_weel_5x and bid not in bid_spinning_weel_14x:
        print('\n'+ Fore.GREEN + "Sorry" + Fore.WHITE +', something ' + Fore.RED + "went wrong" + Fore.WHITE + ', write: ' + Fore.CYAN + "x2" + Fore.WHITE + ", " + Fore.CYAN + "x3" + Fore.WHITE + ", " + Fore.CYAN + "x5" + Fore.WHITE + ' or '  + Fore.CYAN + "x14" + Fore.WHITE)
        main_menu()
#----bid-amount---
    elif bid in bid_spinning_weel_2x or bid in bid_spinning_weel_3x or bid in bid_spinning_weel_5x or bid in bid_spinning_weel_14x:
        try:
            bid_amount = int(input("how much do you want to bid? : "))
        except ValueError:
            print("\n" + Fore.RED + "Error" + Fore.WHITE +": you didn't put the "+ Fore.CYAN + "integer" + Fore.WHITE)
            main_menu()
#----start-spin---
        if 0 < int(bid_amount) <= account_coins or god_mode == True:
            start_spin_weel(bid_amount)
    #--negative-bid-try---
        if int(bid_amount) <= account_coins and int(bid_amount) > 0:
            start_spin_weel(bid_amount)

        elif int(bid_amount) <= 0:
            print("\n"+ Fore.GREEN + "Sorry" + Fore.WHITE +", you need to bid " + Fore.CYAN + "positive" + Fore.WHITE + " amount of" + Fore.YELLOW + " cazi-coins" + Fore.WHITE)
            main_menu()
    #--bigger-that-account-balance--
        else:
            print("\n"+ Fore.GREEN + "Sorry" + Fore.WHITE +", you " + Fore.RED + "don't have" + Fore.WHITE + " that amount of" + Fore.YELLOW + " cazi-coins" + Fore.WHITE)
            main_menu()



#----spin-the-weel-----

def start_spin_weel(bid_amount_inDefVar):
    global spin_drop1
    global account_coins
    global bid

    spin_drop1 = randfloat(0, 100)
    account_coins -= int(bid_amount_inDefVar)
#-x2-
    if spin_drop1 < 42.5:

        if bid in bid_spinning_weel_2x:
            print('\nx2 '+ Fore.GREEN +'dropped' + Fore.WHITE)
            won_the_game(2)

        else:
            print('\nx2 ' + Fore.RED +'dropped' + Fore.WHITE)
            lost_in_game()
#-x3-
    elif spin_drop1 >= 42.5 and spin_drop1 < 72.5:

        if bid in bid_spinning_weel_3x:
            print('\nx3 '+ Fore.GREEN +'dropped' + Fore.WHITE)
            won_the_game(3)

        else:
            print('\nx3 '+ Fore.RED +'dropped' + Fore.WHITE)
            lost_in_game()
#-x5-
    elif spin_drop1 >= 72.5 and spin_drop1 < 92.5:

        if bid in bid_spinning_weel_5x:
            print('\nx5 '+ Fore.GREEN +'dropped' + Fore.WHITE)
            won_the_game(5)

        else:
            print('\nx5 '+ Fore.RED +'dropped' + Fore.WHITE)
            lost_in_game()
#-x14-
    elif spin_drop1 >= 92.5 and spin_drop1 <= 100:

        if bid in bid_spinning_weel_14x:
            print('\nx14 '+ Fore.GREEN +'dropped' + Fore.WHITE)
            won_the_game(14)

        else:
            print('\nx14 '+ Fore.RED +'dropped' + Fore.WHITE)
            lost_in_game()


#-----won-spin-weel-------------
def won_the_game(win_amount):
    global account_coins
    global bid_amount

    account_coins += int(bid_amount) * win_amount
    print(Fore.GREEN + 'Win! ' + Fore.WHITE + ' Your balance: ' + Fore.YELLOW + str(account_coins) + " cc" + Fore.WHITE)
    main_menu()

#-----lost-spin-weel-------------
def lost_in_game():
    print(Fore.RED + 'Lost(' + Fore.WHITE + ' Your balance: ' + Fore.YELLOW + str(account_coins) + " cc" + Fore.WHITE)
    main_menu()





#-----1-to-12-dice-roll------

def dice_roll():
    global bid_amount
    global account_coins

#---how-much-bid----check-int--
    try:
        bid_amount = int(input("how much do you want to bid? : "))
    except ValueError:
        print("\n" + Fore.RED + "Error" + Fore.WHITE +": you didn't put the "+ Fore.CYAN + "integer" + Fore.WHITE)
        main_menu()
#--all-is-ok--
    if int(bid_amount) <= account_coins and int(bid_amount) > 0:

        start_dice_rolling(bid_amount)
#--negative-bid-try---
    elif int(bid_amount) <= 0:
        print("\n"+ Fore.GREEN + "Sorry" + Fore.WHITE +", you need to bid " + Fore.CYAN + "positive" + Fore.WHITE + " amount of" + Fore.YELLOW + " cazi-coins" + Fore.WHITE)
        main_menu()
#--bigger-that-account-balance--
    else:
        print("\n"+ Fore.GREEN + "Sorry" + Fore.WHITE +", you " + Fore.RED + "don't have" + Fore.WHITE + " that amount of" + Fore.YELLOW + " cazi-coins" + Fore.WHITE)
        main_menu()






def start_dice_rolling(bid_amount_inDefVar):
    global spin_drop1
    global spin_drop2
    global account_coins

#--get-2-rand-numbers---for-2-dice---
    spin_drop1 = randint(1, 6)
    spin_drop2 = randint(1, 6)
    account_coins -= int(bid_amount_inDefVar)


    if spin_drop1 == spin_drop2:
        print(Fore.GREEN + "dropped" + Fore.WHITE +": " + str(spin_drop1) + " and " + str(spin_drop2))

        if spin_drop1 == 6:
            won_the_game(4)


        elif spin_drop1 == 5:
            won_the_game(5)


        elif spin_drop1 == 4:
            won_the_game(6)


        elif spin_drop1 == 3:
            won_the_game(8)


        elif spin_drop1 == 2:
            won_the_game(7)


        elif spin_drop1 == 1:
            won_the_game(10)

    else:
        print(Fore.RED + "dropped" + Fore.WHITE +": " + str(spin_drop1) + " and " + str(spin_drop2))
        lost_in_game()









#----mini-defs------------------------------------------------------------------

#--god--mode-)-

def god_mode_swicther():
    global god_mode

    if god_mode == False:
        god_mode = True
        print("\nOuu lala... god-mod activated ;)")
        main_menu()

    else:
        god_mode = False
        print("\ngod-mod deactivated -_-")
        main_menu()


#----saves-all-money---
def save_account_coins():
    global account_coins

    file_saver = open("caziBot_memory.txt", 'w')
    file_saver.write(str(account_coins))
    file_saver.close()

    print(Fore.GREEN + "\nSaved" + Fore.WHITE +', \nYour balance is ' + Fore.YELLOW + str(account_coins) + " cc" + Fore.WHITE)

    main_menu()


def delite_progress():

    file_saver = open("caziBot_memory.txt", 'w')
    file_saver.write("0")
    file_saver.close()

    account_coins = 0

    print(Fore.RED + "\nDelited" + Fore.WHITE +', \nYour balance is ' + Fore.YELLOW + str(account_coins) + " cc" + Fore.WHITE)

    main_menu()




def exit_the_game():
    print("\nsaving...")
    time.sleep(1.5)
    save_account_coins()
    time.sleep(1.5)



#---main-def---------------------------------------------------------------
def main_menu():
    print('')
#--puting-the-mesage-in-small-letter,-no-space-text---and-checking-it--
    message = input().replace(" ", "")
    #god-mode
    if message == "ThXfGm7":
        god_mode_swicther()

    message = message.lower()


    if message in help_words:
        print(help)


    if message in give_coins:   #and timer finished
        give_some_money()       #timer needs to be depending on the amount of money taken (x1.5 sec)

    #elif message in give_coins: #and timer didn't finished                 in process...
        #print("Sorry, you need to wait a bit, before cool down ends...")   in process...
        #main_menu()                                                        in process...

    if message in account_balance:
        print('\nYour balance is ' + Fore.YELLOW + str(account_coins) + " cc" + Fore.WHITE)
        main_menu()

    if message in spinning_weel:
        spin_weel()

    if message in roll_dice:
        dice_roll()

    if message in exit_words:
        exit_the_game()

    if message in save_words:
        save_account_coins()

    if message in delite_words:
        delite_progress()

    else:
        main_menu()


def start():
    global account_coins

    try:
        file_saver = open("caziBot_memory.txt", 'r')
        account_coins = int(file_saver.read())
        file_saver.close()
    except ValueError:
        print("no saves founded")
        account_coins = 0
    except FileNotFoundError:
          file_saver = open("caziBot_memory.txt", 'w')
          file_saver.write("0")
          file_saver.close()

          print("no save-file founded, creating the new one...")
          time.sleep(1)
          print('\nwrite: "!c" to see how to use me')
    else:
        print("\nlet's start")

    main_menu()

#---first-task-------------
start()
