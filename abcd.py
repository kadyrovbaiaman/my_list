import random
a=int(input('Томонку диапазон:'))
b=int(input('Жогорку диапазон:'))
san=0
number=random.randint(a,b)

while True: 

    guess=int(input(f'{a} жана {b} ортосундагы санды табыныз:'))
    san+=1

    if guess<number:
        print('Сиз жазган сан кичине')

    elif guess>number:
        print('Сиз жазган сан чон')

    else:
        print(f'Куттуктайбыз сиз {guess} санын {san} иретте таптыныз')
        break
        class Employee:
    def __init__(self,name,last_name ,age):
        self.name=name
        self.last_nam=last_name
        self.age=age
        
    def get_info(self):
        return self.name,self.last_nam,self.age,


class Maneger(Employee):

   def __init__(self, name, last_name, age,department,salery,):
       super().__init__(name, last_name, age)
       self.department=department
       self.salery=salery
       

   def check(self):
    if self.department=='IT':
        print('cool')
    else:
        print('not cool')   

   def show_info(self):
     return self.name,self.last_nam,self.age,self.department,self.salery
          
   
   
class Intern(Maneger):
    def __init__(self, name, last_name, age, department, salery,experience):
        super().__init__(name, last_name, age, department, salery,)
        self.experience=experience
    
    def data_info(self):
        return self.name,self.last_nam,self.age,self.department,self.salery,self.experience


employee1=Employee('Asan','Ysenov',25)
print(employee1.get_info())

maneger1=Maneger('Sultan','Kutmanov',20,'IT',30000,)
print(maneger1.show_info())

intern1=Intern('Aman','Kadyrov',27,'Marketing',30000,5)
print(intern1.data_info())
