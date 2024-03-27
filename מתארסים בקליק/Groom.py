from Person import Person


class Groom(Person):
    def __init__(self,code, name, family, age, community, address, father_name, mother_name, father_occupation, mother_occupation, prev_mother_family,yeshiva, vaad,style,money):
        Person.__init__(self,code,  name, family, age, community, address, father_name, mother_name, father_occupation, mother_occupation, prev_mother_family,style,money)
        self.yeshiva = yeshiva
        self.vaad = vaad


    def get_groom(self):
        dic = self.get_person()
        dic.update([("ישיבה",self.yeshiva) ,("ועד",self.vaad)])
        return dic

    def get_groom_to_set(self):
        p = self.get_person_to_set()
        p.append(self.yeshiva)
        p.append(self.vaad)
        return p
