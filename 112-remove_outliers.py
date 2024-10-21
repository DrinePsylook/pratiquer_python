# Remove Outliers
l = [6,8,9,1,5,3,88,10,65,426,325,44]

def del_numbers(user_list, n):
    new_list = sorted(user_list)
    print(new_list)

    for i in range(n):
        new_list.pop()
    print(new_list)
    
    for i in range(n):
        new_list.pop(0)
    
    return new_list

lt = del_numbers(l, 3)

print(lt)