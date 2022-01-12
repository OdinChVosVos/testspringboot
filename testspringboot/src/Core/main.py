from tkinter import *
from tkinter import messagebox
import math
import random
import threading
import pygame
import tkinter as tk
import tkinter.ttk as ttk
import psycopg2
import pathlib
from pathlib import Path

print(Path.cwd(), '\n', Path.home())

con = psycopg2.connect(
        database="postgres", 
        user="postgres", 
        password="1488", 
        host="localhost", 
        port="5432"
)

cur = con.cursor()  

cur.execute("SELECT exists(select * from information_schema.tables where table_name=%s)", ('bd',))

if not(cur.fetchone()[0]):

        cur.execute('''CREATE TABLE BD  
        (id INT PRIMARY KEY NOT NULL,
        login TEXT NOT NULL UNIQUE,
        password TEXT,
        achieves INT NOT NULL,
        points INT NOT NULL,
        status INT NOT NULL);'''
        )
        con.commit()

        cur.execute("CREATE SEQUENCE bd_seq start 0 OWNED by bd.id")
        con.commit()

cur.execute("SELECT * from bd ORDER by id")
rows = cur.fetchall()

if  len(rows) == 0:

        cur.execute("INSERT INTO bd VALUES (0, 'admin', 'admin', 4, 0, 1);")
        con.commit()


cur.execute("SELECT * from bd ORDER by id")
rows = cur.fetchall()

rows = [str(row)[1:-1].replace(', ', ' | ').replace('\'', '') for row in rows]
print('id | login | password | achieves | points | status\n', '\n'.join(rows))

cur.close()
con.close()


