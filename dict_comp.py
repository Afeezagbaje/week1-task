stop = int(input("Stop:\n"))
step = int(input("Step:\n"))

def dict_comp(stop, step):
    stop_list = [n for n in range(1,stop + 1)]

    ''' dividing the stop_list into a number(step - which the user will provide) 
    of smaller list and removing list which length is 
    less the step (i.e number given by the user)'''
    stop_yield = [stop_list[i: i + step] for i in range(0, len(stop_list), step)]
    stop_actual = [n for n in stop_yield if len(n) == step]
    # this helps in numbering the items i.e items-**
    items = [f'items-{i + 1}' for i in range(len(stop_actual))]
    # creating a dictionary that takes the items-** with the corresponding stop_actual
    complete_dict = {items[i]:stop_actual[i] for i in range(len(stop_actual))}

    return complete_dict


print(dict_comp(stop, step))