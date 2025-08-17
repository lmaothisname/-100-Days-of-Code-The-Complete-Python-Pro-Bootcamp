enemies = 1 

def increase_enenmies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")
    
increase_enenmies()
def increase_enemies(enemy):
    print(f"enemies inside function: {enemy}")
    return enemy + 1


enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")

