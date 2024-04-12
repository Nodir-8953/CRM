import datetime
data = {
    'name': ['OLMA', 'ANOR'],
    'price': ['20000', '35000'],
    'qty': ['20', '30'],
    'date': ['04.04.24', '03.04.24']
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
    sorov = input("Add product -->1\nSell product -->2\nReport data-->3\nExit -->stop\n>>>")

    # add Product
    if sorov == '1':
        while True:
            name = input('Product name: ').upper()
            if name in data['name']:                
                index = data['name'].index(name)
                print(f"Ushbu mahsulotdan skladda {data['qty'][index]} ta mavjud")
                qty = input('Yana nechta mahsulot qushmoqchisiz: ')
                price = input('Product price: ')
                data['qty'][index] = int(data['qty'][index]) + int(qty)
                data['date'][index] = datetime.datetime.now().strftime("%d.%m.%y")
                data['price'][index] = int(price)
                data_add['name'].append(name)
                data_add['price'].append(price)
                data_add['qty'].append(qty)
                data_add['date'].append(datetime.datetime.now().strftime("%d.%m.%y"))
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
                data['date'].append(datetime.datetime.now().strftime("%d.%m.%y"))
                data_add['name'].append(name)
                data_add['price'].append(price)
                data_add['qty'].append(qty)
                data_add['date'].append(datetime.datetime.now().strftime("%d.%m.%y"))
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
            if stuff in data['name']:
                index = data['name'].index(stuff)
                qty = int(input('Product quantity: '))
                if qty <= int(data['qty'][index]):
                    Summa += (qty * int(data['price'][index]))
                    count += qty

                    data_sell['name'].append(stuff)
                    data_sell['qty'].append(qty)
                    data_sell['price'].append(data['price'][index])
                    data_sell['date'].append(datetime.datetime.now().strftime("%d.%m.%y"))
                    opros = input('Yana mahsulot olish uchun-->1\nChiqish uchun -->2\n>>>')
                    if opros == '1':
                        continue
                    else:
                        print('Sizning savatingizda jami:')
                        print('------------------------------------')
                        for i in range(len(data_sell['name'])):
                            print(f"{data_sell.get('name')[i]}  - {data_sell.get('qty')[i]} x {data_sell.get('price')[i]} som")
                        print(f"""Xaridingiz umumiy miqdori {Summa} som
                                QQS bilan {int(Summa * 1.12)} som
                                --------------------------------------
                                 Umumiy narx: {int(Summa * 1.12)}""")
                        break
                else:
                    print(f"Skladda {data['qty'][index]} ta {data['name'][index]} mavjud")
                    print('------------------------------')
                    opros = input('Kamroq qiymat kiritish uchun -->1\nChiqish uchun -->2\n>>>')
                    if opros == '1':
                        continue
                    else:
                        break
            else:
                print('Ushbu mahsulot skladda mavjud emas')
                print('--------------------------------')
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
            # elif sorov_report == '3':
            #     for i in range(len(data_sell.get('name'))):
            #         son += 1
            #         print(f"""
            #             Name: {data_sell.get('name')[i]}
            #             Price: {data_sell.get('price')[i]}
            #             Quantity: {data_sell.get('qty')[i]}
            #             Time: {data_sell.get('date')[i]}              
            #                """)
            #     break

            # report date
            elif sorov_report == '3':
                # print('salom')
                while True:
                    sorov = input('Umumiy sotilgan tovarlar ruyxati -->1\nQaysidir kuni sotilgan tovarlar ruyxati -->2\nAprel oyida sotilgan tovarlar ruyxati -->3\nExit -->4\n>>>')
                    if sorov == '1':
                        for i in range(len(data_sell.get('name'))):
                            son += 1
                            print(f"""
                                Name: {data_sell.get('name')[i]}
                                Price: {data_sell.get('price')[i]}
                                Quantity: {data_sell.get('qty')[i]}
                                Time: {data_sell.get('date')[i]}              
                                """)
                        # break
                    elif sorov == '2':
                        while True:
                            date = input("Vaqtni kiriting (format day.month.year): ")
                            if (len(date.split('.')) == 3 and 1 <= int(date.split('.')[0]) <= 31 and 1 <= int(date.split('.')[1]) <= 12 and 20 <= int(date.split('.')[2]) <= 24):
                                
                                if date in data_sell['date']:
                                    # i = data_sell['date'].index(date)
                                    for i in range(len(data_sell['name'])):
                                        print(f"{data_sell.get('name')[i]}  - {data_sell.get('qty')[i]} x {data_sell.get('price')[i]} som")
                                    print(f"""Sotuvning umumiy miqdori {Summa} som
                                            QQS bilan {int(Summa * 1.12)} som
                                            --------------------------------------
                                            Umumiy Summa: {int(Summa * 1.12)}""")
                                    break
                                else:
                                    print('Shu kuni mahsulot sotilmagan!!!')
                                    print('--------------------------------')
                                    break
                            else:
                                print('Vaqtni tugri formatda kiriting!!!!')
                    elif sorov == '3':
                        Summ = 0
                        while True:
                            for i, ter in enumerate(data_sell['date']):
                                if data_sell['date'][i].split('.')[1] == '04':
                                    Summ += (qty * int(data['price'][i]))
                                    # print(data_sell['name'][i])
                                    print(f"{data_sell.get('name')[i]}  - {data_sell.get('qty')[i]} x {data_sell.get('price')[i]} som")
                            print(f"""Sotuvning umumiy miqdori {Summa} som
                                            QQS bilan {int(Summ * 1.12)} som
                                            --------------------------------------
                                            Umumiy Summa: {int(Summ * 1.12)}""")
                            break
                    elif sorov == "4":
                        break
                    else:
                        continue
            elif sorov_report == "4":
                break
            else:
                continue 
    # Stop programm
    elif sorov == "stop":
        break
    else:
        continue

