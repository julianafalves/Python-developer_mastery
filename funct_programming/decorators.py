# @decorator -> super charge our function
# Higher order function HOC
'''
def hello():
    print("Helllooooo")
'''
def my_decorator(func):
    def wrap_func():
        a = func()
        b = 'Juliana'
        print(a,b)
    return wrap_func

@my_decorator
def hello():
    return 'Hellooo'

#Decorator Pattern 
def my_decorator2(func):
    def wrap_func(*args, **kwargs):
        a = func(*args, **kwargs)
        b = 'Juliana'
        print('*************')
        print(a,b)
        print('*************')
    return wrap_func

@my_decorator2
def hello2(greeting = 'hi', emoji = ''):
    return greeting +' '+ emoji

hello2('hii', ':)')
