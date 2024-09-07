# class stock:
#     ...
#
# class bond:
#     ...
#
#
# class Security:
#     ...
#
# class RealEstate:
#     ...
# class ChekingAccount:
#     ...
#
#
# class SavingAccount:
#     ...
#
#
# class BankAccount(SavingAccount,ChekingAccount):
#     ...
#
#
#
# class InterestBeringtem(BankAccount):
#     ...
#
# class Asset(BankAccount,Security,RealEstate):
#     ...
#
# class insurabletem(BankAccount):
#     ...
#
#
# Нaледование и полиморф
# абстракция,множественное наследование
# Супер\родительский



class A:
    def __init__(self, a):
        self.a = a

    name = 'A'



# дочерний
class B:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    name = 'B'
    def bisplay(self):
        print('это метод класса B')

class D:
    def __init__(self,d):
        self.d=d
    def bisplay(self):
        print('метод D')
class C(B,D):
    def __init__(self,a,b,d):
        B.__init__(self,a,b)
        D.__init__(self,d)

    name = 'C'
    def bisplay(self):
        D.bisplay(self)


b = C('n','1','1')
print(b.name)
b.bisplay()

print(C.mro())
# MRO - порядок выполнения методов


# git clone
