# As an exercise, write a function that uses inputNumber to input a number
# from the keyboard and that handles the ValueError exception


def my_ValueError_exception():
    try:
        inputNumber = int(input('Enter a number: '))

        print(inputNumber)

    except ValueError:

        print('ValueError occurred')


my_ValueError_exception()
