class Detail:
    def info(self,name,age,tel):
        self.name=name
        self.age=age
        self.tel=tel
    def dail(self):
        print("name -->", self.name ,"\nage -->" ,self.age, "\ntel-->", self.tel)
p=input("enter name :")
q=input("enter age:")
r=input("enter telephone no:")
a=Detail()
a.info(p,q,r)
a.dail()
weight=float(input("enter weight:"))
height=float(input("enter height"))
bmi=weight/pow(height,2)
if bmi<18.5:
    print("Underweight") 
elif bmi>=18.5 and bmi<25:
    print("Normal")
elif bmi>=25 and bmi<30:
    print("Overweight")        
else:
    print("Obesity")


