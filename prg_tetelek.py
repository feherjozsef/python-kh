# Programozási tételek

# Hozzatok létre egy sum függvényt, ami paraméterül egész számok listáját kapja, és összegzi ezeket és az összeggel tér vissza
# Összegzés tétele
def sum_numbers(numbers):
    sumnr = 0
    for i in numbers:
        sumnr += i
    return sumnr

numbers = [1, 2, 3]
if __name__ == "__main__": 
    print(sum_numbers(numbers))
    print(sum_numbers([10, 20, 30, 40]))

# Konvenciók
# snake case name_of_employee
# Csak akkor használj rövidítést, ha triviális
# Óvakodjunk a Hungarian notation-től, nem kell tartalmaznia a típusát a változónak


# Számlálás tétele
# Írjatok 1 olyan függvényt, ami paraméterül kap egy string-et és visszaadja, hogy hány magyar ékezetes karakter van benne!

def hun_counter(word):
    counter = 0
    for c in word:
        if c in ["á", "é", "ó", "ö", "ő", "ú", "ü", "ű"]:
            counter += 1
    return counter

print(hun_counter("tűzőgép"))

def count_accented(text):
    counter = 0
    for c in text.lower():          # Kisbetűsíti a stringet
        if c in "áéíóöőüűú":
            counter += 1
    return counter