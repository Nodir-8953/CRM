import datetime
data = {
    'name': ['OLMA', 'ANOR'],
    'price': ['20000', '35000'],
    'qty': ['20', '30'],
    'date': ['2024-04-04 16:30:23.860902', '2024-04-03 11:15:23.860902']
}

data_add = {
    'name': [],
    'price': [],
    'qty': [],
    'date': [],

}

data_sell = {
    'name': [],
    'price': [],
    'qty': [],
    'date': []
}
son = 0
while True:
    sorov = input("Add product -->1\nSell product -->2\nReport -->3\n>>>")

    # add Product
    if sorov == '1':
        while True:
            name = input('Product name: ').upper()
            if name in data['name']:                
                index = data['name'].index(name)
                print(f'Ushbu mahsulotdan skladda {data['qty'][index]} ta mavjud')
                qty = input('Yana nechta mahsulot qushmoqchisiz: ')
                price = input('Product price: ')
                data['qty'][index] = int(data['qty'][index]) + int(qty)
                data['date'][index] = datetime.datetime.now()
                data['price'][index] = int(price)
                data_add['name'].append(name)
                data_add['price'].append(price)
                data_add['qty'].append(qty)
                data_add['date'].append(datetime.datetime.now())
                finish = input('Add product again -->1\nExit to list of functions --2\n>>>')
                if finish == '1':
                    continue
                else:
                    break
            else:
                price = input('Product price: ')
                qty = input('Product quantity: ')
                data['name'].append(name)
                data['price'].append(price)
                data['qty'].append(qty)
                data['date'].append(datetime.datetime.now())
                data_add['name'].append(name)
                data_add['price'].append(price)
                data_add['qty'].append(qty)
                data_add['date'].append(datetime.datetime.now())
                finish = input('Add product again -->1\nExit to list of functions --2\n>>>')
                if finish == '1':
                    continue
                else:
                    break

    # sell Product
    elif sorov == '2':
        Summa = 0
        count = 0
        while True:
            stuff = input('Product name: ').upper()
            quantity = int(input('Input qty of product: '))
            for i in range(len(data.get('name'))):
                if (stuff == data.get('name')[i] and quantity <= int(data.get('qty')[i])):
                    Summa += (quantity * int(data.get('price')[i]))
                    count += quantity

                    data_sell['name'].append(stuff)
                    data_sell['price'].append(data.get('price')[i])
                    data_sell['qty'].append(quantity)
                    data_sell['date'].append(datetime.datetime.now())

                    opros = input('Savatga yana mahsulot qushishni xoxlasangiz -->1\nChiqish uchun -->2\n>>>')
                    if opros == '1':
                        continue
                    else:
                        print('Sizning savatingizda jami:')
                        for i in range(len(data_sell['name'])):
                            print(f"{data_sell.get('qty')[i]} ta {data_sell.get('name')[i]} mavjud har biri {data_sell.get('price')[i]} somdan ")
                        print(f"""Xaridingiz umumiy miqdori {Summa} som
                                QQS bilan {int(Summa * 1.12)} som
                                --------------------------------------
                                 Umumiy narx: {int(Summa * 1.12)}""")
                        # break
                else:
                    print('Sklada bu mahsulot yoki yetarlicha qiymatda mavjud emas')
                    break
            break
    # Report
    elif sorov == '3':
        while True:
            sorov_report = input('Umumiy tovarlar ruyxati -->1\nQushilgan tovarlar ruyxati-->2\nSotilgan tovarlar ruyxati -->3\nChiqish -->4\n>>>')

            # current data
            if sorov_report == '1':
                for i in range(len(data.get('name'))):
                    son += 1
                    print(f"""
                        Name: {data.get('name')[i]}
                        Price: {data.get('price')[i]}
                        Quantity: {data.get('qty')[i]}
                        Time: {data.get('date')[i]}              
                           """)
                break
            # add data
            elif sorov_report == '2':
                for i in range(len(data_add.get('name'))):
                    son += 1
                    print(f"""
                        Name: {data_add.get('name')[i]}
                        Price: {data_add.get('price')[i]}
                        Quantity: {data_add.get('qty')[i]}
                        Time: {data_add.get('date')[i]}              
                           """)
                break

            # sell data
            elif sorov_report == '3':
                for i in range(len(data_sell.get('name'))):
                    son += 1
                    print(f"""
                        Name: {data_sell.get('name')[i]}
                        Price: {data_sell.get('price')[i]}
                        Quantity: {data_sell.get('qty')[i]}
                        Time: {data_sell.get('date')[i]}              
                           """)
                break

            # exit while
            elif sorov_report == '4':
                break
            else:
                continue

    # Stop programm
    elif sorov == "stop":
        break
    else:
        continue

