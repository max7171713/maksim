command = input("введите + или - или * или /")
while command !="стоп":
    if command == "+":
        a = int(input("введите слагаемое 1"))
        b = int(input("введите слагаемое 2"))
        print(a+b,"вот ваша сумма")
    elif command == "-":
        с = int(input("введите вычитаемое"))
        d = int(input("введите вычитатель"))
        print(c-d,"вот ваша разность")
    elif command == "*":
        v = int(input("введите 1 множетель"))
        n = int(input("введите 2 множетель"))
        print(v*n,"вот ваш результат")
    elif command == "/":
        m = int(input("введите делимое"))
        j = int(input("введите делитель"))
        print(m/j,"вот ваш результат")
    else:
        print("что то не то напишити сного + или - или * или / или стоп что бы выйти")
    command = input("хотите повторить значит напишите + или - или * или / или стоп что бы выйти")