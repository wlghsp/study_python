

class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()



# try:
#     4 / 0
# except ZeroDivisionError as e:
#     print(e)

