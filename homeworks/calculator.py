def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Wybierz operację.")
print("1.Dodawanie")
print("2.Odejmowanie")
print("3.Mnożenie")
print("4.Dzielenie")

while True:
    choice = input("Wybierz operację(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Podaj pierwszą liczbę: "))
        num2 = float(input("Podaj drugą liczbę: "))
        # print(add(num1, num2))

        if choice == '1':
            result = add(num1, num2)
            print(num1, ' + ', num2, ' = ', result)

        elif choice =='2':
            result = subtract(num1, num2)
            print(num1, ' - ', num2, ' = ', result)

        elif choice =='3':
            result = multiply(num1, num2)
            print(num1, ' * ', num2, ' = ', result)

        else:
            result = divide(num1, num2)
            print(num1, ' / ', num2, ' = ', result)

        question = (input('Czy wykonać kolenje działanie? T/N: ')).upper()
        if question == 'N':
            break

        elif question != 'T':
            print('Błędna wartość. Zakończenie programu.')
            break

    else:
        print("Błędna wartość, podaj poprawną.")
        break