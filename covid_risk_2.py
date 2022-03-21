# burada da covid_risk hesaplama satırında değil de print satırında bool(covid_risk) yaparak doğru sonuca ulaşmış oldum.
age = input("Are you a cigarette addict older than 75 yers old ? (Please enter 1(for True) /0 (for False)) : ")
chronic = input("Do you have a severe chronic dissease (Please enter 1(for True) /0 (for False)) : ")
immune = input("Is your immune system too weak? (Please enter 1(for True) /0 (for False)) : ")
covid_risk = int(age) or int(chronic) or int(immune)
print("Your covid risk is : " , bool(covid_risk))
