import os
#from PIL import Image
from Person import Person
from Bride import Bride
from Groom import Groom
import Find_Functions as ff
import Register_Functions as rf


try:
    while(True):
        print("\nברוכים הבאים לאתר מתארסים בקליק>>\n השתדלות להקליק, ומתארסים בקליק!")
        choise = input("להרשמה ✍🏼:הקש 1\nלחיפוש זווג 🔎: הקש 2\nהתארסת 🧐? הקש 3\n")

        #תקינות קלט
        e = 0
        try:
            x = int(choise)
        except Exception:
            e = 1
            print("הקשה שגויה, יש לנסות שוב")
        if e == 1:
            continue

        #הרשמה
        elif(int(choise) == 1):
            rf.set_details()
            print("פרטיך נכנסו בהצלחה למאגר. מעכשו תוכל להיכנס בכל עת לשלוחת החיפוש\n ולאתר עבורך את הזיווג מהשמיים. ברכותינו\nלכניסה לחיפוש, הקש את הקוד האישי שלך")
            print("\nלתשומת ליבך! לשליחת תמונת המועמד.ת יש ליצור עמנו קשר באימייל: mitarsim.beclic@gmail.com")


        # חיפושים
        elif(int(choise) == 2):
            sort = int(input("בחור? הקש 1\nבחורה? הקישי 2\n"))
            code = int(input("הקש את הקוד האישי שלך\n"))

            #התאמה לבחור
            if sort == 1:
                groom = ff.find_groom(code)#מציאת הבחור לפי הקוד
                while groom == None:
                    code = int(input("הקש את הקוד האישי שלך\n"))
                    groom = ff.find_groom(code)
                print(f"שלום {groom.name}🕴🏼")
                print(
                "לתשומת ליבך! הסינון הראשוני מתבצע לפי הפרמטרים הבאים: גיל, קהילה, סגנון, דרישות כספיות.\nהמערכת מעבדת נתונים 💻")
                ff.fit_bride(groom)#התאמת בחורה

            #התאמה לבחורה
            elif sort == 2:
                bride = ff.find_bride(code)#מציאת בחורה לפי הקוד
                while bride == None:
                    code = int(input("הקש את הקוד האישי שלך\n"))
                    bride = ff.find_bride(code)
                print(f"שלום {bride.name}👰")
                print("לתשומת ליבך! הסינון הראשוני מתבצע לפי הפרמטרים הבאים: גיל, קהילה, סגנון, דרישות כספיות.\nהמערכת מעבדת נתונים 💻")
                ff.fit_groom(bride)#התאמת בחור


        # מאורסים
        elif(int(choise)==3):
            type=int(input("בחור? הקש 1\nבחורה? הקישי 2\n"))
            dell = False
            while dell == False:
                code=int(input('הכנס את הקוד האישי שלך'))
                if(type==1):
                    dell = ff.delete_groom(code)
                elif(type==2):
                    dell = ff.delete_bride(code)
                else:
                    print("הקשה שגויה. יש לנסות שוב")
                    break
                if dell==False:
                    print("הקוד שהוקש אינו קיים במאגר, נסה שוב")
            if dell == True:
                print("פרטיך הוסרו מהמאגר בהצלחה. מזל טוב!!! 😂")

        else:
            print("הקשה שגויה, יש לנסות שוב")


except Exception as e:
    print(f"the error is: {e}")

