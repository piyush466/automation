from utilities.deom1 import piyush


class inher(piyush):
    num2 = 100

    def __init__(self):
        piyush.__init__(self, 1, 100)
        print("contructor")

    def before(self):
        return self.num2 + self.num + self.method2()

obj = inher()
print(obj.before())






































# from utilities.deom1 import piyush
#
#
# class child(piyush):
#     num2 =200
#
#     def __init__(self):
#         piyush.__init__(self, 2, 10)
#
#     def gertc(self):
#         print(self.num2, self.num, self.method2())
#         return self.num2 + self.num + self.method2()
#                     # 200 +  100   + 112
# obj = child()
# print(obj.gertc())
#
