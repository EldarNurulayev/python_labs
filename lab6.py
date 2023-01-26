#1
print("Задание 6.1")
arr1  = [1, 2, 3, 4, 5, 20, 7, 11, 10, 9]
print(f"Массив 1: {arr1}")

max = arr1[0]
for item in arr1:
        if item > max:
           max = item

index = arr1.index(max)


higher_elem_count = 0
lower_elem_count = 0
for item in arr1:
        if arr1.index(item) > index:
           higher_elem_count += 1
        
        if arr1.index(item) < index:
           lower_elem_count +=1


print(f"Максимальное число: {max}")
print(f"Чисел больше максимального: {higher_elem_count}")
print(f"Чисел меньше максимального: {lower_elem_count}")


#2
print("\n\nЗадание 6.2")
print("Введите 10 чисел:")

try:
   arr2 = [ int(input()) for i in range(10) ]
   print(f"Массив 2: {arr2}")

   sum = 0
   for item in arr2:
         if item > 5:
              sum += item

   print(f"Сумма чисел больше 5: {sum}")
except:
   print("Please press Enter after every new number add")






