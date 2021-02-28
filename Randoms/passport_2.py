class passport:
    def __init__(self,firstname,lastname,dob,gender,height,weight,nationality,language,allergies,age,count):
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
        self.gender = gender
        self.height = height
        self.weight = weight
        self.nationality = nationality
        self.language = language
        self.allergies = allergies
        self.age = age
        self.count = count


    def port(self):      
        name = self.firstname + " " + self.lastname
        g = len(name)
        h = len(self.dob)
        i = len(self.height)
        j = len(self.nationality)
        k = len(self.language)
        l = len(self.allergies)
        m = len(self.age)
        if h > g:
            g = h
        elif i > g:
            g = i
        elif j > g:
            g = j
        elif k > g:
            g = k
        elif l > g:
            g = l
        elif m > g:
            g = m
        else:
            pass
        print("/",end = "")
        for z in range(g):
            print("-",end = "")
        print("\ ")
        name = name.center(g, " ")
        name = "|" + name + "|"
        print(name)
        self.dob = self.dob.center(g," ")
        print("|",end = "")
        print(self.dob,end = "")
        print("|")
        self.gender = self.gender.center(g," ")
        print("|",end = "")
        print(self.gender,end = "")
        print("|")
        self.height = self.height.center(g," ")
        print("|",end = "")
        print(self.height,end = "")
        print("|")
        self.weight = self.weight.center(g," ")
        print("|",end = "")
        print(self.weight,end = "")
        print("|")
        self.nationality = self.nationality.center(g," ")
        print("|",end = "")
        print(self.nationality,end = "")
        print("|")
        self.language = self.language.center(g," ")
        print("|",end = "")
        print(self.language,end = "")
        print("|")
        self.allergies = self.allergies.center(g," ")
        print("|",end = "")
        print(self.allergies,end = "")
        print("|")
        self.age = self.age.center(g," ")
        print("|",end = "")
        print(self.age,end = "")
        print("|")
        ff = "\ "[0]
        print(ff,end = "")
        for z in range(g):
            print("-",end = "")
        print("/ ")

a = passport("Suhas","Addepalli","15/15/15","male","160","52","Indian","Telugu","none","12",0)
a.port()
