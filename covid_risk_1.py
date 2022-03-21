# Aşağıdaki kod ile doğru sonuca ulaştım. Girdilere ve Türlerine Dikkat!!!!
age = input("Are you a cigarette addict older than 75 yers old ? (Please enter 1(for True) /0 (for False)) : ")
chronic = input("Do you have a severe chronic dissease (Please enter 1(for True) /0 (for False)) : ")
immune = input("Is your immune system too weak? (Please enter 1(for True) /0 (for False)) : ")
covid_risk = bool(int(age)) or bool(int(chronic)) or bool(int(immune))
print("Your covid risk is : " , covid_risk)
