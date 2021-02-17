#Truthy and falsey
print('----- Truthy and Falsey -----')
print('String \'Hello world\': ',bool('Hello world')) #true
print('Empty string \'\': ',bool('')) #false
print('Number 123: ', bool(123)) #true
print('Number 0: ', bool(0)) #false
print('\n')

#so it's possible use these values in conditional logic

#Ternary operator
print('----- Ternary operator -----')
#condidition_if_true if condition else condition if else
age = 20
print('Testing ternary operator:')
print('You can drink') if age >= 21 else print('You can\'t drink')
print('')

#Enumerate
print('----- Enumerate -----')
#enumerate generate a tuple of index and value of anything iterable

for index,value in enumerate(list(range(50,3,-2))):
    if index == 15:
        print('The value is: ',value)
print('')
#Keyarguments e default parameters
#Docstring
# *args and **kwargs
#rule -> params, args, default params, kwargs

#Walrus operator 
#Global and Nonlocal keywords
#How to do not skip a line when you are printing something
print('----- string end != \\n -----')
print('**** same line***** ',end='')
print('#### diferent line #####',end='')  #default: end = \n 