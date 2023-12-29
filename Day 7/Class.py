class Check:
    def __init__(self, n):
        self.n = n

    def check_number(self):
        if self.n % 2 == 0:
            return "even"
        return "odd"

n = int(input("Enter any number: "))
num = Check(n)
print(num.check_number())
