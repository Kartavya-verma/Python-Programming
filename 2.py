class String:
    def get_string(self):
        string=input("Enter the string\n")
        return string
    def print_string(self,strr):
        print(strr.upper())

obj=String()
strr=obj.get_string()
obj.print_string(strr)
