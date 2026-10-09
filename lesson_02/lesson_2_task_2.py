def is_year_leap(number):
    return True if number % 4 == 0 else False


num = int(input("введите номер года: "))
result = is_year_leap(num)

print(f"год {num}: {result}")
