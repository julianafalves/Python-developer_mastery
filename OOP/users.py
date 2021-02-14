class User(object):
    def __init__(self,email):
        self.email = email
    
    def sign_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self,name, power,email):
        super().__init__(email)
        self.name = name
        self.power = power

class Archer(User):
    def __init__(self, name, number_rows,email):
        super().__init__(email)
        self.name = name
        self.number_rows = number_rows
    
    def run(self):
        print('run really fast')

class HibridBorg(Wizard,Archer):
    def __init__(self,name,power,email,number_rows):
        Archer.__init__(self,name,number_rows,email)

hb1 = HibridBorg('borgui',50,'borg@email',50)
print(hb1)
print(HibridBorg.__mro__)

wizerd1 = Wizard('Ju',100, 'ju@email')
#introspection
#print(dir(wizerd1))