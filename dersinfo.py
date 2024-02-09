### Ders notuna ve disiplin cezasına bakarak sınıfı geciren veya biraktiran python yazilimi
print("Please write your note in the lesson\n")

lesson_finish_note = int(input("please sign your lesson note\n"))

x = int(input("did you ever had dicipline punishment in this year? if you had enter 1, if you dont enter 0 "))

if x==1:
    print("you cant pass your class because of dicipline punishment. Firstly, be a good people it is important than your lesson notes")
else:

    if (lesson_finish_note<50):
        print("you cant pass your class please work harder next year")

    else:
        print(" ****CONGRATULATİONS**** Keep hard working man!!!")



    
    