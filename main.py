import os
from tkinter import *
from tkinter import messagebox
# def cheak():
#     names = []
#     for name in list_of_name:
#         names.append(name)
#     mack = names[0]
#     for name in list_of_name:
#         mack = name
#         if list_of_name[name] > list_of_name[mack]:
#             mack = name
#     return mack
#
#
# #TODO 1: biding system
# def bid():
#     global list_of_name
#     list_of_name = {}
#     round = True
#     while round:
#         name = input("what is you name: \n")
#         money = float(input("How much do you what to bid in $:\n$"))
#         play = input("Do anyone want to bid, yes or no?\n")
#         list_of_name[name] = money
#         if play == "yes":
#             round = True
#         else:
#             round = False
#             result = cheak()
#     print(f"{result} {list_of_name[result]}")



#TODO 2: GUI application
data = {}

def bid_gui():
    global smp,mbb
    def fg(e):
        mbb["image"] = mb_bid2
    def gf(e):
        mbb["image"]= mb_bid1
    def hh(e):
        smp["image"]= stop_mb2
    def gg(e):
        smp["image"] = stop_mb1
    def dd():
        mbb.destroy()
        smp.destroy()
        bid_user()
    canver.delete("all")
    bid_f.destroy()
    exi.destroy()
    def enter_opp(e):
        exiw["image"] = ex_no

    def enter_pop(e):
        exiw["image"] = ex_of
    bgp = canver.create_image(450, 250, image=bg)
    mbp = canver.create_image(750, 234, image=mb)
    tbp = canver.create_image(120, 200, image=tb)
    tmp = canver.create_image(300, 150, image=tm)
    smp = Button(canver,image=stop_mb1, border=0, bg="#e26803", command=exit)
    smp.place(x=657,y=230)
    smp.bind("<Enter>", hh)
    smp.bind("<Leave>", gg)
    mbb = Button(canver,image=mb_bid1, border=0, bg="#e26803", command=dd)
    mbb.place(x=750,y=230)
    mbb.bind("<Enter>", fg)
    mbb.bind("<Leave>", gf)
    exiw = Button(image=ex_of, bg="#ffbd04", border=0, command=exit)
    exiw.place(y=430, x=200)
    exiw.bind("<Enter>", enter_opp)
    exiw.bind("<Leave>", enter_pop)
def bid_user():
    def fg(e):
        mbb["image"] = mb_bid2

    def gf(e):
        mbb["image"] = mb_bid1

    def hh(e):
        smp["image"] = stop_mb2

    def gg(e):
        smp["image"] = stop_mb1
    def add_user():
        data[name.get()] = float(bid.get())
        name.delete(0,"end")
        bid.delete(0,"end")
    def results():
        names = []
        for name in data:
            names.append(name)
        mack = names[0]
        for name in data:
            if data[name] > data[mack]:
                mack = name
        messagebox.showinfo("WINNER", f"The winner is {mack} with bid of  ${round(data[mack],2)}")

    canver.create_text(670, 100, text="Name", fill="#ffffff", font=("arial", 10, "bold"))
    name = Entry(canver, width=15, fg="#ffffff", bg="#ba3f23", border=0, font=("arial", 14))
    name.place(x=652, y=110)
    Frame(canver, width=163, height=1, bg="#ffffff").place(x=652, y=133)
    canver.create_text(700, 162, text="Bid amount in $", fill="#ffffff", font=("arial", 10, "bold"))
    bid = Entry(canver, width=15, fg="#ffffff", bg="#ba3f23", border=0, font=("arial", 14))
    bid.place(x=652, y=170)
    Frame(canver, width=163, height=1, bg="#ffffff").place(x=652, y=193)
    smp = Button(canver, image=stop_mb1, border=0, bg="#e26803", command=results)
    smp.place(x=657, y=230)
    smp.bind("<Enter>", hh)
    smp.bind("<Leave>", gg)
    mbb = Button(canver, image=mb_bid1, border=0, bg="#e26803", command=add_user)
    mbb.place(x=750, y=230)
    mbb.bind("<Enter>", fg)
    mbb.bind("<Leave>", gf)


def home():
    global bid_f, exi
    def enter_op(e):
        bid_f["image"] = bdn

    def enter_po(e):
        bid_f["image"] = bd
    def enter_opp(e):
        exi["image"] = ex_no

    def enter_pop(e):
        exi["image"] = ex_of
    canver.delete(ldp)
    bgp = canver.create_image(450,250, image=bg)
    tbp = canver.create_image(120,200,image=tb)
    hmp = canver.create_image(630, 210, image=hm)

  #  jtp = canver.create_image(430,110, image=jt )
    bid_f = Button(image=bd, bg="#ffbd04", border=0, command=bid_gui)
    bid_f.place(y=430,x=60)
    bid_f.bind("<Enter>", enter_op)
    bid_f.bind("<Leave>", enter_po)
    canver.create_text(425,40, text="BLIND AUCTION", fill="#ffffff", font=("Rockwell Extra Bold", 40, "bold"))
    exi = Button(image=ex_of, bg="#ffbd04", border=0, command=exit)
    exi.place(y=430, x=200)
    exi.bind("<Enter>", enter_opp)
    exi.bind("<Leave>", enter_pop)
    pass
root = Tk()
root.title("Biding")
root.geometry("898x500")
loading_page = PhotoImage(file="image/loading page.png")
bg = PhotoImage(file="image/background.png")
tb = PhotoImage(file="image/table.png")
tm = PhotoImage(file="image/time.png")
hm = PhotoImage(file="image/hamma.png")
jt = PhotoImage(file="image/Asset 3.png")
bd = PhotoImage(file="image/BID_BTN_OFF.png")
bdn = PhotoImage(file="image/BID_BTN_ON.png")
ex_of = PhotoImage(file="image/exit_on.png")
ex_no = PhotoImage(file="image/exit_off.png")
mb = PhotoImage(file="image/moblie.png")
mb_bid1 = PhotoImage(file="image/moblie_bid_off.png")
mb_bid2 = PhotoImage(file="image/moblie_bid_on.png")
stop_mb1 = PhotoImage(file="image/moblie_stop_off.png")
stop_mb2 = PhotoImage(file="image/moblie_stop_on.png")

canver = Canvas(width=900, height=500)
ldp = canver.create_image(450,250, image=loading_page)
canver.place(x=-2,y=0)
root.after(3000, home)
root.mainloop()