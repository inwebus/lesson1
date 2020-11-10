def discounted(price, discount, max_discount=50):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
            raise ValueError('Максимальная скидка не может быть больше 99%')
    if discount >= max_discount:
            price_with_discount = price
    else:
            price_with_discount = price - price * discount / 100
    
    return price_with_discount

# product = {'name': "Samsung Galaxy S10", 'stock': 8, 'price': 50000, 'discount': 50}

print(discounted(100, 50))