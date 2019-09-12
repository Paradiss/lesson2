
def input_2_str(str1, str2):
    if type(str1) is not str or type(str2) is not str: result = 0
    elif str1 == str2: result = 1
    elif str1 != str2 and len(str1)>len(str2): result = 2
    elif str1 != str2 and str2 == 'learn': result = 3
    else: result = 'хмм...'
    return result


print(input_2_str('asd', 'add'))
print(input_2_str(3, 'add'))
print(input_2_str('EFf', 5.4))
print(input_2_str('EFf', 'EFf'))
print(input_2_str('EFf', 'Eff'))
print(input_2_str('EFfc', 'EFf'))
print(input_2_str('EFf', 'learn'))