
from os.path import exists
import datetime
if not exists('sample.txt'):
    with open('sample.txt', 'w') as f:
        f.write('Function name\t|\tWorked time\t|\tArguments as list\t|\tArguments as dictionary\t|\tFunction results\t|\n') 
def logger(func):
    def wrapper(*args,**kwargs):
        try:
            result = ''
        except Exception as error:
            result = error
        with open('sample.txt','a') as f:
            if args and kwargs:
                f.write(f'{func.__name__}\t|\t{datetime.datetime.today()}\t|\t{args}\t|\t{kwargs}\t|\t{result}\t|\n')
            elif args:
                f.write(f'{func.__name__}\t|\t{datetime.datetime.today()}\t|\t{args}\t|\t{str()}\t|\t{result}\t|\n')
            elif kwargs:
                f.write(f'{func.__name__}\t|\t{datetime.datetime.today()}\t|\t{str()}\t|\t{kwargs}\t|\t{result}\t|\n')
    return wrapper
@logger
def sum(a,b):
    return a+b
@logger
def divide(a,b):
    return a/b
sum(1,2)
divide(a=4,b=2)
divide(10,0)