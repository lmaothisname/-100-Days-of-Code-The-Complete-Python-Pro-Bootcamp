def calculate_love_score(name1, name2):
    combined = name1 + name2
    score1 = 0
    score2= 0
    for ch in combined:
        if ch in "true":
            score1 += 1
        if ch in "love":
            score2 += 1
    total = score1 * 10 + score2
    print(total)
calculate_love_score("Kanye West", "Kim Kardashian")    