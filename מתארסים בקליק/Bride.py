from Person import Person


class Bride(Person):
    def __init__(self,code, name, family, age, community, address, father_name, mother_name, father_occupation, mother_occupation, prev_mother_family,seminar, specialty,style,money):
        Person.__init__(self, code,name, family, age, community, address, father_name, mother_name, father_occupation, mother_occupation, prev_mother_family,style,money)
        self.seminar = seminar
        self.specialty = specialty

    def get_bride(self):
        dic = self.get_person()
        dic.update([("סמינר",self.seminar) ,("מסלול",self.specialty)])
        return dic

    def get_bride_to_set(self):
        p = self.get_person_to_set()
        p.append(self.seminar)
        p.append(self.specialty)
        return p
