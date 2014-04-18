#!/usr/bin/env python
# -*- coding:Latin-1 -*-

from Tkinter import *
from random import randrange

class Main(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title('Irregular Verbs')
        menu = MenuBar(self)
        menu.grid(row=1,sticky=W,padx=3,pady=3)
        flags = Flags()
        flags.grid(row=1,sticky=E)
        surf = Surface()
        surf.grid(row=2)
        surf.new()
        self.master.configure(bg='red')

    def quitter(self):
        msg = Toplevel(self,bg='red')
        msg.title('Quitter')
        Label(msg,
              text='Vous êtes sûr de vouloir quitter?',
              bg='red',fg='blue').grid(row=1,column=1,columnspan=2,
                                       padx=3,pady=2)
        Button(msg,text='Oui',width=8,
               command=self.master.quit,
               bg='blue',fg='white',activebackground='blue',
               activeforeground='white').grid(row=2,column=1,
                                              pady=2)
        Button(msg,text='Annuler',width=8,
               command=msg.destroy,
               bg='blue',fg='white',activebackground='blue',
              activeforeground='white').grid(row=2,column=2,
                                             pady=2)

    def quoi(self):
        "Renseigne sur l'appli"
        msg = Toplevel(self,bg='red')
        msg.title("C'est quoi?")
        Message(msg,width=200,
                text="Ceci est un programme pour apprendre\n\
les verbes irréguliers d'Anglais.",
                bg='red',fg='blue').grid(padx=3,pady=3)

    def apropos(self):
        "Renseigne sur l'appli, l'auteur, ..."
        msg = Toplevel(self,bg='red')
        msg.title("A propos")
        Message(msg,width =200, justify =CENTER,
                text ="Irregular Verbs\n\n\
(C) R.A.M, Sept 2008.\n\
Licence = GPL",bg='red',fg='blue').pack(padx=20,pady=10)


class Surface(Frame):
    def __init__(self):
        Frame.__init__(self,bg='blue')

        Label(self,text='Infinitive :',
              bg='red',fg='blue',relief=RIDGE).grid(row=1,column=1,
                                           columnspan=2,pady=2)
        self.infVar = StringVar()
        self.inf = Entry(self,textvariable=self.infVar,
                         fg='blue')
        self.inf.grid(row=2,column=1,columnspan=2,
                      pady=4)

        Label(self,text='Past simple :'
              ,bg='red',fg='blue',relief=RIDGE).grid(row=3,column=1)
        self.psVar = StringVar()
        self.ps = Entry(self,textvariable=self.psVar,
                        fg='red')
        self.ps.grid(row=4,column=1,padx=4,pady=4)

        Label(self,text='Past participle :',
              bg='red',fg='blue',relief=RIDGE).grid(row=3,column=2)
        self.ppVar = StringVar()
        self.pp = Entry(self,textvariable=self.ppVar,
                        fg='red')
        self.pp.grid(row=4,column=2,padx=4,pady=4)

        Label(self,text='Traduction :',
              bg='red',fg='blue',relief=RIDGE).grid(row=5,column=1,
                                           columnspan=2)
        self.trdVar=StringVar()
        self.trd = Entry(self,textvariable=self.trdVar,
                         fg='blue')
        self.trd.grid(row=6,column=1,columnspan=2,pady=4)

        Button(self,text='NEW!',command=self.new,
               bg='red',fg='blue',bd=3,relief=RAISED,
               font="bold",activebackground='red',
               activeforeground='blue').grid(row=7,column=1,
                                             columnspan=2,
                                             pady=3)

    def new(self):
        "Affiche un nouveau verbe"
        iv = open("irregularverbs.irv","r")
        c = 1
        while 1:
            lign = iv.readline()
            c += 1
            if lign == '':
                break
        iv.close()
        iv = open("irregularverbs.irv","r")
        n = randrange(1,c)
        a = 0
        while 1:
            a += 1
            line = iv.readline()
            if a == n:
                ligne_ = line
                break
        ligne = ligne_[0:len(ligne_)-1]
        liste = []
        ch = ''
        for car in ligne:
            if car == ' ':
                liste.append(ch)
                ch = ''
            else:
                ch = ch + car
        inf = liste[0]
        ps = liste[2]
        pp = liste[1]
        b = 3
        trd = ''
        while 1:
            try:
                if trd == '':
                    trd = liste[b]
                else:
                    trd = trd+' '+liste[b]
            except:
                break
            b += 1
        iv.close()

        self.infVar.set(inf)
        self.psVar.set(ps)
        self.ppVar.set(pp)
        self.trdVar.set(trd)



class MenuBar(Frame):
    "classe d'un barre de menu"
    def __init__(self,boss):
        Frame.__init__(self,bd=2,relief=RAISED,bg='blue')
        self.quitter = Menubutton(self,text='Quitter',
                                  bd=1,relief=RAISED,bg='blue',
                                  fg='white',
                                  activebackground='red',
                                  activeforeground='blue')
        self.quitter.grid(row=1,column=1,sticky=W)
        menu1 = Menu(self.quitter,bg='red',fg='blue')
        menu1.add_command(label='Quitter',command=boss.quitter)
        self.quitter.configure(menu=menu1)

        self.help = Menubutton(self,text='Aide',
                               bd=1,relief=RAISED,bg='blue',
                               fg='white',
                               activebackground='red',
                               activeforeground='blue')
        self.help.grid(row=1,column=2,sticky=W)
        menu2 = Menu(self.help,bg='red',fg='blue')
        menu2.add_command(label="C'est quoi?",command=boss.quoi)
        menu2.add_command(label='A propos',command=boss.apropos)
        self.help.configure(menu = menu2)


class Flags(Frame):
    "classe de l'aire des drapeaux"
    def __init__(self):
        Frame.__init__(self,bg='red')
        us = Canvas(self,width=27,height=20,bg='black')
        self.flag1 = PhotoImage(file="us.gif")
        us.create_image(13.5,10,image=self.flag1)
        us.grid(row=1,column=1,padx=10)
        
        uk = Canvas(self,width=27,height=20,bg='black')
        self.flag2 = PhotoImage(file="uk.gif")
        uk.create_image(13.5,10,image=self.flag2)
        uk.grid(row=1,column=2,padx=10)
        
        fr = Canvas(self,width=27,height=20,bg='black')
        self.flag3 = PhotoImage(file="fr.gif")
        fr.create_image(13.5,10,image=self.flag3)
        fr.grid(row=1,column=3,padx=10)


Main().mainloop()
