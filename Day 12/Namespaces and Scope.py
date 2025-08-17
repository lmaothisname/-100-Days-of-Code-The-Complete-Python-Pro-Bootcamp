enemies = 1

def increase_enenmies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enenmies()
print(f"enemies outside function: {enemies}")

#local scope
def drink_poition():
    potion_strength = 2
    print(potion_strength)

# print(potion_strength)
# Can't access this potion_strength outside of its scope
drink_poition()

#Global scope
player_health = 10

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_poition()

print(player_health)