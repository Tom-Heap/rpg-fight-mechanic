#Rpg Training
from random import randint as ri
def turn(php,ehp,patk,eatk,game):
    if (php <1):
        game=False
        print("Player is dead")
        return (php,ehp,game)
    if (ehp <1):
        game=False
        print("Monster is dead")
        return (php,ehp,game)
    print("Player Health: {}\nEnemy Health: {}".format(php,ehp))
    user_input=str(input("Do something: "))
    if (user_input=="quit"):
        game=False
        print("Player has quit")
        return (php,ehp,game)
    #player attack
    if (ri(1,10)<3):
        ehp -=patk*2
    else :
        ehp-=patk
    #enemy attack
    if (ri(1,10)<2):
        php -=eatk*2
    else :
        php-=eatk

    
    return (php,ehp,True)
    
php,ehp=10,10
patk,eatk=2,1
palive=True
ret_values=[]
while(palive) :
    ret_values=turn(php,ehp,patk,eatk,palive)
    php=ret_values[0]
    ehp=ret_values[1]
    palive=ret_values[2]
    
