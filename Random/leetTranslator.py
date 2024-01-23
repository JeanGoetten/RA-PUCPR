print("====================== Leet Translator ======================")

mapping_easy = {'a': '4', 'b': '8', 'c': '[', 'd': '|))', 'e': '3', 'f': '|=', 'g': '6', 'h': '#', 'i': '1', 'j': ';',
           'k': "X", 'l': '1', 'm': 'ʍ', 'n': 'π', 'o': '0', 'p': '|^', 'q': '9', 'r': '|2', 's': '5', 't': '7',
           'u': '(_)', 'w': 'ω', 'v': '\\/', 'x': '><', 'z': '2'}

mapping_med = {'a': '\/\\', 'b': 'vb', 'c': '<', 'd': '\)', 'e': '&', 'f': 'ƒ', 'g': '&', 'h': '/-/', 'i': '\|', 'j': ',_|',
           'k': '>|', 'l': '£', 'm': '[V]', 'n': '^/', 'o': '()', 'p': '|*', 'q': '(_,)', 'r': '|`', 's': '$', 't': '+',
           'u': '|_|', 'w': '\/\/', 'v': '|/', 'x': 'Ж', 'z': '7_'}

mapping_hard = {'a': '@', 'b': '13', 'c': '©', 'd': 'cl', 'e': '€', 'f': 'ph', 'g': 'gee', 'h': '1-1', 'i': 'eye', 'j': ',_]',
           'k': "|{", 'l': '|_', 'm': 'JTI', 'n': '{\}', 'o': 'oh', 'p': '[]D', 'q': '0_', 'r': '®', 's': 'ehs', 't': '][',
           'u': '\µ', 'w': '2u', 'v': '\|', 'x': 'ecks', 'z': '%'}

mapping = {}

# Select mode level
level = int(input("Selecione a dificuldade (1 - fácil; 2 - médio; 3 - difícil): "))
if level == 3:
    mapping = mapping_hard
elif level == 2:
    mapping = mapping_med
else:
    mapping = mapping_easy
# Input String
input = input("Insira sua frase: ")

# Convert String To List #
leet_list = list(input)

# Main Loop For Replacing Letters #
for index,item in enumerate(leet_list):
   for key,value in mapping.items():
       if item == key:
           for leet in value:
               leet_list[index] = leet

# Return To String #
leet_string = "".join(leet_list)
print(leet_string)