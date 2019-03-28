
from tkinter import *
from tkinter import ttk
import random



v = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,\
    26,27,28,29,30,31,32,33,34,35,36]

def cpu_play ():
    global x,o,v
    if ga.get() == '3x3':
        r = random.choice(v)
        if r > 9 :
            cpu_play()
        else:

            if r == 1:
                bt1_()
            elif r == 2:
                bt2_()
            elif r == 3:
                bt3_()
            elif r == 4:
                bt4_()
            elif r == 5:
                bt5_()
            elif r == 6:
                bt6_()
            elif r == 7:
                bt7_()
            elif r == 8:
                bt8_()
            elif r == 9:
                bt9_()

    elif ga.get() == '4x4':
        r = random.choice(v)
        if r > 16 :
            cpu_play()
        else:
            if r == 1:
                bt1_()
            elif r == 2:
                bt2_()
            elif r == 3:
                bt3_()
            elif r == 4:
                bt4_()
            elif r == 5:
                bt5_()
            elif r == 6:
                bt6_()
            elif r == 7:
                bt7_()
            elif r == 8:
                bt8_()
            elif r == 9:
                bt9_()
            elif r == 10:
                bt10_()
            elif r == 11:
                bt11_()
            elif r == 12:
                bt12_()
            elif r == 13:
                bt13_()
            elif r == 14:
                bt14_()
            elif r == 15:
                bt15_()
            elif r == 16:
                bt16_()
    elif ga.get() == '5x5':
        r = random.choice(v)
        if r > 25 :
            cpu_play()
        else:
            if r == 1:
                bt1_()
            elif r == 2:
                bt2_()
            elif r == 3:
                bt3_()
            elif r == 4:
                bt4_()
            elif r == 5:
                bt5_()
            elif r == 6:
                bt6_()
            elif r == 7:
                bt7_()
            elif r == 8:
                bt8_()
            elif r == 9:
                bt9_()
            elif r == 10:
                bt10_()
            elif r == 11:
                bt11_()
            elif r == 12:
                bt12_()
            elif r == 13:
                bt13_()
            elif r == 14:
                bt14_()
            elif r == 15:
                bt15_()
            elif r == 16:
                bt16_()
            elif r == 17:
                bt17_()
            elif r == 18:
                bt18_()
            elif r == 19:
                bt19_()
            elif r == 20:
                bt20_()
            elif r == 21:
                bt21_()
            elif r == 22:
                bt22_()
            elif r == 23:
                bt23_()
            elif r == 24:
                bt24_()
            elif r == 25:
                bt25_()

    elif ga.get() == '6x6':
        r = random.choice(v)
        if r > 36 :
            cpu_play()
        else:
            if r == 1:
                bt1_()
            elif r == 2:
                bt2_()
            elif r == 3:
                bt3_()
            elif r == 4:
                bt4_()
            elif r == 5:
                bt5_()
            elif r == 6:
                bt6_()
            elif r == 7:
                bt7_()
            elif r == 8:
                bt8_()
            elif r == 9:
                bt9_()
            elif r == 10:
                bt10_()
            elif r == 11:
                bt11_()
            elif r == 12:
                bt12_()
            elif r == 13:
                bt13_()
            elif r == 14:
                bt14_()
            elif r == 15:
                bt15_()
            elif r == 16:
                bt16_()
            elif r == 17:
                bt17_()
            elif r == 18:
                bt18_()
            elif r == 19:
                bt19_()
            elif r == 20:
                bt20_()
            elif r == 21:
                bt21_()
            elif r == 22:
                bt22_()
            elif r == 23:
                bt23_()
            elif r == 24:
                bt24_()
            elif r == 25:
                bt25_()
            elif r == 26:
                bt26_()
            elif r == 27:
                bt27_()
            elif r == 28:
                bt28_()
            elif r == 29:
                bt29_()
            elif r == 30:
                bt30_()
            elif r == 31:
                bt31_()
            elif r == 32:
                bt32_()
            elif r == 33:
                bt33_()
            elif r == 34:
                bt34_()
            elif r == 35:
                bt35_()
            elif r == 36:
                bt36_()



