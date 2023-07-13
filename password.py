import random

class Password:
    def __init__(self, chars, length):
        self.chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
        self.length = length
    
    def length_input(self):
        Linput = input("How long do you want your Password?")
        length = int(Linput)
        return length
    
    def password_output(self):
        p = ""
        for x in range(length):
            new = random.choice(self.chars)
            p += new
        return p
    
my_password = Password("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()", 0)
length = my_password.length_input()
print(length)
passwordo = my_password.password_output()
print("Your password is:", passwordo)