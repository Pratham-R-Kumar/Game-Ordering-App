from tkinter import *
import os
from PIL import ImageTk, Image
from tkinter import messagebox
import random
crr_page = 0
games = ['Far Cry 5', 'FIFA 21', 'Halo Infinite', 'Minecraft', 'Hitman 3', 'Battlefield Hardline', 'Dishonored 2',
         'Batman Arkham Knight', 'Need for Speed: Most Wanted', 'Resident Evil 2', 'Assassin Creed: Valhalla',
         'Witcher 3: Wild Hunt', 'Valorant', 'Assassin Creed: Origins', 'Uncharted 4: A Thiefs End',
         'Need for Speed: Heat', 'Far Cry 6', 'NBA 2K 2021', 'F1 2021', 'Getting over it', 'Super Mario',
         'Watch Dosg: Legion', 'Days Gone', 'Dota 2', 'Battlefield 2024', 'Call of Duty: Vanguard',
         'Red Dead Redemption Series Bundle', 'GTA 5']
global games_avail
games_avail = []


def started():
    global games_avail
    games_avail = []
    games_avail = random.sample(games,10)


def mainexit():
    global main
    main.destroy()


def check_phno(n):
    if len(n) != 10 or n.isdigit() == False:
        return False
    else:
        return True


def check_email(n):
    temp = '@'
    if temp in n:
        return True
    else:
        return False


def check_name(n):
    n = n.replace(" ", "")
    if any(char.isdigit() for char in n):
        return False
    else:
        return True


def des_login():
    login.destroy()


def des_home():
    home.destroy()


def des_games():
    game.destroy()


def des_ab():
    abt.destroy()


def logout():
    global crr_page
    if crr_page==1:
        home.destroy()
    elif crr_page==3:
        abt.destroy()
    elif crr_page==2:
        game.destroy()


def getgames():
    global username
    global temp
    username = name
    f = open(username+"games","r")
    temp = f.read().splitlines()


def add():
    msg = ""
    global username
    username = StringVar()
    username = name
    global games_list
    temp = games_list.get(ANCHOR)
    append = open(username+"games","a")
    data = open(username+"games","r")
    inc = data.read().splitlines()
    if temp in inc:
        msg = temp + " has already been added to your account"
        messagebox.showinfo("Warning", msg)
    else:
        append.write(temp+"\n")
        msg = temp + " has been added to your account"
        messagebox.showinfo("Success", msg)


def games_owned():
    global game
    global crr_page
    game = Toplevel(main)
    if crr_page==1:
        des_home()
    elif crr_page==3:
        des_ab()
    crr_page=2
    game.title("Games Owned")
    game.geometry("660x600")
    game.configure(background='grey')
    img = Image.open("avatar.png")
    resize_img = img.resize((100, 100))
    final = ImageTk.PhotoImage(resize_img)
    label = Label(game, image=final)
    label.image = final
    label.grid(row=1, padx=10, pady=40)
    home_bt = Button(game,text="HOME",width=15,padx=10,pady=10,command=homepage)
    home_bt.grid(row=3,column=0,padx=40,pady=10)
    games = Button(game,text="GAMES",width=15,padx=10,pady=10,state=DISABLED)
    games.grid(row=4,column=0,padx=40,pady=10)
    ab = Button(game,text="ACCOUNT",width=15,padx=10,pady=10,command=about_us)
    ab.grid(row=5,column=0,padx=40,pady=10)
    log_out = Button(game,text="LOG OUT",width=15,padx=10,pady=10,command=logout)
    log_out.grid(row=6,column=0,padx=40,pady=10)
    head = Label(game,text="Games Owned",width=32,height=3,font=(14),bg="blue",fg="white",relief="ridge")
    head.grid(row=1,column=1, ipadx=20)
    global gameslib
    games_lib = Listbox(game, width=35, font=(18), bd=2, bg="light gray", cursor="hand2", selectmode="single")
    games_lib.grid(row=2, column=1, rowspan=6)
    getgames()
    for item in temp:
        games_lib.insert(END,item)


