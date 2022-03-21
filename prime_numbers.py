num_limit=int(input("Enter a limit number: "))
prime_list=[]

for i in range(2, num_limit+1):
  counter = 0
  for j in range(2, i):
    if i % j == 0:
      counter += 1
  if counter == 0:
    prime_list.append(i)
print(prime_list)
