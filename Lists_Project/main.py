
my_list = [2, 3.14, True, "welcome", [4, 5, 6]]
list2 = list("Hello")
print(list2)
in_check = "e" in list2
print(in_check)
not_in_check = "a" in list2
print(not_in_check)

a = [[0, 2], [4, 6], [8, 10], [12, 14]]
print(a[3][1])
string_list = ["chair", "table", "desk", "lamp", "bed"]
print(f"Most people own {a[0][1]} {string_list[-5]}s")
float_list = [0.98, 8.76, 6.54, 4.32]
sliced_list = float_list[0:2]
print(sliced_list)


arctic_animals = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
del arctic_animals[4]

arctic_animals.remove("elephant")

arctic_animals.insert(2, "snowy owl")
print(arctic_animals)
arctic_animals.sort()
print(arctic_animals)
print(arctic_animals.index("reindeer"))
print(arctic_animals.pop())