def start():
    global player_label, bt1, bt2, bt3, bt4, bt5, bt6, bt7, bt8, bt9,\
        bt10, bt11, bt12, bt13, bt14, bt15, bt16, bt17, bt18,bt19, bt20,\
        bt21, bt22, bt23, bt24, bt25, bt26, bt27, bt28, bt29, bt30, bt31,\
        bt32, bt33, bt34, bt35, bt36,v

    v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, \
          26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]

    player.set("player 1")
    if ga.get() == "":
        pass
    elif ga.get() == '3x3':
        if win.get() != "3":
            pass
        elif win.get() == "3":
            back_bt.place_forget()
            start_bt.place_forget()
            condition.place_forget()
            game_size.place_forget()
            g_bt.place_forget()
            tital_label.place_forget()
            player_label = Label(x_o, textvariable=player, bg="#400040",
                                 font=('arial', 12, 'bold'), fg="red")
            player_label.place(x=120, y=0)
            x_o.geometry('300x325')
            bt1 = Button(x_o, image=e, width=95, height=95, command=bt1_)
            bt1.place(x=0, y=25)
            bt2 = Button(x_o, image=e, width=95, height=95, command=bt2_)
            bt2.place(x=100, y=25)
            bt3 = Button(x_o, image=e, width=95, height=95, command=bt3_)
            bt3.place(x=200, y=25)
            bt4 = Button(x_o, image=e, width=95, height=95, command=bt4_)
            bt4.place(x=0, y=125)
            bt5 = Button(x_o, image=e, width=95, height=95, command=bt5_)
            bt5.place(x=100, y=125)
            bt6 = Button(x_o, image=e, width=95, height=95, command=bt6_)
            bt6.place(x=200, y=125)
            bt7 = Button(x_o, image=e, width=95, height=95, command=bt7_)
            bt7.place(x=0, y=225)
            bt8 = Button(x_o, image=e, width=95, height=95, command=bt8_)
            bt8.place(x=100, y=225)
            bt9 = Button(x_o, image=e, width=95, height=95, command=bt9_)
            bt9.place(x=200, y=225)
    elif ga.get() == '4x4':
        if win.get() != '3' and win.get() != '4':
            pass
        elif win.get() == '3':
            back_bt.place_forget()
            start_bt.place_forget()
            condition.place_forget()
            game_size.place_forget()
            g_bt.place_forget()
            tital_label.place_forget()
            player_label = Label(x_o, textvariable=player, bg="#400040",
                                 font=('arial', 12, 'bold'), fg="red")
            player_label.place(x=170, y=0)
            x_o.geometry('400x425')
            bt1 = Button(x_o, image=e, width=95, height=95, command=bt1_)
            bt1.place(x=0, y=25)
            bt2 = Button(x_o, image=e, width=95, height=95, command=bt2_)
            bt2.place(x=100, y=25)
            bt3 = Button(x_o, image=e, width=95, height=95, command=bt3_)
            bt3.place(x=200, y=25)
            bt4 = Button(x_o, image=e, width=95, height=95, command=bt4_)
            bt4.place(x=300, y=25)
            bt5 = Button(x_o, image=e, width=95, height=95, command=bt5_)
            bt5.place(x=0, y=125)
            bt6 = Button(x_o, image=e, width=95, height=95, command=bt6_)
            bt6.place(x=100, y=125)
            bt7 = Button(x_o, image=e, width=95, height=95, command=bt7_)
            bt7.place(x=200, y=125)
            bt8 = Button(x_o, image=e, width=95, height=95, command=bt8_)
            bt8.place(x=300, y=125)
            bt9 = Button(x_o, image=e, width=95, height=95, command=bt9_)
            bt9.place(x=0, y=225)
            bt10 = Button(x_o, image=e, width=95, height=95, command=bt10_)
            bt10.place(x=100, y=225)
            bt11 = Button(x_o, image=e, width=95, height=95, command=bt11_)
            bt11.place(x=200, y=225)
            bt12 = Button(x_o, image=e, width=95, height=95, command=bt12_)
            bt12.place(x=300, y=225)
            bt13 = Button(x_o, image=e, width=95, height=95, command=bt13_)
            bt13.place(x=0, y=325)
            bt14 = Button(x_o, image=e, width=95, height=95, command=bt14_)
            bt14.place(x=100, y=325)
            bt15 = Button(x_o, image=e, width=95, height=95, command=bt15_)
            bt15.place(x=200, y=325)
            bt16 = Button(x_o, image=e, width=95, height=95, command=bt16_)
            bt16.place(x=300, y=325)
        elif win.get() == '4':
            back_bt.place_forget()
            start_bt.place_forget()
            condition.place_forget()
            game_size.place_forget()
            g_bt.place_forget()
            tital_label.place_forget()
            player_label = Label(x_o, textvariable=player, bg="#400040",
                                 font=('arial', 12, 'bold'), fg="red")
            player_label.place(x=170, y=0)
            x_o.geometry('400x425')
            bt1 = Button(x_o, image=e, width=95, height=95, command=bt1_)
            bt1.place(x=0, y=25)
            bt2 = Button(x_o, image=e, width=95, height=95, command=bt2_)
            bt2.place(x=100, y=25)
            bt3 = Button(x_o, image=e, width=95, height=95, command=bt3_)
            bt3.place(x=200, y=25)
            bt4 = Button(x_o, image=e, width=95, height=95, command=bt4_)
            bt4.place(x=300, y=25)
            bt5 = Button(x_o, image=e, width=95, height=95, command=bt5_)
            bt5.place(x=0, y=125)
            bt6 = Button(x_o, image=e, width=95, height=95, command=bt6_)
            bt6.place(x=100, y=125)
            bt7 = Button(x_o, image=e, width=95, height=95, command=bt7_)
            bt7.place(x=200, y=125)
            bt8 = Button(x_o, image=e, width=95, height=95, command=bt8_)
            bt8.place(x=300, y=125)
            bt9 = Button(x_o, image=e, width=95, height=95, command=bt9_)
            bt9.place(x=0, y=225)
            bt10 = Button(x_o, image=e, width=95, height=95, command=bt10_)
            bt10.place(x=100, y=225)
            bt11 = Button(x_o, image=e, width=95, height=95, command=bt11_)
            bt11.place(x=200, y=225)
            bt12 = Button(x_o, image=e, width=95, height=95, command=bt12_)
            bt12.place(x=300, y=225)
            bt13 = Button(x_o, image=e, width=95, height=95, command=bt13_)
            bt13.place(x=0, y=325)
            bt14 = Button(x_o, image=e, width=95, height=95, command=bt14_)
            bt14.place(x=100, y=325)
            bt15 = Button(x_o, image=e, width=95, height=95, command=bt15_)
            bt15.place(x=200, y=325)
            bt16 = Button(x_o, image=e, width=95, height=95, command=bt16_)
            bt16.place(x=300, y=325)
    elif ga.get() == '5x5':
        if  win.get() != '4' and win.get() != '5':
            pass
        elif win.get() == '4':
            back_bt.place_forget()
            start_bt.place_forget()
            condition.place_forget()
            game_size.place_forget()
            g_bt.place_forget()
            tital_label.place_forget()
            player_label = Label(x_o, textvariable=player, bg="#400040",
                                 font=('arial', 12, 'bold'), fg="red")
            player_label.place(x=220, y=0)
            x_o.geometry('500x525')
            bt1 = Button(x_o, image=e, width=95, height=95, command=bt1_)
            bt1.place(x=0, y=25)
            bt2 = Button(x_o, image=e, width=95, height=95, command=bt2_)
            bt2.place(x=100, y=25)
            bt3 = Button(x_o, image=e, width=95, height=95, command=bt3_)
            bt3.place(x=200, y=25)
            bt4 = Button(x_o, image=e, width=95, height=95, command=bt4_)
            bt4.place(x=300, y=25)
            bt5 = Button(x_o, image=e, width=95, height=95, command=bt5_)
            bt5.place(x=400, y=25)
            bt6 = Button(x_o, image=e, width=95, height=95, command=bt6_)
            bt6.place(x=0, y=125)
            bt7 = Button(x_o, image=e, width=95, height=95, command=bt7_)
            bt7.place(x=100, y=125)
            bt8 = Button(x_o, image=e, width=95, height=95, command=bt8_)
            bt8.place(x=200, y=125)
            bt9 = Button(x_o, image=e, width=95, height=95, command=bt9_)
            bt9.place(x=300, y=125)
            bt10 = Button(x_o, image=e, width=95, height=95, command=bt10_)
            bt10.place(x=400, y=125)
            bt11 = Button(x_o, image=e, width=95, height=95, command=bt11_)
            bt11.place(x=0, y=225)
            bt12 = Button(x_o, image=e, width=95, height=95, command=bt12_)
            bt12.place(x=100, y=225)
            bt13 = Button(x_o, image=e, width=95, height=95, command=bt13_)
            bt13.place(x=200, y=225)
            bt14 = Button(x_o, image=e, width=95, height=95, command=bt14_)
            bt14.place(x=300, y=225)
            bt15 = Button(x_o, image=e, width=95, height=95, command=bt15_)
            bt15.place(x=400, y=225)
            bt16 = Button(x_o, image=e, width=95, height=95, command=bt16_)
            bt16.place(x=0, y=325)
            bt17 = Button(x_o, image=e, width=95, height=95, command=bt17_)
            bt17.place(x=100, y=325)
            bt18 = Button(x_o, image=e, width=95, height=95, command=bt18_)
            bt18.place(x=200, y=325)
            bt19 = Button(x_o, image=e, width=95, height=95, command=bt19_)
            bt19.place(x=300, y=325)
            bt20 = Button(x_o, image=e, width=95, height=95, command=bt20_)
            bt20.place(x=400, y=325)
            bt21 = Button(x_o, image=e, width=95, height=95, command=bt21_)
            bt21.place(x=0, y=425)
            bt22 = Button(x_o, image=e, width=95, height=95, command=bt22_)
            bt22.place(x=100, y=425)
            bt23 = Button(x_o, image=e, width=95, height=95, command=bt23_)
            bt23.place(x=200, y=425)
            bt24 = Button(x_o, image=e, width=95, height=95, command=bt24_)
            bt24.place(x=300, y=425)
            bt25 = Button(x_o, image=e, width=95, height=95, command=bt25_)
            bt25.place(x=400, y=425)
        elif win.get() == '5':
            back_bt.place_forget()
            start_bt.place_forget()
            condition.place_forget()
            game_size.place_forget()
            g_bt.place_forget()
            tital_label.place_forget()
            player_label = Label(x_o, textvariable=player, bg="#400040",
                                 font=('arial', 12, 'bold'), fg="red")
            player_label.place(x=220, y=0)
            x_o.geometry('500x525')
            bt1 = Button(x_o, image=e, width=95, height=95, command=bt1_)
            bt1.place(x=0, y=25)
            bt2 = Button(x_o, image=e, width=95, height=95, command=bt2_)
            bt2.place(x=100, y=25)
            bt3 = Button(x_o, image=e, width=95, height=95, command=bt3_)
            bt3.place(x=200, y=25)
            bt4 = Button(x_o, image=e, width=95, height=95, command=bt4_)
            bt4.place(x=300, y=25)
            bt5 = Button(x_o, image=e, width=95, height=95, command=bt5_)
            bt5.place(x=400, y=25)
            bt6 = Button(x_o, image=e, width=95, height=95, command=bt6_)
            bt6.place(x=0, y=125)
            bt7 = Button(x_o, image=e, width=95, height=95, command=bt7_)
            bt7.place(x=100, y=125)
            bt8 = Button(x_o, image=e, width=95, height=95, command=bt8_)
            bt8.place(x=200, y=125)
            bt9 = Button(x_o, image=e, width=95, height=95, command=bt9_)
            bt9.place(x=300, y=125)
            bt10 = Button(x_o, image=e, width=95, height=95, command=bt10_)
            bt10.place(x=400, y=125)
            bt11 = Button(x_o, image=e, width=95, height=95, command=bt11_)
            bt11.place(x=0, y=225)
            bt12 = Button(x_o, image=e, width=95, height=95, command=bt12_)
            bt12.place(x=100, y=225)
            bt13 = Button(x_o, image=e, width=95, height=95, command=bt13_)
            bt13.place(x=200, y=225)
            bt14 = Button(x_o, image=e, width=95, height=95, command=bt14_)
            bt14.place(x=300, y=225)
            bt15 = Button(x_o, image=e, width=95, height=95, command=bt15_)
            bt15.place(x=400, y=225)
            bt16 = Button(x_o, image=e, width=95, height=95, command=bt16_)
            bt16.place(x=0, y=325)
            bt17 = Button(x_o, image=e, width=95, height=95, command=bt17_)
            bt17.place(x=100, y=325)
            bt18 = Button(x_o, image=e, width=95, height=95, command=bt18_)
            bt18.place(x=200, y=325)
            bt19 = Button(x_o, image=e, width=95, height=95, command=bt19_)
            bt19.place(x=300, y=325)
            bt20 = Button(x_o, image=e, width=95, height=95, command=bt20_)
            bt20.place(x=400, y=325)
            bt21 = Button(x_o, image=e, width=95, height=95, command=bt21_)
            bt21.place(x=0, y=425)
            bt22 = Button(x_o, image=e, width=95, height=95, command=bt22_)
            bt22.place(x=100, y=425)
            bt23 = Button(x_o, image=e, width=95, height=95, command=bt23_)
            bt23.place(x=200, y=425)
            bt24 = Button(x_o, image=e, width=95, height=95, command=bt24_)
            bt24.place(x=300, y=425)
            bt25 = Button(x_o, image=e, width=95, height=95, command=bt25_)
            bt25.place(x=400, y=425)
    elif ga.get() == '6x6':
        if  win.get() != '4' and win.get() != '5' and win.get() != '6':
            pass
        elif win.get() == '4':
            back_bt.place_forget()
            start_bt.place_forget()
            condition.place_forget()
            game_size.place_forget()
            g_bt.place_forget()
            tital_label.place_forget()
            player_label = Label(x_o, textvariable=player, bg="#400040",
                                 font=('arial', 12, 'bold'), fg="red")
            player_label.place(x=270, y=0)
            x_o.geometry('600x625')
            bt1 = Button(x_o, image=e, width=95, height=95, command=bt1_)
            bt1.place(x=0, y=25)
            bt2 = Button(x_o, image=e, width=95, height=95, command=bt2_)
            bt2.place(x=100, y=25)
            bt3 = Button(x_o, image=e, width=95, height=95, command=bt3_)
            bt3.place(x=200, y=25)
            bt4 = Button(x_o, image=e, width=95, height=95, command=bt4_)
            bt4.place(x=300, y=25)
            bt5 = Button(x_o, image=e, width=95, height=95, command=bt5_)
            bt5.place(x=400, y=25)
            bt6 = Button(x_o, image=e, width=95, height=95, command=bt6_)
            bt6.place(x=500, y=25)
            bt7 = Button(x_o, image=e, width=95, height=95, command=bt7_)
            bt7.place(x=0, y=125)
            bt8 = Button(x_o, image=e, width=95, height=95, command=bt8_)
            bt8.place(x=100, y=125)
            bt9 = Button(x_o, image=e, width=95, height=95, command=bt9_)
            bt9.place(x=200, y=125)
            bt10 = Button(x_o, image=e, width=95, height=95, command=bt10_)
            bt10.place(x=300, y=125)
            bt11 = Button(x_o, image=e, width=95, height=95, command=bt11_)
            bt11.place(x=400, y=125)
            bt12 = Button(x_o, image=e, width=95, height=95, command=bt12_)
            bt12.place(x=500, y=125)
            bt13 = Button(x_o, image=e, width=95, height=95, command=bt13_)
            bt13.place(x=0, y=225)
            bt14 = Button(x_o, image=e, width=95, height=95, command=bt14_)
            bt14.place(x=100, y=225)
            bt15 = Button(x_o, image=e, width=95, height=95, command=bt15_)
            bt15.place(x=200, y=225)
            bt16 = Button(x_o, image=e, width=95, height=95, command=bt16_)
            bt16.place(x=300, y=225)
            bt17 = Button(x_o, image=e, width=95, height=95, command=bt17_)
            bt17.place(x=400, y=225)
            bt18 = Button(x_o, image=e, width=95, height=95, command=bt18_)
            bt18.place(x=500, y=225)
            bt19 = Button(x_o, image=e, width=95, height=95, command=bt19_)
            bt19.place(x=0, y=325)
            bt20 = Button(x_o, image=e, width=95, height=95, command=bt20_)
            bt20.place(x=100, y=325)
            bt21 = Button(x_o, image=e, width=95, height=95, command=bt21_)
            bt21.place(x=200, y=325)
            bt22 = Button(x_o, image=e, width=95, height=95, command=bt22_)
            bt22.place(x=300, y=325)
            bt23 = Button(x_o, image=e, width=95, height=95, command=bt23_)
            bt23.place(x=400, y=325)
            bt24 = Button(x_o, image=e, width=95, height=95, command=bt24_)
            bt24.place(x=500, y=325)
            bt25 = Button(x_o, image=e, width=95, height=95, command=bt25_)
            bt25.place(x=0, y=425)
            bt26 = Button(x_o, image=e, width=95, height=95, command=bt26_)
            bt26.place(x=100, y=425)
            bt27 = Button(x_o, image=e, width=95, height=95, command=bt27_)
            bt27.place(x=200, y=425)
            bt28 = Button(x_o, image=e, width=95, height=95, command=bt28_)
            bt28.place(x=300, y=425)
            bt29 = Button(x_o, image=e, width=95, height=95, command=bt29_)
            bt29.place(x=400, y=425)
            bt30 = Button(x_o, image=e, width=95, height=95, command=bt30_)
            bt30.place(x=500, y=425)
            bt31 = Button(x_o, image=e, width=95, height=95, command=bt31_)
            bt31.place(x=0, y=525)
            bt32 = Button(x_o, image=e, width=95, height=95, command=bt32_)
            bt32.place(x=100, y=525)
            bt33 = Button(x_o, image=e, width=95, height=95, command=bt33_)
            bt33.place(x=200, y=525)
            bt34 = Button(x_o, image=e, width=95, height=95, command=bt34_)
            bt34.place(x=300, y=525)
            bt35 = Button(x_o, image=e, width=95, height=95, command=bt35_)
            bt35.place(x=400, y=525)
            bt36 = Button(x_o, image=e, width=95, height=95, command=bt36_)
            bt36.place(x=500, y=525)
        elif win.get() == '5':
            back_bt.place_forget()
            start_bt.place_forget()
            condition.place_forget()
            game_size.place_forget()
            g_bt.place_forget()
            tital_label.place_forget()
            player_label = Label(x_o, textvariable=player, bg="#400040",
                                 font=('arial', 12, 'bold'), fg="red")
            player_label.place(x=270, y=0)
            x_o.geometry('600x625')
            bt1 = Button(x_o, image=e, width=95, height=95, command=bt1_)
            bt1.place(x=0, y=25)
            bt2 = Button(x_o, image=e, width=95, height=95, command=bt2_)
            bt2.place(x=100, y=25)
            bt3 = Button(x_o, image=e, width=95, height=95, command=bt3_)
            bt3.place(x=200, y=25)
            bt4 = Button(x_o, image=e, width=95, height=95, command=bt4_)
            bt4.place(x=300, y=25)
            bt5 = Button(x_o, image=e, width=95, height=95, command=bt5_)
            bt5.place(x=400, y=25)
            bt6 = Button(x_o, image=e, width=95, height=95, command=bt6_)
            bt6.place(x=500, y=25)
            bt7 = Button(x_o, image=e, width=95, height=95, command=bt7_)
            bt7.place(x=0, y=125)
            bt8 = Button(x_o, image=e, width=95, height=95, command=bt8_)
            bt8.place(x=100, y=125)
            bt9 = Button(x_o, image=e, width=95, height=95, command=bt9_)
            bt9.place(x=200, y=125)
            bt10 = Button(x_o, image=e, width=95, height=95, command=bt10_)
            bt10.place(x=300, y=125)
            bt11 = Button(x_o, image=e, width=95, height=95, command=bt11_)
            bt11.place(x=400, y=125)
            bt12 = Button(x_o, image=e, width=95, height=95, command=bt12_)
            bt12.place(x=500, y=125)
            bt13 = Button(x_o, image=e, width=95, height=95, command=bt13_)
            bt13.place(x=0, y=225)
            bt14 = Button(x_o, image=e, width=95, height=95, command=bt14_)
            bt14.place(x=100, y=225)
            bt15 = Button(x_o, image=e, width=95, height=95, command=bt15_)
            bt15.place(x=200, y=225)
            bt16 = Button(x_o, image=e, width=95, height=95, command=bt16_)
            bt16.place(x=300, y=225)
            bt17 = Button(x_o, image=e, width=95, height=95, command=bt17_)
            bt17.place(x=400, y=225)
            bt18 = Button(x_o, image=e, width=95, height=95, command=bt18_)
            bt18.place(x=500, y=225)
            bt19 = Button(x_o, image=e, width=95, height=95, command=bt19_)
            bt19.place(x=0, y=325)
            bt20 = Button(x_o, image=e, width=95, height=95, command=bt20_)
            bt20.place(x=100, y=325)
            bt21 = Button(x_o, image=e, width=95, height=95, command=bt21_)
            bt21.place(x=200, y=325)
            bt22 = Button(x_o, image=e, width=95, height=95, command=bt22_)
            bt22.place(x=300, y=325)
            bt23 = Button(x_o, image=e, width=95, height=95, command=bt23_)
            bt23.place(x=400, y=325)
            bt24 = Button(x_o, image=e, width=95, height=95, command=bt24_)
            bt24.place(x=500, y=325)
            bt25 = Button(x_o, image=e, width=95, height=95, command=bt25_)
            bt25.place(x=0, y=425)
            bt26 = Button(x_o, image=e, width=95, height=95, command=bt26_)
            bt26.place(x=100, y=425)
            bt27 = Button(x_o, image=e, width=95, height=95, command=bt27_)
            bt27.place(x=200, y=425)
            bt28 = Button(x_o, image=e, width=95, height=95, command=bt28_)
            bt28.place(x=300, y=425)
            bt29 = Button(x_o, image=e, width=95, height=95, command=bt29_)
            bt29.place(x=400, y=425)
            bt30 = Button(x_o, image=e, width=95, height=95, command=bt30_)
            bt30.place(x=500, y=425)
            bt31 = Button(x_o, image=e, width=95, height=95, command=bt31_)
            bt31.place(x=0, y=525)
            bt32 = Button(x_o, image=e, width=95, height=95, command=bt32_)
            bt32.place(x=100, y=525)
            bt33 = Button(x_o, image=e, width=95, height=95, command=bt33_)
            bt33.place(x=200, y=525)
            bt34 = Button(x_o, image=e, width=95, height=95, command=bt34_)
            bt34.place(x=300, y=525)
            bt35 = Button(x_o, image=e, width=95, height=95, command=bt35_)
            bt35.place(x=400, y=525)
            bt36 = Button(x_o, image=e, width=95, height=95, command=bt36_)
            bt36.place(x=500, y=525)
        elif win.get() == '6':
            back_bt.place_forget()
            start_bt.place_forget()
            condition.place_forget()
            game_size.place_forget()
            g_bt.place_forget()
            tital_label.place_forget()
            player_label = Label(x_o, textvariable=player, bg="#400040",
                                 font=('arial', 12, 'bold'), fg="red")
            player_label.place(x=270, y=0)
            x_o.geometry('600x625')
            bt1 = Button(x_o, image=e, width=95, height=95, command=bt1_)
            bt1.place(x=0, y=25)
            bt2 = Button(x_o, image=e, width=95, height=95, command=bt2_)
            bt2.place(x=100, y=25)
            bt3 = Button(x_o, image=e, width=95, height=95, command=bt3_)
            bt3.place(x=200, y=25)
            bt4 = Button(x_o, image=e, width=95, height=95, command=bt4_)
            bt4.place(x=300, y=25)
            bt5 = Button(x_o, image=e, width=95, height=95, command=bt5_)
            bt5.place(x=400, y=25)
            bt6 = Button(x_o, image=e, width=95, height=95, command=bt6_)
            bt6.place(x=500, y=25)
            bt7 = Button(x_o, image=e, width=95, height=95, command=bt7_)
            bt7.place(x=0, y=125)
            bt8 = Button(x_o, image=e, width=95, height=95, command=bt8_)
            bt8.place(x=100, y=125)
            bt9 = Button(x_o, image=e, width=95, height=95, command=bt9_)
            bt9.place(x=200, y=125)
            bt10 = Button(x_o, image=e, width=95, height=95, command=bt10_)
            bt10.place(x=300, y=125)
            bt11 = Button(x_o, image=e, width=95, height=95, command=bt11_)
            bt11.place(x=400, y=125)
            bt12 = Button(x_o, image=e, width=95, height=95, command=bt12_)
            bt12.place(x=500, y=125)
            bt13 = Button(x_o, image=e, width=95, height=95, command=bt13_)
            bt13.place(x=0, y=225)
            bt14 = Button(x_o, image=e, width=95, height=95, command=bt14_)
            bt14.place(x=100, y=225)
            bt15 = Button(x_o, image=e, width=95, height=95, command=bt15_)
            bt15.place(x=200, y=225)
            bt16 = Button(x_o, image=e, width=95, height=95, command=bt16_)
            bt16.place(x=300, y=225)
            bt17 = Button(x_o, image=e, width=95, height=95, command=bt17_)
            bt17.place(x=400, y=225)
            bt18 = Button(x_o, image=e, width=95, height=95, command=bt18_)
            bt18.place(x=500, y=225)
            bt19 = Button(x_o, image=e, width=95, height=95, command=bt19_)
            bt19.place(x=0, y=325)
            bt20 = Button(x_o, image=e, width=95, height=95, command=bt20_)
            bt20.place(x=100, y=325)
            bt21 = Button(x_o, image=e, width=95, height=95, command=bt21_)
            bt21.place(x=200, y=325)
            bt22 = Button(x_o, image=e, width=95, height=95, command=bt22_)
            bt22.place(x=300, y=325)
            bt23 = Button(x_o, image=e, width=95, height=95, command=bt23_)
            bt23.place(x=400, y=325)
            bt24 = Button(x_o, image=e, width=95, height=95, command=bt24_)
            bt24.place(x=500, y=325)
            bt25 = Button(x_o, image=e, width=95, height=95, command=bt25_)
            bt25.place(x=0, y=425)
            bt26 = Button(x_o, image=e, width=95, height=95, command=bt26_)
            bt26.place(x=100, y=425)
            bt27 = Button(x_o, image=e, width=95, height=95, command=bt27_)
            bt27.place(x=200, y=425)
            bt28 = Button(x_o, image=e, width=95, height=95, command=bt28_)
            bt28.place(x=300, y=425)
            bt29 = Button(x_o, image=e, width=95, height=95, command=bt29_)
            bt29.place(x=400, y=425)
            bt30 = Button(x_o, image=e, width=95, height=95, command=bt30_)
            bt30.place(x=500, y=425)
            bt31 = Button(x_o, image=e, width=95, height=95, command=bt31_)
            bt31.place(x=0, y=525)
            bt32 = Button(x_o, image=e, width=95, height=95, command=bt32_)
            bt32.place(x=100, y=525)
            bt33 = Button(x_o, image=e, width=95, height=95, command=bt33_)
            bt33.place(x=200, y=525)
            bt34 = Button(x_o, image=e, width=95, height=95, command=bt34_)
            bt34.place(x=300, y=525)
            bt35 = Button(x_o, image=e, width=95, height=95, command=bt35_)
            bt35.place(x=400, y=525)
            bt36 = Button(x_o, image=e, width=95, height=95, command=bt36_)
            bt36.place(x=500, y=525)

