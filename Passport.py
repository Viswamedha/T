class passport:
    def __init__(self, firstname, lastname, DOB, gender, height, weight, nationality, language, age, family):
        self.firstname = firstname
        self.lastname = lastname
        self.DOB = DOB
        self.gender = gender
        self.height = height
        self.weight = weight
        self.nationality = nationality
        self.language = language
        self.age = age
        self.family = family
    def port(self):
        print("----------------------------------------------------------------")
        print(self.firstname+" "+self.lastname)
        print("                             "+self.DOB)
        print("Height(cm) = "+self.height+ "    "+ "weight(kg) ="+ self.weight)
        print("Gender ="+ self.gender+"         "+"nationality ="+ self.nationality)
        print("language ="+ self.language+"      "+"age="+self.age)
        print("                        "+"family members="+ self.family)

class passport:
    def __init__(self, firstname,lastname,dob,gender,height,weight,nationality,language,allergies,age):
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
        self.gender = gender
        self.height = height
        self.weight = weight
        
        self.nationality = nationality
        self.language = language
        self.age = age
        self.allergies = allergies

    def port(self):
        a = 0
        print("/-------------------------------")
        print("  " + self.firstname + "  " + self.lastname)
        print("           " + self.dob + "      ")
        print("              "  + self.gender + "    ")
        print("   " + self.height + "cm   " + self.weight + "kg")
        print("   " + self.nationality + "  " + self.language)
        print("         " + self.allergies + "        ")
        print("               " + self.age + "       ")
        print("\-------------------------------/")
message= "Suhas lost! "
print(message, end="")
print(message)
# 
# S R
# 3 7
# 6 2
# 8 10
# 17 19
