# vartest_error.py

a = 1
def vartest(a):
    a = a + 1
    return a

a = vartest(3)
print(a)

