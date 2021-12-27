from entity import Entity
from random import randint


class Boss(Entity):
    def attack(self, target: Entity) -> None:
        if not randint(0, 2):  # One in three chance of missing
            print("The dark lord attacks, but misses. You take no damage.")
            return

        # FIXME: Don't hard code damage value. Also, should this method be
        # responsible for both attacking and printing?
        print("The dark lord attacks. It does 10 damage.")
        target.decrease_health(10)

    def decrease_health(self, value: int) -> None:
        self.health -= value

    def freeze(self) -> None:
        self.frozen = True

    def unfreeze(self) -> None:
        self.frozen = False


