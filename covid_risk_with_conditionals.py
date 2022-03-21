# Covid assignment ının if conditionals ile çözümü:
age = input("Are you a cigarette addict older than 75 yers old ? (Please enter 1(for True) /0 (for False)) : ")
chronic = input("Do you have a severe chronic dissease (Please enter 1(for True) /0 (for False)) : ")
immune = input("Is your immune system too weak? (Please enter 1(for True) /0 (for False)) : ")
covid_risk = bool(int(age) or int(chronic) or int(immune))
if covid_risk == True:
  print("You are in risky group!")
else:
  print("You are not in risky group!")
