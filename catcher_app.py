

import requests
from bs4 import BeautifulSoup
from time import sleep

#----------FUNCTİON------------#
#------------------------------#
from tkinter import messagebox
import tkinter
import requests
from threading import Thread
import socket
import datetime
import time
def start():
   
    uyarilar = ""
    bekleme=E1.get()
    islem = ""
    messagebox.showwarning("Lütfen Bekleyin","İnternet Hızı Ve Sunucu Yogunlugu Nedeniyle\nİşlemler Gecikebilir,Sonuçları Görene Kadar Bekleyiniz\nYanıt Vermiyor Hatası Normaldir")
    from bs4 import BeautifulSoup
    import requests
    if var.get():

        
        if var.get() == 1:

            islem += "[*]>>> {} Sonuçları Görüyorsunuz...\n".format(bekleme)
            metin_alani2.insert(END,islem,"style")
            domain = E1.get()
            url = "https://who.is/whois/{}".format(domain)

            r = requests.get(url)
            sleep(3)
            soup = BeautifulSoup(r.content,"lxml")
            bilgi = soup.find_all("div",attrs={"class":"col-md-12 queryResponseBodyValue"})

            for bilgiler in bilgi:

                v = bilgiler.text
                veriler = v
                metin_alani2.insert(END,veriler,"style")
                metin_alani2.tag_configure('style',foreground='green',background="black",font=('Verdana',8,'bold'))


        
        elif var.get() == 2:
            islem += "[*]>>> {} Sonuçları Görüyorsunuz...\n".format(bekleme)
            metin_alani2.insert(END,islem,"style")
            domain = E1.get()
            url = "https://who.is/dns/{}".format(domain)

            r = requests.get(url)
            sleep(3)
            soup = BeautifulSoup(r.content,"lxml")
            bilgi = soup.find_all("div",attrs={"class":"col-md-12 queryResponseBodyKey"})

            for bilgiler in bilgi:

                v = bilgiler.text
                veriler = v
                metin_alani2.insert(END,veriler,"style")
                metin_alani2.tag_configure('style',foreground='green',background="black",font=('Verdana',8,'bold'))

    
        elif var.get() == 3:
            islem += "[*]>>> {} Sonuçları Görüyorsunuz...\n".format(bekleme)
            metin_alani2.insert(END,islem,"style")
            domain = E1.get()
            url = "https://check-host.net/ip-info?host={}".format(domain)

            r = requests.get(url)
            sleep(3)
            soup = BeautifulSoup(r.content,"lxml")
            bilgi = soup.find_all("div",attrs={"class":"ipinfo-item"})

            for bilgiler in bilgi:

                v = bilgiler.text
                veriler = v
                metin_alani2.insert(END,veriler,"style")
                metin_alani2.tag_configure('style',foreground='green',background="black",font=('Verdana',8,'bold'))


        elif var.get() == 4:
            islem += "[*]>>> {} Sonuçları Görüyorsunuz...\n".format(bekleme)
            metin_alani2.insert(END,islem,"style")
            metin_alani2.tag_configure('style',foreground='green',background="black",font=('Verdana',8,'bold'))
            dosya = open("fuzzing.txt","r")
            icerik = dosya.read()
            dosya.close()
           
            hedef = E1.get()
            for i in icerik.splitlines():

                metin_alani2.insert(END,i,"style")
                url = "http://"+hedef+str(i)

                sonuc = requests.get(url=url)
                if "200" in str(sonuc.status_code):
                    mesaj = "\nDosya veya klasör mevcut olabilir: {}\n".format(i)
                    metin_alani2.insert(END,mesaj,"style")

                else:
                    
                    mesaj = "\nDosya veya klasör yok: {}\n".format(i)
                    metin_alani2.insert(END,mesaj,"style")

        elif var.get() == 5:
            islem += "[*]>>> {} Sonuçları Görüyorsunuz...\n".format(bekleme)
            metin_alani2.insert(END,islem,"style")
            if E2.get():
            
                target = E2.get()
                str_target = "http://{}".format(target)
                def d1():

              
                   
                    try:
                        r=requests.get(str_target)
                        code = r.status_code
                        statu = ""
                        if "200" in str(code):
                            x=0
                            while True:
                                metin_alani.tag_configure('style',foreground='green',background="black",font=('Verdana',8,'bold'))
                                r=requests.get(str_target)
                                statu += " ping to target status_code: {}  succes[*]\n".format(code)
                                metin_alani.insert(END,statu,"style")
                                x+=1
                                sleep(1)
                                if x == 10:
                                    ip = socket.gethostbyname(target)
                                    statu += "\nDate: {} \npinging to target = 10\n[ping end]\nIP: {}".format(datetime.datetime.now(),ip)
                                    metin_alani.insert(END,statu,"style")
                                    break
                                else:
                                    continue

                                

                        else:

                            x=0
                            while True:
                                metin_alani.tag_configure('style',foreground='red',font=('Verdana',8,'bold'))
                               
                                r=requests.get(str_target)
                                statu += " ping to target status_code: {}   target off[blocked]\n".format(code)
                                metin_alani.insert(END,statu,"style")
                                x+=1
                                sleep(1)
                                if x == 10:
                                    ip = socket.gethostbyname(target)
                                    statu += "\nDate: {} \npinging to target = 10\n[ping end]\nIP: {}".format(datetime.datetime.now(),ip)
                                    metin_alani.insert(END,statu,"style")
                                    break
                                else:
                                    continue



                        


                    except:

                        error_http1 = "Lütfen Geçerli Bir Domain Giriniz\nÖrnek: www.orneksite.com"
                        messagebox.showerror("HTTP URL HATASI",error_http1)
                        metin_alani2.insert(END,"[Geçerli Domain Girilmedi]","style")

                t1=Thread(target = d1)
                t1.start()
            else:

                uyarilar+="Lütfen Bir Domain Giriniz!"
                messagebox.showerror("Domain ismi Boş Veya Hatalı",uyarilar)
                metin_alani2.insert(END,"[Domain ismi bos veya hatalı]","style")

            
   

    else:
        uyarilar += "LÜTFEN GEREKLİ İŞLEMLERİ SEÇİNİZ!"
        messagebox.showerror("BOŞ ALANLAR VAR",uyarilar)
        metin_alani2.insert(END,"[Gerekli Alanları Doldurunuz]","style")
        

      

           
