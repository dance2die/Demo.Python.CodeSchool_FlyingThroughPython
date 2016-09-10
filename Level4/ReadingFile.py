def read_sales_log():
    file = open('sales_log.txt', 'r')
    for line in file:
        line = line.strip()
        print(line)

    file.close()


def main():
    read_sales_log()


main()