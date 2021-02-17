#list, set, dictionary 

#list
my_list = [char for char in 'hello']
print('List 1: \n',my_list)
'''
my_list2 = [num*2 for num in range (100)]
print('List 2: \n',my_list2)

my_list3= [ num for num in range(100) if num %2 !=0]
print('List 3: \n',my_list3)
'''
#set
my_set1 = {char for char in 'hello'}
print('Set 1: \n',my_set1)

#dict
listinha = [('a',1),('b',2)]
my_dict1  = {key:value**2 for key, value in listinha }
print('Dict 1: \n',my_dict1)
