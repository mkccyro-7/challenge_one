print("your date of birth (mm dd yyyy)")
date_of_birth = input("--->")

print("Today's date: (mm dd yyyy)")
todays_date = input("--->")

from datetime import date
def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month,born.day))
age = calculate_age(date_of_birth)
str(age ='calculate_age') 
