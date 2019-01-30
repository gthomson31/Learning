import sys

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format

cprint(figlet_format('Taco List!', font='starwars'),
       'white', 'on_green', attrs=['bold'])


space = '  '

def taco():
    print ("Here are some of my favourite taco flavours")
    flavours = ["Steak" , "Chilli and Cheese" , "Double Crunch"]
    for tacos in flavours:
        print (tacos)
    print (space)
    print ('Now time to add your favourite')
    flavours.insert(3,input(" so whats your favourite taco ?: "))

    print ("Nice choice I have updated taco this onto my list : ")

    for tacos in flavours:
        print (tacos)
    print (space)
    print (space)
    print ("Will need to give a", flavours[3] , " taco a try next time !")

taco()
