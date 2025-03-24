x = input("Donner votre mot à chiffrer : ").lower()

binaire = {
    'a': '00001',
    'b': '00010',
    'c': '00011',
    'd': '00100',
    'e': '00101',
    'f': '00110',
    'g': '00111',
    'h': '01000',
    'i': '01001',
    'j': '01010',
    'k': '01011',  
    'l': '01100',
    'm': '01101', 
    'n': '01110',  
    'o': '01111',  
    'p': '10000',
    'q': '10001',
    'r': '10010',
    's': '10011',
    't': '10100',
    'u': '10101',
    'v': '10110',
    'w': '10111',
    'x': '11000',
    'y': '11001',
    'z': '11010'
}

hexa = {
    'a': '1',
    'b': '2',
    'c': '3',
    'd': '4',
    'e': '5',
    'f': '6',
    'g': '7',
    'h': '8',
    'i': '9',
    'j': 'A',
    'k': 'B',  
    'l': 'C',
    'm': 'D', 
    'n': 'E',  
    'o': 'F',  
    'p': '10',
    'q': '11',
    'r': '12',
    's': '13',
    't': '14',
    'u': '15',
    'v': '16',
    'w': '17',
    'x': '18',
    'y': '19',
    'z': 'A1'
}



mot_chiffre = " ".join(binaire[lettre] for lettre in x if lettre in binaire)
mot_hexa = " ".join(hexa[lettre] for lettre in x if lettre in hexa)

print(f"Mot original : {x}")
print(f"Mot binaire  : {mot_chiffre}")
print(f"Mot hexa  : {mot_hexa}")