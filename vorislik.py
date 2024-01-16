# #Vorislik va Polimorfizm

# class Dukon:
#     def __init__(self, nomi,manzili,turi,telefoni):
#         self.nomi=nomi
#         self.manzili=manzili
#         self.turi=turi
#         self.telefoni=telefoni
#         self.tovarlar=[]
         
#     def get_info (self):
#         return f"{self.nomi}\n {self.manzili}\n {self.telefoni}"
        
#     def add_tovar (self, new):
#         self.tovarlar.append(new)
        
#     def get_tovarlar(self):
#         return self.tovarlar
    
#     def __repr__(self):
#         return self.nomi
    
    
# class gul_dukon(Dukon):
#     def __init__(self, nomi, manzili, turi, telefoni,gullar_soni ):
#         super().__init__(nomi, manzili, turi, telefoni)
#         self.gullar_soni = gullar_soni
        
#     def get_info(self):
#         full=super().get_info()
#         full+=self.gullar_soni
#         return full
        


###//////////////////////////////////////////////////////////////////////////////////////////////////
###//////////////////////////////////////////////////////////////////////////////////////////////////

    
class Shaxs:
    def __init__(self, ism, familiya, ish_joyi):
        self.ism = ism
        self.familiya = familiya
        self.ish_joyi = ish_joyi

    def get_info(self):
        return f"{self.ism}   {self.familiya}   {self.ish_joyi}"


class Foydalanuvchi(Shaxs):
    def __init__(self, ism, familiya, ish_joyi, login, parol):
        super().__init__(ism, familiya, ish_joyi)
        self.login = login
        self.parol = parol

    def get_info(self):
        return f"{super().get_info()}   Login: {self.login}    Parol: {self.parol}"


class Admin(Foydalanuvchi):
    def __init__(self, ism, familiya, ish_joyi, login, parol):
        super().__init__(ism, familiya, ish_joyi, login, parol)

    def ban_user(self, foydalanuvchi):
        print(f"{foydalanuvchi.ism} {foydalanuvchi.familiya} bloklandi")


shaxs1 = Shaxs("Mansurbek", "Qazaqov", "Office")

foydalanuvchi1 = Foydalanuvchi("Asqar", "Sobirov", "firma", "asqar123", "123456")

admin1 = Admin("Admin", "Superuser", "Admin Office", "admin", "admin123")

print(shaxs1.get_info())

print(foydalanuvchi1.get_info())

print(admin1.get_info())


    
    
    
        