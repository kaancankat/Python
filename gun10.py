#atilName ="atil"
#atilAge = 90
#atilGender ="male"
#atlasage = 10

#class Person():
#    name = ""
#    age=""
#    
#    def __init__(self,nameInput,ageInput,genderInput):
#        self.name=nameInput
#        self.age=ageInput
#        print("çalıştı")
#myList=list()
#
#atil =Person()
#
#class dog():
#    year = 7
#    def __init__(self,age):
#        self.age = age
##    def humanAge(self):
##        return self.age *self.year
##mydog = dog(3)
##print(mydog.age)
##print(mydog.humanAge())
#
#class musican():
#    
#    def __init__(self,name):
#        self.name = name
#        print("musican class")
#        
#    def test1(self):
#        print("test1")
#    def test2(self):
#        print("test2")
#
#class musicianPlus(musican):
#    def __init__(self,name):
#        musican.__init__(self,name)
#        print("musician plus")
#atlas = musicianPlus("atlas")
#atlas.name = "atlas samancıoğlu"
#
#class banana():
#    def __init__(self,name):
#        self.name = name
#    
#    def info(self):
#        return f"100 calories {self.name}"
#class apple():
#    def __init__(self,name):
#        self.name = name
#    
#    def info(self):
#        return f"150 calories {self.name}"
#    
#banana = banana("banana")
#apple = apple("apple")
#print(banana.info())
#
#fruitlist = [banana,apple]
#for fruit in fruitlist:
##    print(fruit.info())
#
#class phone():
#    def __init__(self,name,price) -> None:
#        self.name = name
#        self.__price = price
#    def info(self):
#        print(f"{self.name} price is {self.__price}")
#    def changePrice(self,price):
#        self.__price = price
#
#iphone = phone("iphone 14" ,500)
#iphone.info()
#
#iphone.__price= 400
#iphone.info()
#iphone.changePrice(400)
#iphone.info()

#from abc import ABC, abstractmethod
#class Car(ABC):
#    @abstractmethod 
#    def maxSpeed(self):
#        pass
#
#class tesla(Car):
#    def maxSpeed(self):
#        print("200km")
#        
#class Mercedes(Car):
#    
#    def maxSpeed(self):
#        print("250km")
#        
#mercedes = Mercedes()
#mercedes.maxSpeed()

class fruit():
    def __init__(self,name,calories):
        self.name = name
        self.calories =calories

    def __str__(self):
        return f"{self.name}: {self.calories} calories"
    
    def __len__(self):
        return self.calories
    
    
    
myFruit = fruit("banana",150)
myFruit.calories
myFruit.name
print(myFruit)

print(len(myFruit))