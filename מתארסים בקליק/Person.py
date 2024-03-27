do_code = lambda x: x*x
def create_code():
    for i in range(30,1000000000):
        yield do_code(i)

class Person:
    """basic details of all person"""

    def __init__(self,code, name, family, age, community, address, father_name, mother_name, father_occupation, mother_occupation, prev_mother_family,style,money):
        if code == 0:
            get_code = create_code()
            code = next(get_code)
        self.code = code
        self.name = name
        self.family = family
        self.age = age
        self.community = community
        self.address = address
        self.father_name = father_name
        self.mother_name = mother_name
        self.father_occupation = father_occupation
        self.mother_occupation = mother_occupation
        self.prev_mother_family = prev_mother_family
        self.style=style
        self.money=money


    def get_code(self):
        return self.code


    def get_person(self):
        """return dictionary with person details"""
        return {"קוד": self.code, "שם": self.name, "משפחה": self.family, "גיל": self.age, "קהילה": self.community,
                "כתובת": self.address, "שם אב": self.father_name, "שם אם": self.mother_name,
                "עיסוק אב": self.father_occupation, "עיסוק אם":self.mother_occupation,
                "אמא לבית": self.prev_mother_family,"סגנון":self.style,"דרישות כספיות":self.money}


    def get_person_to_set(self):
        return [self.code, self.name, self.family, self.age, self.community,self.address,  self.father_name, self.mother_name, self.father_occupation, self.mother_occupation,self.prev_mother_family,self.style,self.money]
