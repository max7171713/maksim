a = int(input("сколько вам лет"))
b = int(input("какое у вас з/п?"))
c = input("вы судимы?")
if a>=25 and b>=35000 and c == "нет":
    if b <= 35000:
        print("мы предлогаем вам не более 2kk с процентом 7% годовых")
        exit()
    if b <= 70000:
        print("мы предлогаем вам не более 5kk с процентом 10% годовых")
        exit()
    if b <= 100000:
        print("мы предлогаем вам не более 10kk с процентом 8% годовых")
        exit()
    if b > 100001:
        print("мы предлогаем вам не более 13kk с процентом 6% годовых и вам нужно это сдать не менее 2 лет и не более 10 лет")
        print("мы предлогаем вам не более 20kk с процентом 6.5% годовых и вам нужно это сдать не менее 2 лет и не более 10 лет")
        exit()
if a<25 and b<35000 and c == "да":
    print("вам отказано")
    exit()
if a<25 and b<35000:
    print("вам отказано")
    exit()
if b<35000 and c == "да":
    print("вам отказано")
    exit()
if a<25 and c == "да":
    print("вам отказано")
    exit()
if a<14:
    print("иди подрости")
    exit()
if a<=18 or a==14:
    v = input("вы дееспасобны?")
    if v == "да":
        d = input("у вас был успешный кредит,у вас есть машина,у вас есть дом на более 3.5kk?")
        if d == "нет":
            b = int(input("повторите какая увас з/п"))
            if b >= 25000:
                print("предлогаем вам кредитку на 100k")
            else:
                print("вам отказано")
        if d == "да":
            print("вам одобрено")
            if b >= 70000 or b == 99999:
                print("мы предлогаем вам не более 5kk с процентом 10% годовых")
                exit()
            if b >= 40000 or b == 69999:
                print("мы предлогаем вам не более 2kk с процентом 7% годовых")
    else:
        print("вам отказано")
        
else:
    d = input("у вас был успешный кредит,у вас есть машина,у вас есть дом на более 3.5kk?")
    if d == "нет":
        b = int(input("повторите какая увас з/п"))
        if b >= 25000:
            print("предлогаем вам кредитку на 100k")
        else:
            print("вам отказано")
    if d == "да":
        print("вам принято")
        if b <= 35000:
            print("мы предлогаем вам не более 2kk с процентом 7% годовых")
            exit()
        if b <= 70000:
            print("мы предлогаем вам не более 5kk с процентом 10% годовых")
            exit()
        if b <= 100000:
            print("мы предлогаем вам не более 10kk с процентом 8% годовых")
            exit()
        if b > 100001:
            print("мы предлогаем вам не более 13kk с процентом 6% годовых и вам нужно это сдать не менее 2 лет и не более 10 лет")
            print("мы предлогаем вам не более 20kk с процентом 6.5% годовых и вам нужно это сдать не менее 2 лет и не более 10 лет")
            exit()