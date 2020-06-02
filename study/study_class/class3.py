
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return "Fail"
        else:
            return self.first/self.second

class Family:
    lastname = "김"



a = FourCal()
b = FourCal()

a.setdata(4,2)
b.setdata(3,8)

a.add()
a.mul()
print(a.add())

