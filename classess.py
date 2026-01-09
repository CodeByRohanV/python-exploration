# class laptop :
#     def __init__(self,version,price):
#         self.version = version
#         self.price  = price   
#     def display(self):
#         print(self.version,self.price)
# comp = laptop(2.0,20000)
# comp2 = laptop(3.0,30000)
# comp.display()
# comp2.display()


# class computer:
#     def __init__(self):
#         self.brand = "lenovo"
#         self.price = 20000
#     def update(self):
#         self.price = 50000
    
# comp = computer()
# comp.brand = "apple"
# comp2 = computer()

# comp.update()
# print(comp.brand,comp.price)


# print(comp.brand,comp2.brand)

class student:
    # def __init__(self,name, roll_no,):
    #     self.name = name
    #     self.roll_no = roll_no
        

    def __init__(self):
        self.hisName = input("enter your name: ")
        self.hisNum = int(input('roll number :'))
        self.data = []
        self.data.append(self.hisName)
   
# stud = student("Rohan",24)
# stud2 = student("naga",56)
# students = [stud,stud2]
# for i in students:
#     print(i.name , i.roll_no)
stud = student()
print(stud.data)
    
