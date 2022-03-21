num = input("Please enter a number :")

if num.isdigit():  # Girilen verinin ondalıklı sayı olup olmadığını kontrol edelim.
  
    num_list = list(num)
    num_armst = 0
    
    for i in range(len(num_list)):
      num_armst += int(num_list[i]) ** len(num_list)
       
    if num_armst == int(num):
      print(f"{num} is an Armstrong number.")
    else:
      print(f"{num} is not an Armstrong number.")
  
else:  # Girilen değer isdigit() kuralına uymuyorsa negatif, float veya string olabilir.
    print(" It is an invalid entry. Don't use non-numeric, float or negative values!")
