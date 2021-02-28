#import json
# storage of dictionary data in a file

import json

a = open("data.json")
# json files - read -> load

b = json.load(a)
a.close()
print(b)

b[0] = "eats icecream! "
b["Hello"] = "No"
a = open("data.json", "w")
json.dump(b, a, indent=4)
a.truncate()
a.close()


# instead of while loop, ur gonna need to save it inside the class using a save() function
# self.details

class myclass:
    def __init__(self):
        self.something = ""
        self.a = "a"