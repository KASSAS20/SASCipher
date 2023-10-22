from SAScipher.sys_modul import error_control


def encryption(data: str, shift: int = 1) -> str:
    if not isinstance(data, str) and not isinstance(data, int):
        error_control.ertype('data')
    elif not isinstance(shift, int):
        error_control.ertype('shift')
    else:
        result = list()
        for symbol in str(data):
            if symbol == ' ':
                char = ' '
            else:
                char = chr(ord(symbol)+shift)
            result.append(char)
        return ''.join(result)


def decryption(data: str, shift: int = 1) -> str:
    if not isinstance(data, str) and not isinstance(data, int):
        error_control.ertype('data')
    elif not isinstance(shift, int):
        error_control.ertype('shift')
    else:
        result = list()
        for symbol in str(data):
            if symbol == ' ':
                char = ' '
            else:
                char = chr(ord(symbol)-shift)
            result.append(char)
        return ''.join(result)
