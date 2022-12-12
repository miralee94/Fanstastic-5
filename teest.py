from karaktärer import Riddaren

char_stats = {}

char = Riddaren()
char_stats["name"] = char.name
char_stats["initiativ"] = 5
char_stats["tålighet"] = 9
char_stats["attack"] = 6
char_stats["smidighet"] = 4

print(char_stats)

heros_liv = char_stats.get('tålighet')

print(type(heros_liv))
