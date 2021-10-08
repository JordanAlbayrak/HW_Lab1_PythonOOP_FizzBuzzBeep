output_1 = "BEEP"
output_2 = "FIZZ"
output_3 = "BUZZ"

num = 0;
division_1 = 3
division_2 = 5
division_3 = 15


def fizzbuzzbeep(number):
    if number >= division_3 and number % division_1 == 0 and number % division_2 == 0 and number % division_3 == 0:
        print(output_2 + output_3 + output_1)
    elif number >= division_2 and number % division_1 == 0 and number % division_2 == 0:
        print(output_2 + output_3)
    elif number >= division_1 and number % division_1 == 0 and number % division_2 != 0:
        print(output_2)
    elif number >= division_2 and number % division_1 != 0 and number % division_2 == 0:
        print(output_3)
    else:
        print("Number cannot be divided by 3, 5 or 15")


while 1:
    num = input("Enter a number")

    try:
        if num == 'q':
            print("Exiting")
            quit()
        elif int(num):
            fizzbuzzbeep(int(num))
        else:
            pass
    except ValueError:
        print("You must enter an integer number!")
