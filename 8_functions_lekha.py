# import statements are always at the top of code
#from fml import MyClass

'''
class stuff(MyClass):
    
    def cleanup(self, data):
        data = list(str(data)) #2342347823462834234
        return data
    
a = stuff("Jesus","Satan","God")
print(a.cleanup('bahaha'))


'''

class MyClass:

    def hello(self):
        print('hi')

class MyClass3:

    def hello(self):
        print("hello")


class MyClass2(MyClass3, MyClass):

    '''def hello(self):
        #"hello".split()
        print(list("hello"))'''
    pass



a = MyClass2()
a.hello()



# 3 files
# only those with valid credentials can use the calculator
# first file - class - calculator - 9 basic operations, needs to be usable till the user no longer wants to - keyword
# second file - 2 classes - one is for signup and stores in json file second class is for login, login gives access to calculator
# third file - json file to store all of this



