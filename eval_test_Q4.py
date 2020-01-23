class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def display_dog(self):
        print(self.name," is ", self.age)
        
    
class pet:
    
    def __init__(self,dog):
        self.dog=dog
    
    def display_pet(self,dog_instance):
        print("i have ",len(dog_instance), " kids")
        for i in dog_instance:
            i.display_dog()
               
         
        
obj_first=dog("tom",6)
obj_second=dog("fletcher",7)
obj_third=dog("larry",9)

pet_obj=pet(dog)


dog_instance=[obj_first,obj_second,obj_third]

pet_obj.display_pet(dog_instance)

#for i in dog_instance:
 #   i.display_dog()

