from SAScipher.sys_modul import error_control

table = {
    'q': 1,
    'w': 2,
    'e': 3,
    'r': 4,
    't': 5,
    'y': 6,
    'u': 7,
    'i': 8,
    'o': 9,
    'p': 10,
    'a': 0,
    's': 11,
    'd': 12,
    'f': 13,
    'g': 14,
    'h': 15,
    'j': 16,
    'k': 17,
    'l': 18,
    'z': 19,
    'x': 20,
    'c': 21,
    'v': 22,
    'b': 23,
    'n': 24,
    'm': 25,
    'Q': 26,
    'W': 27,
    'E': 28,
    'R': 29,
    'T': 30,
    'Y': 31,
    'U': 32,
    'I': 33,
    'O': 34,
    'P': 35,
    'A': 36,
    'S': 37,
    'D': 38,
    'F': 39,
    'G': 40,
    'H': 41,
    'J': 42,
    'K': 43,
    'L': 44,
    'Z': 45,
    'X': 46,
    'C': 47,
    'V': 48,
    'B': 49,
    'N': 50,
    'M': 51,
    '1': 52,
    '2': 53,
    '3': 54,
    '4': 55,
    '5': 56,
    '6': 57,
    '7': 58,
    '8': 59,
    '9': 60,
    '0': 61,
    '`': 62,
    '-': 63,
    '=': 64,
    '[': 65,
    ']': 66,
    ';': 67,
    "'": 68,
    ':': 69,
    '.': 70,
    '/': 71,
    '~': 72,
    '!': 73,
    '@': 74,
    '#': 75,
    '$': 76,
    '%': 77,
    '^': 78,
    '&': 79,
    '*': 80,
    '(': 81,
    ')': 82,
    '_': 83,
    '+': 84,
    'й': 85,
    'ц': 86,
    'у': 87,
    'к': 88,
    'е': 89,
    'н': 90,
    'г': 91,
    'ш': 92,
    'щ': 93,
    'з': 94,
    'х': 95,
    'ъ': 96,
    'ф': 97,
    'ы': 98,
    'в': 99,
    'а': 100,
    'п': 101,
    'р': 102,
    'о': 103,
    'л': 104,
    'д': 105,
    'ж': 106,
    'э': 107,
    'я': 108,
    'ч': 109,
    'с': 110,
    'м': 111,
    'и': 112,
    'т': 113,
    'ь': 114,
    'б': 115,
    'ю': 116,
    '\\': 117,
    '|': 118,
    'Й': 119,
    'Ц': 120,
    'У': 121,
    'К': 122,
    'Е': 123,
    'Н': 124,
    'Г': 125,
    'Ш': 126,
    'Щ': 127,
    'З': 128,
    'Х': 129,
    'Ъ': 130,
    'Ф': 131,
    'Ы': 132,
    'В': 133,
    'А': 134,
    'П': 135,
    'Р': 136,
    'О': 137,
    'Л': 138,
    'Д': 139,
    'Ж': 140,
    'Э': 141,
    'Я': 142,
    'Ч': 143,
    'С': 144,
    'М': 145,
    'И': 146,
    'Т': 147,
    'Ь': 148,
    'Б': 149,
    'Ю': 150,
    ' ': 151,
    'Ё': 152,
    'ё': 153,
}


def encryption(data: str, key: str):
    if not isinstance(data, str) and not isinstance(data, int):
        error_control.ertype('data')
    elif not isinstance(key, str) and not isinstance(key, str):
        error_control.ertype('column')
    else:
        data = str(data)
        key = str(key)
        result = str()
        index = 0
        for char in data:
            if index == len(key):
                index = 0
            if char not in table:
                shift = 228
            else:
                shift = table[key[index]]
            result = f'{result}{chr(ord(char)+shift)}'
            index += 1
        return result


def decryption(data: str, key: str):
    if not isinstance(data, str) and not isinstance(data, int):
        error_control.ertype('data')
    elif not isinstance(key, str) and not isinstance(key, str):
        error_control.ertype('column')
    else:
        data = str(data)
        key = str(key)
        result = str()
        index = 0
        for char in data:
            if index == len(key):
                index = 0
            if chr(ord(char)-table[key[index]]) not in table:
                shift = 228
            else:
                shift = table[key[index]]
            result = f'{result}{chr(ord(char)-shift)}'
            index += 1
        return result
