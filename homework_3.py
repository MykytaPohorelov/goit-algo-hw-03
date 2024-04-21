from datetime import datetime


def get_days_from_today(date):
  
    try:
        input_date = datetime.strptime(date, "%Y.%m.%d")
        current_date = datetime.today()
        diff_days = current_date - input_date
        return (f"Days difference: {diff_days.days}")
    except ValueError:
        print ('Please add the date in format: Year.Month.Day')
      


print (get_days_from_today('2020.10.09'))


#_______________________


from random import randint, sample
def get_numbers_ticket(min, max, quantity):
       lottery_numbers = set()
       while len(lottery_numbers) != quantity:
            lottery_numbers.add(randint(min, max))
            return sorted(sample(range(min, max), quantity))


print(f"Ваші лотерейні числа: {get_numbers_ticket(1, 49, 6)}")


#_______________________


import re


raw_numbers = [
   "067\\t123 4567",
   "(095) 234-5678\\n",
   "+380 44 123 4567",
   "380501234567",
   "    +38(050)123-32-34",
   "     0503451234",
   "(050)8889900",
   "38050-111-22-22",
   "38050 111 22 11   ",
]


def normalize_phone(phone_number):
   normalized_numbers = []
   for number in phone_number:
       clean_number = re.sub(r'[^0-9]', '', number)
       if not clean_number.startswith('+'):
           if clean_number.startswith('380'):
               clean_number = '+' + clean_number
           else:
               clean_number = '+38' + clean_number
       normalized_numbers.append(clean_number)
   return normalized_numbers


normalized_numbers = normalize_phone(raw_numbers)
print(f"Нормалізовані номери телефонів для SMS-розсилки: {normalized_numbers}")
