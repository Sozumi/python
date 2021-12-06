price_list = [36.6, 999.99, 17.5, 55, 83.37, 45.9, 69.69, 0.5, 123, 28.03, 11.22, 72.4, 71.5, 325.07, 13.09]

for p in price_list:
    print(f'{int(p)} руб. {int(p * 100 % 100):02d} коп.', end=', ')

print(f'\nСписок цен: {price_list} id списка цен: {id(price_list)}')
price_list.sort()
print(f'\nСписок цен после сортировки: {price_list} id списка цен: {id(price_list)}')

new_price = sorted(price_list, reverse=True)
print(f'\nНовый список цен отсортированных по убыванию: {new_price} id нового списка цен: {id(new_price)}')

print(f'\nСписок цен пяти самых дорогих товаров: {price_list[-5:]}')
