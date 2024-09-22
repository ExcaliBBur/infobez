# Метод Виженера

# for ru.txt keys is ПЕРВЫЙ БУКВА
# for en.txt keys is SOME KEYS IS HERE

ALPHABET_RU = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ '
ALPHABET_EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '

# Функция для определения языка файла
def detect_language(text):
    if ALPHABET_RU.find(text[0]) != -1:
        return "ru"
    return "en"

# Функция для шифрирования текста
def encrypt(data, keys, alphabet, num):
    answer = ''
    
    for i in range(len(data)):
        number = (alphabet.find(data[i]) + sumKeys(keys, i, alphabet)) % num
        answer += alphabet[number]
    return answer

# Функция для дешифрации текста
def decrypt(data, keys, alphabet, num):
    answer = ''
    
    for i in range(len(data)):
        number = (alphabet.find(data[i]) - sumKeys(keys, i, alphabet))
        if number < 0:
            number += num
        number %= num
        answer += alphabet[number]
    return answer

# Функция для суммирования ключей
def sumKeys(keys, index, alphabet):
    result = 0
    for key in keys:
        result += alphabet.find(key[index % len(key)])
    
    return result
        

fileName = str(input("Введите название файла: "))

f = open(fileName, "r", encoding="utf-8")
data = f.read().replace("\n", "")

keys = list(map(str, input("Введите ключи через пробел: ").split(" ")))

language = detect_language(data)

alphabet = ALPHABET_RU if language == "ru" else ALPHABET_EN
num = 32 if language == "ru" else 27

mode = str(input("Режим шифрования или дешифрования? (encr, decr): "))

if mode == "encr":
    print(encrypt(data, keys, alphabet, num))
else:
    print(decrypt(data, keys, alphabet, num))