from tkinter import *
import tkinter

master = Tk()
master.title("Catcher&Terminal")
photo = PhotoImage(file = "catcher_icon.png")
master.iconphoto(False, photo)
master.geometry("1000x600+200+100")
master.minsize(930,400)
master.maxsize(1100,660)


#----------------frame1--------------#
#------------------------------------#
frame1 = Frame(master,bg="darkslategrey")
frame1.place(relx=0,rely=0,relwidth=0.31,relheight=0.1)

Label(frame1,text="DOMAİN İSMİ:",bg="darkslategrey",fg="white",font="Courier 15 bold").pack(padx=2,pady=10,side=LEFT)
E1 = Entry(frame1,bd=2,relief=SOLID,font="Arial 10 bold")
E1.pack(side=LEFT)


#----------------frame2--------------#
#------------------------------------#

frame2 = Frame(master,bg="darkslategrey")
frame2.place(relx=0,rely=0.1,relwidth=0.31,relheight=0.55)
Label(frame2,text="Lütfen Bir İşlem Seçiniz",bg="darkslategrey",fg="white",font="Courier 15 bold",relief=GROOVE).pack(padx=2,pady=10,anchor=S)

#----------------İSLEMLER--RADİO BUTTON-----------------#
#-------------------------------------------------------#

var = IntVar()
R1 = Radiobutton(frame2,text='WHOİS SORGUSU',variable=var,value=1,bg='darkslategrey',fg='white',font='Arial 10 bold',relief=GROOVE,activebackground="darkseagreen",selectcolor="darkgreen")
R1.pack(anchor=NW,pady=5,padx=15)

#----------------
R2 = Radiobutton(frame2,text='DNS SORGUSU',variable=var,value=2,bg='darkslategrey',fg='white',font='Arial 10 bold',relief=GROOVE,activebackground="darkseagreen",selectcolor="darkgreen")
R2.pack(anchor=NW,pady=5,padx=15)
#----------------
R3 = Radiobutton(frame2,text='IP SORGUSU',variable=var,value=3,bg='darkslategrey',fg='white',font='Arial 10 bold',relief=GROOVE,activebackground="darkseagreen",selectcolor="darkgreen")
R3.pack(anchor=NW,pady=5,padx=15)
#----------------
R4 = Radiobutton(frame2,text='FUZZİNG TEST',variable=var,value=4,bg='darkslategrey',fg='white',font='Arial 10 bold',relief=GROOVE,activebackground="darkseagreen",selectcolor="darkgreen")
R4.pack(anchor=NW,pady=5,padx=15)
#----------------
R5 = Radiobutton(frame2,text='SUNUCU İSTEGİ',variable=var,value=5,bg='darkslategrey',fg='white',font='Arial 10 bold',relief=GROOVE,activebackground="darkseagreen",selectcolor="darkgreen")
R5.pack(anchor=NW,pady=5,padx=15)

