import os

def write_sales_log(order):
    #file = open(os.getcwd() + 'sales_log.txt', 'a')
    file = open('sales_log.txt', 'a')

    total = 0
    for item, price in order.items():
        file.write(item + ' ' + format(price, '.2f') + '\n')
        total += price

    file.write('total = ' + format(total, '.2f') + '\n\n')
    file.close()


def main():
    print(os.getcwd())

    order = {"Matcha": 5.0, "Gyokuro": 4.0}
    write_sales_log(order)

    order = {"Chocolate": 3.5, "Candies": 2.0}
    write_sales_log(order)
    

main()