def chick_win():
    global x, o, player_label, win_label, play_again_bt, main_window_bt,runing
    if runing == 'vs_player':
        if   ga.get() == '3x3' and win.get() == '3':
            if player.get() == 'player 1':
                if (1 in x and 2 in x and 3 in x) or (4 in x and 5 in x and 6 in x) or \
                        (7 in x and 8 in x and 9 in x) or (1 in x and 4 in x and 7 in x) or \
                        (2 in x and 5 in x and 8 in x) or (3 in x and 6 in x and 9 in x) or \
                        (1 in x and 5 in x and 9 in x) or (3 in x and 5 in x and 7 in x):
                    win_label = Label(x_o, text='x_x', bg="red", font=('arial', 28, 'bold'))
                    win_label.place(x=115, y=100)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=5, y=200)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=150, y=200)
                    x = []
                    o = []
                elif len(x) + len(o) == 9:
                    win_label = Label(x_o, text='^_^', bg="#400040", font=('arial', 28, 'bold'))
                    win_label.place(x=115, y=100)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=5, y=200)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=150, y=200)
                    x = []
                    o = []
                else:
                    player.set('player 2')
                    player_label.configure(fg='blue')
            elif player.get() == 'player 2':
                if (1 in o and 2 in o and 3 in o) or (4 in o and 5 in o and 6 in o) or \
                        (7 in o and 8 in o and 9 in o) or (1 in o and 4 in o and 7 in o) or \
                        (2 in o and 5 in o and 8 in o) or (3 in o and 6 in o and 9 in o) or \
                        (1 in o and 5 in o and 9 in o) or (3 in o and 5 in o and 7 in o):
                    win_label = Label(x_o, text='o_o', bg="blue", font=('arial', 28, 'bold'))
                    win_label.place(x=115, y=100)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=5, y=200)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=150, y=200)
                    x = []
                    o = []
                elif len(x) + len(o) == 9:
                    win_label = Label(x_o, text='^_^', bg="#400040", font=('arial', 28, 'bold'))
                    win_label.place(x=115, y=100)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=5, y=200)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=150, y=200)
                    x = []
                    o = []
                else:
                    player.set('player 1')
                    player_label.configure(fg='red')
        elif ga.get() == '4x4' and win.get() == '3':
            if player.get() == 'player 1':
                if (1 in x and 2 in x and 3 in x) or (2 in x and 3 in x and 4 in x) or \
                        (5 in x and 6 in x and 7 in x) or (6 in x and 7 in x and 8 in x) or \
                        (9 in x and 10 in x and 11 in x) or (10 in x and 11 in x and 12 in x) or \
                        (13 in x and 14 in x and 15 in x) or (14 in x and 15 in x and 16 in x) or \
                        (1 in x and 5 in x and 9 in x) or (5 in x and 9 in x and 13 in x) or \
                        (2 in x and 6 in x and 10 in x) or (6 in x and 10 in x and 14 in x) or \
                        (3 in x and 7 in x and 11 in x) or (7 in x and 11 in x and 15 in x) or \
                        (4 in x and 8 in x and 12 in x) or (8 in x and 12 in x and 16 in x) or \
                        (3 in x and 6 in x and 9 in x) or (4 in x and 7 in x and 10 in x) or \
                        (1 in x and 6 in x and 11 in x) or (6 in x and 11 in x and 16 in x) or \
                        (7 in x and 10 in x and 13 in x) or (8 in x and 11 in x and 14 in x) or \
                        (5 in x and 10 in x and 15 in x) or (2 in x and 7 in x and 12 in x):
                    win_label = Label(x_o, text='x_x', bg="red", font=('arial', 28, 'bold'))
                    win_label.place(x=165, y=150)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=55, y=250)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=200, y=250)
                    x = []
                    o = []
                elif len(x) + len(o) == 16:
                    win_label = Label(x_o, text='^_^', bg="#400040", font=('arial', 28, 'bold'))
                    win_label.place(x=165, y=150)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=55, y=250)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=200, y=250)
                    x = []
                    o = []
                else:
                    player.set('player 2')
                    player_label.configure(fg='blue')
            elif player.get() == 'player 2':
                if (1 in o and 2 in o and 3 in o) or (2 in o and 3 in o and 4 in o) or \
                        (5 in o and 6 in o and 7 in o) or (6 in o and 7 in o and 8 in o) or \
                        (9 in o and 10 in o and 11 in o) or (10 in o and 11 in o and 12 in o) or \
                        (13 in o and 14 in o and 15 in o) or (14 in o and 15 in o and 16 in o) or \
                        (1 in o and 5 in o and 9 in o) or (5 in o and 9 in o and 13 in o) or \
                        (2 in o and 6 in o and 10 in o) or (6 in o and 10 in o and 14 in o) or \
                        (3 in o and 7 in o and 11 in o) or (7 in o and 11 in o and 15 in o) or \
                        (4 in o and 8 in o and 12 in o) or (8 in o and 12 in o and 16 in o) or \
                        (3 in o and 6 in o and 9 in o) or (4 in o and 7 in o and 10 in o) or \
                        (1 in o and 6 in o and 11 in o) or (6 in o and 11 in o and 16 in o) or \
                        (7 in o and 10 in o and 13 in o) or (8 in o and 11 in o and 14 in o) or \
                        (5 in o and 10 in o and 15 in o) or (2 in o and 7 in o and 12 in o):
                    win_label = Label(x_o, text='o_o', bg="blue", font=('arial', 28, 'bold'))
                    win_label.place(x=165, y=150)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=55, y=250)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=200, y=250)
                    x = []
                    o = []
                elif len(x) + len(o) == 16:
                    win_label = Label(x_o, text='^_^', bg="#400040", font=('arial', 28, 'bold'))
                    win_label.place(x=165, y=150)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=55, y=250)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=200, y=250)
                    x = []
                    o = []
                else:
                    player.set('player 1')
                    player_label.configure(fg='red')
        elif ga.get() == '4x4' and win.get() == '4':
            if player.get() == 'player 1':
                if (1 in x and 2 in x and 3 in x and 4 in x) or \
                        (5 in x and 6 in x and 7 in x and 8 in x) \
                        or (9 in x and 10 in x and 11 in x and 12 in x) or \
                        (13 in x and 14 in x and 15 in x and 16 in x) \
                        or (1 in x and 5 in x and 9 in x and 13 in x) or (
                        2 in x and 6 in x and 10 in x and 14 in x) \
                        or (3 in x and 7 in x and 11 in x and 15 in x) or \
                        (4 in x and 8 in x and 12 in x and 16 in x) \
                        or (1 in x and 6 in x and 11 in x and 16 in x) or \
                        (4 in x and 7 in x and 10 in x and 13 in x):
                    win_label = Label(x_o, text='x_x', bg="red", font=('arial', 28, 'bold'))
                    win_label.place(x=165, y=150)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=55, y=250)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=200, y=250)
                    x = []
                    o = []
                elif len(x) + len(o) == 16:
                    win_label = Label(x_o, text='^_^', bg="#400040", font=('arial', 28, 'bold'))
                    win_label.place(x=165, y=150)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=55, y=250)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=200, y=250)
                    x = []
                    o = []
                else:
                    player.set('player 2')
                    player_label.configure(fg='blue')
            elif player.get() == 'player 2':
                if (1 in o and 2 in o and 3 in o and 4 in o) or \
                        (5 in o and 6 in o and 7 in o and 8 in o) \
                        or (9 in o and 10 in o and 11 in o and 12 in o) or \
                        (13 in o and 14 in o and 15 in o and 16 in o) \
                        or (1 in o and 5 in o and 9 in o and 13 in o) or (
                        2 in o and 6 in o and 10 in o and 14 in o) \
                        or (3 in o and 7 in o and 11 in o and 15 in o) or \
                        (4 in o and 8 in o and 12 in o and 16 in o) \
                        or (1 in o and 6 in o and 11 in o and 16 in o) or \
                        (4 in o and 7 in o and 10 in o and 13 in o):
                    win_label = Label(x_o, text='o_o', bg="blue", font=('arial', 28, 'bold'))
                    win_label.place(x=165, y=150)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=55, y=250)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=200, y=250)
                    x = []
                    o = []
                elif len(x) + len(o) == 16:
                    win_label = Label(x_o, text='^_^', bg="#400040", font=('arial', 28, 'bold'))
                    win_label.place(x=165, y=150)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=55, y=250)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=200, y=250)
                    x = []
                    o = []
                else:
                    player.set('player 1')
                    player_label.configure(fg='red')
        elif ga.get() == '5x5' and win.get() == '4':
            if player.get() == 'player 1':
                if (1 in x and 2 in x and 3 in x and 4 in x) or (2 in x and 3 in x and 4 in x and 5 in x) or \
                        (6 in x and 7 in x and 8 in x and 9 in x) or (7 in x and 8 in x and 9 in x and 10 in x) or \
                        (11 in x and 12 in x and 13 in x and 14 in x) or (12 in x and 13 in x and 14 in x and 15 in x) or \
                        (16 in x and 17 in x and 18 in x and 19 in x) or (17 in x and 18 in x and 19 in x and 20 in x) or \
                        (21 in x and 22 in x and 23 in x and 24 in x) or (22 in x and 23 in x and 24 in x and 25 in x) or \
                        (1 in x and 6 in x and 11 in x and 16 in x) or (6 in x and 11 in x and 16 in x and 21 in x) or \
                        (2 in x and 7 in x and 12 in x and 17 in x) or (7 in x and 12 in x and 17 in x and 22 in x) or \
                        (3 in x and 8 in x and 13 in x and 18 in x) or (8 in x and 13 in x and 18 in x and 23 in x) or \
                        (4 in x and 9 in x and 14 in x and 19 in x) or (9 in x and 14 in x and 19 in x and 24 in x) or \
                        (5 in x and 10 in x and 15 in x and 20 in x) or (10 in x and 15 in x and 20 in x and 25 in x) or \
                        (2 in x and 8 in x and 14 in x and 20 in x) or (6 in x and 12 in x and 18 in x and 24 in x) or \
                        (1 in x and 7 in x and 13 in x and 19 in x) or (7 in x and 13 in x and 19 in x and 25 in x) or \
                        (4 in x and 8 in x and 12 in x and 16 in x) or (10 in x and 14 in x and 18 in x and 22 in x) or \
                        (5 in x and 9 in x and 13 in x and 17 in x) or (9 in x and 13 in x and 17 in x and 21 in x) :
                    win_label = Label(x_o, text='x_x', bg="red", font=('arial', 28, 'bold'))
                    win_label.place(x=215, y=200)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=105, y=300)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=250, y=300)
                    x = []
                    o = []
                elif len(x) + len(o) == 25:
                    win_label = Label(x_o, text='^_^', bg="#400040", font=('arial', 28, 'bold'))
                    win_label.place(x=215, y=200)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=105, y=300)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=250, y=300)
                    x = []
                    o = []
                else:
                    player.set('player 2')
                    player_label.configure(fg='blue')
            elif player.get() == 'player 2':
                if (1 in o and 2 in o and 3 in o and 4 in o) or (2 in o and 3 in o and 4 in o and 5 in o) or \
                        (6 in o and 7 in o and 8 in o and 9 in o) or (7 in o and 8 in o and 9 in o and 10 in o) or \
                        (11 in o and 12 in o and 13 in o and 14 in o) or (
                        12 in o and 13 in o and 14 in o and 15 in o) or \
                        (16 in o and 17 in o and 18 in o and 19 in o) or (
                        17 in o and 18 in o and 19 in o and 20 in o) or \
                        (21 in o and 22 in o and 23 in o and 24 in o) or (
                        22 in o and 23 in o and 24 in o and 25 in o) or \
                        (1 in o and 6 in o and 11 in o and 16 in o) or (6 in o and 11 in o and 16 in o and 21 in o) or \
                        (2 in o and 7 in o and 12 in o and 17 in o) or (7 in o and 12 in o and 17 in o and 22 in o) or \
                        (3 in o and 8 in o and 13 in o and 18 in o) or (8 in o and 13 in o and 18 in o and 23 in o) or \
                        (4 in o and 9 in o and 14 in o and 19 in o) or (9 in o and 14 in o and 19 in o and 24 in o) or \
                        (5 in o and 10 in o and 15 in o and 20 in o) or (10 in o and 15 in o and 20 in o and 25 in o) or \
                        (2 in o and 8 in o and 14 in o and 20 in o) or (6 in o and 12 in o and 18 in o and 24 in o) or \
                        (1 in o and 7 in o and 13 in o and 19 in o) or (7 in o and 13 in o and 19 in o and 25 in o) or \
                        (4 in o and 8 in o and 12 in o and 16 in o) or (10 in o and 14 in o and 18 in o and 22 in o) or \
                        (5 in o and 9 in o and 13 in o and 17 in o) or (9 in o and 13 in o and 17 in o and 21 in o):
                    win_label = Label(x_o, text='o_o', bg="blue", font=('arial', 28, 'bold'))
                    win_label.place(x=215, y=200)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=105, y=300)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=250, y=300)
                    x = []
                    o = []
                elif len(x) + len(o) == 25:
                    win_label = Label(x_o, text='^_^', bg="#400040", font=('arial', 28, 'bold'))
                    win_label.place(x=215, y=200)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=105, y=300)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=250, y=300)
                    x = []
                    o = []
                else:
                    player.set('player 1')
                    player_label.configure(fg='red')
        elif ga.get() == '5x5' and win.get() == '5':
            if player.get() == 'player 1':
                if (1 in x and 2 in x and 3 in x and 4 in x and 5 in x) or \
                        (6 in x and 7 in x and 8 in x and 9 in x and 10 in x) \
                        or (11 in x and 12 in x and 13 in x and 14 in x and 15 in x) \
                        or (16 in x and 17 in x and 18 in x and 19 in x and 20 in x) \
                        or (21 in x and 22 in x and 23 in x and 24 in x and 25 in x) or \
                        (1 in x and 6 in x and 11 in x and 16 in x and 21 in x) or \
                        (2 in x and 7 in x and 12 in x and 17 in x and 22 in x) \
                        or (3 in x and 8 in x and 13 in x and 18 in x and 23 in x) \
                        or (4 in x and 9 in x and 14 in x and 19 in x and 24 in x) \
                        or (5 in x and 10 in x and 15 in x and 20 in x and 25 in x) \
                        or (1 in x and 7 in x and 13 in x and 19 in x and 25 in x) \
                        or (5 in x and 9 in x and 13 in x and 17 in x and 21 in x):
                    win_label = Label(x_o, text='x_x', bg="red", font=('arial', 28, 'bold'))
                    win_label.place(x=215, y=200)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=105, y=300)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=250, y=300)
                    x = []
                    o = []
                elif len(x) + len(o) == 25:
                    win_label = Label(x_o, text='^_^', bg="#400040", font=('arial', 28, 'bold'))
                    win_label.place(x=215, y=200)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=105, y=300)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=250, y=300)
                    x = []
                    o = []
                else:
                    player.set('player 2')
                    player_label.configure(fg='blue')
            elif player.get() == 'player 2':
                if (1 in o and 2 in o and 3 in o and 4 in o and o in o) or \
                        (6 in o and 7 in o and 8 in o and 9 in o and 10 in o) \
                        or (11 in o and 12 in o and 13 in o and 14 in o and 15 in o) \
                        or (16 in o and 17 in o and 18 in o and 19 in o and 20 in o) \
                        or (21 in o and 22 in o and 23 in o and 24 in o and 25 in o) or \
                        (1 in o and 6 in o and 11 in o and 16 in o and 21 in o) or \
                        (2 in o and 7 in o and 12 in o and 17 in o and 22 in o) \
                        or (3 in o and 8 in o and 13 in o and 18 in o and 23 in o) \
                        or (4 in o and 9 in o and 14 in o and 19 in o and 24 in o) \
                        or (5 in o and 10 in o and 15 in o and 20 in o and 25 in o) \
                        or (1 in o and 7 in o and 13 in o and 19 in o and 25 in o) \
                        or (5 in o and 9 in o and 13 in o and 17 in o and 21 in o):
                    win_label = Label(x_o, text='o_o', bg="blue", font=('arial', 28, 'bold'))
                    win_label.place(x=215, y=200)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=105, y=300)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=250, y=300)
                    x = []
                    o = []
                elif len(x) + len(o) == 25:
                    win_label = Label(x_o, text='^_^', bg="#400040", font=('arial', 28, 'bold'))
                    win_label.place(x=215, y=200)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=105, y=300)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=250, y=300)
                    x = []
                    o = []
                else:
                    player.set('player 1')
                    player_label.configure(fg='red')
        elif ga.get() == '6x6' and win.get() == '4':
            if player.get() == 'player 1':
                if (1 in x and 2 in x and 3 in x and 4 in x)\
                        or (2 in x and 3 in x and 4 in x and 5 in x)\
                        or (3 in x and 4 in x and 5 in x and 6 in x)\
                        or (7 in x and 8 in x and 9 in x and 10 in x)\
                        or (8 in x and 9 in x and 10 in x and 11 in x)\
                        or (9 in x and 10 in x and 11 in x and 12 in x)\
                        or (13 in x and 14 in x and 15 in x and 16 in x)\
                        or (14 in x and 15 in x and 16 in x and 17 in x)\
                        or (15 in x and 16 in x and 17 in x and 18 in x)\
                        or (19 in x and 20 in x and 21 in x and 22 in x)\
                        or (20 in x and 21 in x and 22 in x and 23 in x)\
                        or (21 in x and 22 in x and 23 in x and 24 in x)\
                        or (25 in x and 26 in x and 27 in x and 28 in x)\
                        or (26 in x and 27 in x and 28 in x and 29 in x)\
                        or (27 in x and 28 in x and 29 in x and 30 in x)\
                        or (31 in x and 32 in x and 33 in x and 34 in x)\
                        or (32 in x and 33 in x and 34 in x and 35 in x)\
                        or (33 in x and 34 in x and 35 in x and 36 in x)\
                        or (1 in x and 7 in x and 13 in x and 19 in x)\
                        or (7 in x and 13 in x and 19 in x and 25 in x)\
                        or (13 in x and 19 in x and 25 in x and 31 in x)\
                        or (2 in x and 8 in x and 14 in x and 20 in x)\
                        or (8 in x and 14 in x and 20 in x and 26 in x)\
                        or (14 in x and 20 in x and 26 in x and 32 in x)\
                        or (3 in x and 9 in x and 15 in x and 21 in x)\
                        or (9 in x and 15 in x and 21 in x and 27 in x)\
                        or (15 in x and 21 in x and 27 in x and 33 in x)\
                        or (4 in x and 10 in x and 16 in x and 22 in x) \
                        or (10 in x and 16 in x and 22 in x and 28 in x)\
                        or (16 in x and 22 in x and 28 in x and 34 in x)\
                        or (5 in x and 11 in x and 17 in x and 23 in x)\
                        or (11 in x and 17 in x and 23 in x and 29 in x)\
                        or (17 in x and 23 in x and 29 in x and 35 in x)\
                        or (6 in x and 12 in x and 18 in x and 24 in x)\
                        or (12 in x and 18 in x and 24 in x and 30 in x)\
                        or (18 in x and 24 in x and 30 in x and 36 in x)\
                        or (3 in x and 10 in x and 17 in x and 24 in x)\
                        or (13 in x and 20 in x and 27 in x and 34 in x)\
                        or (2 in x and 9 in x and 16 in x and 23 in x)\
                        or (9 in x and 16 in x and 23 in x and 30 in x)\
                        or (7 in x and 14 in x and 21 in x and 28 in x)\
                        or (14 in x and 21 in x and 28 in x and 35 in x)\
                        or (1 in x and 8 in x and 15 in x and 22 in x)\
                        or (8 in x and 15 in x and 22 in x and 29 in x)\
                        or (15 in x and 22 in x and 29 in x and 36 in x)\
                        or (4 in x and 9 in x and 14 in x and 19 in x)\
                        or (18 in x and 23 in x and 28 in x and 33 in x)\
                        or (5 in x and 10 in x and 15 in x and 20 in x)\
                        or (10 in x and 15 in x and 20 in x and 25 in x)\
                        or (12 in x and 17 in x and 22 in x and 27 in x)\
                        or (17 in x and 22 in x and 27 in x and 32 in x)\
                        or (6 in x and 11 in x and 16 in x and 21 in x)\
                        or (11 in x and 16 in x and 21 in x and 26 in x)\
                        or (16 in x and 21 in x and 26 in x and 31 in x):
                    win_label = Label(x_o, text='x_x', bg="red", font=('arial', 28, 'bold'))
                    win_label.place(x=265, y=250)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=155, y=350)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=300, y=350)
                    x = []
                    o = []
                elif len(x) + len(o) == 36:
                    win_label = Label(x_o, text='^_^', bg="#400040", font=('arial', 28, 'bold'))
                    win_label.place(x=265, y=250)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=155, y=350)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=300, y=350)
                    x = []
                    o = []
                else:
                    player.set('player 2')
                    player_label.configure(fg='blue')
            elif player.get() == 'player 2':
                if (1 in o and 2 in o and 3 in o and 4 in o) \
                        or (2 in o and 3 in o and 4 in o and 5 in o) \
                        or (3 in o and 4 in o and 5 in o and 6 in o) \
                        or (7 in o and 8 in o and 9 in o and 10 in o) \
                        or (8 in o and 9 in o and 10 in o and 11 in o) \
                        or (9 in o and 10 in o and 11 in o and 12 in o) \
                        or (13 in o and 14 in o and 15 in o and 16 in o) \
                        or (14 in o and 15 in o and 16 in o and 17 in o) \
                        or (15 in o and 16 in o and 17 in o and 18 in o) \
                        or (19 in o and 20 in o and 21 in o and 22 in o) \
                        or (20 in o and 21 in o and 22 in o and 23 in o) \
                        or (21 in o and 22 in o and 23 in o and 24 in o) \
                        or (25 in o and 26 in o and 27 in o and 28 in o) \
                        or (26 in o and 27 in o and 28 in o and 29 in o) \
                        or (27 in o and 28 in o and 29 in o and 30 in o) \
                        or (31 in o and 32 in o and 33 in o and 34 in o) \
                        or (32 in o and 33 in o and 34 in o and 35 in o) \
                        or (33 in o and 34 in o and 35 in o and 36 in o) \
                        or (1 in o and 7 in o and 13 in o and 19 in o) \
                        or (7 in o and 13 in o and 19 in o and 25 in o) \
                        or (13 in o and 19 in o and 25 in o and 31 in o) \
                        or (2 in o and 8 in o and 14 in o and 20 in o) \
                        or (8 in o and 14 in o and 20 in o and 26 in o) \
                        or (14 in o and 20 in o and 26 in o and 32 in o) \
                        or (3 in o and 9 in o and 15 in o and 21 in o) \
                        or (9 in o and 15 in o and 21 in o and 27 in o) \
                        or (15 in o and 21 in o and 27 in o and 33 in o) \
                        or (4 in o and 10 in o and 16 in o and 22 in o) \
                        or (10 in o and 16 in o and 22 in o and 28 in o) \
                        or (16 in o and 22 in o and 28 in o and 34 in o) \
                        or (5 in o and 11 in o and 17 in o and 23 in o) \
                        or (11 in o and 17 in o and 23 in o and 29 in o) \
                        or (17 in o and 23 in o and 29 in o and 35 in o) \
                        or (6 in o and 12 in o and 18 in o and 24 in o) \
                        or (12 in o and 18 in o and 24 in o and 30 in o) \
                        or (18 in o and 24 in o and 30 in o and 36 in o) \
                        or (3 in o and 10 in o and 17 in o and 24 in o) \
                        or (13 in o and 20 in o and 27 in o and 34 in o) \
                        or (2 in o and 9 in o and 16 in o and 23 in o) \
                        or (9 in o and 16 in o and 23 in o and 30 in o) \
                        or (7 in o and 14 in o and 21 in o and 28 in o) \
                        or (14 in o and 21 in o and 28 in o and 35 in o) \
                        or (1 in o and 8 in o and 15 in o and 22 in o) \
                        or (8 in o and 15 in o and 22 in o and 29 in o) \
                        or (15 in o and 22 in o and 29 in o and 36 in o) \
                        or (4 in o and 9 in o and 14 in o and 19 in o) \
                        or (18 in o and 23 in o and 28 in o and 33 in o) \
                        or (5 in o and 10 in o and 15 in o and 20 in o) \
                        or (10 in o and 15 in o and 20 in o and 25 in o) \
                        or (12 in o and 17 in o and 22 in o and 27 in o) \
                        or (17 in o and 22 in o and 27 in o and 32 in o) \
                        or (6 in o and 11 in o and 16 in o and 21 in o) \
                        or (11 in o and 16 in o and 21 in o and 26 in o) \
                        or (16 in o and 21 in o and 26 in o and 31 in o):
                    win_label = Label(x_o, text='o_o', bg="blue", font=('arial', 28, 'bold'))
                    win_label.place(x=265, y=250)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=155, y=350)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=300, y=350)
                    x = []
                    o = []
                elif len(x) + len(o) == 36:
                    win_label = Label(x_o, text='^_^', bg="#400040", font=('arial', 28, 'bold'))
                    win_label.place(x=265, y=250)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=155, y=350)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=300, y=350)
                    x = []
                    o = []
                else:
                    player.set('player 1')
                    player_label.configure(fg='red')
        elif ga.get() == '6x6' and win.get() == '5':
            if player.get() == 'player 1':
                if (1 in x and 2 in x and 3 in x and 4 in x and 5 in x)\
                        or (2 in x and 3 in x and 4 in x and 5 in x and 6 in x) \
                        or (7 in x and 8 in x and 9 in x and 10 in x and 11 in x) \
                        or (8 in x and 9 in x and 10 in x and 11 in x and 12 in x) \
                        or (13 in x and 14 in x and 15 in x and 16 in x and 17 in x)\
                        or (14 in x and 15 in x and 16 in x and 17 in x and 18 in x)\
                        or (19 in x and 20 in x and 21 in x and 22 in x and 23 in x) \
                        or (20 in x and 21 in x and 22 in x and 23 in x and 24 in x) \
                        or (25 in x and 26 in x and 27 in x and 28 in x and 29 in x) \
                        or (26 in x and 27 in x and 28 in x and 29 in x and 30 in x) \
                        or (31 in x and 32 in x and 33 in x and 34 in x and 35 in x) \
                        or (32 in x and 33 in x and 34 in x and 35 in x and 36 in x) \
                        or (1 in x and 7 in x and 13 in x and 19 in x and 25 in x) \
                        or (7 in x and 13 in x and 19 in x and 25 in x and 31 in x) \
                        or (2 in x and 8 in x and 14 in x and 20 in x and 26 in x) \
                        or (8 in x and 14 in x and 20 in x and 26 in x and 32 in x)\
                        or (3 in x and 9 in x and 15 in x and 21 in x and 27 in x) \
                        or (9 in x and 15 in x and 21 in x and 27 in x and 33 in x) \
                        or (4 in x and 10 in x and 16 in x and 22 in x and 28 in x) \
                        or (10 in x and 16 in x and 22 in x and 28 in x and 34 in x) \
                        or (5 in x and 11 in x and 17 in x and 23 in x and 29 in x) \
                        or (11 in x and 17 in x and 23 in x and 29 in x and 35 in x) \
                        or (6 in x and 12 in x and 18 in x and 24 in x and 30 in x) \
                        or (11 in x and 18 in x and 24 in x and 30 in x and 36 in x) \
                        or (2 in x and 9 in x and 16 in x and 23 in x and 30 in x) \
                        or (7 in x and 14 in x and 21 in x and 28 in x and 35 in x) \
                        or (1 in x and 8 in x and 15 in x and 22 in x and 29 in x) \
                        or (8 in x and 15 in x and 22 in x and 29 in x and 36 in x) \
                        or (5 in x and 10 in x and 15 in x and 20 in x and 25 in x) \
                        or (12 in x and 17 in x and 22 in x and 27 in x and 32 in x) \
                        or (6 in x and 11 in x and 16 in x and 21 in x and 26 in x) \
                        or (11 in x and 16 in x and 21 in x and 26 in x and 31 in x) :
                    win_label = Label(x_o, text='x_x', bg="red", font=('arial', 28, 'bold'))
                    win_label.place(x=265, y=250)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=155, y=350)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=300, y=350)
                    x = []
                    o = []
                elif len(x) + len(o) == 36:
                    win_label = Label(x_o, text='^_^', bg="#400040", font=('arial', 28, 'bold'))
                    win_label.place(x=265, y=250)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=155, y=350)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=300, y=350)
                    x = []
                    o = []
                else:
                    player.set('player 2')
                    player_label.configure(fg='blue')
            elif player.get() == 'player 2':
                if (1 in o and 2 in o and 3 in o and 4 in o and 5 in o) \
                        or (2 in o and 3 in o and 4 in o and 5 in o and 6 in o) \
                        or (7 in o and 8 in o and 9 in o and 10 in o and 11 in o) \
                        or (8 in o and 9 in o and 10 in o and 11 in o and 12 in o) \
                        or (13 in o and 14 in o and 15 in o and 16 in o and 17 in o) \
                        or (14 in o and 15 in o and 16 in o and 17 in o and 18 in o) \
                        or (19 in o and 20 in o and 21 in o and 22 in o and 23 in o) \
                        or (20 in o and 21 in o and 22 in o and 23 in o and 24 in o) \
                        or (25 in o and 26 in o and 27 in o and 28 in o and 29 in o) \
                        or (26 in o and 27 in o and 28 in o and 29 in o and 30 in o) \
                        or (31 in o and 32 in o and 33 in o and 34 in o and 35 in o) \
                        or (32 in o and 33 in o and 34 in o and 35 in o and 36 in o) \
                        or (1 in o and 7 in o and 13 in o and 19 in o and 25 in o) \
                        or (7 in o and 13 in o and 19 in o and 25 in o and 31 in o) \
                        or (2 in o and 8 in o and 14 in o and 20 in o and 26 in o) \
                        or (8 in o and 14 in o and 20 in o and 26 in o and 32 in o) \
                        or (3 in o and 9 in o and 15 in o and 21 in o and 27 in o) \
                        or (9 in o and 15 in o and 21 in o and 27 in o and 33 in o) \
                        or (4 in o and 10 in o and 16 in o and 22 in o and 28 in o) \
                        or (10 in o and 16 in o and 22 in o and 28 in o and 34 in o) \
                        or (5 in o and 11 in o and 17 in o and 23 in o and 29 in o) \
                        or (11 in o and 17 in o and 23 in o and 29 in o and 35 in o) \
                        or (6 in o and 12 in o and 18 in o and 24 in o and 30 in o) \
                        or (11 in o and 18 in o and 24 in o and 30 in o and 36 in o) \
                        or (2 in o and 9 in o and 16 in o and 23 in o and 30 in o) \
                        or (7 in o and 14 in o and 21 in o and 28 in o and 35 in o) \
                        or (1 in o and 8 in o and 15 in o and 22 in o and 29 in o) \
                        or (8 in o and 15 in o and 22 in o and 29 in o and 36 in o) \
                        or (5 in o and 10 in o and 15 in o and 20 in o and 25 in o) \
                        or (12 in o and 17 in o and 22 in o and 27 in o and 32 in o) \
                        or (6 in o and 11 in o and 16 in o and 21 in o and 26 in o) \
                        or (11 in o and 16 in o and 21 in o and 26 in o and 31 in o):
                    win_label = Label(x_o, text='o_o', bg="blue", font=('arial', 28, 'bold'))
                    win_label.place(x=265, y=250)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=155, y=350)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=300, y=350)
                    x = []
                    o = []
                elif len(x) + len(o) == 36:
                    win_label = Label(x_o, text='^_^', bg="#400040", font=('arial', 28, 'bold'))
                    win_label.place(x=265, y=250)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=155, y=350)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=300, y=350)
                    x = []
                    o = []
                else:
                    player.set('player 1')
                    player_label.configure(fg='red')
        elif ga.get() == '6x6' and win.get() == '6':
            if player.get() == 'player 1':
                if (1 in x and 2 in x and 3 in x and 4 in x and 5 in x and 6 in x) \
                        or (7 in x and 8 in x and 9 in x and 10 in x and 11 in x and 12 in x) \
                        or (13 in x and 14 in x and 15 in x and 16 in x and 17 in x and 18 in x) \
                        or (19 in x and 20 in x and 21 in x and 22 in x and 23 in x and 24 in x) \
                        or (25 in x and 26 in x and 27 in x and 28 in x and 28 in x and 30 in x) \
                        or (31 in x and 32 in x and 33 in x and 34 in x and 35 in x and 36 in x) \
                        or (1 in x and 7 in x and 13 in x and 19 in x and 25 in x and 31 in x) \
                        or (2 in x and 8 in x and 14 in x and 20 in x and 26 in x and 32 in x) \
                        or (3 in x and 9 in x and 15 in x and 21 in x and 27 in x and 33 in x) \
                        or (4 in x and 10 in x and 16 in x and 22 in x and 28 in x and 34 in x) \
                        or (5 in x and 11 in x and 17 in x and 23 in x and 29 in x and 35 in x) \
                        or (6 in x and 12 in x and 18 in x and 24 in x and 30 in x and 36 in x) \
                        or (1 in x and 8 in x and 15 in x and 22 in x and 29 in x and 36 in x) \
                        or (6 in x and 11 in x and 16 in x and 21 in x and 26 in x and 31 in x):
                    win_label = Label(x_o, text='x_x', bg="red", font=('arial', 28, 'bold'))
                    win_label.place(x=265, y=250)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=155, y=350)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=300, y=350)
                    x = []
                    o = []
                elif len(x) + len(o) == 36:
                    win_label = Label(x_o, text='^_^', bg="#400040", font=('arial', 28, 'bold'))
                    win_label.place(x=265, y=250)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=155, y=350)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=300, y=350)
                    x = []
                    o = []
                else:
                    player.set('player 2')
                    player_label.configure(fg='blue')
            elif player.get() == 'player 2':
                if (1 in o and 2 in o and 3 in o and 4 in o and 5 in o and 6 in o) \
                        or (7 in o and 8 in o and 9 in o and 10 in o and 11 in o and 12 in o) \
                        or (13 in o and 14 in o and 15 in o and 16 in o and 17 in o and 18 in o) \
                        or (19 in o and 20 in o and 21 in o and 22 in o and 23 in o and 24 in o) \
                        or (25 in o and 26 in o and 27 in o and 28 in o and 28 in o and 30 in o) \
                        or (31 in o and 32 in o and 33 in o and 34 in o and 35 in o and 36 in o) \
                        or (1 in o and 7 in o and 13 in o and 19 in o and 25 in o and 31 in o) \
                        or (2 in o and 8 in o and 14 in o and 20 in o and 26 in o and 32 in o) \
                        or (3 in o and 9 in o and 15 in o and 21 in o and 27 in o and 33 in o) \
                        or (4 in o and 10 in o and 16 in o and 22 in o and 28 in o and 34 in o) \
                        or (5 in o and 11 in o and 17 in o and 23 in o and 29 in o and 35 in o) \
                        or (6 in o and 12 in o and 18 in o and 24 in o and 30 in o and 36 in o) \
                        or (1 in o and 8 in o and 15 in o and 22 in o and 29 in o and 36 in o) \
                        or (6 in o and 11 in o and 16 in o and 21 in o and 26 in o and 31 in o):
                    win_label = Label(x_o, text='o_o', bg="red", font=('arial', 28, 'bold'))
                    win_label.place(x=265, y=250)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=155, y=350)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=300, y=350)
                    x = []
                    o = []
                elif len(x) + len(o) == 36:
                    win_label = Label(x_o, text='^_^', bg="#400040", font=('arial', 28, 'bold'))
                    win_label.place(x=265, y=250)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=155, y=350)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=300, y=350)
                    x = []
                    o = []
                else:
                    player.set('player 1')
                    player_label.configure(fg='red')

    elif runing == 'vs_cpu':
        if   ga.get() == '3x3' and win.get() == '3':
            if player.get() == 'player 1':
                if (1 in x and 2 in x and 3 in x) or (4 in x and 5 in x and 6 in x) or \
                        (7 in x and 8 in x and 9 in x) or (1 in x and 4 in x and 7 in x) or \
                        (2 in x and 5 in x and 8 in x) or (3 in x and 6 in x and 9 in x) or \
                        (1 in x and 5 in x and 9 in x) or (3 in x and 5 in x and 7 in x):
                    win_label = Label(x_o, text='x_x', bg="red", font=('arial', 28, 'bold'))
                    win_label.place(x=115, y=100)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=5, y=200)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=150, y=200)
                    x = []
                    o = []
                elif len(x) + len(o) == 9:
                    win_label = Label(x_o, text='^_^', bg="#400040", font=('arial', 28, 'bold'))
                    win_label.place(x=115, y=100)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=5, y=200)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=150, y=200)
                    x = []
                    o = []
                else:
                    player.set('cpu')
                    player_label.configure(fg='blue')
                    cpu_play()
            elif player.get() == 'cpu':
                if (1 in o and 2 in o and 3 in o) or (4 in o and 5 in o and 6 in o) or \
                        (7 in o and 8 in o and 9 in o) or (1 in o and 4 in o and 7 in o) or \
                        (2 in o and 5 in o and 8 in o) or (3 in o and 6 in o and 9 in o) or \
                        (1 in o and 5 in o and 9 in o) or (3 in o and 5 in o and 7 in o):
                    win_label = Label(x_o, text='o_o', bg="blue", font=('arial', 28, 'bold'))
                    win_label.place(x=115, y=100)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=5, y=200)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=150, y=200)
                    x = []
                    o = []
                elif len(x) + len(o) == 9:
                    win_label = Label(x_o, text='^_^', bg="#400040", font=('arial', 28, 'bold'))
                    win_label.place(x=115, y=100)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=5, y=200)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=150, y=200)
                    x = []
                    o = []
                else:
                    player.set('player 1')
                    player_label.configure(fg='red')
        elif ga.get() == '4x4' and win.get() == '3':
            if player.get() == 'player 1':
                if (1 in x and 2 in x and 3 in x) or (2 in x and 3 in x and 4 in x) or \
                        (5 in x and 6 in x and 7 in x) or (6 in x and 7 in x and 8 in x) or \
                        (9 in x and 10 in x and 11 in x) or (10 in x and 11 in x and 12 in x) or \
                        (13 in x and 14 in x and 15 in x) or (14 in x and 15 in x and 16 in x) or \
                        (1 in x and 5 in x and 9 in x) or (5 in x and 9 in x and 13 in x) or \
                        (2 in x and 6 in x and 10 in x) or (6 in x and 10 in x and 14 in x) or \
                        (3 in x and 7 in x and 11 in x) or (7 in x and 11 in x and 15 in x) or \
                        (4 in x and 8 in x and 12 in x) or (8 in x and 12 in x and 16 in x) or \
                        (3 in x and 6 in x and 9 in x) or (4 in x and 7 in x and 10 in x) or \
                        (1 in x and 6 in x and 11 in x) or (6 in x and 11 in x and 16 in x) or \
                        (7 in x and 10 in x and 13 in x) or (8 in x and 11 in x and 14 in x) or \
                        (5 in x and 10 in x and 15 in x) or (2 in x and 7 in x and 12 in x):
                    win_label = Label(x_o, text='x_x', bg="red", font=('arial', 28, 'bold'))
                    win_label.place(x=165, y=150)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=55, y=250)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=200, y=250)
                    x = []
                    o = []
                elif len(x) + len(o) == 16:
                    win_label = Label(x_o, text='^_^', bg="#400040", font=('arial', 28, 'bold'))
                    win_label.place(x=165, y=150)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=55, y=250)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=200, y=250)
                    x = []
                    o = []
                else:
                    player.set('cpu')
                    player_label.configure(fg='blue')
                    cpu_play()
            elif player.get() == 'cpu':
                if (1 in o and 2 in o and 3 in o) or (2 in o and 3 in o and 4 in o) or \
                        (5 in o and 6 in o and 7 in o) or (6 in o and 7 in o and 8 in o) or \
                        (9 in o and 10 in o and 11 in o) or (10 in o and 11 in o and 12 in o) or \
                        (13 in o and 14 in o and 15 in o) or (14 in o and 15 in o and 16 in o) or \
                        (1 in o and 5 in o and 9 in o) or (5 in o and 9 in o and 13 in o) or \
                        (2 in o and 6 in o and 10 in o) or (6 in o and 10 in o and 14 in o) or \
                        (3 in o and 7 in o and 11 in o) or (7 in o and 11 in o and 15 in o) or \
                        (4 in o and 8 in o and 12 in o) or (8 in o and 12 in o and 16 in o) or \
                        (3 in o and 6 in o and 9 in o) or (4 in o and 7 in o and 10 in o) or \
                        (1 in o and 6 in o and 11 in o) or (6 in o and 11 in o and 16 in o) or \
                        (7 in o and 10 in o and 13 in o) or (8 in o and 11 in o and 14 in o) or \
                        (5 in o and 10 in o and 15 in o) or (2 in o and 7 in o and 12 in o):
                    win_label = Label(x_o, text='o_o', bg="blue", font=('arial', 28, 'bold'))
                    win_label.place(x=165, y=150)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=55, y=250)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=200, y=250)
                    x = []
                    o = []
                elif len(x) + len(o) == 16:
                    win_label = Label(x_o, text='^_^', bg="#400040", font=('arial', 28, 'bold'))
                    win_label.place(x=165, y=150)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=55, y=250)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=200, y=250)
                    x = []
                    o = []
                else:
                    player.set('player 1')
                    player_label.configure(fg='red')
        elif ga.get() == '4x4' and win.get() == '4':
            if player.get() == 'player 1':
                if (1 in x and 2 in x and 3 in x and 4 in x) or \
                        (5 in x and 6 in x and 7 in x and 8 in x) \
                        or (9 in x and 10 in x and 11 in x and 12 in x) or \
                        (13 in x and 14 in x and 15 in x and 16 in x) \
                        or (1 in x and 5 in x and 9 in x and 13 in x) or (
                        2 in x and 6 in x and 10 in x and 14 in x) \
                        or (3 in x and 7 in x and 11 in x and 15 in x) or \
                        (4 in x and 8 in x and 12 in x and 16 in x) \
                        or (1 in x and 6 in x and 11 in x and 16 in x) or \
                        (4 in x and 7 in x and 10 in x and 13 in x):
                    win_label = Label(x_o, text='x_x', bg="red", font=('arial', 28, 'bold'))
                    win_label.place(x=165, y=150)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=55, y=250)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=200, y=250)
                    x = []
                    o = []
                elif len(x) + len(o) == 16:
                    win_label = Label(x_o, text='^_^', bg="#400040", font=('arial', 28, 'bold'))
                    win_label.place(x=165, y=150)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=55, y=250)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=200, y=250)
                    x = []
                    o = []
                else:
                    player.set('cpu')
                    player_label.configure(fg='blue')
                    cpu_play()
            elif player.get() == 'cpu':
                if (1 in o and 2 in o and 3 in o and 4 in o) or \
                        (5 in o and 6 in o and 7 in o and 8 in o) \
                        or (9 in o and 10 in o and 11 in o and 12 in o) or \
                        (13 in o and 14 in o and 15 in o and 16 in o) \
                        or (1 in o and 5 in o and 9 in o and 13 in o) or (
                        2 in o and 6 in o and 10 in o and 14 in o) \
                        or (3 in o and 7 in o and 11 in o and 15 in o) or \
                        (4 in o and 8 in o and 12 in o and 16 in o) \
                        or (1 in o and 6 in o and 11 in o and 16 in o) or \
                        (4 in o and 7 in o and 10 in o and 13 in o):
                    win_label = Label(x_o, text='o_o', bg="blue", font=('arial', 28, 'bold'))
                    win_label.place(x=165, y=150)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=55, y=250)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=200, y=250)
                    x = []
                    o = []
                elif len(x) + len(o) == 16:
                    win_label = Label(x_o, text='^_^', bg="#400040", font=('arial', 28, 'bold'))
                    win_label.place(x=165, y=150)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=55, y=250)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=200, y=250)
                    x = []
                    o = []
                else:
                    player.set('player 1')
                    player_label.configure(fg='red')
        elif ga.get() == '5x5' and win.get() == '4':
            if player.get() == 'player 1':
                if (1 in x and 2 in x and 3 in x and 4 in x) or (2 in x and 3 in x and 4 in x and 5 in x) or \
                        (6 in x and 7 in x and 8 in x and 9 in x) or (7 in x and 8 in x and 9 in x and 10 in x) or \
                        (11 in x and 12 in x and 13 in x and 14 in x) or (12 in x and 13 in x and 14 in x and 15 in x) or \
                        (16 in x and 17 in x and 18 in x and 19 in x) or (17 in x and 18 in x and 19 in x and 20 in x) or \
                        (21 in x and 22 in x and 23 in x and 24 in x) or (22 in x and 23 in x and 24 in x and 25 in x) or \
                        (1 in x and 6 in x and 11 in x and 16 in x) or (6 in x and 11 in x and 16 in x and 21 in x) or \
                        (2 in x and 7 in x and 12 in x and 17 in x) or (7 in x and 12 in x and 17 in x and 22 in x) or \
                        (3 in x and 8 in x and 13 in x and 18 in x) or (8 in x and 13 in x and 18 in x and 23 in x) or \
                        (4 in x and 9 in x and 14 in x and 19 in x) or (9 in x and 14 in x and 19 in x and 24 in x) or \
                        (5 in x and 10 in x and 15 in x and 20 in x) or (10 in x and 15 in x and 20 in x and 25 in x) or \
                        (2 in x and 8 in x and 14 in x and 20 in x) or (6 in x and 12 in x and 18 in x and 24 in x) or \
                        (1 in x and 7 in x and 13 in x and 19 in x) or (7 in x and 13 in x and 19 in x and 25 in x) or \
                        (4 in x and 8 in x and 12 in x and 16 in x) or (10 in x and 14 in x and 18 in x and 22 in x) or \
                        (5 in x and 9 in x and 13 in x and 17 in x) or (9 in x and 13 in x and 17 in x and 21 in x) :
                    win_label = Label(x_o, text='x_x', bg="red", font=('arial', 28, 'bold'))
                    win_label.place(x=215, y=200)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=105, y=300)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=250, y=300)
                    x = []
                    o = []
                elif len(x) + len(o) == 25:
                    win_label = Label(x_o, text='^_^', bg="#400040", font=('arial', 28, 'bold'))
                    win_label.place(x=215, y=200)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=105, y=300)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=250, y=300)
                    x = []
                    o = []
                else:
                    player.set('cpu')
                    player_label.configure(fg='blue')
                    cpu_play()
            elif player.get() == 'cpu':
                if (1 in o and 2 in o and 3 in o and 4 in o) or (2 in o and 3 in o and 4 in o and 5 in o) or \
                        (6 in o and 7 in o and 8 in o and 9 in o) or (7 in o and 8 in o and 9 in o and 10 in o) or \
                        (11 in o and 12 in o and 13 in o and 14 in o) or (
                        12 in o and 13 in o and 14 in o and 15 in o) or \
                        (16 in o and 17 in o and 18 in o and 19 in o) or (
                        17 in o and 18 in o and 19 in o and 20 in o) or \
                        (21 in o and 22 in o and 23 in o and 24 in o) or (
                        22 in o and 23 in o and 24 in o and 25 in o) or \
                        (1 in o and 6 in o and 11 in o and 16 in o) or (6 in o and 11 in o and 16 in o and 21 in o) or \
                        (2 in o and 7 in o and 12 in o and 17 in o) or (7 in o and 12 in o and 17 in o and 22 in o) or \
                        (3 in o and 8 in o and 13 in o and 18 in o) or (8 in o and 13 in o and 18 in o and 23 in o) or \
                        (4 in o and 9 in o and 14 in o and 19 in o) or (9 in o and 14 in o and 19 in o and 24 in o) or \
                        (5 in o and 10 in o and 15 in o and 20 in o) or (10 in o and 15 in o and 20 in o and 25 in o) or \
                        (2 in o and 8 in o and 14 in o and 20 in o) or (6 in o and 12 in o and 18 in o and 24 in o) or \
                        (1 in o and 7 in o and 13 in o and 19 in o) or (7 in o and 13 in o and 19 in o and 25 in o) or \
                        (4 in o and 8 in o and 12 in o and 16 in o) or (10 in o and 14 in o and 18 in o and 22 in o) or \
                        (5 in o and 9 in o and 13 in o and 17 in o) or (9 in o and 13 in o and 17 in o and 21 in o):
                    win_label = Label(x_o, text='o_o', bg="blue", font=('arial', 28, 'bold'))
                    win_label.place(x=215, y=200)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=105, y=300)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=250, y=300)
                    x = []
                    o = []
                elif len(x) + len(o) == 25:
                    win_label = Label(x_o, text='^_^', bg="#400040", font=('arial', 28, 'bold'))
                    win_label.place(x=215, y=200)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=105, y=300)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=250, y=300)
                    x = []
                    o = []
                else:
                    player.set('player 1')
                    player_label.configure(fg='red')
        elif ga.get() == '5x5' and win.get() == '5':
            if player.get() == 'player 1':
                if (1 in x and 2 in x and 3 in x and 4 in x and 5 in x) or \
                        (6 in x and 7 in x and 8 in x and 9 in x and 10 in x) \
                        or (11 in x and 12 in x and 13 in x and 14 in x and 15 in x) \
                        or (16 in x and 17 in x and 18 in x and 19 in x and 20 in x) \
                        or (21 in x and 22 in x and 23 in x and 24 in x and 25 in x) or \
                        (1 in x and 6 in x and 11 in x and 16 in x and 21 in x) or \
                        (2 in x and 7 in x and 12 in x and 17 in x and 22 in x) \
                        or (3 in x and 8 in x and 13 in x and 18 in x and 23 in x) \
                        or (4 in x and 9 in x and 14 in x and 19 in x and 24 in x) \
                        or (5 in x and 10 in x and 15 in x and 20 in x and 25 in x) \
                        or (1 in x and 7 in x and 13 in x and 19 in x and 25 in x) \
                        or (5 in x and 9 in x and 13 in x and 17 in x and 21 in x):
                    win_label = Label(x_o, text='x_x', bg="red", font=('arial', 28, 'bold'))
                    win_label.place(x=215, y=200)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=105, y=300)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=250, y=300)
                    x = []
                    o = []
                elif len(x) + len(o) == 25:
                    win_label = Label(x_o, text='^_^', bg="#400040", font=('arial', 28, 'bold'))
                    win_label.place(x=215, y=200)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=105, y=300)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=250, y=300)
                    x = []
                    o = []
                else:
                    player.set('cpu')
                    player_label.configure(fg='blue')
                    cpu_play()
            elif player.get() == 'cpu':
                if (1 in o and 2 in o and 3 in o and 4 in o and o in o) or \
                        (6 in o and 7 in o and 8 in o and 9 in o and 10 in o) \
                        or (11 in o and 12 in o and 13 in o and 14 in o and 15 in o) \
                        or (16 in o and 17 in o and 18 in o and 19 in o and 20 in o) \
                        or (21 in o and 22 in o and 23 in o and 24 in o and 25 in o) or \
                        (1 in o and 6 in o and 11 in o and 16 in o and 21 in o) or \
                        (2 in o and 7 in o and 12 in o and 17 in o and 22 in o) \
                        or (3 in o and 8 in o and 13 in o and 18 in o and 23 in o) \
                        or (4 in o and 9 in o and 14 in o and 19 in o and 24 in o) \
                        or (5 in o and 10 in o and 15 in o and 20 in o and 25 in o) \
                        or (1 in o and 7 in o and 13 in o and 19 in o and 25 in o) \
                        or (5 in o and 9 in o and 13 in o and 17 in o and 21 in o):
                    win_label = Label(x_o, text='o_o', bg="blue", font=('arial', 28, 'bold'))
                    win_label.place(x=215, y=200)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=105, y=300)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=250, y=300)
                    x = []
                    o = []
                elif len(x) + len(o) == 25:
                    win_label = Label(x_o, text='^_^', bg="#400040", font=('arial', 28, 'bold'))
                    win_label.place(x=215, y=200)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=105, y=300)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=250, y=300)
                    x = []
                    o = []
                else:
                    player.set('player 1')
                    player_label.configure(fg='red')
        elif ga.get() == '6x6' and win.get() == '4':
            if player.get() == 'player 1':
                if (1 in x and 2 in x and 3 in x and 4 in x)\
                        or (2 in x and 3 in x and 4 in x and 5 in x)\
                        or (3 in x and 4 in x and 5 in x and 6 in x)\
                        or (7 in x and 8 in x and 9 in x and 10 in x)\
                        or (8 in x and 9 in x and 10 in x and 11 in x)\
                        or (9 in x and 10 in x and 11 in x and 12 in x)\
                        or (13 in x and 14 in x and 15 in x and 16 in x)\
                        or (14 in x and 15 in x and 16 in x and 17 in x)\
                        or (15 in x and 16 in x and 17 in x and 18 in x)\
                        or (19 in x and 20 in x and 21 in x and 22 in x)\
                        or (20 in x and 21 in x and 22 in x and 23 in x)\
                        or (21 in x and 22 in x and 23 in x and 24 in x)\
                        or (25 in x and 26 in x and 27 in x and 28 in x)\
                        or (26 in x and 27 in x and 28 in x and 29 in x)\
                        or (27 in x and 28 in x and 29 in x and 30 in x)\
                        or (31 in x and 32 in x and 33 in x and 34 in x)\
                        or (32 in x and 33 in x and 34 in x and 35 in x)\
                        or (33 in x and 34 in x and 35 in x and 36 in x)\
                        or (1 in x and 7 in x and 13 in x and 19 in x)\
                        or (7 in x and 13 in x and 19 in x and 25 in x)\
                        or (13 in x and 19 in x and 25 in x and 31 in x)\
                        or (2 in x and 8 in x and 14 in x and 20 in x)\
                        or (8 in x and 14 in x and 20 in x and 26 in x)\
                        or (14 in x and 20 in x and 26 in x and 32 in x)\
                        or (3 in x and 9 in x and 15 in x and 21 in x)\
                        or (9 in x and 15 in x and 21 in x and 27 in x)\
                        or (15 in x and 21 in x and 27 in x and 33 in x)\
                        or (4 in x and 10 in x and 16 in x and 22 in x) \
                        or (10 in x and 16 in x and 22 in x and 28 in x)\
                        or (16 in x and 22 in x and 28 in x and 34 in x)\
                        or (5 in x and 11 in x and 17 in x and 23 in x)\
                        or (11 in x and 17 in x and 23 in x and 29 in x)\
                        or (17 in x and 23 in x and 29 in x and 35 in x)\
                        or (6 in x and 12 in x and 18 in x and 24 in x)\
                        or (12 in x and 18 in x and 24 in x and 30 in x)\
                        or (18 in x and 24 in x and 30 in x and 36 in x)\
                        or (3 in x and 10 in x and 17 in x and 24 in x)\
                        or (13 in x and 20 in x and 27 in x and 34 in x)\
                        or (2 in x and 9 in x and 16 in x and 23 in x)\
                        or (9 in x and 16 in x and 23 in x and 30 in x)\
                        or (7 in x and 14 in x and 21 in x and 28 in x)\
                        or (14 in x and 21 in x and 28 in x and 35 in x)\
                        or (1 in x and 8 in x and 15 in x and 22 in x)\
                        or (8 in x and 15 in x and 22 in x and 29 in x)\
                        or (15 in x and 22 in x and 29 in x and 36 in x)\
                        or (4 in x and 9 in x and 14 in x and 19 in x)\
                        or (18 in x and 23 in x and 28 in x and 33 in x)\
                        or (5 in x and 10 in x and 15 in x and 20 in x)\
                        or (10 in x and 15 in x and 20 in x and 25 in x)\
                        or (12 in x and 17 in x and 22 in x and 27 in x)\
                        or (17 in x and 22 in x and 27 in x and 32 in x)\
                        or (6 in x and 11 in x and 16 in x and 21 in x)\
                        or (11 in x and 16 in x and 21 in x and 26 in x)\
                        or (16 in x and 21 in x and 26 in x and 31 in x):
                    win_label = Label(x_o, text='x_x', bg="red", font=('arial', 28, 'bold'))
                    win_label.place(x=265, y=250)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=155, y=350)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=300, y=350)
                    x = []
                    o = []
                elif len(x) + len(o) == 36:
                    win_label = Label(x_o, text='^_^', bg="#400040", font=('arial', 28, 'bold'))
                    win_label.place(x=265, y=250)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=155, y=350)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=300, y=350)
                    x = []
                    o = []
                else:
                    player.set('cpu')
                    player_label.configure(fg='blue')
                    cpu_play()
            elif player.get() == 'cpu':
                if (1 in o and 2 in o and 3 in o and 4 in o) \
                        or (2 in o and 3 in o and 4 in o and 5 in o) \
                        or (3 in o and 4 in o and 5 in o and 6 in o) \
                        or (7 in o and 8 in o and 9 in o and 10 in o) \
                        or (8 in o and 9 in o and 10 in o and 11 in o) \
                        or (9 in o and 10 in o and 11 in o and 12 in o) \
                        or (13 in o and 14 in o and 15 in o and 16 in o) \
                        or (14 in o and 15 in o and 16 in o and 17 in o) \
                        or (15 in o and 16 in o and 17 in o and 18 in o) \
                        or (19 in o and 20 in o and 21 in o and 22 in o) \
                        or (20 in o and 21 in o and 22 in o and 23 in o) \
                        or (21 in o and 22 in o and 23 in o and 24 in o) \
                        or (25 in o and 26 in o and 27 in o and 28 in o) \
                        or (26 in o and 27 in o and 28 in o and 29 in o) \
                        or (27 in o and 28 in o and 29 in o and 30 in o) \
                        or (31 in o and 32 in o and 33 in o and 34 in o) \
                        or (32 in o and 33 in o and 34 in o and 35 in o) \
                        or (33 in o and 34 in o and 35 in o and 36 in o) \
                        or (1 in o and 7 in o and 13 in o and 19 in o) \
                        or (7 in o and 13 in o and 19 in o and 25 in o) \
                        or (13 in o and 19 in o and 25 in o and 31 in o) \
                        or (2 in o and 8 in o and 14 in o and 20 in o) \
                        or (8 in o and 14 in o and 20 in o and 26 in o) \
                        or (14 in o and 20 in o and 26 in o and 32 in o) \
                        or (3 in o and 9 in o and 15 in o and 21 in o) \
                        or (9 in o and 15 in o and 21 in o and 27 in o) \
                        or (15 in o and 21 in o and 27 in o and 33 in o) \
                        or (4 in o and 10 in o and 16 in o and 22 in o) \
                        or (10 in o and 16 in o and 22 in o and 28 in o) \
                        or (16 in o and 22 in o and 28 in o and 34 in o) \
                        or (5 in o and 11 in o and 17 in o and 23 in o) \
                        or (11 in o and 17 in o and 23 in o and 29 in o) \
                        or (17 in o and 23 in o and 29 in o and 35 in o) \
                        or (6 in o and 12 in o and 18 in o and 24 in o) \
                        or (12 in o and 18 in o and 24 in o and 30 in o) \
                        or (18 in o and 24 in o and 30 in o and 36 in o) \
                        or (3 in o and 10 in o and 17 in o and 24 in o) \
                        or (13 in o and 20 in o and 27 in o and 34 in o) \
                        or (2 in o and 9 in o and 16 in o and 23 in o) \
                        or (9 in o and 16 in o and 23 in o and 30 in o) \
                        or (7 in o and 14 in o and 21 in o and 28 in o) \
                        or (14 in o and 21 in o and 28 in o and 35 in o) \
                        or (1 in o and 8 in o and 15 in o and 22 in o) \
                        or (8 in o and 15 in o and 22 in o and 29 in o) \
                        or (15 in o and 22 in o and 29 in o and 36 in o) \
                        or (4 in o and 9 in o and 14 in o and 19 in o) \
                        or (18 in o and 23 in o and 28 in o and 33 in o) \
                        or (5 in o and 10 in o and 15 in o and 20 in o) \
                        or (10 in o and 15 in o and 20 in o and 25 in o) \
                        or (12 in o and 17 in o and 22 in o and 27 in o) \
                        or (17 in o and 22 in o and 27 in o and 32 in o) \
                        or (6 in o and 11 in o and 16 in o and 21 in o) \
                        or (11 in o and 16 in o and 21 in o and 26 in o) \
                        or (16 in o and 21 in o and 26 in o and 31 in o):
                    win_label = Label(x_o, text='o_o', bg="blue", font=('arial', 28, 'bold'))
                    win_label.place(x=265, y=250)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=155, y=350)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=300, y=350)
                    x = []
                    o = []
                elif len(x) + len(o) == 36:
                    win_label = Label(x_o, text='^_^', bg="#400040", font=('arial', 28, 'bold'))
                    win_label.place(x=265, y=250)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=155, y=350)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=300, y=350)
                    x = []
                    o = []
                else:
                    player.set('player 1')
                    player_label.configure(fg='red')
        elif ga.get() == '6x6' and win.get() == '5':
            if player.get() == 'player 1':
                if (1 in x and 2 in x and 3 in x and 4 in x and 5 in x)\
                        or (2 in x and 3 in x and 4 in x and 5 in x and 6 in x) \
                        or (7 in x and 8 in x and 9 in x and 10 in x and 11 in x) \
                        or (8 in x and 9 in x and 10 in x and 11 in x and 12 in x) \
                        or (13 in x and 14 in x and 15 in x and 16 in x and 17 in x)\
                        or (14 in x and 15 in x and 16 in x and 17 in x and 18 in x)\
                        or (19 in x and 20 in x and 21 in x and 22 in x and 23 in x) \
                        or (20 in x and 21 in x and 22 in x and 23 in x and 24 in x) \
                        or (25 in x and 26 in x and 27 in x and 28 in x and 29 in x) \
                        or (26 in x and 27 in x and 28 in x and 29 in x and 30 in x) \
                        or (31 in x and 32 in x and 33 in x and 34 in x and 35 in x) \
                        or (32 in x and 33 in x and 34 in x and 35 in x and 36 in x) \
                        or (1 in x and 7 in x and 13 in x and 19 in x and 25 in x) \
                        or (7 in x and 13 in x and 19 in x and 25 in x and 31 in x) \
                        or (2 in x and 8 in x and 14 in x and 20 in x and 26 in x) \
                        or (8 in x and 14 in x and 20 in x and 26 in x and 32 in x)\
                        or (3 in x and 9 in x and 15 in x and 21 in x and 27 in x) \
                        or (9 in x and 15 in x and 21 in x and 27 in x and 33 in x) \
                        or (4 in x and 10 in x and 16 in x and 22 in x and 28 in x) \
                        or (10 in x and 16 in x and 22 in x and 28 in x and 34 in x) \
                        or (5 in x and 11 in x and 17 in x and 23 in x and 29 in x) \
                        or (11 in x and 17 in x and 23 in x and 29 in x and 35 in x) \
                        or (6 in x and 12 in x and 18 in x and 24 in x and 30 in x) \
                        or (11 in x and 18 in x and 24 in x and 30 in x and 36 in x) \
                        or (2 in x and 9 in x and 16 in x and 23 in x and 30 in x) \
                        or (7 in x and 14 in x and 21 in x and 28 in x and 35 in x) \
                        or (1 in x and 8 in x and 15 in x and 22 in x and 29 in x) \
                        or (8 in x and 15 in x and 22 in x and 29 in x and 36 in x) \
                        or (5 in x and 10 in x and 15 in x and 20 in x and 25 in x) \
                        or (12 in x and 17 in x and 22 in x and 27 in x and 32 in x) \
                        or (6 in x and 11 in x and 16 in x and 21 in x and 26 in x) \
                        or (11 in x and 16 in x and 21 in x and 26 in x and 31 in x) :
                    win_label = Label(x_o, text='x_x', bg="red", font=('arial', 28, 'bold'))
                    win_label.place(x=265, y=250)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=155, y=350)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=300, y=350)
                    x = []
                    o = []
                elif len(x) + len(o) == 36:
                    win_label = Label(x_o, text='^_^', bg="#400040", font=('arial', 28, 'bold'))
                    win_label.place(x=265, y=250)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=155, y=350)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=300, y=350)
                    x = []
                    o = []
                else:
                    player.set('cpu')
                    player_label.configure(fg='blue')
                    cpu_play()
            elif player.get() == 'cpu':
                if (1 in o and 2 in o and 3 in o and 4 in o and 5 in o) \
                        or (2 in o and 3 in o and 4 in o and 5 in o and 6 in o) \
                        or (7 in o and 8 in o and 9 in o and 10 in o and 11 in o) \
                        or (8 in o and 9 in o and 10 in o and 11 in o and 12 in o) \
                        or (13 in o and 14 in o and 15 in o and 16 in o and 17 in o) \
                        or (14 in o and 15 in o and 16 in o and 17 in o and 18 in o) \
                        or (19 in o and 20 in o and 21 in o and 22 in o and 23 in o) \
                        or (20 in o and 21 in o and 22 in o and 23 in o and 24 in o) \
                        or (25 in o and 26 in o and 27 in o and 28 in o and 29 in o) \
                        or (26 in o and 27 in o and 28 in o and 29 in o and 30 in o) \
                        or (31 in o and 32 in o and 33 in o and 34 in o and 35 in o) \
                        or (32 in o and 33 in o and 34 in o and 35 in o and 36 in o) \
                        or (1 in o and 7 in o and 13 in o and 19 in o and 25 in o) \
                        or (7 in o and 13 in o and 19 in o and 25 in o and 31 in o) \
                        or (2 in o and 8 in o and 14 in o and 20 in o and 26 in o) \
                        or (8 in o and 14 in o and 20 in o and 26 in o and 32 in o) \
                        or (3 in o and 9 in o and 15 in o and 21 in o and 27 in o) \
                        or (9 in o and 15 in o and 21 in o and 27 in o and 33 in o) \
                        or (4 in o and 10 in o and 16 in o and 22 in o and 28 in o) \
                        or (10 in o and 16 in o and 22 in o and 28 in o and 34 in o) \
                        or (5 in o and 11 in o and 17 in o and 23 in o and 29 in o) \
                        or (11 in o and 17 in o and 23 in o and 29 in o and 35 in o) \
                        or (6 in o and 12 in o and 18 in o and 24 in o and 30 in o) \
                        or (11 in o and 18 in o and 24 in o and 30 in o and 36 in o) \
                        or (2 in o and 9 in o and 16 in o and 23 in o and 30 in o) \
                        or (7 in o and 14 in o and 21 in o and 28 in o and 35 in o) \
                        or (1 in o and 8 in o and 15 in o and 22 in o and 29 in o) \
                        or (8 in o and 15 in o and 22 in o and 29 in o and 36 in o) \
                        or (5 in o and 10 in o and 15 in o and 20 in o and 25 in o) \
                        or (12 in o and 17 in o and 22 in o and 27 in o and 32 in o) \
                        or (6 in o and 11 in o and 16 in o and 21 in o and 26 in o) \
                        or (11 in o and 16 in o and 21 in o and 26 in o and 31 in o):
                    win_label = Label(x_o, text='o_o', bg="blue", font=('arial', 28, 'bold'))
                    win_label.place(x=265, y=250)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=155, y=350)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=300, y=350)
                    x = []
                    o = []
                elif len(x) + len(o) == 36:
                    win_label = Label(x_o, text='^_^', bg="#400040", font=('arial', 28, 'bold'))
                    win_label.place(x=265, y=250)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=155, y=350)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=300, y=350)
                    x = []
                    o = []
                else:
                    player.set('player 1')
                    player_label.configure(fg='red')
        elif ga.get() == '6x6' and win.get() == '6':
            if player.get() == 'player 1':
                if (1 in x and 2 in x and 3 in x and 4 in x and 5 in x and 6 in x) \
                        or (7 in x and 8 in x and 9 in x and 10 in x and 11 in x and 12 in x) \
                        or (13 in x and 14 in x and 15 in x and 16 in x and 17 in x and 18 in x) \
                        or (19 in x and 20 in x and 21 in x and 22 in x and 23 in x and 24 in x) \
                        or (25 in x and 26 in x and 27 in x and 28 in x and 28 in x and 30 in x) \
                        or (31 in x and 32 in x and 33 in x and 34 in x and 35 in x and 36 in x) \
                        or (1 in x and 7 in x and 13 in x and 19 in x and 25 in x and 31 in x) \
                        or (2 in x and 8 in x and 14 in x and 20 in x and 26 in x and 32 in x) \
                        or (3 in x and 9 in x and 15 in x and 21 in x and 27 in x and 33 in x) \
                        or (4 in x and 10 in x and 16 in x and 22 in x and 28 in x and 34 in x) \
                        or (5 in x and 11 in x and 17 in x and 23 in x and 29 in x and 35 in x) \
                        or (6 in x and 12 in x and 18 in x and 24 in x and 30 in x and 36 in x) \
                        or (1 in x and 8 in x and 15 in x and 22 in x and 29 in x and 36 in x) \
                        or (6 in x and 11 in x and 16 in x and 21 in x and 26 in x and 31 in x):
                    win_label = Label(x_o, text='x_x', bg="red", font=('arial', 28, 'bold'))
                    win_label.place(x=265, y=250)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=155, y=350)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=300, y=350)
                    x = []
                    o = []
                elif len(x) + len(o) == 36:
                    win_label = Label(x_o, text='^_^', bg="#400040", font=('arial', 28, 'bold'))
                    win_label.place(x=265, y=250)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=155, y=350)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=300, y=350)
                    x = []
                    o = []
                else:
                    player.set('cpu')
                    player_label.configure(fg='blue')
                    cpu_play()
            elif player.get() == 'cpu':
                if (1 in o and 2 in o and 3 in o and 4 in o and 5 in o and 6 in o) \
                        or (7 in o and 8 in o and 9 in o and 10 in o and 11 in o and 12 in o) \
                        or (13 in o and 14 in o and 15 in o and 16 in o and 17 in o and 18 in o) \
                        or (19 in o and 20 in o and 21 in o and 22 in o and 23 in o and 24 in o) \
                        or (25 in o and 26 in o and 27 in o and 28 in o and 28 in o and 30 in o) \
                        or (31 in o and 32 in o and 33 in o and 34 in o and 35 in o and 36 in o) \
                        or (1 in o and 7 in o and 13 in o and 19 in o and 25 in o and 31 in o) \
                        or (2 in o and 8 in o and 14 in o and 20 in o and 26 in o and 32 in o) \
                        or (3 in o and 9 in o and 15 in o and 21 in o and 27 in o and 33 in o) \
                        or (4 in o and 10 in o and 16 in o and 22 in o and 28 in o and 34 in o) \
                        or (5 in o and 11 in o and 17 in o and 23 in o and 29 in o and 35 in o) \
                        or (6 in o and 12 in o and 18 in o and 24 in o and 30 in o and 36 in o) \
                        or (1 in o and 8 in o and 15 in o and 22 in o and 29 in o and 36 in o) \
                        or (6 in o and 11 in o and 16 in o and 21 in o and 26 in o and 31 in o):
                    win_label = Label(x_o, text='o_o', bg="blue", font=('arial', 28, 'bold'))
                    win_label.place(x=265, y=250)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=155, y=350)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=300, y=350)
                    x = []
                    o = []
                elif len(x) + len(o) == 36:
                    win_label = Label(x_o, text='^_^', bg="#400040", font=('arial', 28, 'bold'))
                    win_label.place(x=265, y=250)
                    play_again_bt = ttk.Button(x_o, text='play again', width=22, command=other_game)
                    play_again_bt.place(x=155, y=350)
                    main_window_bt = ttk.Button(x_o, text='main window', width=22, command=main)
                    main_window_bt.place(x=300, y=350)
                    x = []
                    o = []
                else:
                    player.set('player 1')
                    player_label.configure(fg='red')


