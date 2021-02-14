class PlayerCharacter:
    membership =  True #Class Object Attribute -> STATIC
    def __init__(self,name,age): 
        self.name = name #-> Dynamic
        self.age = age
    def run(self):
        print('RUN')

player1 = PlayerCharacter('Juliana',20)
print(player1.name)
print(player1.age)
player2 = PlayerCharacter('Ana', 22)
#player 1 and 2 are allocated in 2 different places in the memory:
print(player1)
print(player2) 

#show all class information 
help(player1)
#help(list)