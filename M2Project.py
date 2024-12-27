import random

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit
        self.shield_active = False

    def attack(self, opponent):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)

        if hasattr(opponent, 'shield_active') and opponent.shield_active:
            damage = int(damage * 0.5)  
            opponent.shield_active = False 
            print(f"{opponent.name}'s shield reduces the damage to {damage}!")

        opponent.health -= damage
        if opponent.health < 0:
            opponent.health = 0

        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        print(f"{opponent.name}'s health: {opponent.health}/{opponent.max_health}")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    def heal(self):
        heal_amount = 35
        self.health += heal_amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} heals for {heal_amount}. Health: {self.health}/{self.max_health}")


# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)  # Boost health and attack power
    # Add your power attack method here
    def heavy_sword_attack(self, opponent):
        damage = random.randint(self.attack_power + 10, self.attack_power + 20)
        opponent.health -= damage
        print(f"{self.name} does a Heavy Sword Attack for {damage} damage!")
        if opponent.health <= 0: 
            opponent.health = 0
            print(f"Victory!")

    def shield_block(self):
        self.shield_active = True
        print(f"{self.name} raises a shield, deflecting the damage of the next attack by 50%.")
        
# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)  # Boost attack power
    # Add your cast spell method here
    def lightning_blast(self, opponent):
        damage = random.randint(self.attack_power + 5, self.attack_power + 15)
        opponent.health -= damage
        print(f"{self.name} casts Lightning Blast for {damage} damage!")
        if opponent.health <= 0:
            opponent.health = 0
            print(f"Victory!")

    def magical_shield(self):
        self.shield_active = True
        print(f"{self.name} casts a Magical Shield, absorbing 50% of the damage from the next attack.")

class Sniper(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=30)

    def deadeye(self, opponent):
        damage = random.randint(self.attack_power + 10, self.attack_power + 20)
        opponent.health -= damage
        print(f"{self.name} uses his Deadeye ability to snipe for {damage} damage!")
        if opponent.health <= 0:
            opponent.health = 0
            print(f"Victory!")

    def juggernaut(self):
        self.shield_active = True
        print(f"{self.name} uses his Juggernaut suit to deflect incoming damage by 50% for the next attack")

class LebronJames(Character):
    def __init__(self, name):
        super().__init__(name, health=200, attack_power=23)
    
    def ledunk(self, opponent):
        damage = random.randint(self.attack_power + 10, self.attack_power + 20)
        opponent.health -= damage
        print(f"{self.name} posterizes his opponent with his signature Tomahawk dunk, causing {damage} damage!")
        if opponent.health <= 0:
            opponent.health = 0
            print(f"Victory!")

    def leblocked_by_james(self):
        self.shield_active = True
        print(f"{self.name} blocks the next attack by 50%!")


# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)  # Lower attack power
        
    
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        self.health += 5  # Lower regeneration amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Function to create player character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Sniper")  
    print("4. Lebron James")  
    
    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Sniper(name)
    elif class_choice == '4':
        return LebronJames(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

# Battle function with user menu for actions
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability 1")
        print("3. Use Special Ability 2")
        print("4. Heal")
        print("5. View Stats")
        
        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            if isinstance(player, Warrior):
                player.heavy_sword_attack(wizard)
            elif isinstance(player, Mage):
                player.lightning_blast(wizard)
            elif isinstance(player, Sniper):
                player.deadeye(wizard)
            elif isinstance(player, LebronJames):
                player.ledunk(wizard)    
        elif choice == '3':
            if isinstance(player, Warrior):
                player.shield_block()
            elif isinstance(player, Mage):
                player.magical_shield()
            elif isinstance(player, Sniper):
                player.juggernaut()
            elif isinstance(player, LebronJames):
                player.leblocked_by_james()
        elif choice == '4':
            player.heal()
        elif choice == '5':
            player.display_stats()
        else:
            print("Invalid choice, try again.")
            continue

        # Evil Wizard's turn to attack and regenerate
        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"{wizard.name} has been defeated by {player.name}!")

# Main function to handle the flow of the game
def main():
    # Character creation phase
    player = create_character()

    # Evil Wizard is created
    wizard = EvilWizard("The Dark Wizard")

    # Start the battle
    battle(player, wizard)

if __name__ == "__main__":
    main()