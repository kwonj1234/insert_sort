import random

def insert_sort(x):
    #for an unordered list x, create a function that sorts the list
    #using an insertion sort algorithm 
    #that means you have to sort in place!
    for i in range(len(x)):
        j = i
        k = i - 1
        while k >= 0:
            if x[j] < x[k]:
                x[j], x[k] = x[k], x[j]
            j -= 1
            k -= 1

    return x

x = [random.randrange(0,100) for i in range(0,11)]
print(x)
print(insert_sort(x))

 

