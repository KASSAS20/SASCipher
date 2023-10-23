from SAScipher.sys_modul import error_control


def cryption(data: str, column: int = 2):
    if not isinstance(data, str) and not isinstance(data, int):
        error_control.ertype('data')
    elif not isinstance(column, int):
        error_control.ertype('column')
    elif column > len(data):
        error_control.erindex('data')
    else:
        result = str()
        data = str(data)
        list_of_lists = list()
        row_list = list()
        data = data + ' ' * (len(data) % column)
        for index, char in enumerate(data):
            if (index+1) % column == 0:
                row_list.append(char)
                list_of_lists.append(row_list)
                row_list = list()
            else:
                row_list.append(char)
        for index in range(0, column):
            for column in list_of_lists:
                result = f'{result}{column[index]}'
        return result
