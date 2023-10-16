from tkinter import *

root = Tk()
root.geometry('320x240')
root.resizable(0,0)
root.title('Select mode')
root.config(bg='#9999ee')

score = [10,10,0,9,10,8,9,7,9,10]

camera_axis = '50:900, 80:700'

def pistol_module():
    return(score)

def rifil_module():
    return(score)

def align_camera():
    return(camera_axis)

rifil_button = Button(root, text='Rifil Mode', font=('Helvetica', 14,'bold'), width=10, height=3, bg='#ffbd03', command=rifil_module)
rifil_button.place(relx = 0.25, rely=0.4, anchor=CENTER)
pistol_button = Button(root, text='Pistol Mode', font=('Helvetica', 14,'bold'), width=10, height=3, bg='#ffbd03', command=pistol_module)
pistol_button.place(relx = 0.75, rely=0.4, anchor=CENTER)
camera_aligner_button = Button(root, text='Camera Aligner', font=('Helvetica', 12), height=1, bg='#ffbd03', command=align_camera)
camera_aligner_button.place(relx = 0.5, rely=0.8, anchor=CENTER)

root.mainloop()