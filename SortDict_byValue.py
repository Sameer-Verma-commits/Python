D={}
# Input for dictionary
n=int(input("Enter Number of Key-Value Pairs: "))
for i in range(n):
    key=input(f"Enter a Key{i+1}: ")
    value=input(f"Enter a Value{i+1}: ")
    D[key]=value
#sorting dict
rev=int(input("1.Ascending \n2.Descending \nEnter Your Choice {1/2}: "))
new={}
keys = list(D.keys())
values = list(D.values())

# Bubble sort logic
for i in range(len(values)):
    for j in range(len(values) - i - 1):
        
        if rev == 1 and values[j] > values[j + 1]:
            values[j], values[j + 1] = values[j + 1], values[j]
            keys[j], keys[j + 1] = keys[j + 1], keys[j]
        if rev == 2 and values[j] < values[j + 1]:
            values[j], values[j + 1] = values[j + 1], values[j]
            keys[j], keys[j + 1] = keys[j + 1], keys[j]
for i in range(len(keys)):
    new[keys[i]] = values[i]
print("\nSorted Dictionary: ",new)
