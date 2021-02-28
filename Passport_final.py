class passport:
    def __init__(self,firstname,lastname,dob,gender,height,weight,nationality,language,allergies,age):
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
    


    def port(self):
        name = self.firstname + " " + self.lastname 
        a = len(name)
        b = len(self.dob)
        c = len(self.gender)
        d = len(self.height)
        e = len(self.weight)
        f = len(self.nationality)
        g = len(self.language)
        h = len(self.allergies)
        i = len(self.age)
        if b > a:
            a = b
        if c > a:
            a = c
        if d > a:
            a = d
        if e > a:
             a = e
        if f > a:
            a = e
        if g > a:
            a = g
        if h > a:
            a = h
        if i > a:
            a = i

        print("/",end = "")
        for x in range(a):
            print("-",end = "")
        print("\ ")
        
        name = name.center(a, " ")
        self.dob = self.dob.center(b, " ")
        self.gender = self.gender.center(c, " ")
        self.height = self.height.center(d, " ")
        self.weight = self.weight.center(e, " ")
        self.nationality = self.nationality.center(f, " ")
        self.language = self.language.center(g, " ")
        self.allergies = self.allergies.center(h, " ")
        self.age = self.age.center(i, " ")

        print(name)
        print(self.dob)
        print(self.gender)
        print(self.height)
        print(self.weight)
        print(self.nationality)
        print(self.language)
        print(self.allergies)
        print(self.age)

a = passport("vish","nalabotu","2003-12-14", "male","12cm","200tonnes","chinese","gibberish","nuts","18")
a.port()
        
