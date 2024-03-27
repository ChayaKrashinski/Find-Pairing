from Person import Person
from Bride import Bride
from Groom import Groom


style_types = ["פתוח", "רגיל", "סגור"]
comminity_types = ["חסידי", "ליטאי", "ספרדי", "תימני"]

def remove_space(word):#הפונקציה מסירה רווח בין שתי מילים באותו שדה
    new_word = ""
    for t in word:
        if t==' ':
            new_word+='_'
        else:
            new_word+=t
    return new_word


def set_details():#הפונקציה קולטת מהמשתמש פרטים, ומכניסה אותם למערכת בתנאי שהם תקינים
    is_set = False
    while(is_set == False):#קליטת הנתונים כל עוד לא התקבלו נתונים תקינים.
        sort = remove_space(input("לבחור הקש 1, לבחורה הקש 2\n"))
        name = remove_space(input("שם פרטי"))
        family = remove_space(input("שם משפחה"))
        age = input("גיל")
        community = remove_space(input(f"קהילה: הקש מבין האפשרויות הבאות: {comminity_types}"))
        address = remove_space(input("כתובת"))
        father_name = remove_space(input("שם האב"))
        mother_name = remove_space(input("שם האם"))
        father_occupation = remove_space(input("עיסוק אב"))
        mother_occupation = remove_space(input("עיסוק אם"))
        prev_mother_family = remove_space(input("משפחת האם מהבית"))
        style=remove_space(input(f"סגנון: הקש מהרשימה להלן: {style_types}"))

        # פרטי בחור
        if(int(sort)==1):
            yeshiva = remove_space(input("ישיבה").strip())
            vaad = input("ועד")
            money=input("דרישות כספיות: הכנס את הסכום המינמאלי שתרצה")
            fileWrite = open("grooms.txt", "a",encoding="utf-8")
            try:#בדיקה שהנתונים מתאימים לתבנית
                someone = Groom(0,name, family, int(age), community, address, father_name, mother_name, father_occupation, mother_occupation, prev_mother_family,yeshiva, vaad, style, int(money))
                fileWrite.write(str(someone.get_code())+" "+name+" "+family+" "+age+" "+community+" "+address+" "+father_name+" "+mother_name+" "+
                            father_occupation+" "+mother_occupation+" "+prev_mother_family+" "+yeshiva+" "+vaad+" "+style+" "+money)
                fileWrite.close()
                is_set = True
            except:
                is_set = False


        #פרטי בחורה
        else:
            seminar = remove_space(input("סמינר").strip())
            specialty = remove_space(input("מסלול").strip())
            money=input("דרישות כספיות: הכנס את הסכום שינתן")
            fileWrite = open("brides.txt", "a",encoding="utf-8")
            try:#בדיקה שהנתונים מתאימים לתבנית
                someone = Bride(0,name, family, int(age), community, address, father_name, mother_name, father_occupation, mother_occupation, prev_mother_family,seminar, specialty, style, int(money))
                fileWrite.write(str(someone.get_code())+" "+name+" "+family+" "+age+" "+community+" "+address+" "+father_name+" "+mother_name+" "+
                            father_occupation+" "+mother_occupation+" "+prev_mother_family+" "+seminar+" "+specialty+" "+style+" "+money)
                fileWrite.close()
                is_set = True
            except:
                 is_set = False

    print(f"\nהקוד האישי שלך הוא:{someone.get_code()}\n")
