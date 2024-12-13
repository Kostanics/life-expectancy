from ast import If


print(" "*20,"LIFE EXPECTANCY")
print(" "*19,"CREATIVE COMPUTING")
print(" "*17,"MORRISTOWN, NEW JERSEY")
print('\n\n\n\n\n')
print("THIS IS A LIFE EXPECTANCY TEST.")
print("   DO YOU WISH INSTRUCTIONS?", end=' ')
i = input()
if not(i[0] == "N"):
    print('\n')
    print("   THIS IS A TEST TO PREDICT YOUR LIFE EXPECTANCY.  I")
    print("WILL ASK YOU A SERIES OF SHORT QUESTIONS, WHICH YOU WILL")
    print("REPLY BY TYPING IN THE CORRESPONDING ANSWER TO THE")
    print("QUESTION.")
    print()
    print("        EXAMPLE:  WHAT IS YOUR SEX?")
    print("               M=MALE")
    print("               F=FEMALE")
    print("'M' AND 'F' ARE THE POSSIBLE REPLIES TO THE QUESTION, ANSWER")
    print("LIKE THIS:")
    print("              CHOOSE ONE OF THE LETTERS ABOVE? M")
    print("TYPING AN 'M' SIGNIFIES YOU ARE A MALE.")
    print('\n\n')
