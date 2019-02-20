class Employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal

    def display(self):
        print("Employee Number : ",self.eno)
        print("Employee Name : ",self.ename)
        print("Employee Salary : ",self.esal)

    class Test:
        def modify(emp):
            emp.esal= Employee.esal+10000
            emp.display()


#e=Employee(101,'dddd',70000)
#Test.modify(e)
i=Employee(101,'dddd',70000).display()


          

