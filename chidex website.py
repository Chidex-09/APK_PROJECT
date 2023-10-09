class Student ():
    def __init__(self, name, Class, teacher):

        self.name = name 
        self.Class = Class
        self.teacher = teacher
         
    def get_name (self):
        return self.name
    
    def get_class (self):
        return self.Class
    
    def get_teacher (self):
        return self.teacher
    
    def __str__(self):
        return f"{self.name} is a stdent,{self.name} is in {self.Class}{self.name} bes teacher is {self.teacher}."
    
chidex=student("chidex","ss3","tracher_okem.")
print(chidex)
    
    