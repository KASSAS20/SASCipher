def encryption(data: str, shift: int = 1) -> str:
    result = list()
    for symbol in data:
        if symbol == ' ':
            char = ' '
        else:
            char = chr(ord(symbol)+shift)
        result.append(char)
    return ''.join(result)

def decryption(data: str, shift: int = 1) -> str:
    result = list()
    for symbol in data:
        if symbol == ' ':
            char = ' '
        else:
            char = chr(ord(symbol)-shift)
        result.append(char)
    return ''.join(result)