def homepage():
    global home
    global crr_page
    home = Toplevel(main)
    if crr_page==2:
        des_games()
    elif crr_page==3:
        des_ab()
    elif crr_page==0:
        des_login()
    crr_page=1
    home.title("Homepage")
    home.geometry("660x600")
    home.configure(background='grey')
    img = Image.open("avatar.png")
    resize_img = img.resize((100,100))
    final = ImageTk.PhotoImage(resize_img)
    label = Label(home, image=final)
    label.image = final
    label.grid(row=1,padx=10, pady=40)
    home_bt = Button(home, text="HOME",width=15 ,padx=10, pady=10, state=DISABLED)
    home_bt.grid(row=3, column=0, padx=40, pady=10)
    games = Button(home, text="GAMES",width=15 ,padx=10, pady=10, command=games_owned)
    games.grid(row=4, column=0, padx=40, pady=10)
    ab = Button(home, text="ACCOUNT",width=15 ,padx=10, pady=10, command=about_us)
    ab.grid(row=5, column=0, padx=40, pady=10)
    log_out = Button(home, text="LOG OUT",width=15 ,padx=10, pady=10, command=logout)
    log_out.grid(row=6, column=0, padx=40, pady=10)

    head = Label(home,text="10 Games to get this month!!",width=32,height=3,font=(14),bg="blue",fg="white",relief="ridge")
    head.grid(row=1,column=1, ipadx=20)
    global games_list
    games_list = Listbox(home,width=35,font=(18), bd=2, bg="light gray",cursor="hand2",selectmode="single")
    games_list.grid(row=2,column=1,rowspan=6)
    for item in games_avail:
        games_list.insert(END,item)
    addgame = Button(home,text="ADD SELECTED GAME",width=52,padx=10,pady=10,command=add)
    addgame.grid(row=12,column=1,pady=20)


def about_us():
    global abt
    global crr_page
    global username_entry
    abt = Toplevel(main)
    if crr_page==1:
        des_home()
    elif crr_page==2:
        des_games()
    crr_page=3
    abt.title("About us")
    abt.geometry("660x600")
    abt.configure(background='grey')
    img = Image.open("avatar.png")
    resize_img = img.resize((100, 100))
    final = ImageTk.PhotoImage(resize_img)

    label = Label(abt, image=final)
    label.image = final
    label.grid(row=1, padx=10, pady=40)
    home_bt = Button(abt,text="HOME",width=15,padx=10,pady=10,command=homepage)
    home_bt.grid(row=3,column=0,padx=40,pady=10)
    games = Button(abt,text="GAMES",width=15,padx=10,pady=10,command=games_owned)
    games.grid(row=4,column=0,padx=40,pady=10)
    ab = Button(abt,text="ACCOUNT",width=15,padx=10,pady=10,state=DISABLED)
    ab.grid(row=5,column=0,padx=40,pady=10)
    log_out = Button(abt,text="LOG OUT",width=15,padx=10,pady=10,command=logout)
    log_out.grid(row=6,column=0,padx=40,pady=10)

    global fname
    fname = name
    f = open(fname,"r")
    temp = f.read().splitlines()
    head = Label(abt,text="Account Details",width=32,height=3,font=(14),bg="blue",fg="white",relief="ridge")
    head.grid(row=1,column=1, ipadx=20)

    l1 = Label(abt, text="Full Name:   "+temp[2],bg="light grey",fg="black",font=(14),width=30,anchor="w",padx=10)
    l1.grid(row=3,column=1)
    l2 = Label(abt, text="Username:   "+temp[0],bg="light grey",fg="black",font=(14),width=30,anchor="w",padx=10)
    l2.grid(row=4,column=1)
    l3 = Label(abt, text="Email ID:   "+temp[3],bg="light grey",fg="black",font=(14),width=30,anchor="w",padx=10)
    l3.grid(row=5,column=1)
    l3 = Label(abt, text="Phone Number:   "+temp[4],bg="light grey",fg="black",font=(14),width=30,anchor="w",padx=10)
    l3.grid(row=6,column=1)



def del2():
    scr2.destroy()


def wrong_pass():
    global scr2
    scr2 = Toplevel(main)
    scr2.title("Invalid Password")
    scr2.geometry("200x100")
    Label(scr2,text="Invalid password entered").pack()
    Button(scr2,text="Exit",command=del2).pack()


def del3():
    scr3.destroy()


def user_not_found():
    global scr3
    scr3 = Toplevel(main)
    scr3.title("User Not Found")
    scr3.geometry("200x100")
    Label(scr3,text="User not found").pack()
    Button(scr3,text="Exit",command=del3).pack()