def none():
    pass


def bt1_():
    v.remove(1)
    if player.get() == 'player 1':
        bt1.configure(image=x_, command=none)
        x.append(1)
        chick_win()
    else:
        bt1.configure(image=o_, command=none)
        o.append(1)
        chick_win()

def bt2_():
    v.remove(2)
    if player.get() == 'player 1':
        bt2.configure(image=x_, command=none)
        x.append(2)
        chick_win()

    else:
        bt2.configure(image=o_, command=none)
        o.append(2)
        chick_win()

def bt3_():
    v.remove(3)
    if player.get() == 'player 1':
        bt3.configure(image=x_, command=none)
        x.append(3)
        chick_win()

    else:
        bt3.configure(image=o_, command=none)
        o.append(3)
        chick_win()

def bt4_():
    v.remove(4)
    if player.get() == 'player 1':
        bt4.configure(image=x_, command=none)
        x.append(4)
        chick_win()
    else:
        bt4.configure(image=o_, command=none)
        o.append(4)
        chick_win()

def bt5_():
    v.remove(5)
    if player.get() == 'player 1':
        bt5.configure(image=x_, command=none)
        x.append(5)
        chick_win()
    else:
        bt5.configure(image=o_, command=none)
        o.append(5)
        chick_win()

def bt6_():
    v.remove(6)
    if player.get() == 'player 1':
        bt6.configure(image=x_, command=none)
        x.append(6)
        chick_win()
    else:
        bt6.configure(image=o_, command=none)
        o.append(6)
        chick_win()

