# 
# Miguel Ravagnani de Carvalho
# 

#------------------------------------------------#
print("\n#------------------------------------------------#\n")

def hello_func():
    print("Hello Function")

hello_func()

#------------------------------------------------#
print("\n#------------------------------------------------#\n")

def hello_func_2(greeting):
    return '{} Function'.format(greeting)

print(hello_func_2('Hi'))

#------------------------------------------------#
print("\n#------------------------------------------------#\n")

def hello_func_3(greeting, name='You'):
    return '{}, {}'.format(greeting, name)

print(hello_func_3('Hi', 'name'))
print(hello_func_3('Hi'))

#------------------------------------------------#
print("\n#------------------------------------------------#\n")

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'Atr', name='John', age=22)

#------------------------------------------------#
print("\n#------------------------------------------------#\n")


month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(days_in_month(2020, 2))
