class piyush:
    num = 100

    def __init__(self,a, b):
        self.one = a
        self.two  =b
        print("i m automatcalty called when object is created ")

    def method(self):
        print("i m method")

    def method2(self):
        return self.one + self.two + piyush.num

obj = piyush(10, 10)
obj.method()
print(obj.method2())


