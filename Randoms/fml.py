
# 2 classes
# ill make the first one
# MyClass
# Use my class from a separate file called ^ 
# Override cleanup function which takes in 1 parameter and returns as a list

class MyClass:

    def __init__(self, param1, param2, param3, *args, **kwargs):
        self.winner = param1
        self.second = param2
        self.loser = param3
    
    def cleanup(self, data):
        return data + "/../../"
   
    def screen(self):
        print(f'Go to paris my friend, its been a long day! {self.winner}')

a = MyClass("Jesus","Satan","God")
a.screen()