Z=72
a="ABCDEMGHIJKLFNO"
DATAS = [["+++SEX+++", "ARE YOU MALE OR FEMALE?", "M= MALE.", " F= FEMALE.", "MF"], 
         ["+++LIFE STYLE+++", "WHERE DO YOU LIVE?", "G= IF YOU LIVE IN AN URBAN AREA WITH A POPULATION OVER 2 MIL.", "K= IF YOU LIVE IN A TOWN UNDER 10,000, OR ON A FARM.", " I= NEITHER.", "GKI"], 
         ["HOW DO YOU WORK?", "M= IF YOU WORK BEHIND A DESK.", "L= IF YOUR WORK REQUIRES HEAVY PHYSICAL LABOR.", " I= NONE OF THE ABOVE.", "MLI"], 
         ["HOW LONG DO YOU EXERCISE STRENUOUSLY,", "(TENNIS, RUNNING, SWIMMING, ETC.)?", "F= FIVE TIMES A WEEK FOR AR LEAST A HALF HOUR.", "K= JUST TWO OR THREE TIMES A WEEK.", " I= DO NOT EXERCISE IN THIS FASHION.", "FKI"], 
         ["WHO DO YOU LIVE WITH?", "N= IF YOU LIVE WITH A SPOUSE, FRIEND, OR IN A FAMILY.", "H= IF YOU'VE LIVED ALONE FOR 1-10 YEARS SINCE AGE 25.", "G= FOR 11-20 YEARS.", "M= FOR 21-30 YEARS.", "E= FOR 31-40 YEARS.", " D= MORE THAN 40 YEARS.", "NHGMED"], 
         ["+++PSYCHE+++", "DO YOU SLEEP MORE THAN 10 HOURS A NIGHT?", "I= NO.", " E=YES.", "IE"], 
         ["+++MENTAL STATE+++", "M= IF YOU ARE INTENSE, AGGRESSIVE, OR EASILY ANGERED.", "L= IF YOU ARE EASY GOING, RELAXED, OR A FOLLOWER.", " I= NEITHER.", "MLI"], 
         ["+++HOW YOU FEEL+++", "ARE YOU HAPPY OR UNHAPPY?", "J= HAPPY.", "G= UNHAPPY.", " I= NEITHER.", "JGI"], 
         ["+++FACTORS+++", "HAVE YOU HAD A SPEEDING TICKET IN THE LAST YEAR?", "H= YES.", " I=NO.", "HI"], 
         ["+++INCOME+++", "DO YOU EARN MORE THAN $50,000 A YEAR?", "G= YES.", " I=NO.", "GI"], 
         ["+++SCHOOLING+++", "J= IF YOU HAVE FINISHED COLLEGE.", "L= IF YOU HAVE FINISHED COLLEGE WITH A GRADUATE", "OR PROFESSIONAL DEGREE.", " I= NOTHING LISTED.", "JLI"], 
         ["+++AGE+++", "ARE YOU 65 OR OLDER AND STILL WORKING?", "L= YES.", " I= NO.", "LI"], 
         ["+++HEREDITY+++", "K= IF ANY GRANDPARENTS LIVED TO 85 YEARS OLD.", "O= IF ALL FOUR GRANDPARENTS LIVED TO 80 YEARS OLD.", " I= NO GRANDPARENTS QUALIFY IN THE ABOVE.", "KOI"], 
         ["HAS ANY PARENT DIED OF A STROKE OR HEART ATTACK", "BEFORE THE AGE OF 50?", "E= YES.", " I= NO.", "EI"], 
         ["+++FAMILY DISEASES+++", "ANY PARENT, BROTHER, OR SISTER UNDER 50 HAS (OR HAD) ", "CANCER, A HEART CONDITION, OR DIABETES SINCE CHILDHOOD?", "M= YES.", " I= NO.", "MI"], 
         ["+++HEALTH+++", "HOW MUCH DO YOU SMOKE?", "A= IF YOU SMOKE MORE THAN TWO PACKS A DAY.", "C= ONE TO TWO PACKS A DAY.", "M= ONE HALF TO ONE PACK A DAY.", " I= DON'T SMOKE.", "ACMI"], 
         ["+++DRINK+++", "DO YOU DRINK THE EQUIVALENT OF A ", "QUARTER BOTTLE OF ALCOHOLIC BEVERAGE A DAY?", "H= YES.", " I= NO.", "HI"], 
         ["+++WEIGHT+++", "A= IF YOU ARE OVERWEIGHT BY 50 POUNDS OR MORE.", "E= OVER BY 30-50 POUNDS.", "G= OVER BY 10-30 POUNDS.", " I= NOT OVER WEIGHT.", "AEGI"], 
         ["+++CHECKUPS+++", "DO YOU?  IF YOU ARE A MALE OVER 40 HAVE AN ANNUAL CHECKUP?", "K= YES.", " I= IF NO OR NOT A MALE OR UNDER 40 YEARS OLD.", "KI"], 
         ["DO YOU? IF YOU ARE A WOMAN SEE A GYNECOLOGIST ONCE A YEAR?", "K= YES.", " I= IF NO OR NOT A WOMAN.", "KI"], 
         ["+++CURRENT AGE+++", "K= IF YOU ARE BETWEEN 30 AND 40 YEARS OLD.", "L= BETWEEN 40 AND 50.", "F= BETWEEN 50 AND 70.", "N= OVER 70.", " I= UNDER 30.", "KLFNI"]]
for DATA in DATAS:
    for q in DATA:
        if q[0] == " ":
            print("", q)
            true = True
            while true:
                print("CHOOSE ONE OF THE LETTERS ABOVE?", end=' ')
                g = input()
                if g == '': g = 'q'
                for qq in DATA[-1]:
                    if g[0] == qq:
                        true = False
                        print()
                        aa = list(a)
                        for N in range(15):
                            if g[0] == aa[N]:
                                M=(N+1)-9
                                Z=Z+M
            break
        else:
            print(" ", q)
print("YOU ARE EXPECTED TO LIVE TO THE AGE OF",Z,"YEARS")
SEX = ["26%","15%","36%","20%","48%","30%","61%","39%", "75%","53%","87%","70%","96%","88%","99.9%","99.6%"]
if Z>=60:
    i = 1
    for Y in range(60, Z + 1, 5):
        i=i+1
    m = SEX[i]
    f=SEX[i+1]
    print("OUT LIVING", m,"OF THE MEN AND", f,"OF THE WOMEN.")
print("Для продолжения нажмите любую клавишу . . . ",  end="")
input()