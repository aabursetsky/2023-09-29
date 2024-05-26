my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
len_my_list = len(my_list)
counter = 0

while counter < len_my_list:    # строго меньше
    if my_list[counter] > 0:
        print(my_list[counter])
        counter += 1
        continue
    if my_list[counter] == 0:   # если 0 продолжаем
        counter += 1
        continue
#    if my_list[counter] < 0:   # можно без него 
    break
