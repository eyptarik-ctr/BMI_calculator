from tkinter import *
#resaults
def resault():
    kulanıcı_boy = boy_int.get()
    kulanıcı_kg = kg_int.get()
    if kulanıcı_kg == "" or kulanıcı_boy == "":
        resault_label.config(text="Lütfen boyunuzu kilonuzu doğru girin",bg="black",fg="white")
    else:
        bmı=float(kulanıcı_kg)/((float(kulanıcı_boy)/100)**2)
        resault_label.config(text="BMI'nız {} ".format(bmı), bg="black", fg="white")
    if bmı <= 18 :
        değerlendirme.config(text="BMI' nıza göre sınıfınız zayıf ", bg="black", fg="white")
    elif bmı > 18 and bmı < 25:
        değerlendirme.config(text="BMI' nıza göre sınıfınız orta ", bg="black", fg="white")
    else:
        değerlendirme.config(text="BMI' nıza göre sınıfınız obez ", bg="black", fg="white")
#screen
window = Tk()
window.minsize(width=200 ,height=250 )
window.title("BMI hesplayıcı")

#label1 kg label
kg_label = Label(text="kilonuzu girin (kg)")
kg_label.config(bg="black",fg="white")
kg_label.pack()

#entry1 kg input
kg_int = Entry()
kg_int.pack()

#label2 boy label
boy_label = Label(text="Boyunuzu girin (cm)")
boy_label.config(bg="black",fg="white")
boy_label.pack()

#entry2 boy input
boy_int = Entry()
boy_int.pack()

#calculater button
calculate_but = Button(text="Sonuç",command=resault)
calculate_but.pack()

#resault
resault_label = Label()
resault_label.pack()

#değerlendieme

değerlendirme = Label()
değerlendirme.pack()

window.mainloop()