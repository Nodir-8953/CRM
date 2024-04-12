import datetime
def data_func():
    global data, data_add, data_sell
    data = {'name': [],
    'price': [],
    'qty': [],
    'date': [],}
    data_add = {'name': [],
    'price': [],
    'qty': [],
    'date': [],}
    data_sell = {'name': [],
    'price': [],
    'qty': [],
    'date': [],}

def add_product():
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
            add_product()
        else:
            main()
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
            add_product()
        else:
            main()
        
def sell_product():
        Summa = 0
        count = 0
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
                opros = input('Yana mahsulot qushish uchun-->1\nChiqish uchun -->2\n>>>')
                if opros == '1':
                    sell_product()
                else:
                    print('Sotilgan tovarlar jami:')
                    print('------------------------------------')
                    for i in range(len(data_sell['name'])):
                        print(f"{data_sell.get('name')[i]}  - {data_sell.get('qty')[i]} x {data_sell.get('price')[i]} som")
                    print(f"""Tovarlarning umumiy miqdori {Summa} som
                                QQS bilan {int(Summa * 1.12)} som
                                --------------------------------------
                                 Umumiy narx: {int(Summa * 1.12)}""")
                    main()
            else:
                print(f"Skladda {data['qty'][index]} ta {data['name'][index]} mavjud")
                print('------------------------------')
                opros = input('Kamroq qiymat kiritish uchun -->1\nChiqish uchun -->2\n>>>')
                if opros == '1':
                    sell_product()
                else:
                    main()
        else:
            print('Ushbu mahsulot skladda mavjud emas')
            print('--------------------------------')
            opros = input('Boshqa mahsulot olish uchun -->1\nChiqish uchun -->2\n>>>')
            if opros == '1':
                sell_product()
            else:
                main()
    
def report_product():
    sorov_report = input('Umumiy tovarlar ruyxati -->1\nQushilgan tovarlar ruyxati-->2\nSotilgan tovarlar ruyxati -->3\nChiqish -->4\n>>>')
    if sorov_report == '1':
        for i in range(len(data.get('name'))):
            print(f"""
                        Name: {data.get('name')[i]}
                        Price: {data.get('price')[i]}
                        Quantity: {data.get('qty')[i]}
                        Time: {data.get('date')[i]}              
                           """)
        main()
    elif sorov_report == '2':
        for i in range(len(data_add.get('name'))):
            print(f"""
                        Name: {data_add.get('name')[i]}
                        Price: {data_add.get('price')[i]}
                        Quantity: {data_add.get('qty')[i]}
                        Time: {data_add.get('date')[i]}              
                           """)
        main()
    elif sorov_report == '3':
        sorov = input('Umumiy sotilgan tovarlar ruyxati -->1\nQaysidir kuni sotilgan tovarlar ruyxati -->2\nOy kesimida sotilgan tovarlar ruyxati -->3\nExit -->4\n>>>')
        if sorov == '1':
            for i in range(len(data_sell.get('name'))):
                print(f"""
                                Name: {data_sell.get('name')[i]}
                                Price: {data_sell.get('price')[i]}
                                Quantity: {data_sell.get('qty')[i]}
                                Time: {data_sell.get('date')[i]}              
                                """)
            main()    
        elif sorov == '2':
            Summa = 0
            date = input("Vaqtni kiriting (format day.month.year): ")
            if (len(date.split('.')) == 3 and 1 <= int(date.split('.')[0]) <= 31 and 1 <= int(date.split('.')[1]) <= 12 and 20 <= int(date.split('.')[2]) <= 24):                    
                if date in data_sell['date']:
                    for i in range(len(data_sell['name'])):
                        Summa += (int(data_sell.get('qty')[i]) * int(data['price'][i]))
                        print(f"{data_sell.get('name')[i]}  - {data_sell.get('qty')[i]} x {data_sell.get('price')[i]} som")
                    print(f"""Sotuvning umumiy miqdori {Summa} som
                                            QQS bilan {int(Summa * 1.12)} som
                                            --------------------------------------
                                            Umumiy Summa: {int(Summa * 1.12)}""")
                    main()                
                else:
                    print('Shu kuni mahsulot sotilmagan!!!')
                    print('--------------------------------')
                    main()                
            else:
                print('Vaqtni tugri formatda kiriting!!!!')
                report_product()
        elif sorov == '3':
            Summ = 0
            oy = input("Oyni kiriting (01,02,03....12 formatda)\n>>>")
            for i, ter in enumerate(data_sell['date']):
                if data_sell['date'][i].split('.')[1] == oy:
                    Summ += (int(data_sell.get('qty')[i]) * int(data['price'][i]))
                    print(f"{data_sell.get('name')[i]}  - {data_sell.get('qty')[i]} x {data_sell.get('price')[i]} som")
                else:
                    print(f"{oy.capitalize()}da tovar sotilmagan!!!! ")    
                    report_product()
            print(f"""Sotuvning umumiy miqdori {Summ} som
                        QQS bilan {int(Summ * 1.12)} som
                    --------------------------------------
                        Umumiy Summa: {int(Summ * 1.12)}""")
            main()                
        
        else:
            main()                       
    elif sorov_report == "4":
        main()
    else:
        report_product()
def main():
    sorov = input('1,2,3>>>')
    if sorov == '1':
        add_product()
    elif sorov == '2':
        sell_product()
    elif sorov == '3':
        report_product()
    else:
        print('notugri buyruq')
        main()

data_func()
if __name__ == "__main__":
    main()
