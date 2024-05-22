try:
    print([].pop(1))
except IndexError as ex:
    print(ex)