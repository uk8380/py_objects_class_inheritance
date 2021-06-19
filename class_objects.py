class my_class:#class
    x=5

p1=my_class#object
print(p1.x)
#__init__
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=person("uday",99)
print(p1.name)
print(p1.age)



#for better understand
class hit:
    def __init__(h,f,e):
        h.f=f
        h.e=e
p2=hit("love",00)
print(p2.f)
print(p2.e)

#self parameter
class love:
    def __init__(po,naam,haal):
        po.naam=naam
        po.haal=haal
    def my_fun(abc):
        print("hello love",abc.naam)
p3=love("uday",98)
p3.my_fun()
p3.naam="ajat"#acessing object
print(p3.naam,p3.haal)
#inheritance
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):#parent
    print(self.firstname, self.lastname)

class Student(Person):#child
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)#super function is used for parent to child inheritance
    self.graduationyear = year

  def welcome(self):#sub_child
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()

