L=[]
n=int(input("Enter Number of Tuples: "))
for x in range(n):
    T=tuple(map(int,input(f"Enter Tuple {x+1} separated by comma: ").split(',')))
    L.append(T)
# Bubble sort logic
for i in range(len(L)):
    for j in range(len(L) - i - 1):
        if L[j][-1] >L[j+1][-1]:
            L[j],L[j+1]=L[j+1],L[j]
print("Sorted List of Tuple By Last Element of Each Tuple: ")
print(L)
