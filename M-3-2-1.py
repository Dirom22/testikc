list = [1, 6, 8, 5, "hello", 6, 9, 7, "world", 5, 7, "hello"]
for i in range(0, len(list)):
    for j in range(i +1, len(list)):
        if (list[i] == list[j]):
            print(list[j])