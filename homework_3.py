from datetime import datetime


def get_days_from_today(date):
  
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d")
        current_date = datetime.today()
        diff_days = current_date - input_date
        return (f"Days difference: {diff_days.days}")
    except ValueError:
        print ('Please add the date in format: Year-Month-Day')
      
print (get_days_from_today('2020-10-09'))


#_______________________


from random import randint
def get_numbers_ticket(min, max, quantity):

    if min < 1 or max > 1000 or min >= max or quantity < 1 or quantity > (max - min + 1):
        return []
    
    random_numbers = set()
    while len(random_numbers) < quantity:
        random_numbers.add(randint(min, max))

    return sorted(list(random_numbers))

print(f"Ваші лотерейні числа: {get_numbers_ticket(1, 49, 6)}")

#_______________________


import re

def normalize_phone(phone_number):
       clean_number = re.sub(r'[^0-9]', '', phone_number)
       if not clean_number.startswith('+'):
           if clean_number.startswith('380'):
               return '+' + clean_number[0:]
           else:
               return '+38' + clean_number[0:]

raw_numbers = """
   "067\\t123 4567",
   "(095) 234-5678\\n",
   "+380 44 123 4567",
   "380501234567",
   "    +38(050)123-32-34",
   "     0503451234",
   "(050)8889900",
   "38050-111-22-22",
   "38050 111 22 11   ",
"""

phone_numbers_list = raw_numbers.strip().split('\n')

sanitized_numbers = [normalize_phone(num) for num in phone_numbers_list]
final_output = ', '.join(sanitized_numbers)
print("Нормалізовані номери телефонів для SMS-розсилки:", final_output)

print(type(raw_numbers)) #string / рядок
print(type(final_output)) #string / рядок