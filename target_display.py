from tkinter import *

win=Tk()
win.title('Target')
win.geometry('840x520')
win.resizable(0,0)
win.config(bg='black')

score = [10,10,0,9,10,8,9,7,9,10]
board = ['S1','S2','S3','S4','S5','S6','S7','S8','S9','S10']
sum_score=sum(score)
print('Round Score: ',score)
print('Total SCore: ',sum_score)

label_sum_title = Label(win, text="Round Scores\nRound 1", font=('Arial ', 16), bg='black', fg='white')
label_sum_title.place(relx=0.80,rely=0.10,anchor=CENTER)
board_label = Label(win, text=board,font=('Arial', 14), anchor='w', bg='black',fg='white')
board_label.place(relx=0.63, rely=0.25, anchor='w')
#label_score = Label(win, text=score,font=('Arial', 14), anchor='w', bg='black',fg='white')
#label_score.place(relx=0.80, rely=0.3, anchor=CENTER)

row_one = Label(win,text=score[0],font=('Arial', 12,'bold'), bg='white', fg='black',width=2).place(relx=.650,rely= 0.3,anchor=CENTER)
row_two = Label(win,text=score[1],font=('Arial', 12,'bold'), bg='gray', fg='white',width=2).place(relx=.685,rely= 0.3,anchor=CENTER)
row_three = Label(win,text=score[1],font=('Arial', 12,'bold'), bg='white', fg='black',width=2).place(relx=.720,rely= 0.3,anchor=CENTER)
row_four = Label(win,text=score[2],font=('Arial', 12,'bold'), bg='gray', fg='white',width=2).place(relx=.755,rely= 0.3,anchor=CENTER)
row_five = Label(win,text=score[3],font=('Arial', 12,'bold'), bg='white', fg='black',width=2).place(relx=.790,rely= 0.3,anchor=CENTER)
row_six = Label(win,text=score[4],font=('Arial', 12,'bold'), bg='gray', fg='white',width=2).place(relx=.825,rely= 0.3,anchor=CENTER)
row_seven = Label(win,text=score[5],font=('Arial', 12,'bold'), bg='white', fg='black',width=2).place(relx=.860,rely= 0.3,anchor=CENTER)
row_eight = Label(win,text=score[6],font=('Arial', 12,'bold'), bg='gray', fg='white',width=2).place(relx=.895,rely= 0.3,anchor=CENTER)
row_nine = Label(win,text=score[7],font=('Arial', 12,'bold'), bg='white', fg='black',width=2).place(relx=.930,rely= 0.3,anchor=CENTER)
row_ten = Label(win,text=score[8],font=('Arial', 12,'bold'), bg='gray', fg='white',width=2).place(relx=.965,rely= 0.3,anchor=CENTER)


label_sum_title = Label(win, text="Total Score:", font=('Arial ', 16), bg='black',fg='white')
label_sum_title.place(relx=0.69,rely=0.9,anchor='w')
label_sum = Label(win, text=sum_score, font=('Arial black', 16), bg='black',fg='yellow')
label_sum.place(relx=0.85,rely=0.9,anchor=CENTER)

target_img = PhotoImage(file = 'D:\Python Codes\Target_pistol\display_image.png')
img_label = Label(image = target_img)
img_label.place(relx=0.005,rely=0.5,anchor='w')

win.mainloop()