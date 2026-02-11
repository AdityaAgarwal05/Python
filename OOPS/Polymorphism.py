#pollymorphism is a way in which different object classes can share the same name

class Dog():
    def __init__(self,name):
        self.name=name

    def speak(self):
        return self.name + ' says WOOF!!'


class Cat():
    def __init__(self,name):
        self.name=name

    def speak(self):
        return self.name + ' says Meow!!'
        

adi = Dog('adi')
joshi = Cat('joshi')     

print(adi.speak())                #o/p:- adi says WOOF!!
print(joshi.speak())              #o/p:- joshi says Meow!!

for pat in [adi,joshi]:
    print(type(pat))
    print(type(pat.speak()))
'''  o/p:-
 <class '__main__.Dog'>
<class 'str'>
<class '__main__.Cat'>
<class 'str'>
'''    




def pet_speak(pet):
    print(pet.speak())

pet_speak(adi)        # adi says WOOF!!
pet_speak(joshi)      # joshi says Meow!!
