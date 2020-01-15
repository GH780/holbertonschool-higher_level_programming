#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list = [None] * list_length
    for i in range(list_length):
        try:
            list[i] = (my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            list[i] = 0
            print("division by 0")
        except TypeError:
            print("wrong type")
            list[i] = 0
        except IndexError:
            print("out of range")
            list[i] = 0

    return list