def bt7_():
    v.remove(7)
    if player.get() == 'player 1':
        bt7.configure(image=x_, command=none)
        x.append(7)
        chick_win()

    else:
        bt7.configure(image=o_, command=none)
        o.append(7)
        chick_win()

def bt8_():
    v.remove(8)
    if player.get() == 'player 1':
        bt8.configure(image=x_, command=none)
        x.append(8)
        chick_win()

    else:
        bt8.configure(image=o_, command=none)
        o.append(8)
        chick_win()

def bt9_():
    v.remove(9)
    if player.get() == 'player 1':
        bt9.configure(image=x_, command=none)
        x.append(9)
        chick_win()

    else:
        bt9.configure(image=o_, command=none)
        o.append(9)
        chick_win()

def bt10_():
    v.remove(10)
    if player.get() == 'player 1':
        bt10.configure(image=x_, command=none)
        x.append(10)
        chick_win()
    else:
        bt10.configure(image=o_, command=none)
        o.append(10)
        chick_win()

def bt11_():
    v.remove(11)
    if player.get() == 'player 1':
        bt11.configure(image=x_, command=none)
        x.append(11)
        chick_win()
    else:
        bt11.configure(image=o_, command=none)
        o.append(11)
        chick_win()

def bt12_():
    v.remove(12)
    if player.get() == 'player 1':
        bt12.configure(image=x_, command=none)
        x.append(12)
        chick_win()
    else:
        bt12.configure(image=o_, command=none)
        o.append(12)
        chick_win()

