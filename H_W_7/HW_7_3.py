def ser_value(my_list):
    rez = sum(my_list)/len(my_list)
    return rez

def mediana(my_list):

    if len(my_list) % 2 == 0:
        rez = (my_list[len(my_list)//2] + my_list[len(my_list)//2 - 1]) / 2
        return rez
    else:
        rez = my_list[len(my_list)//2]
        return rez



gen_list = [i for i in range(2, 10)]
print(f' We have the list - {gen_list} his average value is {ser_value(gen_list)}, and mediana - {mediana(gen_list)}')
