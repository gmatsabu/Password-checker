import re



class Password(object):
    def __init__(self,password=''):
        self.password = password

    def lowercase(self):
        lowercase = any(c.islower() for c in self.password)
        return lowercase

    def uppercase(self):
        uppercase = any(c.isupper() for c in self.password)
        return uppercase

    def digit(self):
        digit = any(c.isdigit() for c in self.password)
        return digit

    def special(self):
        special_char = "$#@!$%*"
        special_char = any(c in special_char for c in self.password)
        return special_char

    def validate(self):
        lowercase = self.lowercase()
        uppercase = self.uppercase()
        digit = self.digit()
        special = self.special()

        length = len(self.password)
        

        report = lowercase and uppercase and digit and special and length >=8

        if report:
            print ("Password meet all requirements")
            return True

        elif not lowercase:
            print("Password must have at  least one lowercase character")
            return True

        elif not uppercase:
            print("Password must have at least one uppercase character")     
            return True

        elif not length:
            print("Length should be longer than 8")
            return True    

        elif not digit:
            print("Password must have at least one numeric character") 
            return True

        elif not special:
            print("Password must have at least one special character")        
        else:
            pass

c =  Password("tebohsA$2")
print(c.validate())              