def bt13_():
    v.remove(13)
    if player.get() == 'player 1':
        bt13.configure(image=x_, command=none)
        x.append(13)
        chick_win()
    else:
        bt13.configure(image=o_, command=none)
        o.append(13)
        chick_win()

def bt14_():
    v.remove(14)
    if player.get() == 'player 1':
        bt14.configure(image=x_, command=none)
        x.append(14)
        chick_win()
    else:
        bt14.configure(image=o_, command=none)
        o.append(14)
        chick_win()

def bt15_():
    v.remove(15)
    if player.get() == 'player 1':
        bt15.configure(image=x_, command=none)
        x.append(15)
        chick_win()
    else:
        bt15.configure(image=o_, command=none)
        o.append(15)
        chick_win()

def bt16_():
    v.remove(16)
    if player.get() == 'player 1':
        bt16.configure(image=x_, command=none)
        x.append(16)
        chick_win()
    else:
        bt16.configure(image=o_, command=none)
        o.append(16)
        chick_win()

def bt17_():
    v.remove(17)
    if player.get() == 'player 1':
        bt17.configure(image=x_, command=none)
        x.append(17)
        chick_win()
    else:
        bt17.configure(image=o_, command=none)
        o.append(17)
        chick_win()

def bt18_():
    v.remove(18)
    if player.get() == 'player 1':
        bt18.configure(image=x_, command=none)
        x.append(18)
        chick_win()
    else:
        bt18.configure(image=o_, command=none)
        o.append(18)
        chick_win()

