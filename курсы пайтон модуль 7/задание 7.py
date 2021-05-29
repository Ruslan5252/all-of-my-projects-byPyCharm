def palindrom(str=''):
    str=str.lower()
    if str==str[::-1]:
        return "Yes"
    else:
        return "No"
print(palindrom("Kazak"))