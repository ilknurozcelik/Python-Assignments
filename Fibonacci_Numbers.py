# Control flow statements ve range fonksiyonu kullanılarak 1-55 arası 
# Fibonacci sayılarının listesini yazdıran bir kod yazalım.

fibn_list = []
a = 0
b = 1

for i in range(20):
  fibn_list.append(b)
  c = a + b
  a = b
  b = c

  if b > 55:
    break
   
print(fibn_list)
