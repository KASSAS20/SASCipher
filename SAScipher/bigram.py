from SAScipher.sys_modul import error_control


def cryption(data: str) -> str:  # function both encrypts and decrypts
    if not isinstance(data, str) and not isinstance(data, int):
        error_control.ertype('data')
    elif len(str(data)) < 2:
        error_control.erlen('data')
    else:
        result = str()
        char_list_1 = str(data)[::2]
        char_list_2 = str(data)[1::2]
        for index in range(0, len(char_list_2)):
            result = f'{result}{char_list_2[index]}{char_list_1[index]}'
        if len(str(data)) % 2:
            result = f'{result}{char_list_1[-1]}'
        return result