def bt19_():
    v.remove(19)
    if player.get() == 'player 1':
        bt19.configure(image=x_, command=none)
        x.append(19)
        chick_win()
    else:
        bt19.configure(image=o_, command=none)
        o.append(19)
        chick_win()

def bt20_():
    v.remove(20)
    if player.get() == 'player 1':
        bt20.configure(image=x_, command=none)
        x.append(20)
        chick_win()
    else:
        bt20.configure(image=o_, command=none)
        o.append(20)
        chick_win()

def bt21_():
    v.remove(21)
    if player.get() == 'player 1':
        bt21.configure(image=x_, command=none)
        x.append(21)
        chick_win()
    else:
        bt21.configure(image=o_, command=none)
        o.append(21)
        chick_win()

def bt22_():
    v.remove(22)
    if player.get() == 'player 1':
        bt22.configure(image=x_, command=none)
        x.append(22)
        chick_win()
    else:
        bt22.configure(image=o_, command=none)
        o.append(22)
        chick_win()

def bt23_():
    v.remove(23)
    if player.get() == 'player 1':
        bt23.configure(image=x_, command=none)
        x.append(23)
        chick_win()
    else:
        bt23.configure(image=o_, command=none)
        o.append(23)
        chick_win()

def bt24_():
    v.remove(24)
    if player.get() == 'player 1':
        bt24.configure(image=x_, command=none)
        x.append(24)
        chick_win()
    else:
        bt24.configure(image=o_, command=none)
        o.append(24)
        chick_win()

