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
        print("/--------------------------------\ ")      
        name = self.firstname + " " + self.lastname
        length = len(name)
        for i in range(length):
            self.count = self.count + 1
        self.count = 34 - self.count
        self.count = self.count / 2
        for j in range(int(self.count)):
            print(" ", end = "")
        g = True
        while g: # FIX Here
            if len(name) > 10:
                print(name[:33])
                name = name[33:]
            elif len(name) == 0:
                break
            else: 
                print(name,end = "")
        for j in range(int(self.count)):
            print(" ", end = "")
        print("\n")
        print("            " + self.dob + "            ")
        if self.gender == "female":
            print("             female             ")
        else:
            print("              male              ")
        print("        " + self.height + "cm        " + self.weight + "kg        ")
        print("             " + self.nationality + "             ")
        print("             " + self.language + "             ")
        print("              " + self.allergies + "              ")
        print("               " + self.age + "               ")
        print("\--------------------------------/ ")

#a = passport("Senuka","Te","15/15/15","male","160","52","Indian","Telugu","none","12",0)
#a.port()


name = "Senuka Thenujaya Nawarathna Rathnayaka Mudiyanselage"
g = len(name)
age = 23234234234234234
if len(str(age)) > g:
    g = len(str(age)) 
# .ljust()
# .rjust()
h = "/"
for i in name:
    h = h + "-"

h += "\ "
print(h)
print(" "+name)



