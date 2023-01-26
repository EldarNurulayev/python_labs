f = open('Нурулаев_Э_С_ЗИТ22м_vvod.txt')
input = f.read().splitlines()
f.close()

output = open('Нурулаев_Э_С_ЗИТ22м_vivod.txt', "w")



#Определение начала и окончания чтения массивов
s = [line.split() for line in input]


arr1_read_stop = len(s[0])
arr2_read_start = len(s[0]) + 1

arr1 = [line.split() for line in input[:arr1_read_stop]]
arr2 = [line.split() for line in input[arr2_read_start:]]




print("Array 1:")
output.write("Array 1:"+'\n') 
for i in range(len(arr1[0])):
    print(arr1[i])
    output.write(str(arr1[i])+'\n') 

print("\n")
output.write("\n")

#Поиск наибольших элементов строк в массиве 1
print("The greatest elements of the array1 rows:")
output.write("The greatest elements of the array1 rows:"+'\n') 
for i in range(len(arr1[0])):
    max = int(arr1[i][0])
    for j in range(len(arr1[0])):
        if int(arr1[i][j]) > max:
            max = int(arr1[i][j])
    print(f"Row {i+1}: {max}")
    output.write(f"Row {i+1}: {max}\n")

#Поиск наименьших элементов столбцов в массиве 1
print("\nThe smallest elements of the array1 columns:")
output.write("\nThe smallest elements of the array1 columns:"+'\n') 
for i in range(len(arr1[0])):
    min = int(arr1[0][i])
    for j in range(len(arr1[0])):
        if int(arr1[j][i]) < min:
            min = int(arr1[j][i])
    print(f"Column {i+1}: {min}")
    output.write(f"Column {i+1}: {min}\n")





print("\n\nArray 2:")
output.write("\n\nArray 2:"+'\n') 
for i in range(len(arr1[0])):
    print(arr2[i])
    output.write(str(arr2[i])+'\n')

#Поиск наибольшего элемента диагоналей в массиве 2
max_d = 0
s_index = len(arr2[0]) - 1 #Максимальный индекс массива 2 (для прохода по побочной диагонали)


for i in range(len(arr2[0])):
    if float(arr2[i][i]) > max_d:
        max_d = float(arr2[i][i])
    if float(arr2[i][s_index - i]) > max_d:
        max_d = float(arr2[i][s_index - i])
print(f"\nThe greatest element of the array 2 diagonals: {max_d}")
output.write(f"\nThe greatest element of the array 2 diagonals: {max_d}\n")

#Замена центрального элемента массива 2 на наибольший диагональный элемент массива 2
center_index = (len(arr2[0]) - 1) // 2 #Индекс центрального элемента

for i in range(len(arr2[0])):
    for j in range(len(arr2[0])):
        if float(arr2[i][j]) == max_d:
            max_d_i = i #Индекс i наибольшего элемента диагоналей в массиве 2
            max_d_j = j #Индекс j наибольшего элемента диагоналей в массиве 2

temp = arr2[center_index][center_index]
arr2[center_index][center_index] = arr2[max_d_i][max_d_j]
arr2[max_d_i][max_d_j] = temp

print("\nArray 2 (updated):")
output.write("\nArray 2 (updated):"+'\n') 
for i in range(len(arr1[0])):
    print(arr2[i])
    output.write(str(arr2[i])+'\n')

output.close()