def vxod():
        global pole
        global root
        global login
        global parol
        global vmenu
        global rediting_bd
        global rdl
        global idd
        global login_rdl
        global vixod

        def rediting_bd():
                global root
                global rdl
                global vmenu
                global idd
                global proxod
                global flag_admin
                global new_login
                global new_status
                global new_parol
                global nom_udalenie
                global login_rdl

                flag_admin=0
                root.destroy()
                root=Tk()
                root.geometry('1005x500')
                root.title('Angry gun')
                root.resizable(False, False)
                root.config(bg='#d6edfb')

                ramka_tree=LabelFrame(root)
                ramka_tree.pack(anchor=NW, padx=5, pady=5)
                
                tree=ttk.Treeview(ramka_tree, show='headings', columns=('ID пользователя', 'Логин', 'Пароль', 'Достижения', 'Баллы'), height=19)
                tree.heading('#1', text='ID пользователя')
                tree.heading('#2', text='Логин')
                tree.heading('#3', text='Пароль')
                tree.heading('#4', text='Достижения')
                tree.heading('#5', text='Баллы')
                tree.column('#1', width=130)
                tree.column('#2', width=200)
                tree.column('#3', width=150)
                tree.column('#4', width=100)
                tree.column('#5', width=100)
                        
                tree.pack(side=LEFT)

                scroll=Scrollbar(ramka_tree, command=tree.yview)
                scroll.pack(side=LEFT, fill=Y)
                tree.config(yscrollcommand=scroll.set)


                con = psycopg2.connect(
                database="postgres", 
                user="postgres", 
                password="1488", 
                host="localhost", 
                port="5432"
                )

                cur = con.cursor() 

                cur.execute("SELECT * from bd ORDER by id")
                rdl = cur.fetchall()
                rdl = [str(row)[1:-1].replace('\'', '') for row in rdl]
               

                cur.execute('''ALTER SEQUENCE bd_seq RESTART WITH 1;
                ALTER TABLE journal DROP CONSTRAINT journal_bd_id_fk;
                Delete from bd;
                ''')
                con.commit()

                for i in range(len(rdl)):
                        cur.execute("INSERT INTO bd VALUES ({}, '{}', '{}', {}, {}, {});"
                        .format(rdl[i].split(', ')[0], rdl[i].split(', ')[1], rdl[i].split(', ')[2]
                        , rdl[i].split(', ')[3], rdl[i].split(', ')[4], rdl[i].split(', ')[5]))
                        con.commit()

                cur.execute('''UPDATE bd SET id = nextval('bd_seq') where id != 0;
                ALTER TABLE journal ADD CONSTRAINT journal_bd_id_fk FOREIGN KEY (user_id) 
                REFERENCES bd(id) ON UPDATE CASCADE;''')
                con.commit()

                cur.execute("SELECT * from bd ORDER by id")
                rdl = cur.fetchall()
                rdl = [str(row)[1:-1].replace('\'', '') for row in rdl]
                
                cur.close()
                con.close()

                login_rdl=[]
                
                for i in rdl: login_rdl.append(i.split(', ')[1])
                
                for i in range(1, len(rdl)):
                        if idd!=0:
                                if rdl[i].split(', ')[-1] != '1':
                                        tree.insert('', 'end', i, values=(f'{rdl[i].split(", ")[0]}', f'{rdl[i].split(", ")[1]}', f'{rdl[i].split(", ")[2]}', f'{rdl[i].split(", ")[3]}', f'{rdl[i].split(", ")[4]}'))
                                        
                        else: tree.insert('', 'end', i, values=(f'{rdl[i].split(", ")[0]}', f'{rdl[i].split(", ")[1]}', f'{rdl[i].split(", ")[2]}', f'{rdl[i].split(", ")[3]}', f'{rdl[i].split(", ")[4]}'))
                        
                proxod=len(rdl)        
                vmenu_iztree=Button( root, font='GothicRus', text='⌂', fg='dimgray', bg='silver', width=4, command=vmenu)
                vmenu_iztree.place(x=910, y=450)

                ramka_login=LabelFrame(root, bg='#d6edfb')
                ramka_login.place(x=720, y=5)
                
                new_login_l=Label(ramka_login, text='Логин:', bg='#d6edfb')
                new_login_l.pack(pady=5)
                
                new_login=Entry(ramka_login)
                new_login.pack(padx=5)

                new_parol_l=Label(ramka_login, text='Пароль:', bg='#d6edfb')
                new_parol_l.pack(pady=5)

                new_parol=Entry(ramka_login)
                new_parol.pack()

                if idd == 0:
                        flag_admin=1
                        
                        new_status_l=Label(ramka_login, text='Статус доступа:', bg='#d6edfb')
                        new_status_l.pack(pady=5)
                        
                        new_status=Entry(ramka_login)
                        new_status.pack(pady=5)
                
                ramka_ud=LabelFrame(root, bg='#d6edfb')
                ramka_ud.place(x=720, y=185)
                
                nomudl=Label(ramka_ud, text='id номер:', bg='#d6edfb')
                nomudl.pack(pady=2.5)
                
                nom_udalenie=Entry(ramka_ud)
                nom_udalenie.pack(padx=5, pady=2.5)

                ramka_red=LabelFrame(root, bg='#d6edfb')
                ramka_red.place(x=720, y=255)

                nomredactl=Label(ramka_red, text='id номер:', bg='#d6edfb')
                nomredactl.pack(pady=5)
                
                nom_redact=Entry(ramka_red)
                nom_redact.pack(padx=5)

                redlogl=Label(ramka_red, text='Логин:', bg='#d6edfb')
                redlogl.pack(pady=5)
                
                redlog=Entry(ramka_red)
                redlog.pack()

                redparol_l=Label(ramka_red, text='Пароль:', bg='#d6edfb')
                redparol_l.pack(pady=5)
                
                redparol=Entry(ramka_red)
                redparol.pack(pady=2.5)
                
                search=Entry(root)
                search.pack(anchor=SW, pady=30, padx=5)

                search_l=Label(root, text='Логин:', bg='#d6edfb')
                search_l.place(x=50, y=420)

                def sozdanie():
                        global proxod
                        global flag_admin
                        global new_login
                        global new_status
                        global new_parol
                        global login_rdl
                        
                        proxod+=1
                        if flag_admin:
                                try:       
                                        if (int(new_status.get())==1 or int(new_status.get())==0) and new_login.get()!='' and new_status.get()!='' and new_login.get() not in login_rdl:
                                                
                                                con = psycopg2.connect(
                                                database="postgres", 
                                                user="postgres", 
                                                password="1488", 
                                                host="localhost", 
                                                port="5432"
                                                )

                                                cur = con.cursor() 

                                                cur.execute("SELECT * from bd ORDER by id")
                                                konez = cur.fetchall()
                                                konez = int([str(row)[1:-1].replace('\'', '') for row in konez][-1].split(', ')[0])

                                                cur.execute("INSERT INTO bd VALUES (%s, %s, %s, 0, 0, %s);", 
                                                (konez+1, new_login.get(), new_parol.get(), new_status.get()))
                                                con.commit()

                                                cur.execute("ALTER Sequence bd_seq restart with {};".format(konez+2))
                                                con.commit()

                                                cur.close()
                                                con.close()

                                                tree.insert('', 'end', proxod, values=(f'{konez+1}', f'{new_login.get()}', f'{new_parol.get()}', f'{0}', f'{0}'))
                                                login_rdl.append(new_login.get())

                                        else: messagebox.showerror(title = 'Ошибка', message = 'Логин не введён ил такой пользователь уже существует, или не верно введён статус')
                                except: messagebox.showerror(title = 'Ошибка', message = 'Не верно указан доступ')
                        else:
                                if new_login.get() != '' and new_login.get() not in login_rdl:
                                        
                                        con = psycopg2.connect(
                                        database="postgres", 
                                        user="postgres", 
                                        password="1488", 
                                         host="localhost", 
                                        port="5432"
                                        )

                                        cur = con.cursor() 

                                        cur.execute("SELECT * from bd ORDER by id")
                                        konez = cur.fetchall()
                                        konez = int([str(row)[1:-1].replace('\'', '') for row in konez][-1].split(', ')[0])

                                        cur.execute("INSERT INTO bd VALUES (%s, %s, %s, 0, 0, 0);", 
                                        (konez+1, new_login.get(), new_parol.get() ))
                                        con.commit()

                                        cur.execute("ALTER Sequence bd_seq restart with {};".format(konez+2))
                                        con.commit()

                                        cur.close()
                                        con.close()

                                        tree.insert('', 'end', proxod, values=(f'{konez+1}', f'{new_login.get()}', f'{new_parol.get()}', f'{0}', f'{0}'))
                                        login_rdl.append(new_login.get())
                                else: messagebox.showerror(title = 'Ошибка', message = 'Логин не введён либо такой пользователь уже существует')
                                        
                def udalenie():
                        global nom_udalenie
                        global flag_admin

                        try: int(nom_udalenie.get())
                        except: messagebox.showerror(title = 'Ошибка', message = 'Удалить данного пользователя невозможно либо его не существует')
                        if int(nom_udalenie.get())>0:

                                con = psycopg2.connect(
                                database="postgres", 
                                user="postgres", 
                                password="1488", 
                                host="localhost", 
                                port="5432"
                                )

                                cur = con.cursor() 

                                cur.execute("SELECT * from bd ORDER by id")
                                rdl = cur.fetchall()
                                rdl = [str(row)[1:-1].replace('\'', '') for row in rdl]

                                cur.close()
                                con.close()


                                try: rdl[int(nom_udalenie.get())]
                                except: messagebox.showerror(title = 'Ошибка', message = 'Удалить данного пользователя невозможно либо его не существует')
                                if (not(flag_admin) and rdl[int(nom_udalenie.get())].split(', ')[-1] != '1') or flag_admin:

                                        try:
                                                con = psycopg2.connect(
                                                database="postgres", 
                                                user="postgres", 
                                                password="1488", 
                                                host="localhost", 
                                                port="5432"
                                                )

                                                cur = con.cursor() 

                                                cur.execute("SELECT * from bd ORDER by id")
                                                rdl_udalenie = cur.fetchall()
                                                rdl_udalenie = [str(row)[1:-1].replace('\'', '') for row in rdl_udalenie]

                                                cur.close()
                                                con.close()

                                                dlina=len(rdl_udalenie)
                                                ud_login=rdl_udalenie[int(nom_udalenie.get())].split(', ')[1]
                                        
                                        except: messagebox.showerror(title = 'Ошибка', message = 'Удалить данного пользователя невозможно либо его не существует')
                                        for i in range(len(rdl_udalenie)-1-int(nom_udalenie.get())):
                                                rdl_udalenie[int(nom_udalenie.get())+i+1]=str(int(rdl_udalenie[int(nom_udalenie.get())+i+1].split(', ')[0])-1)+', '+', '.join(rdl_udalenie[int(nom_udalenie.get())+i+1].split(', ')[1:])
                                                

                                        con = psycopg2.connect(
                                        database="postgres", 
                                        user="postgres", 
                                        password="1488", 
                                        host="localhost", 
                                        port="5432"
                                        )

                                        cur = con.cursor() 

                                        cur.execute("DELETE from journal WHERE user_id = %s;", (nom_udalenie.get()))
                                        con.commit()

                                        cur.execute("DELETE from bd WHERE id = %s;", (nom_udalenie.get()))
                                        con.commit()

                                        cur.execute("UPDATE bd SET id = id-1 WHERE id > %s;", (nom_udalenie.get()))
                                        con.commit()

                                        cur.execute("ALTER Sequence bd_seq restart with {};".format(nom_udalenie.get()))
                                        con.commit()

                                        login_rdl.remove(ud_login)

                                        cur.execute("SELECT * from bd ORDER by id")
                                        rdl_udalenie = cur.fetchall()
                                        rdl_udalenie = [str(row)[1:-1].replace('\'', '') for row in rdl_udalenie]

                                        cur.close()
                                        con.close()
                                        
                                        for i in tree.get_children(): tree.delete(i)
                                        if flag_admin!=1:
                                                for i in range(1, len(rdl_udalenie)):
                                                        if rdl_udalenie[i].split(", ")[5] != '1':
                                                                tree.insert('', 'end', i, values=(f'{rdl_udalenie[i].split(", ")[0]}', f'{rdl_udalenie[i].split(", ")[1]}', f'{rdl_udalenie[i].split(", ")[2]}', f'{rdl_udalenie[i].split(", ")[3]}', f'{rdl_udalenie[i].split(", ")[4]}'))
                                        else:
                                                for i in range(1, len(rdl_udalenie)):
                                                        tree.insert('', 'end', i, values=(f'{rdl_udalenie[i].split(", ")[0]}', f'{rdl_udalenie[i].split(", ")[1]}', f'{rdl_udalenie[i].split(", ")[2]}', f'{rdl_udalenie[i].split(", ")[3]}', f'{rdl_udalenie[i].split(", ")[4]}'))
                                else: 
                                        messagebox.showerror(title = 'Ошибка', message = 'Удалить данного пользователя невозможно либо его не существует')
                        else: 
                                messagebox.showerror(title = 'Ошибка', message = 'Удалить данного пользователя невозможно либо его не существует')

                def redach():
                        global flag_admin

                        try: 
                                int(nom_redact.get())
                        except: 
                                messagebox.showerror(title = 'Ошибка', message = 'Данного пользователя нельзя редактировать, либо его не существует')

                        if int(nom_redact.get())>0:

                                con = psycopg2.connect(
                                database="postgres", 
                                user="postgres", 
                                password="1488", 
                                host="localhost", 
                                port="5432"
                                )

                                cur = con.cursor() 

                                cur.execute("SELECT * from bd ORDER by id")
                                rdl = cur.fetchall()
                                rdl = [str(row)[1:-1].replace('\'', '') for row in rdl]

                                cur.close()
                                con.close()

                                try: 
                                        rdl[int(nom_redact.get())]
                                except: 
                                        messagebox.showerror(title = 'Ошибка', message = 'Данного пользователя нельзя редактировать, либо его не существует')
                                
                                if (not(flag_admin) and rdl[int(nom_redact.get())].split(', ')[-1] != '1') or flag_admin:

                                        con = psycopg2.connect(
                                        database="postgres", 
                                        user="postgres", 
                                        password="1488", 
                                        host="localhost", 
                                        port="5432"
                                        )

                                        cur = con.cursor() 

                                        cur.execute("SELECT * from bd ORDER by id")
                                        rdl_redact = cur.fetchall()
                                        rdl_redact = [str(row)[1:-1].replace('\'', '') for row in rdl_redact]

                                        cur.close()
                                        con.close()

                                        try: 
                                                rdl_redact[int(nom_redact.get())]=nom_redact.get()+', '+redlog.get()+', '+redparol.get()+', '+', '.join(rdl_redact[int(nom_redact.get())].split(', ')[3:])
                                        except: 
                                                messagebox.showerror(title = 'Ошибка', message = 'Данного пользователя нельзя редактировать, либо его не существует')

                                        con = psycopg2.connect(
                                        database="postgres", 
                                        user="postgres", 
                                        password="1488", 
                                        host="localhost", 
                                        port="5432"
                                        )

                                        cur = con.cursor() 

                                        cur.execute("UPDATE bd SET login= %s, password= %s WHERE id = %s",
                                        (redlog.get(), redparol.get(), nom_redact.get()))
                                        con.commit()

                                        cur.close()
                                        con.close()

                                        login_rdl[int(nom_redact.get())]=redlog.get()
                                        
                                        for i in tree.get_children(): tree.delete(i)

                                        for i in range(1, len(rdl_redact)):
                                                if idd!=0:
                                                        if rdl_redact[i].split(', ')[-1] != '1':
                                                                tree.insert('', 'end', i, values=(f'{rdl_redact[i].split(", ")[0]}', f'{rdl_redact[i].split(", ")[1]}', f'{rdl_redact[i].split(", ")[2]}', f'{rdl_redact[i].split(", ")[3]}', f'{rdl_redact[i].split(", ")[4]}'))
                                                                
                                                else: tree.insert('', 'end', i, values=(f'{rdl_redact[i].split(", ")[0]}', f'{rdl_redact[i].split(", ")[1]}', f'{rdl_redact[i].split(", ")[2]}', f'{rdl_redact[i].split(", ")[3]}', f'{rdl_redact[i].split(", ")[4]}'))
                                else:  
                                        messagebox.showerror(title = 'Ошибка', message = 'Данного пользователя нельзя редактировать, либо его не существует')
                        else:  
                                messagebox.showerror(title = 'Ошибка', message = 'Данного пользователя нельзя редактировать, либо его не существует')

                def poiski():

                        con = psycopg2.connect(
                        database="postgres", 
                        user="postgres", 
                        password="1488", 
                        host="localhost", 
                        port="5432"
                        )

                        cur = con.cursor() 
                        
                        cur.execute("SELECT * from bd ORDER by id")
                        rdl = cur.fetchall()
                        rdl = [str(row)[1:-1].replace('\'', '') for row in rdl]

                        cur.close()
                        con.close()

                        for i in tree.get_children(): tree.delete(i)

                        for i in range(1, len(rdl)):
                                if idd!=0:
                                        if rdl[i].split(', ')[-1] != '1':
                                                tree.insert('', 'end', i, values=(f'{rdl[i].split(", ")[0]}', f'{rdl[i].split(", ")[1]}', f'{rdl[i].split(", ")[2]}', f'{rdl[i].split(", ")[3]}', f'{rdl[i].split(", ")[4]}'))
                                                                
                                else: tree.insert('', 'end', i, values=(f'{rdl[i].split(", ")[0]}', f'{rdl[i].split(", ")[1]}', f'{rdl[i].split(", ")[2]}', f'{rdl[i].split(", ")[3]}', f'{rdl[i].split(", ")[4]}'))
                        
                        for i in rdl: 
                                if search.get()==i.split(', ')[1]: search_nom=i.split(', ')[0]
                        
                        try: 
                                tree.selection_set(search_nom)
                        except:  
                                messagebox.showerror(title = 'Ошибка', message = 'Пользователя с введенным логином не существует или у вас нет доступа')


                Sozdat=Button(root, text='Создать', command=sozdanie, bg='khaki1')
                Sozdat.place(x=920, y=55)

                Udalit=Button(root, text='Удалить', command=udalenie, bg='khaki1')
                Udalit.place(x=920, y=200)

                redact=Button(root, text='Редактировать', command=redach, bg='khaki1')
                redact.place(x=900, y=320)

                poisk=Button(root, text='Поиск', command=poiski, bg='khaki1')
                poisk.place(x=150, y=430)


        con = psycopg2.connect(
        database="postgres", 
        user="postgres", 
        password="1488", 
        host="localhost", 
        port="5432"
        )

        cur = con.cursor() 

        cur.execute("SELECT * from bd ORDER by id")
        rdl = cur.fetchall()
        rdl = [str(row)[1:-1].replace('\'', '') for row in rdl]

        cur.close()
        con.close()

        login_rdl = []
        
        for i in rdl: login_rdl.append(i.split(', ')[1])

        if login.get() in login_rdl and parol.get() == rdl[login_rdl.index(login.get())].split(', ')[2]:

                idd = login_rdl.index(login.get())

                text = open(Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', 'Data.txt'), 'a', encoding='utf-8')      
                text.write(f'Пользователь {login.get()} номер {idd} \n')
                text.close()
                
                root.destroy()
                root=Tk()
                root.geometry('270x500')
                root.resizable(False, False)
                pole=PhotoImage(file=Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', 'pole.png'))
                root.title('Angry gun')
                        
                def vmenu():
                        global root
                        global pole
                        global rediting_bd
                        global vixod
        
                        root.destroy()
                        root=Tk()
                        root.resizable(False, False)
                        root.geometry('270x500')
                        pole=PhotoImage(file=Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', 'pole.png'))
                        root.title('Angry gun')

                        pygame.init()
                        
                        lpole=Label(root, image=pole)
                        lpole.place(x=-100, y=-120)

                        Rama=LabelFrame(root)
                        Rama.place(x=30, y=100)

                        lpole2=Label(Rama, image=pole)
                        lpole2.place(x=-60, y=-165)

                        Start=Button(Rama, font=('GothicRus', '20'), text='Начать игру', bg='khaki1', command=start, bd=5)
                        Start.pack(padx=10, pady=15)

                        Achieves=Button(Rama, font=('GothicRus', '20'), text='Достижения', bg='khaki1', command=achieves, bd=5)
                        Achieves.pack()

                        Exit=Button(Rama, font=('GothicRus', '20'), text='Выход из игры', bg='khaki1', command=exit, bd=5)
                        Exit.pack(pady=15, padx=10)

                        smena=PhotoImage(file=Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', 'smena.png'))
                        
                        Exit_pers=Button(root, command=vixod, image=smena, bd=0, bg='#c3e6fa')
                        Exit_pers.place(x=235, y=5)
                        
                        if rdl[idd].split(', ')[-1] == '1':
                                redit=PhotoImage(file=Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', 'redit2.png'))
                                rediting=Button(root, image=redit, command=rediting_bd, bd=0, bg='#c3e6fa')
                                rediting.place(x=5, y=5)
                        
                        pygame.mixer.Channel(0).pause()
                        pygame.mixer.Channel(1).pause()

                        root.mainloop()
                        
                def start():
                    global j
                    global yz
                    global flag
                    global canvas
                    global canvas2
                    global M
                    global canvas3
                    global root
                    global bal
                    global kolpopad
                    global kolvistrel
                    global otchet
                    global pole
                    global vmenu
                    global rdl
                    global idd
                    
                    root.geometry('1920x1080')
                    root.resizable(True, True)
                    fon=PhotoImage(file=Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', 'fon.png'))
                    root.config(bg='grey')
                    root.title('Angry gun')
                    root.state('zoomed')

                    lbg=Label(image=fon)
                    lbg.place(x=-1, y=-1)

                    M=random.randint(700, 1450)
                    bal=0
                    flag=0
                    kolpopad=0
                    kolvistrel=0
                    pygame.init()
                    Lock=random.randint(1,3)
                    otchet=''
                    
                    def click():
                        global yz
                        global z
                        global b
                        global j
                        global i
                        global k
                        global lg
                        global image_gun
                        global canvas2
                        global flag
                        global Lock
                        global canvas
                        global kolpopad
                        global kolvistrel
                        global pole
                        global root
                        flagm=0
                        xm=[]
                        ym=[]
                        Lock=random.randint(1,3)
                        kolvistrel+=1
                        try:
                            alfa=int(e1.get())
                            h=int(e2.get())
                            v0=int(e3.get())
                        except:
                            flagm=1
                            e1.delete(0, END)
                            e2.delete(0, END)
                            e3.delete(0, END)
                            messagebox.showerror(title = 'Ошибка', message = 'Проверьте правильность введенных данных\nУгол над горизонтом должен быть целым\n числом от 0 до 88\nНачальная высота должна быть целым\n числом от 0 до 200\nНачальная скорость должна быть целым\n числом от 10 до 100')
                            
                        if alfa>=88 or alfa<0 or v0>100 or v0<10 or h<0 or h>200:
                            flagm=1
                            e1.delete(0, END)
                            e2.delete(0, END)
                            e3.delete(0, END)
                            messagebox.showerror(title = 'Ошибка', message = 'Проверьте правильность введенных данных\nУгол над горизонтом должен быть целым\n числом от 0 до 88\nНачальная высота должна быть целым\n числом от 0 до 200\nНачальная скорость должна быть целым\n числом от 10 до 100')
                     
                       
                        if flag!=1 and flagm!=1:
                            global oval
                            global canvas2
                            global canvas
                            global pole
                            global root
                            global bal
                            flag=1
                            bal-=50
                            btn.config(bg='salmon', text='Заряжаю', width=8)
                            def cooldown():
                                global flag
                                global canvas
                                flag=0
                                canvas.place(x=2000, y=1100)
                                btn.config(bg='silver', text='Огонь')
                                  
                            t = threading.Timer(4.5, cooldown)
                            t.start()
                            
                            canvas2.place(x=2000, y=2000)
                            b=580-alfa*(math.pi/2)
                            z=270-alfa*(math.pi/2)
                            
                            if 0<=h<=50:
                                canvas2.config(highlightthickness=0, width=270, height=280)
                                
                                if 0<=alfa<15: image_gun = canvas2.create_image(182, 140, image=gun0)  
                                elif 15<=alfa<=37: image_gun = canvas2.create_image(182, 134, image=gun30)
                                elif 37<alfa<=52: image_gun = canvas2.create_image(181, 134, image=gun45)
                                elif 52<alfa<75: image_gun = canvas2.create_image(182, 140, image=gun60)
                                elif 75<=alfa<90: image_gun = canvas2.create_image(181, 129, image=gun90)
                                 
                                canvas2.place(x=0, y=420)
                                lpod.place(x=2000, y=590)
                                    
                            elif 50<h<=100:
                                lpod.config(image=pod)
                                
                                if 0<=alfa<15:
                                    canvas2.config(highlightthickness=0, width=290, height=270)
                                    image_gun = canvas2.create_image(185, 100, image=gun0s2)
                                    
                                elif 15<=alfa<=37:
                                    canvas2=Canvas(root, highlightthickness=0, width=280, height=270)
                                    image_gun = canvas2.create_image(185, 100, image=gun30s2)
                             
                                elif 37<alfa<=52:
                                    canvas2=Canvas(root, highlightthickness=0, width=270, height=270)
                                    image_gun = canvas2.create_image(185, 100, image=gun45s2)
                                   
                                elif 52<alfa<75:
                                    canvas2=Canvas(root, highlightthickness=0, width=270, height=270)
                                    image_gun = canvas2.create_image(185, 100, image=gun60s2)
                                    
                                elif 75<=alfa<90:
                                    canvas2=Canvas(root, highlightthickness=0, width=270, height=270)
                                    image_gun = canvas2.create_image(185, 100, image=gun90s2)
                                    
                                canvas2.place(x=0, y=320)
                                lpod.place(x=0, y=590)
                                 
                            elif 100<h<=200:
                                
                                if 0<=alfa<15:
                                    canvas2.config(highlightthickness=0, width=290, height=270)
                                    image_gun = canvas2.create_image(185, 100, image=gun0s3)
                                   
                                elif 15<=alfa<=37:
                                    canvas2=Canvas(root, highlightthickness=0, width=280, height=270)
                                    image_gun = canvas2.create_image(185, 100, image=gun30s3)
                                 
                                elif 37<alfa<=52:
                                    canvas2=Canvas(root, highlightthickness=0, width=270, height=270)
                                    image_gun = canvas2.create_image(185, 100, image=gun45s3)
                                    
                                elif 52<alfa<75:
                                    canvas2=Canvas(root, highlightthickness=0, width=270, height=270)
                                    image_gun = canvas2.create_image(185, 100, image=gun60s3)
                                  
                                elif 75<=alfa<90:
                                    canvas2=Canvas(root, highlightthickness=0, width=270, height=270)
                                    image_gun = canvas2.create_image(185, 100, image=gun90s3)
                                    
                                canvas2.place(x=0, y=220)
                                lpod.config(image=pod3)
                                lpod.place(x=0, y=490)
                                 
                           
                            j=0
                            a=alfa*math.pi/180
                            x=0
                            i=0
                            yz=b
                            canvas=Canvas(root, background='snow', highlightthickness=0, width=26, height=27)  
                            
                            while yz<669:
                                x=round(v0*math.cos(a)*i/100, 2)
                                xm.append(z+x)
                                y=round(h+v0*math.sin(a)*i/100-9.8*i*i/20000, 2)
                                ym.append(b-y)
                                yz=b-y 
                                i+=12
                        
                            def moving():
                                global kolpopad
                                global kolvistrel
                                global bal
                                global oval
                                global j
                                global root
                                global btn
                                global M
                                global pomenial
                                
                                image_id = canvas.create_image(961-xm[j], 541-ym[j], image=fon)
                                oval=canvas.create_oval(0 ,0, 25, 25, fill = 'black')
                                canvas.place(x=xm[j], y=ym[j])
                                
                                if M-27<=xm[j]<=M+70 and 626-27<=ym[j]<=626+70:
                                   canvas.place(x=2000, y=1200)
                                   j=1000
                                   pomenial=0
                                   pygame.mixer.Channel(1).set_volume(1.0)
                                   pygame.mixer.Channel(1).play(pygame.mixer.Sound(Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', 'Bah.mp3')))

                                   pygame.mixer.Channel(1).queue(pygame.mixer.Sound(Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', 'victory.mp3')))
                                  
                                   mibr_frames=[PhotoImage(file=Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', 'mibr.gif'), format='gif -index %i' %(i)) for i in range(4)]

                                   ind=0
                                   def update(ind):
                                           global pomenial
                                           if ind==4: ind=0
                                           frame = mibr_frames[ind]
                                           ind += 1
                                           canvas3.delete('all')
                                           image_mi=canvas3.create_image(35, 37, image=frame)
                                           if pomenial!=1: root.after(150, update, ind)
                                           else:
                                                   canvas3.delete('all')       
                                                   image_mi=canvas3.create_image(35, 37, image=Mi)
                                                   canvas3.place(x=M, y=626)
                                           

                                   update(ind)
                                  
                                   canvas3.place(x=M, y=626)
                                   bal+=150
                                   l4.config(text='Очки: '+str(bal))
                                   
                                   kolpopad+=1
                                   text= open(Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', 'Data.txt'), 'a', encoding='utf-8')      
                                   text.write(f'\t\tПопадание номер {str(kolpopad)} с попытки {str(kolvistrel)}\n\t\t\tРасстояние до мишени {str(M)}\n\t\t\tНачальная скорость {str(v0)}\n\t\t\tНачальная высота {str(h)}\n\t\t\tУгол над горизонтом {str(alfa)}\n')
                                   text.close()
                                   kolvistrel=0
                                   
                                   def change():
                                        global pomenial
                                        global M
                                        global canvas3
                                        pomenial=1
                                        M=random.randint(700, 1450)

                                        con = psycopg2.connect(
                                        database="postgres", 
                                        user="postgres", 
                                        password="1488", 
                                        host="localhost", 
                                        port="5432"
                                        )

                                        cur = con.cursor() 

                                        cur.execute("SELECT * from bd ORDER by id")
                                        rdl_new = cur.fetchall()
                                        rdl_new = [str(row)[1:-1].replace('\'', '') for row in rdl_new]

                                        cur.close()
                                        con.close()

                
                                        if rdl_new[idd].split(', ')[3]=='0':

                                                text= open(Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', 'Data.txt'), 'a', encoding='utf-8')      
                                                text.write(f'\tЗадача номер 1 выполнена\n')
                                                text.close()

                                                con = psycopg2.connect(
                                                database="postgres", 
                                                user="postgres", 
                                                password="1488", 
                                                host="localhost", 
                                                port="5432"
                                                )

                                                cur = con.cursor() 

                                                cur.execute("UPDATE bd SET achieves = 1 WHERE id = %s", (str(idd)))
                                                con.commit()

                                                cur.close()
                                                con.close()

                                                zadacha1.config(text='ЗАДАЧА\nМишень расположена\nна расстоянии\nS='+str(M)+'м.\nРассчитать подхо\nдящую скорость и\nугол над горизонтом,\nпри которых\nснаряд попадёт в\nмишень, если\nначальная высота\nh=70 м.')
                                        
                                        elif rdl_new[idd].split(', ')[3]=='1':
                                                
                                                if h==70:

                                                        text= open(Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', 'Data.txt'), 'a', encoding='Utf-8')      
                                                        text.write(f'\tЗадача номер 2 выполнена\n')
                                                        text.close()

                                                        
                                                        con = psycopg2.connect(
                                                        database="postgres", 
                                                        user="postgres", 
                                                        password="1488", 
                                                        host="localhost", 
                                                        port="5432"
                                                        )

                                                        cur = con.cursor() 

                                                        cur.execute("UPDATE bd SET achieves = 2 WHERE id = %s", (str(idd)))
                                                        con.commit()

                                                        cur.close()
                                                        con.close()

                                                        zadacha1.config(text='ЗАДАЧА\nМишень расположена\nна расстоянии\nS='+str(M)+'м.\nРассчитать угол над\nгоризонтом, при\nкотором снаряд попа\nдёт в мишень, если\nначальная высота\nh=70 м.\nа скорость v=100 м/с.')                    
                                                else: zadacha1.config(text='ЗАДАЧА\nМишень расположена\nна расстоянии\nS='+str(M)+'м.\nРассчитать подхо\nдящую скорость и\nугол над горизонтом,\nпри которых\nснаряд попадёт в\nмишень, если\nначальная высота\nh=70 м.')
                                                        
                                        elif rdl_new[idd].split(', ')[3]=='2':
                                                if h==70 and v0==100:

                                                        text= open(Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', 'Data.txt'), 'a', encoding='Utf-8')      
                                                        text.write(f'\tЗадача номер 3 выполнена\n')
                                                        text.close()

                                                        con = psycopg2.connect(
                                                        database="postgres", 
                                                        user="postgres", 
                                                        password="1488", 
                                                        host="localhost", 
                                                        port="5432"
                                                        )

                                                        cur = con.cursor() 

                                                        cur.execute("UPDATE bd SET achieves = 3 WHERE id = %s", (str(idd)))
                                                        con.commit()

                                                        cur.close()
                                                        con.close()

                                                        zadacha1.config(text='ЗАДАЧА\nМишень расположена\nна расстоянии\nS='+str(M)+'м.\nРассчитать началь\nную скорость, при\nкоторой снаряд попа\nдёт в мишень,\nесли начальная\nвысота h=70 м.\nа угол alfa=45')
                                                else: zadacha1.config(text='ЗАДАЧА\nМишень расположена\nна расстоянии\nS='+str(M)+'м.\nРассчитать угол над\nгоризонтом, при\nкотором снаряд попа\nдёт в мишень, если\nначальная высота\nh=70 м.\nа скорость v=100 м/с.')                    

                                        elif rdl_new[idd].split(', ')[3]=='3':
                                                if h==70 and alfa==45:

                                                        text= open(Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', 'Data.txt'), 'a', encoding='Utf-8')      
                                                        text.write(f'\tЗадача номер 4 выполнена\n')
                                                        text.close()

                                                        con = psycopg2.connect(
                                                        database="postgres", 
                                                        user="postgres", 
                                                        password="1488", 
                                                        host="localhost", 
                                                        port="5432"
                                                        )

                                                        cur = con.cursor() 

                                                        cur.execute("UPDATE bd SET achieves = 4 WHERE id = %s", (str(idd)))
                                                        con.commit()

                                                        cur.close()
                                                        con.close()

                                                        zadacha1.config(text='ПОЗДРАВЛЯЕМ\nВы выполнили все\nзадачи\nПоследующий прогресс\nне будет учитываться')

                                                else: 
                                                        zadacha1.config(text='ЗАДАЧА\nМишень расположена\nна расстоянии\nS='+str(M)+'м.\nРассчитать началь\nную скорость, при\nкоторой снаряд попа\nдёт в мишень,\nесли начальная\nвысота h=70 м.\nа угол alfa=45')
                                        
                                        elif rdl_new[idd].split(', ')[3]=='4':
                                                text= open(Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', 'Data.txt'), 'a', encoding='Utf-8')      
                                                text.write(f'\tВсе задачи выполнены\n')
                                                text.close()
                                        
                                   t2 = threading.Timer(2.5, change)
                                   t2.start()
                                  
                                
                                l4.config(text='Очки: '+str(bal))
                                if ym[j]>=669:

                                    pygame.mixer.Channel(1).set_volume(1.0)
                                    pygame.mixer.Channel(1).play(pygame.mixer.Sound(Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', 'Baz.mp3')))

                                j+=1
                                canvas.after(2, moving)
                                

                            pygame.mixer.Channel(1).set_volume(1.0)
                            pygame.mixer.Channel(1).play(pygame.mixer.Sound(Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', 'Bam.mp3')))

                            
                            moving()

                    def stop(): pygame.mixer.Channel(0).pause()
                    def play(): pygame.mixer.Channel(0).unpause()
                    def on_scroll(val):
                        vol=int(float(val))/100
                        pygame.mixer.Channel(0).set_volume(vol)
                        
                            
                    gun45=PhotoImage(file=Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', 'gun45f.png'))
                    gun0=PhotoImage(file=Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', 'gun0f.png'))
                    gun90=PhotoImage(file=Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', 'gun90f.png'))
                    gun30=PhotoImage(file=Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', 'gun30f.png'))
                    gun60=PhotoImage(file=Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', 'gun60f.png'))

                    gun45s2=PhotoImage(file=Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', '45s2.png'))
                    gun0s2=PhotoImage(file=Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', '10s2.png'))
                    gun90s2=PhotoImage(file=Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', '85s2.png'))
                    gun30s2=PhotoImage(file=Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', '30s2.png'))
                    gun60s2=PhotoImage(file=Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', '60s2.png'))

                    gun45s3=PhotoImage(file=Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', '45s3.png'))
                    gun0s3=PhotoImage(file=Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', '10s3.png'))
                    gun90s3=PhotoImage(file=Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', '85s3.png'))
                    gun30s3=PhotoImage(file=Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', '30s3.png'))
                    gun60s3=PhotoImage(file=Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', '60s3.png'))

                    floor=PhotoImage(file=Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', 'floor.png'))
                    Mi=PhotoImage(file=Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', 'mi.png'))
                    pod=PhotoImage(file=Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', 'pod2.png'))
                    pod3=PhotoImage(file=Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', 'pod.png'))
                    scroll=PhotoImage(file=Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', 'scroll.png'))

                    canvas2=Canvas(root, highlightthickness=0, width=270, height=280)
                    image_gun = canvas2.create_image(181, 134, image=gun45)
                    canvas2.place(x=0, y=420)

                    canvas3=Canvas(root, highlightthickness=0, width=70, height=74)
                    image_mi=canvas3.create_image(35, 37, image=Mi)
                    canvas3.place(x=M, y=626)

                    lf=Label(bd=0, highlightthickness=0, image=floor)
                    lf.place(x=0, y=700)

                    frame=LabelFrame(root, text='  Угол над горизонтом       Начальная высота        Начальная скорость ', bg='silver',
                                     font=('GothicRus', '14'), foreground='dimgrey')
                    frame.place(x=15, y=710)

                    btn=Button(root, font=('GothicRus', '24'),  text='Огонь', fg='dimgrey', background='silver', command=click, width=8)
                    btn.place(x=690, y=720)

                    pause=Button(root, font='GothicRus', text='◼', fg='dimgrey', background='silver', width=4, command=stop)
                    pause.place(x=1070, y=750)

                    play=Button(root, font='GothicRus', text='▶', fg='dimgrey', background='silver', width=4, command=play)
                    play.place(x=910, y=750)

                    vmenub=Button( root, font='GothicRus', text='⌂', fg='dimgray', bg='silver', width=4, command=vmenu)
                    vmenub.place(x=1480, y=738)

                    e1=Entry(frame, font=('GothicRus', '14'), foreground='dimgrey', width=15, justify=CENTER)
                    e1.pack(side=LEFT, padx=25, pady=10)

                    e2=Entry(frame, font=('GothicRus', '14'), foreground='dimgrey', width=15, justify=CENTER)
                    e2.pack(side=LEFT, padx=30, pady=10)

                    e3=Entry(frame, font=('GothicRus', '14'), foreground='dimgrey', width=15, justify=CENTER)
                    e3.pack(side=LEFT, padx=20, pady=10)

                    l4=Label(font=('GothicRus', '25'), foreground='gold', text='Очки: '+str(bal), background='silver')
                    l4.place(x=1265, y=730)


                    oblik=Label(bd=0, image=scroll)
                    oblik.place(x=1260, y=0)

                    con = psycopg2.connect(
                    database="postgres", 
                    user="postgres", 
                    password="1488", 
                    host="localhost", 
                    port="5432"
                    )

                    cur = con.cursor()

                    cur.execute("SELECT * from bd ORDER by id")

                    rdl_new = cur.fetchall()
                    rdl_new = [str(row)[1:-1].replace('\'', '') for row in rdl_new]

                    cur.close()
                    con.close()
                    
                    zadacha1=Label(font=('GothicRus', '14'), bg='#E0DDCF', text='ЗАДАЧА\nМишень расположена\nна расстоянии\nS='+str(M)+'м.\nРассчитать подхо\nдящую скорость, \nугол над горизонтом и\nвысоту при которых\nснаряд попадёт в\nмишень')
                    if rdl_new[idd].split(', ')[3]=='0': zadacha1.config(text='ЗАДАЧА\nМишень расположена\nна расстоянии\nS='+str(M)+'м.\nРассчитать подхо\nдящую скорость, \nугол над горизонтом и\nвысоту при которых\nснаряд попадёт в\nмишень')
                    elif rdl_new[idd].split(', ')[3]=='1': zadacha1.config(text='ЗАДАЧА\nМишень расположена\nна расстоянии\nS='+str(M)+'м.\nРассчитать подхо\nдящую скорость и\nугол над горизонтом,\nпри которых\nснаряд попадёт в\nмишень, если\nначальная высота\nh=70 м.')
                    elif rdl_new[idd].split(', ')[3]=='2': zadacha1.config(text='ЗАДАЧА\nМишень расположена\nна расстоянии\nS='+str(M)+'м.\nРассчитать угол над\nгоризонтом, при\nкотором снаряд попа\nдёт в мишень, если\nначальная высота\nh=70 м.\nа скорость v=100 м/с.')                    
                    elif rdl_new[idd].split(', ')[3]=='3': zadacha1.config(text='ЗАДАЧА\nМишень расположена\nна расстоянии\nS='+str(M)+'м.\nРассчитать началь\nную скорость, при\nкоторой снаряд попа\nдёт в мишень,\nесли начальная\nвысота h=70 м.\nа угол alfa=45')
                    elif rdl_new[idd].split(', ')[3]=='4': zadacha1.config(text='ПОЗДРАВЛЯЕМ\nВы выполнили все\nзадачи\nПоследующий прогресс\nне будет учитываться')
                    zadacha1.place(x=1313, y=45)
                    
                    lpod=Label(image=pod, bd=0, highlightthickness=0)

                    pygame.mixer.Channel(0).set_volume(0.5)
                    pygame.mixer.Channel(0).play(pygame.mixer.Sound(Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', 'music.mp3')), loops=10)

                    scale=Scale(root, from_=0, to=100, orient='horizontal', width=20, command=on_scroll)
                    scale.place(x=960, y=743)
                    scale.set(50)
                         
                    root.mainloop()

                def achieves():
                    global root
                    global vmenu

                    root.destroy()
                    root=Tk()
                    root.resizable(False, False)
                    root.title('Angry gun')
                    root.geometry('1000x400')
                    root.config(bg='grey0')

                    pygame.init()
                    
                    torch_frames=[PhotoImage(file=Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', 'torch2.gif'), format='gif -index %i' %(i)) for i in range(5)]
                    ramka=LabelFrame(root, bg='grey0', bd=0)
                    ramka.place(x=200, y=100)
                    
                    troph=PhotoImage(file=Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', 'troph.png'))
                    trophopen=PhotoImage(file=Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', 'trophopen2.png'))
                    
                    ach1=Label(ramka, image=troph, bg='grey0')
                    ach1.pack(side=LEFT)

                    ach2=Label(ramka, image=troph, bg='grey0')
                    ach2.pack(side=LEFT, padx=80)
                    
                    ach3=Label(ramka, image=troph, bg='grey0')
                    ach3.pack(side=LEFT)
                    
                    ach4=Label(ramka, image=troph, bg='grey0')
                    ach4.pack(side=LEFT, padx=80)

                    con = psycopg2.connect(
                    database="postgres", 
                    user="postgres", 
                    password="1488", 
                    host="localhost", 
                    port="5432"
                    )

                    cur = con.cursor()

                    cur.execute("SELECT * from bd ORDER by id")

                    rdl_ach = cur.fetchall()
                    rdl_ach = [str(row)[1:-1].replace('\'', '') for row in rdl_ach]

                    cur.close()
                    con.close()

                    otkr=int(rdl_ach[idd].split(', ')[3])
                
                    if otkr==4:
                            ach1.config(image=trophopen)
                            ach2.config(image=trophopen)
                            ach3.config(image=trophopen)
                            ach4.config(image=trophopen)
                    elif otkr==3:
                            ach1.config(image=trophopen)
                            ach2.config(image=trophopen)
                            ach3.config(image=trophopen)
                    elif otkr==2:
                            ach1.config(image=trophopen)
                            ach2.config(image=trophopen)
                    elif otkr==1:ach1.config(image=trophopen)
                            
                    pygame.mixer.Channel(0).set_volume(1.0)
                    pygame.mixer.Channel(0).play(pygame.mixer.Sound(Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', 'castle.mp3')), loops=10)

                    pygame.mixer.Channel(1).set_volume(1.0)
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound(Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', 'torch.mp3')), loops=10)
                    
                    ind=0
                    def update(ind):
                        if ind==5: ind=0
                        frame = torch_frames[ind]
                        ind += 1
                        label_torch1.config(image=frame)
                        label_torch2.config(image=frame)
                        root.after(150, update, ind)

                    label_torch1= Label(root, bd=0, bg='grey0')
                    label_torch1.pack(side=LEFT, padx=10)
                    
                    label_torch2= Label(root, bd=0, bg='grey0')
                    label_torch2.pack(side=RIGHT, padx=10)
                    
                    update(0)
                    
                    vmenu_ach=Button( root, font='GothicRus', text='⌂', fg='dimgray', bg='silver', width=4, command=vmenu)
                    vmenu_ach.place(x=10, y=350)
                    
                    root.mainloop()
                    

                lpole=Label(root, image=pole)
                lpole.place(x=-100, y=-120)

                Rama=LabelFrame(root)
                Rama.place(x=30, y=100)

                lpole2=Label(Rama, image=pole)
                lpole2.place(x=-60, y=-165)

                Start=Button(Rama, font=('GothicRus', '20'), text='Начать игру', bg='khaki1', command=start, bd=5)
                Start.pack(padx=10, pady=15)

                Achieves=Button(Rama, font=('GothicRus', '20'), text='Достижения', bg='khaki1', command=achieves, bd=5)
                Achieves.pack()

                Exit=Button(Rama, font=('GothicRus', '20'), text='Выход из игры', bg='khaki1', command=exit, bd=5)
                Exit.pack(pady=15, padx=10)

                smena=PhotoImage(file=Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', 'smena.png'))
                
                Exit_pers=Button(root, command=vixod, image=smena, bd=0, bg='#c3e6fa')
                Exit_pers.place(x=235, y=5)

                if rdl[idd].split(', ')[-1] == '1':

                        redit=PhotoImage(file=Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', 'redit2.png'))
                        rediting=Button(root, image=redit, command=rediting_bd, bd=0, bg='#c3e6fa')
                        rediting.place(x=5, y=5)

                root.mainloop()
                
        else:
                messagebox.showinfo(title = 'Ошибка', message ='Неверное имя пользователя или пароль')

                
def vixod():
        global root
        global login
        global parol
        
        root.destroy()
        root=Tk()
        root.geometry()
        root.resizable(False, False)
        root.title('Angry gun')
        root.geometry('320x300')

        pole=PhotoImage(file=Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', 'pole.png'))
        lpole=Label(root, image=pole)
        lpole.place(x=-100, y=-120)

        info=Label(font=('GothicRus', '18'), text='Подтвердите пользователя', bg='#c3e6fa')
        info.pack(side=TOP)

        info=Label(font='17', text='Логин:', bg='#cce9fb')
        info.place(x=130, y=50)

        login=Entry(root, font='14', width=25, justify=CENTER)
        login.pack(side=TOP, pady=46)

        info=Label(font='17', text='  Пароль:', bg='#d6edfb')
        info.pack(side=TOP)

        parol=Entry(root, font='14', width=25, justify=CENTER)
        parol.pack(side=TOP, pady=5)

        registr_vxod=Button(root, font=('GothicRus', '18'), text='Войти', command=vxod, bg='khaki1', bd=5)
        registr_vxod.pack(side=TOP, pady=15)

        root.mainloop()

        
root=Tk()
root.geometry()
root.resizable(False, False)
root.title('Angry gun')
root.geometry('320x300')

pole=PhotoImage(file=Path(Path.home(), 'IdeaProjects', 'project-final', 'testspringboot', 'src', 'Core', 'pole.png'))
lpole=Label(root, image=pole)
lpole.place(x=-100, y=-120)

info=Label(font=('GothicRus', '18'), text='Подтвердите пользователя', bg='#c3e6fa')
info.pack(side=TOP)

info=Label(font='17', text='Логин:', bg='#cce9fb')
info.place(x=130, y=50)

login=Entry(root, font='14', width=25, justify=CENTER)
login.pack(side=TOP, pady=46)

info=Label(font='17', text='  Пароль:', bg='#d6edfb')
info.pack(side=TOP)

parol=Entry(root, font='14', width=25, justify=CENTER)
parol.pack(side=TOP, pady=5)

registr_vxod=Button(root, font=('GothicRus', '18'), text='Войти', command=vxod, bg='khaki1', bd=5)
registr_vxod.pack(side=TOP, pady=15)

root.mainloop()