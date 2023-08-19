# Bossfight redone

import random

boss_health = 100
player_health = 20
fire_stam = 5
ice_stam = 5
earth_stam = 5
ser_num = 3
sser_num = 2
stam_fruit = 1

def boss_attack():
    global player_health
    num = random.randint(0, 2)
    
    if num == 0:
        print("The dark lord attacks, but misses. You take no damage.")
        print("You have", player_health, "health remaining.")
    
    else:
        player_health -= 10
        print("The dark lord attacks. It does 10 damage.")
        print("You have", player_health, "health remaining.")

def check_health():
    if player_health <= 0:
        print("\nYou have died.")
        input("Press any button to quit.")
        quit()

    if boss_health <= 0:
        print("\nCongratulations! You defeated the boss!")
        input("Press any button to quit.")
        quit()

def use_ser():
    global ser_num
    
    if ser_num > 0:
        ser_num -= 1
    
    else:
        print("You are out of serum.")

    boss_attack()
    check_health()

def use_sser():
    global sser_num
    
    if sser_num > 0:
        sser_num -= 1
    
    else:
        print("You are out of super serum.")

    boss_attack()
    check_health()

def use_stam_fruit():
    global stam_fruit
    
    if stam_fruit > 0:
        stam_fruit -= 1
    
    else:
        print("You are out of stamina fruit.")

    boss_attack()
    check_health()

def fire_attack():
    global fire_stam
    global boss_health
    
    if fire_stam > 0:
        boss_health -= 15
        fire_stam -= 1
        print("You use a fire attack. It does 15 damage.")
    
    else:
        print("Your fire attack is out of stamina.")

    boss_attack()
    check_health()

def ice_attack():
    global ice_stam
    global boss_health
    
    if ice_stam > 0:
        boss_health -= 5
        ice_stam -= 1
        print("You use an ice attack. It does 5 damage and freezes the dark lord.")
    
    else:
        print("Your ice attack is out of stamina.")

def earth_attack():
    global earth_stam
    global boss_health
    
    if earth_stam > 0:
        global player_health
        boss_health -= 5
        player_health += 5
        earth_stam -= 1
        print("You use an earth attack. It does 5 damage and you heal 5 health.")
    
    else:
        print("Your earth attack is out of stamina.")

    boss_attack()
    check_health()

print("You face off against the dark lord.")

loop = True
while loop:

    what_do = input("\nWhat would you like to do? (Attack, Item, Flee): ")

    if what_do.lower() == "attack":
        attack = input("What attack do you want to use? (Fire, Ice, Earth): ")

        if attack.lower() == "fire":
            fire_attack()

        elif attack.lower() == "ice":
            ice_attack()

        elif attack.lower() == "earth":
            earth_attack()

        else:
            print("Please input a valid attack next time. You forfeit your turn.")
            boss_attack()
            check_health()

    elif what_do.lower() == "item":
        item = input("What item do you want to use? (Serum, Super Serum, Stamina Fruit): ")

        if item.lower() == "serum":
            use_ser()

        elif item.lower() == "super serum":
            use_sser()

        elif item.lower() == "stamina fruit":
            use_stam_fruit()

        else:
            print("Please input a valid item next time. You forfeit your turn.")
            boss_attack()
            check_health()

    elif what_do.lower() == "flee":
        input("You surrender the battle. Press any key to quit.")
        loop = False

    else:
        print("Please input a valid action next time. You forfeit your turn")
        boss_attack()
        check_health()