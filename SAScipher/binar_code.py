from SAScipher.sys_modul import error_control


def encryption(data: str):
    if not isinstance(data, str) and not isinstance(data, int):
        error_control.ertype('data')
    else:
        result = str()
        data = str(data)
        for char in data:
            result = f'{result}{bin(ord(char))} '
        return result


def decryption(data: str):
    if not isinstance(data, str):
        error_control.ertype('data')
    else:
        result = str()
        data = str(data).strip().split(' ')
        for char in data:
            result = f'{result}{chr(int(char, 2))}'
            print(result)
        return result
