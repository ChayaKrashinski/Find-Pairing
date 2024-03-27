from Person import Person
from Bride import Bride
from Groom import Groom
import os
from PIL import Image


def find_groom(code):#מציאת בחור לפי קוד
    fileRead = open("grooms.txt", "r",encoding="utf-8")
    for line_str in fileRead.readlines():
        line_cut = line_str
        line = line_cut.split()
        if(int(line[0])==code):
            return Groom(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8],line[9],line[10], line[11], line[12], line[13], line[14])

    print("הקוד שהוקש שגוי, נסה שנית")
    fileRead.close()
    return None

def find_bride(code):#מציאת בחורה לפי קוד
    fileRead = open("brides.txt", "r",encoding="utf-8")
    for line_str in fileRead.readlines():
        line_cut = line_str
        line = line_cut.split()
        bride = Bride(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8],line[9],line[10], line[11], line[12], line[13], line[14])
        if(int(line[0])==code):
            return bride
    print("הקוד שהוקש שגוי, נסה שנית")
    fileRead.close()
    return None

def print_person(p):#הדפסה מסודרת של בחור/ בחורה
    for k, v in p.items():
        print(f"{k}: {v}")

def fit_pair(groom, bride):#בדיקת התאמה לזוג
        fit = 0
        #שמות ההורים אינם זהים
        if groom.father_name == bride.father_name or groom.mother_name == bride.mother_name:
            return 0
        #גיל מתאים
        diff_age = int(groom.age) - int(bride.age)
        if diff_age >= 0 and diff_age <= 8:
            if diff_age <= 2:
                fit += 25
            elif diff_age <= 5:
                fit += 12.5
        else:
            return 0
        if groom.community == bride.community:
            fit += 25
        else:
            return 0
        #סגנון מתאים
        if groom.style == bride.style:
            fit += 25
        elif (groom.style == "סגור" or groom.style == "פתוח") and bride.style == "רגיל":
            fit += 12.5
        elif groom.style == "רגיל" and (bride.style == "סגור" or bride.style == "פתוח"):
            fit += 12.5
        else:
            return 0
        #דרישות כספיות תואמות
        if int(groom.money) - int(bride.money) > 0:
             return 0
        else:
            fit += 25
        print("\nנמצאה התאמה!!!\n**********************")
        return fit


def fit_bride(groom):#התאמת בחורה לפי הבחור שנשלח
    fileRead = open("brides.txt", "r",encoding="utf-8")
    flag = False
    for line_str in fileRead.readlines():
        line_cut = line_str
        line = line_cut.split()
        bride = Bride(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8],line[9],line[10], line[11], line[12], line[13], line[14])
        fit = fit_pair(groom, bride)
        if fit >0:
            print(f"\nאחוזי התאמה: {fit}% 🧥👠")
            print_person(bride.get_bride())
            print("תמונת המועמד תוצג כעת")
            try:
                input("להצגת תמונת המועמד.ת הקש על מקש כלשהוא")
                img = Image.open(f"./images/brides/{bride.code}.jpg")
                img.show()
            except:
                print("לא קיימת תמונה במאגר")
            print("\nאם אכן השידוך יצא אל הפועל בסיעתא דשמייא, חובה לעדכן את המאגר")
            print("-------------------------------------------------------------------")
            flag = True
            input("להמשך, יש להקיש על מקש כלשהוא")
    if flag == False:
        print("\nמצטערים,לא נמצאו מועמדות מתאימות😭 התפללו חזק!!!!\n")
    else:
        print("\nאין הצעות נוספות במאגר.\nואולי עוד ניפגש עוד 20 שנה בשידוך של ילדכם...")
    fileRead.close()
    input("לחזרה לתפריט הראשי, יש להקיש על מקש כלשהוא")

def fit_groom(bride):#התאמת בחור לפי בחורה שנשלחת
    fileRead = open("grooms.txt", "r",encoding="utf-8")
    flag = False
    for line_str in fileRead.readlines():
        line_cut = line_str
        line = line_cut.split()
        groom = Groom(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8],line[9],line[10], line[11], line[12], line[13], line[14])
        fit = fit_pair(groom, bride)
        if fit >0:
            print(f"\nאחוזי התאמה: {fit}% 🧥👠")
            print_person(groom.get_groom())
            print("תמונת המועמד תוצג כעת\n")
            try:
                input("להצגת תמונת המועמד.ת הקש על מקש כלשהוא")
                img = Image.open(f"./images/grooms/{groom.code}.jpg")
                img.show()
            except:
                print("לא קיימת תמונה במאגר")
            print("\nאם אכן השידוך יצא אל הפועל בסיעתא דשמייא, חובה לעדכן את המאגר")
            print("-------------------------------------------------------------------")
            flag = True
            input("להמשך, יש להקיש על מקש כלשהוא")
    if flag is False:
        print("\nמצטערים,לא נמצאו מועמדים מתאימים😭 התפללו חזק!!!!\n")
    else:
        print("\nאין הצעות נוספות במאגר.\nואולי עוד ניפגש עוד 20 שנה בשידוך של ילדכם...")
    fileRead.close()
    input("לחזרה לתפריט הראשי, יש להקיש על מקש כלשהוא")


def delete_groom(code):
     fileRead =open("grooms.txt",'r',encoding="utf-8")
     find = False
     newFile=""
     for line_str in fileRead:
             line = line_str.split()
             if(int(line[0])!=code):
                 newFile+=line_str
             else:
                 find = True
     fileRead.close()
     fileWrite=open("grooms.txt",'w',encoding="utf-8")
     fileWrite.write(newFile)
     fileWrite.close()
     return  find


def delete_bride(code):
     fileRead =open("brides.txt",'r',encoding="utf-8")
     newFile=""
     find = False
     for line_str in fileRead:
             line = line_str.split()
             if(int(line[0])!=code):
                 newFile+=line_str
             else:
                 find = True
     fileRead.close()
     fileWrite=open("brides.txt",'w',encoding="utf-8")
     fileWrite.write(newFile)
     fileWrite.close()
     return find




