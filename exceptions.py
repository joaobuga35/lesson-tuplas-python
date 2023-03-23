# main.py
def div_by_zero():
    try:
        a = 1
        b = 0
    except ZeroDivisionError:
        print('Não é possível dividir por zero')
    return a / b


def unexisting_key():
    my_dict = {"name": "Alex", "module": "M5"}

    return my_dict["address"]


def unexisting_index():
    my_list = [0, 1]

    return my_list[5]


def misterious_error():
    try:
        a = 5
    except TypeError:
        print('Value not defined')
    return a.capitalize()


if __name__ == "__main__":
    div_by_zero()
    unexisting_key()
    unexisting_index()
    misterious_error()