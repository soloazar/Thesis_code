# sum_integers_args_2.py
def my_sum(*integers):
    result = 0
    for x in integers:
        result += x
    return result

print(my_sum())
