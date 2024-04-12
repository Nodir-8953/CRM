data_sell = {
    'name': ['OLMA', 'ANOR', 'UZUM'],
    'price': ['20000', '35000', '23000'],
    'qty': ['20', '30', '45'],
    'date': ['04.01.24', '03.04.24', '03.01.24']
}

# date = input("Vaqtni kiriting (format day.month.year): ")
# date2 = date.split('.')
# print(type(date[0]))
# print(type(data_sell['date'][0]))
# if (len(date) == 3 and 1 <= int(date[0]) <= 31 and 1 <= int(date[1]) <= 12 and 2000 <= int(date[2]) <= 2024):
    
    
# else:
#     print('bad')
# print(list(date))
# print(".".join(date2))
# if data_sell['date'][1][1]  == '01':
#     print(data_sell['date'][1])
#     # print(date)
#     print('ok')
# else:
#     print('bad')
for i, ter in enumerate(data_sell['date']):
    # print(data_sell['date'][i].split('.')[1])
    # print(i)
    if data_sell['date'][i].split('.')[1] == '01':
        print(data_sell['name'][i])
    