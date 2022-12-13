from karaktärer import Riddaren, Trollkarlen, Tjuven
import random
# char_stats = {}

# char = Riddaren()
# char_stats["name"] = char.name
# char_stats["initiativ"] = char.initiativ
# char_stats["tålighet"] = 9
# char_stats["attack"] = 6
# char_stats["smidighet"] = 4

# print(char_stats)

# heros_liv = char_stats.get('tålighet')

# print(type(heros_liv))

#r = Riddaren()
#print(r.tålighet)

# def hero_choose():
#     choice2 = input("Enter your choice 1-3")
#     if choice2 == "1":
#         hero = "Riddaren"
#     elif choice2 == "2":
#         hero = "Trollkaren"
#     elif choice2 == "3":
#         hero = "Tjuven"
#     else:
#         print("\nYou didn't enter a valid input, try again!")
#     return hero


# print(hero_choose())

def bla():
    smidighet = 4
    procent = smidighet * 10
    procent = procent/100
    return random.random() <= procent
if bla() is True:
    print('Hero lyckats')
elif bla() is False:
    print('Hero misslyckats')


bla()