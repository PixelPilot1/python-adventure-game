import time
import random

# Define player attributes
player = {
    "max_health": 100,
    "health": 100,
    "attack": 10,
    "defense": 0,
    "healing_potions": 2,
    "sword_damage": 10,
    "armor_points": 0,
    "gold": 0
}

top_goblin_count = 0
top_goblin_max = 3  # Limit Top Goblin appearances

# Generate random goblin encounters
def generate_goblin(level):
    if level <= 20:
        return {"health": 50, "attack": 8, "coins": 4}  # Normal goblin for levels 1-20
    else:
        global top_goblin_count
        if top_goblin_count < top_goblin_max and random.random() < 0.3:
            top_goblin_count += 1
            return {"health": 200, "attack": 20, "coins": 50}  # Top Goblin
        else:
            return {"health": 80, "attack": 8, "coins": 4}  # Normal goblin for levels 21-50

# Display player stats
def display_player_stats():
    print(f"Player Health: {player['health']}/{player['max_health']}")
    print(f"Attack Power: {player['attack']}")
    print(f"Defense: {player['defense']}")
    print(f"Gold: {player['gold']}")

# Simulate the game loading
def loading_screen():
    print("Loading game, please wait...")
    for i in range(15):
        time.sleep(1)
        print(f"Loading... {int((i+1)/15*100)}%")
    print("Game Loaded!\n")

# Shop system
def show_shop():
    while True:
        print("\n--- Welcome to the Shop! ---")
        print(f"You have {player['gold']} gold.")
        print("1. Buy Healing Potion (10 gold, restores 10 health)")
        print("2. Buy Ultra Healing Potion (100 gold, restores 100 health)")
        print("3. Buy Sword")
        print("4. Buy Armor")
        print("5. Leave Shop")
        choice = input("Choose an option: ")

        if choice == "1" and player["gold"] >= 10:
            player["gold"] -= 10
            player["healing_potions"] += 1
            print("You bought a healing potion!")
        elif choice == "2" and player["gold"] >= 100:
            player["gold"] -= 100
            player["health"] = min(player["max_health"], player["health"] + 100)
            print(f"You bought an Ultra Healing Potion! Your health is now {player['health']}.")
        elif choice == "3":
            buy_sword()
        elif choice == "4":
            buy_armor()
        elif choice == "5":
            break
        else:
            print("Invalid choice or insufficient gold!")

# Sword purchase system
def buy_sword():
    print("\n--- Swords for Sale ---")
    print("1. Wood Sword (5 gold, 5 damage)")
    print("2. Stone Sword (20 gold, 10 damage)")
    print("3. Iron Sword (50 gold, 20 damage)")
    print("4. Gold Sword (100 gold, 50 damage)")
    print("5. Platinum Sword (200 gold, 100 damage)")
    print("6. Diamond Sword (500 gold, 200 damage)")
    print("7. Obsidian Sword (1000 gold, 500 damage)")
    choice = input("Choose a sword: ")

    swords = {
        "1": {"cost": 5, "damage": 5},
        "2": {"cost": 20, "damage": 10},
        "3": {"cost": 50, "damage": 20},
        "4": {"cost": 100, "damage": 50},
        "5": {"cost": 200, "damage": 100},
        "6": {"cost": 500, "damage": 200},
        "7": {"cost": 1000, "damage": 500},
    }

    if choice in swords and player["gold"] >= swords[choice]["cost"]:
        player["gold"] -= swords[choice]["cost"]
        player["sword_damage"] = swords[choice]["damage"]
        print(f"You bought a sword with {player['sword_damage']} damage!")
    else:
        print("Invalid choice or insufficient gold!")

# Armor purchase system
def buy_armor():
    print("\n--- Armor for Sale ---")
    print("1. Leather Armor (10 gold, 20 armor points)")
    print("2. Chain Armor (20 gold, 30 armor points)")
    print("3. Steel Armor (50 gold, 50 armor points)")
    print("4. Gold Armor (100 gold, 75 armor points)")
    print("5. Diamond Armor (200 gold, 100 armor points)")
    print("6. Obsidian Armor (500 gold, 200 armor points)")
    choice = input("Choose armor: ")

    armor = {
        "1": {"cost": 10, "armor_points": 20},
        "2": {"cost": 20, "armor_points": 30},
        "3": {"cost": 50, "armor_points": 50},
        "4": {"cost": 100, "armor_points": 75},
        "5": {"cost": 200, "armor_points": 100},
        "6": {"cost": 500, "armor_points": 200},
    }

    if choice in armor and player["gold"] >= armor[choice]["cost"]:
        player["gold"] -= armor[choice]["cost"]
        player["armor_points"] = armor[choice]["armor_points"]
        print(f"You bought armor with {player['armor_points']} points!")
    else:
        print("Invalid choice or insufficient gold!")

# Fight goblins
def fight_goblin(level):
    goblin = generate_goblin(level)
    print(f"A goblin appears with {goblin['health']} health and {goblin['attack']} attack!")

    while goblin["health"] > 0 and player["health"] > 0:
        print("\n1. Attack\n2. Defend\n3. Use Potion")
        choice = input("Choose an action: ")

        if choice == "1":
            damage = max(1, player["sword_damage"] - goblin["attack"])
            goblin["health"] -= damage
            print(f"You hit the goblin for {damage} damage!")
            if goblin["health"] > 0:
                player["health"] -= goblin["attack"]
                print(f"The goblin hits you for {goblin['attack']} damage. Your health: {player['health']}")
        elif choice == "2":
            print("You defend yourself. The goblin's attack is reduced!")
            player["health"] -= max(1, goblin["attack"] - player["defense"])
            print(f"The goblin hits you for reduced damage. Your health: {player['health']}")
        elif choice == "3" and player["healing_potions"] > 0:
            player["health"] = min(player["max_health"], player["health"] + 10)
            player["healing_potions"] -= 1
            print(f"You use a healing potion. Your health: {player['health']}")
        else:
            print("Invalid action or no potions left!")

    if player["health"] > 0:
        print(f"You defeated the goblin and earned {goblin['coins']} gold!")
        player["gold"] += goblin["coins"]
    else:
        print("You were defeated... Game Over.")

# Main game loop
def game_loop():
    loading_screen()
    for level in range(1, 51):
        if player["health"] <= 0:
            break
        print(f"\n--- Level {level} ---")
        fight_goblin(level)
        if player["health"] > 0 and level % 5 == 0:
            show_shop()

# Start the game
if __name__ == "__main__":
    game_loop()
