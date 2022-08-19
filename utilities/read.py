file = open("test.txt")
# print(file.readlines())

# for line in file.readlines():
#     print(line)
line = file.readline()
while line != "":
    print(line)
    line = file.readline()

file.close()
































# file = open("test.txt")
# # print(file.read(10))
# #
# # print(file.readline())
# # print(file.readline())
#
# # line = file.readline()
# # while line != "":
# #     print(line)
# #     line = file.readline()
#
# for line in file.readlines():
#     print(line)
#
# file.close()