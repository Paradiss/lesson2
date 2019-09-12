
i_age = int(input('Введите ваш возраст: '))
print(i_age)
def ocupation(age):
    if age < 0: result = 'пользователь ещё не родился'
    elif age < 8: result = 'пользователь учится в детском саду'
    elif 8 <= age < 18: result = 'пользователь учится в школе'
    elif 18 <= age < 24: result = 'пользователь учится в ВУЗе'
    else: result = 'пользователь работает'
    return result

f_result = ocupation(i_age)
print(f_result)
    