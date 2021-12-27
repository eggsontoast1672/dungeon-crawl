# Bossfight redone

# TODO Add burning effect to fire attack

from boss import Boss
from element import Element
from player import Player

boss = Boss()
player = Player()


def main() -> None:
    running = True
    
    print("You face off against the dark lord.")
    while running:
        action = input("\nWhat would you like to do? (Attack, Item, Flee): ")
        if action.lower() == "attack":
            attack = input("What attack do you want to use? (Fire, Ice, Earth): ")

            if attack.lower() == "fire":
                player.attack(boss, Element.FIRE)
            elif attack.lower() == "ice":
                player.attack(boss, Element.ICE)
            elif attack.lower() == "earth":
                player.attack(boss, Element.EARTH)
            else:
                print("Please input a valid attack next time. You forfeit your turn.")
                boss_attack()
                check_health()

        elif action.lower() == "item":
            item = input("What item do you want to use? (Serum, Super Serum, Stamina Fruit): ")
            if item.lower() == "serum":
                use_serum()
            elif item.lower() == "super serum":
                use_super_serum()
            elif item.lower() == "stamina fruit":
                use_stam_fruit()
            else:
                print("Please input a valid item next time. You forfeit your turn.")
                boss_attack()
                check_health()

        elif action.lower() == "flee":
            input("You surrender the battle. Press any key to quit.")
            running = False

        else:
            print("Please input a valid action next time. You forfeit your turn")
            boss_attack()
            check_health()