dwnd = PhotoImage(file='button_on.png')
Button(frame2, image=dwnd, command=start,relief=FLAT,bg="darkslategrey",activebackground="darkslategrey").pack(pady=10)

#----------------frame3--------------#
#------------------------------------#

frame3 = Frame(master,bg="darkslategrey")
frame3.place(relx=0,rely=0.65,relwidth=0.31,relheight=0.1)

Label(frame3,text="DOMAİN PİNG:",bg="darkslategrey",fg="white",font="Courier 15 bold").pack(padx=2,pady=10,side=LEFT)
E2 = Entry(frame3,bd=2,relief=SOLID,font="Arial 10 bold")
E2.pack(side=LEFT)

#----------------frame4--------------#
#------------------------------------#

frame4 = Frame(master,bg="darkslategrey")
frame4.place(relx=0,rely=0.75,relwidth=0.31,relheight=0.25)

metin_alani = Text(frame4,height=9,width=38,bg="black")
metin_alani.tag_configure('style',foreground='red',background="black",font=('Verdana',8,'bold'))
metin_alani.pack()
example = "[root&root]>>>"
metin_alani.insert(END,example,"style")

#----------------frame5--------------#
#------------------------------------#
img = PhotoImage(file='catcher.png')
frame5 = Frame(master,bg="darkslategrey",bd=2,relief=GROOVE)
frame5.place(relx=0.31,rely=0,relwidth=0.69,relheight=0.17)
Label(frame5,image=img,bg="white").place(relwidth=1.0,relheight=1.0)
#----------------frame6--------------#
#------------------------------------#
frame6 = Frame(master,bg="darkslategrey",bd=3,relief=GROOVE)
frame6.place(relx=0.31,rely=0.17,relwidth=0.69,relheight=0.6)
Label(frame6,text="[information flow terminal]",bg="darkslategrey",fg="#d1d1d1",font="Arial 10 bold").pack()
metin_alani2 = Text(frame6,height=21,width=83,bg="black")
metin_alani2.tag_configure('style',foreground='red',background="black",font=('Verdana',8,'bold'))
metin_alani2.pack()
root = "[root&root]>>>"
metin_alani2.insert(END,root,"style")


#----------------frame7--------------#
#------------------------------------#
frame7 = Frame(master,bg="darkslategrey",bd=3,relief=GROOVE)
frame7.place(relx=0.31,rely=0.77,relwidth=0.69,relheight=0.23)
Label(frame7,text="Bu program kopyalanamaz ve satılamaz, ticari amaçla kullanılamaz. Telif hakkı yapımcıya aittir.\nBilgi toplamak için ücretsiz hizmete sunulan catcher gizlilik politikaları geregi yapımcı tarafından degiştirilebilme\nve kaldırılabilme hakkına sahiptir.Ticari amaçla kullanılması halinde gerekli işlemler yapılacaktır\nYapımcı: Yasincan olcay - ©catcher 2021 - olcaySoftware\nTüm hakları saklıdır\n",bg="darkslategrey",fg="#d1d1d1").pack()
icons = PhotoImage(file='github.png')
Label(frame7,image=icons,bg="darkslategrey").pack(side=LEFT)
icons2 = PhotoImage(file='instagram.png')
Label(frame7,image=icons2,bg="darkslategrey").pack(side=LEFT)
icons3 = PhotoImage(file='facebook.png')
Label(frame7,image=icons3,bg="darkslategrey").pack(side=LEFT)
icons6 = PhotoImage(file='onay.png')
Label(frame7,image=icons6,bg="darkslategrey").pack(side=RIGHT)
icons4 = PhotoImage(file='windows.png')
Label(frame7,image=icons4,bg="darkslategrey").pack(side=RIGHT)
icons5 = PhotoImage(file='linux.png')
Label(frame7,image=icons5,bg="darkslategrey").pack(side=RIGHT)


master.mainloop()







