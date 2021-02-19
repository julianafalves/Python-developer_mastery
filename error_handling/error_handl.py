#Error Hanfling
while True:
    try: 
        age = int(input('age: '))
        print(10/age)
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print('please enter age higher than 0')
    else:
        print('Thank you')
        break
    finally:
        print('Finally here')

def sum(num1, num2):
    try:
        return  num1 / num2 
    except (TypeError,ZeroDivisionError) as err:
        print(f'oops: {err}')

print(sum(1,0))