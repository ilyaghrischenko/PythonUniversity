from task2 import is_year_leap, days_in_month

def day_of_year(year, month, day):
    if day < 1 or month < 1 or month > 12:
        return None
    days = 0
    for m in range(1, month):
        month_days = days_in_month(year, m)
        if month_days is None:
            return None
        days += month_days
    if day > days_in_month(year, month):
        return None
    return days + day

print(day_of_year(2000, 12, 31)) #366
print(day_of_year(1900, 2, 29)) #None
