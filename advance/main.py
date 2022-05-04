# class link:
    
    
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     def __add__(self , list):
#         return link(self.x + list.x, self.y + list.y)
    
#     def __repr__(self):
#         return f"X ning qiymati {self.x} va Y ning qiymati {self.y}:" 
           
           
# li1 = link(20, 30)
# li2 = link(40, 20)           
# li3 = link(10, 10) 
# li4 = link(40, 20)
# li5 = link(70, 60) 

# print(li1 + li2 + li3 + li4 + li5)         

# # murakkab funksiyalar
def decorative_function(func):
    def ichki(text):
        return [func(value[0], value[1],) for value in text] 
    return ichki
# Ikkinchisi
@decorative_function 
def number(a, b):
    print(a + b)  

print(number([(10, 20), (40, 50), (25, 55)]))           
# Ikkinchisi
def decorative_function(func):
    def ichki(link):
        return [func(value[0], value[1],) for value in link] 
    return ichki

@decorative_function 
def raqam(a, b):
    print(a - b)  

print(raqam([(50, 20), (50, 50), (25, 10)])) 

# Uchunchisi
def decorative_function(func):
    def ichki(list):
        return [func(value[0], value[1],) for value in list] 
    return ichki

@decorative_function 
def raqamlar(a, b):
    print(a * b)  

print(raqam([(50, 20), (50, 50), (25, 10)]))

# Tortinchisi
def decorative_function(func):
    def ichki(link):
        return [func(value[0], value[1],) for value in link] 
    return ichki

@decorative_function 
def raqam(a, b):
    print(a / b)  

print(raqam([(50, 20), (50, 50), (25, 10)]))   