def signup():
    global signup
    signup = Toplevel(main)
    signup.title("Signup")
    signup.geometry("600x500")
    signup.configure(background="grey")

    global username
    global password
    global username_entry
    global password_entry
    global name_full
    global email
    global ph_no
    global email_entry
    global phno_entry
    global fullname_entry
    username = StringVar()
    password = StringVar()
    name_full = StringVar()
    ph_no = StringVar()
    email = StringVar()
    Label(signup, text="", bg="grey").pack()
    fullname_lable = Label(signup, text="Full Name", bg="grey", font=("Helvetica", 15))
    fullname_lable.pack()
    fullname_entry = Entry(signup, textvariable=name_full, width="45")
    fullname_entry.pack()
    Label(signup, text="", bg="grey").pack()
    email_lable = Label(signup, text="Email", bg="grey", font=("Helvetica", 15))
    email_lable.pack()
    email_entry = Entry(signup, textvariable=email, width="45")
    email_entry.pack()
    Label(signup, text="", bg="grey").pack()
    phno_lable = Label(signup, text="Phone Number", bg="grey", font=("Helvetica", 15))
    phno_lable.pack()
    phno_entry = Entry(signup, textvariable=ph_no, width="45")
    phno_entry.pack()
    Label(signup, text="", bg="grey").pack()
    username_lable = Label(signup, text="Username", bg="grey", font=("Helvetica", 15))
    username_lable.pack()
    username_entry = Entry(signup, textvariable=username, width="45")
    username_entry.pack()
    Label(signup, text="",bg="grey").pack()
    password_lable = Label(signup, text="Password", bg="grey", font=("Helvetica", 15))
    password_lable.pack()
    password_entry = Entry(signup, textvariable=password, show='*', width="45")
    password_entry.pack()
    Label(signup, text="", bg="grey").pack()
    Button(signup, text="Register", width=15, height=2, font=("Helvetica", 15), command=register_user).pack()


def login_fun():
    global login
    global crr_page
    crr_page=0
    login = Toplevel(main)
    login.title("Login")
    login.geometry("500x300")
    login.configure(background="grey")
    Label(login, text="",bg="grey").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login, text="Username",bg="grey" ,font=("Helvetica", 15)).pack()
    username_login_entry = Entry(login, textvariable=username_verify, width="45")
    username_login_entry.pack()
    Label(login, text="",bg="grey").pack()
    Label(login, text="Password",bg="grey" ,font=("Helvetica", 15)).pack()
    password_login_entry = Entry(login, textvariable=password_verify, show='*', width="45")
    password_login_entry.pack()
    Label(login, text="",bg="grey").pack()
    Button(login, text="Login", width=15, height=2, font=("Helvetica", 13), command=login_verify).pack()
    started()

def register_user():
    username_info = username.get()
    password_info = password.get()
    fullname_info = name_full.get()
    email_info = email.get()
    phno_info = ph_no.get()
    status = 0
    while(status==0):
        if check_phno(phno_info)==False:
            phno_entry.delete(0, END)
            messagebox.showerror("Error","Invalid phone number,please open window and enter proper phone number")
            return
        elif check_email(email_info)==False:
            email_entry.delete(0, END)
            messagebox.showerror("Error","Invalid email address, please open window and enter proper email")
            return
        elif check_name(fullname_info) == False:
            fullname_entry.delete(0, END)
            messagebox.showerror("Error","Invalid name, please open window and enter proper name")
            return
        else:
            status = 1
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info+ "\n")
    file.write(fullname_info + "\n")
    file.write(email_info + "\n")
    file.write(phno_info + "\n")
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)
    fullname_entry.delete(0, END)
    email_entry.delete(0, END)
    phno_entry.delete(0, END)

    Label(signup, text="",bg="grey").pack()
    Label(signup, text="SignUp Successful", fg="white", bg="grey", font=("Helvetica", 11)).pack()


def login_verify():
    global name
    name = username_verify.get()
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            homepage()
        else:
            wrong_pass()
    else:
        user_not_found()


def main_fun():
    global main
    main = Tk()
    main.geometry("800x600")
    main.configure(background='grey')
    main.title("Game Corner")
    Label(text="Welcome", bg="Blue",fg="white", width="300", height="3", font=("Helvetica", 15, "bold"),relief="ridge").pack()
    Label(text="", bg="grey").pack()

    frame = LabelFrame(main,padx=2,pady=2)
    frame.pack()
    img = Image.open("Logo.png")
    resize_img = img.resize((100,100))
    final = ImageTk.PhotoImage(resize_img)
    lb = Label(frame,image=final,bg="black")
    lb.pack()
    Label(text="", bg="grey").pack()
    b1 = Button(main, text="Login", height="3", width="30", font=("Helvetica", 13), command=login_fun).pack()
    Label(text="", bg="grey").pack()
    b2 = Button(main, text="SignUp", height="3", width="30", font=("Helvetica", 13), command=signup).pack()
    Label(text="", bg="grey").pack()
    b3 = Button(main, text="Exit", height="3", width="30", font=("Helvetica", 13), command=mainexit).pack()
    main.mainloop()


main_fun()
Footer
© 2023 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
Frame.py/Frame.py at master · Pratham-R-Kumar/Frame.py
