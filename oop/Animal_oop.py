class Animal:
    zoo_name = 'sofeh_zoo'
    def __init__(self, name, soecies, age, sound):
        self.name = name
        self.age = age
        self.soecies = soecies
        self.sound = sound

    def make_sound(self):
        return (f"the sound of this animal is ({self.sound})")

    def __str__(self): 
        return (f"the name is {self.name},is {self.soecies} and {self.age} and the sound is {self.sound}")
    
lion = Animal('lion','cat',12,'aaaaaaaaaaa')
print(lion.age)
print(lion)
print(lion.make_sound())       
print(lion.name)
print(lion.soecies)


class Bird(Animal):
    def __init__(self, wing_span,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wing_span = wing_span

    def make_sound(self):
        return f"the sound of {self.name} is {self.sound}"
          
toti = Bird( 10, 'toti', 'Bird', 11, 'gikgik')
print(toti.make_sound())
print(toti.zoo_name)
print(toti.wing_span)
print(toti.sound)
print(toti)