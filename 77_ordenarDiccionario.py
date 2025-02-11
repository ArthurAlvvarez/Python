poblaciones = {
    "China": 1411778724,
    "India": 1393409038,
    "Estados Unidos": 332915073,
    "Indonesia": 276361783,
    "Pakistán": 225199937,
    "Brasil": 213993437,
    "Nigeria": 211400708
}

array = []
dic ={}

for i,j in poblaciones.items():
    array.append(j)

array.sort(reverse=True)

for i in array:
    for j,k in poblaciones.items():
        if i == k:
            dic[j] = k
print(dic)
