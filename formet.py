def print_name_in_x(name, size):
    for i in range(size):
        print(' ' * (size - i - 1) + name[0] + ' ' * (2 * i) + name[1]+ ' ' * (2* i) + name[2])
    for i in range(size - 2, -1, -1):
        print(' ' * (size - i - 1) + name[0] + ' ' * (2 * i) + name[1]+ ' ' * (2* i) + name[2])

print_name_in_x('Sathvik', 5)






































