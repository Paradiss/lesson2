def discounted(price, discount, max_discount=20):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(float(max_discount))
        if max_discount > 99:
            raise ValueError('Слишком большая максимальная скидка')
        else:
            return price - (price * discount / 100)
    except(ValueError):print('Некорректный аргумент')

phone1 = {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 'qwe', 'discount': 25}
phone2 = {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 10}

dis_iphone = discounted(phone1['price'], phone1['discount'])
print(dis_iphone)
dis_android = discounted(phone2['price'], phone2['discount'])
print(dis_android)