def bt25_():
    v.remove(25)
    if player.get() == 'player 1':
        bt25.configure(image=x_, command=none)
        x.append(25)
        chick_win()
    else:
        bt25.configure(image=o_, command=none)
        o.append(25)
        chick_win()

def bt26_():
    v.remove(26)
    if player.get() == 'player 1':
        bt26.configure(image=x_, command=none)
        x.append(26)
        chick_win()
    else:
        bt26.configure(image=o_, command=none)
        o.append(26)
        chick_win()

def bt27_():
    v.remove(27)
    if player.get() == 'player 1':
        bt27.configure(image=x_, command=none)
        x.append(27)
        chick_win()
    else:
        bt27.configure(image=o_, command=none)
        o.append(27)
        chick_win()

def bt28_():
    v.remove(28)
    if player.get() == 'player 1':
        bt28.configure(image=x_, command=none)
        x.append(28)
        chick_win()
    else:
        bt28.configure(image=o_, command=none)
        o.append(28)
        chick_win()

def bt29_():
    v.remove(29)
    if player.get() == 'player 1':
        bt29.configure(image=x_, command=none)
        x.append(29)
        chick_win()
    else:
        bt29.configure(image=o_, command=none)
        o.append(29)
        chick_win()

def bt30_():
    v.remove(30)
    if player.get() == 'player 1':
        bt30.configure(image=x_, command=none)
        x.append(30)
        chick_win()
    else:
        bt30.configure(image=o_, command=none)
        o.append(30)
        chick_win()

def bt31_():
    v.remove(31)
    if player.get() == 'player 1':
        bt31.configure(image=x_, command=none)
        x.append(31)
        chick_win()
    else:
        bt31.configure(image=o_, command=none)
        o.append(31)
        chick_win()

def bt32_():
    v.remove(32)
    if player.get() == 'player 1':
        bt32.configure(image=x_, command=none)
        x.append(32)
        chick_win()
    else:
        bt32.configure(image=o_, command=none)
        o.append(32)
        chick_win()

def bt33_():
    v.remove(33)
    if player.get() == 'player 1':
        bt33.configure(image=x_, command=none)
        x.append(33)
        chick_win()
    else:
        bt33.configure(image=o_, command=none)
        o.append(33)
        chick_win()

def bt34_():
    v.remove(34)
    if player.get() == 'player 1':
        bt34.configure(image=x_, command=none)
        x.append(34)
        chick_win()
    else:
        bt34.configure(image=o_, command=none)
        o.append(34)
        chick_win()

def bt35_():
    v.remove(35)
    if player.get() == 'player 1':
        bt35.configure(image=x_, command=none)
        x.append(35)
        chick_win()
    else:
        bt35.configure(image=o_, command=none)
        o.append(35)
        chick_win()

def bt36_():
    v.remove(36)
    if player.get() == 'player 1':
        bt36.configure(image=x_, command=none)
        x.append(36)
        chick_win()
    else:
        bt36.configure(image=o_, command=none)
        o.append(36)
        chick_win()

def back():

    back_bt.place_forget()
    start_bt.place_forget()
    condition.place_forget()
    game_size.place_forget()
    vs_player_bt.place(x=45, y=90)
    vs_cpu_bt.place(x=45, y=140)
    g_bt.place_forget()

def set():
    game = ga.get()
    if game == '':
        pass
    elif game == '3x3':
        condition.configure(values=('3'))
    elif game == '4x4':
        condition.configure(values=('3', '4'))
    elif game == '5x5':
        condition.configure(values=('4', '5'))
    elif game == '6x6':
        condition.configure(values=('4', '5', '6'))

def main():
    global vs_player_bt,vs_cpu_bt ,x,o,v,player
    v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,\
         18, 19, 20, 21, 22, 23, 24, 25, \
         26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
    x = []
    o = []
    x_o.geometry('250x250+400+90')
    player_label.place_forget()
    tital_label = Label(x_o, text='x_o', bg="#400040", font=('arial', 28, 'bold'))
    tital_label.place(x=95, y=30)
    vs_player_bt = ttk.Button(x_o, text='vs player', width=25, command=vs_player)
    vs_player_bt.place(x=45, y=90)
    vs_cpu_bt = ttk.Button(x_o, text='vs cpu', width=25, command=vs_cpu)
    vs_cpu_bt.place(x=45, y=140)
    player.set("")
    win_label.place_forget()
    play_again_bt.place_forget()
    main_window_bt.place_forget()
    if  ga.get() == '3x3':
        bt1.place_forget()
        bt2.place_forget()
        bt3.place_forget()
        bt4.place_forget()
        bt5.place_forget()
        bt6.place_forget()
        bt7.place_forget()
        bt8.place_forget()
        bt9.place_forget()
    elif  ga.get() == '4x4':
        bt1.place_forget()
        bt2.place_forget()
        bt3.place_forget()
        bt4.place_forget()
        bt5.place_forget()
        bt6.place_forget()
        bt7.place_forget()
        bt8.place_forget()
        bt9.place_forget()
        bt10.place_forget()
        bt11.place_forget()
        bt12.place_forget()
        bt13.place_forget()
        bt14.place_forget()
        bt15.place_forget()
        bt16.place_forget()
    elif  ga.get() == '5x5':
        bt1.place_forget()
        bt2.place_forget()
        bt3.place_forget()
        bt4.place_forget()
        bt5.place_forget()
        bt6.place_forget()
        bt7.place_forget()
        bt8.place_forget()
        bt9.place_forget()
        bt10.place_forget()
        bt11.place_forget()
        bt12.place_forget()
        bt13.place_forget()
        bt14.place_forget()
        bt15.place_forget()
        bt16.place_forget()
        bt17.place_forget()
        bt18.place_forget()
        bt19.place_forget()
        bt20.place_forget()
        bt21.place_forget()
        bt22.place_forget()
        bt23.place_forget()
        bt24.place_forget()
        bt25.place_forget()
    elif  ga.get() == '6x6':
        bt1.place_forget()
        bt2.place_forget()
        bt3.place_forget()
        bt4.place_forget()
        bt5.place_forget()
        bt6.place_forget()
        bt7.place_forget()
        bt8.place_forget()
        bt9.place_forget()
        bt10.place_forget()
        bt11.place_forget()
        bt12.place_forget()
        bt13.place_forget()
        bt14.place_forget()
        bt15.place_forget()
        bt16.place_forget()
        bt17.place_forget()
        bt18.place_forget()
        bt19.place_forget()
        bt20.place_forget()
        bt21.place_forget()
        bt22.place_forget()
        bt23.place_forget()
        bt24.place_forget()
        bt25.place_forget()
        bt26.place_forget()
        bt27.place_forget()
        bt28.place_forget()
        bt29.place_forget()
        bt30.place_forget()
        bt31.place_forget()
        bt32.place_forget()
        bt33.place_forget()
        bt34.place_forget()
        bt35.place_forget()
        bt36.place_forget()

def other_game ():
        global  x, o,v,player
        player_label.place_forget()
        player.set("")
        v =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,\
            26,27,28,29,30,31,32,33,34,35,36]
        x = []
        o = []
        if ga.get() == '3x3':
            bt1.place_forget()
            bt2.place_forget()
            bt3.place_forget()
            bt4.place_forget()
            bt5.place_forget()
            bt6.place_forget()
            bt7.place_forget()
            bt8.place_forget()
            bt9.place_forget()
        elif ga.get() == '4x4':
            bt1.place_forget()
            bt2.place_forget()
            bt3.place_forget()
            bt4.place_forget()
            bt5.place_forget()
            bt6.place_forget()
            bt7.place_forget()
            bt8.place_forget()
            bt9.place_forget()
            bt10.place_forget()
            bt11.place_forget()
            bt12.place_forget()
            bt13.place_forget()
            bt14.place_forget()
            bt15.place_forget()
            bt16.place_forget()
        elif ga.get() == '5x5':
            bt1.place_forget()
            bt2.place_forget()
            bt3.place_forget()
            bt4.place_forget()
            bt5.place_forget()
            bt6.place_forget()
            bt7.place_forget()
            bt8.place_forget()
            bt9.place_forget()
            bt10.place_forget()
            bt11.place_forget()
            bt12.place_forget()
            bt13.place_forget()
            bt14.place_forget()
            bt15.place_forget()
            bt16.place_forget()
            bt17.place_forget()
            bt18.place_forget()
            bt19.place_forget()
            bt20.place_forget()
            bt21.place_forget()
            bt22.place_forget()
            bt23.place_forget()
            bt24.place_forget()
            bt25.place_forget()
        elif ga.get() == '6x6':
            bt1.place_forget()
            bt2.place_forget()
            bt3.place_forget()
            bt4.place_forget()
            bt5.place_forget()
            bt6.place_forget()
            bt7.place_forget()
            bt8.place_forget()
            bt9.place_forget()
            bt10.place_forget()
            bt11.place_forget()
            bt12.place_forget()
            bt13.place_forget()
            bt14.place_forget()
            bt15.place_forget()
            bt16.place_forget()
            bt17.place_forget()
            bt18.place_forget()
            bt19.place_forget()
            bt20.place_forget()
            bt21.place_forget()
            bt22.place_forget()
            bt23.place_forget()
            bt24.place_forget()
            bt25.place_forget()
            bt26.place_forget()
            bt27.place_forget()
            bt28.place_forget()
            bt29.place_forget()
            bt30.place_forget()
            bt31.place_forget()
            bt32.place_forget()
            bt33.place_forget()
            bt34.place_forget()
            bt35.place_forget()
            bt36.place_forget()
        win_label.place_forget()
        play_again_bt.place_forget()
        main_window_bt.place_forget()
        start()

def gamee ():
    global condition, back_bt, start_bt, game_size, g_bt

    vs_player_bt.place_forget()
    vs_cpu_bt.place_forget()

    start_bt = ttk.Button(x_o, text='start', width=25, command=start)
    start_bt.place(x=45, y=140)

    back_bt = ttk.Button(x_o, text='back', width=25, command=back)
    back_bt.place(x=45, y=170)

    g_bt = ttk.Button(x_o, text='✔', command=set, width=2)
    g_bt.place(x=183, y=85)

    game_size = ttk.Combobox(x_o, width=18, values=('3x3', '4x4', '5x5', '6x6'), textvariable=ga)
    game_size.place(x=45, y=85)

    condition = ttk.Combobox(x_o, width=23, textvariable=win)
    condition.place(x=45, y=112)

def vs_player ():
    global runing
    runing = 'vs_player'
    gamee()

def vs_cpu ():
    global runing
    runing = 'vs_cpu'
    gamee()


x_o = Tk()
x_o.geometry('250x250+400+90')
x_o.iconbitmap('icon.ico')
x_o.title('x/o')
x_o.resizable(0,0)
x_o.configure(bg = '#400040')
player = StringVar()
player.set('player 1')
ga = StringVar()
win = StringVar()
x =[]
o =[]
e= PhotoImage(file='e.png')
o_= PhotoImage(file='o.png')
x_= PhotoImage(file='x.png')




tital_label = Label(x_o, text = 'x_o',bg = "#400040" ,font=('arial',28,'bold'))
tital_label.place(x=95,y=30)
vs_player_bt = ttk.Button(x_o, text = 'vs player',width = 25,command = vs_player )
vs_player_bt.place(x=45,y=90)

vs_cpu_bt = ttk.Button(x_o, text = 'vs cpu',width = 25 ,command = vs_cpu)
vs_cpu_bt.place(x=45,y=140)





x_o.mainloop()
