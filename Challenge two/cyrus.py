year = int(input("year of birth"))
Age = 2019 - year

if Age < 18:
    print("minor")
elif Age > 18:
    print("youth")
elif Age > 36:
    print("elder")