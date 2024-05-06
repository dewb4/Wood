import random

vowels = ["a", "e", "i", "o"]
consonants = ["b", "d", 
              "l", "m", "n", "p",
              "r", "s", "t", "z"]
fricatives = ["l", "r"]
stinkers = ["h", "m", "n", "t"]
launchers = ["b", "d", "p", "z"]
rockets = vowels + fricatives
special = ["s"]
special_friends = ["h", "m", "n", "l", "p", "r", "t"]
bad_ends = ["b", "e", "i", "p", "s", "z", "g"]
ends = ["a", "o", "on"]
start_vowels = ["a", "i", "o"]
possibles = []

word = ""
n_o_w = int(input("How many words?\n"))


for _ in range(n_o_w):
    word = ""
    starter_letter = random.choice(start_vowels + consonants)
    word += starter_letter
    length = random.randint(2, 6)
    for _ in range(length):
        if starter_letter in vowels:
            next_letter = random.choice(consonants)
        elif starter_letter in fricatives or stinkers:
            next_letter = random.choice(vowels)
        elif starter_letter in launchers:
            next_letter = random.choice(rockets)
        elif starter_letter in special:
            next_letter = random.choice(special_friends)
        word += next_letter
        starter_letter = next_letter
        continue
    if next_letter in bad_ends:
        ending = random.choice(ends)
        word += ending
    print(word)