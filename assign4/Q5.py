class Workdatabase:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def func(self):
        print(f'Name: {self.name}, salary: {self.salary}')

p1 = Workdatabase('mehak',40000)
p2 = Workdatabase('ashok',50000)
p3 = Workdatabase('viren', 60000)

p1.func()
p2.func()
p3.func()

p1.salary = 70000 # modifying salary
print('part (a)')
p1.func()
p2.func()
p3.func()
del p3 #deleating data
print('part (b)')
p1.func()
p2.func()


