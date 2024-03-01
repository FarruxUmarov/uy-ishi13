def son(lst):
    lst = sorted(lst,key = lambda y : sum([int(son1) for son1 in str(y)]))
    return lst

lst = input("3 ta son kiriting: ").split()
lst = [int(number) for number in lst]

print(son(lst))