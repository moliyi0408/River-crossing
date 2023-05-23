
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import time
import os
#conda install pillow

#person,wolf,sheep,vegetable = 0,0,0,0
root = Tk()    
root.geometry("600x400")
root.title('人羊狼菜')

def wolf_click():
    btn_click('W')
def sheep_click():
    btn_click('S')
def vegetable_click():
    btn_click('V')
def person_click():
    btn_click('P')
def btn_click(n):
    global  person,wolf,sheep,vegetable
    
    if person == 0 and wolf == 0 and sheep == 0 and vegetable == 0  :
        if n == 'W':
            wolfcross(1)
            wolf == 1
        elif n == 'S':
            sheepcross(1)
            sheep = 1
        elif n == 'V' :
            vegetablecross(1)
            vegetable = 1
        elif n == 'P' :
            personcross(1)
            person = 1
            
    
    #人的情況
    if  person == 1  and wolf == 0 and sheep == 0 and vegetable == 0 :
        if n == 'W':
            wolfcross(1)
            wolf == 1
            messagebox.askyesno(title='遊戲結束', message='菜被羊吃了')
        elif n == 'S':
            sheepcross(1)
            sheep = 1
        elif n == 'V' :
            vegetablecross(1)
            vegetable = 1
            messagebox.askyesno(title='遊戲結束', message='羊被狼吃了')
    if  person == 1  and wolf == 0 and sheep == 1 and vegetable == 0 :
        if n == 'W':
            wolfcross(1)
            wolf == 1
        elif n == 'V' :
            vegetablecross(1)
            vegetable = 1
    if  person == 1  and wolf == 1 and sheep == 1 and vegetable == 0 :
        if n == 'V' :
            vegetablecross(1)
            vegetable = 1
            messagebox.askyesno(title='遊戲結束', message='你贏了')
    if  person == 1  and wolf == 0 and sheep == 1 and vegetable == 1 :
        if n == 'W':
            wolfcross(1)
            wolf == 1
            messagebox.askyesno(title='遊戲結束', message='你贏了')

    #狼的情況
    if  wolf == 1 and person == 0  and sheep == 0 and vegetable == 0 :
        messagebox.askyesno(title='遊戲結束', message='狼不能自己過河')
    if  wolf == 0 and person == 0  and sheep == 1 and vegetable == 0 :
        messagebox.askyesno(title='遊戲結束', message='羊不能自己過河')
    if  wolf == 0 and person == 0  and sheep == 0 and vegetable == 1 :
        messagebox.askyesno(title='遊戲結束', message='菜不能自己過河')
    


#飛到右岸  
def wolfcross(n):
    if n == 1:  #左岸到右岸
        for  x in range(0,40):
            bg_canvas.move(wolf_canvas,10,0)
            root.update()
            time.sleep(0.025)
            '''
    elif n == 2:
        for x in range(40,0):
            bg_canvas.move(wolf_canvas,10,0)
            root.update()
            time.sleep(0.025)
            '''



def sheepcross(n):
    if n == 1:  #左岸到右岸
        for  x in range(0,40):
            bg_canvas.move(sheep_canvas,10,0)
            root.update()
            time.sleep(0.025)
    

def vegetablecross(n):
    if n == 1:  #左岸到右岸
        for  x in range(0,40):
            bg_canvas.move(vegetable_canvas,10,0)
            root.update()
            time.sleep(0.025)

def personcross(n):
    if n == 1:  #左岸到右岸
        for  x in range(0,40):
            bg_canvas.move(person_canvas,10,0)
            root.update()
            time.sleep(0.025)

#def result(n):
    #if n == 1:
       # messagebox.askyesno(title='遊戲結束', message='菜被羊吃了')
       

size_x = 50
size_y = 50

#背景處理

bg_canvas = Canvas(root,width=600,height=400,bg='#FFFFE0')
bg_canvas.pack()
bg_canvas.create_rectangle(0,0,200,310,fill='#98FB98',outline='#98FB98')
bg_canvas.create_rectangle(600,0,200,310,fill='#87CEFA',outline='#87CEFA')
bg_canvas.create_rectangle(800,0,400,310,fill='#98FB98',outline='#98FB98')

current_dir = os.path.dirname(__file__)
#__file__ 代表目前正在執行的程式碼檔案的檔案路徑。
# 狼圖片處理
wolf_path = os.path.join(current_dir, 'images', 'wolf.png')
wolf = Image.open(wolf_path)
wolf_resize = wolf.resize((size_x, size_y), Image.ANTIALIAS)
wolf_img = ImageTk.PhotoImage(wolf_resize)

# 羊圖片處理
sheep_path = os.path.join(current_dir, 'images', 'sheep.png')
sheep = Image.open(sheep_path)
sheep_resize = sheep.resize((size_x, size_y), Image.ANTIALIAS)
sheep_img = ImageTk.PhotoImage(sheep_resize)

# 菜圖片處理
vegetable_path = os.path.join(current_dir, 'images', 'vegetable.png')
vegetable = Image.open(vegetable_path)
vegetable_resize = vegetable.resize((size_x, size_y), Image.ANTIALIAS)
vegetable_img = ImageTk.PhotoImage(vegetable_resize)

# 人圖片處理
person_path = os.path.join(current_dir, 'images', 'farmer.png')
person = Image.open(person_path)
person_resize = person.resize((size_x, size_y), Image.ANTIALIAS)
person_img = ImageTk.PhotoImage(person_resize)

person,wolf,sheep,vegetable = 0,0,0,0 #放在這圖才會動

#狼按鈕處理
wolf_btn = Button(root, image=wolf_img,  command=wolf_click)#borderwidth=0去圖片框
wolf_btn.place(x=30, y=330)
#羊按鈕處理
sheep_btn = Button(root,image=sheep_img, command=sheep_click) 
sheep_btn.place(x=100, y=330)
#菜按鈕處理
vegetable_btn = Button(root,image=vegetable_img, command=  vegetable_click)
vegetable_btn.place(x=170, y=330)
#人按鈕處理
person_btn = Button(root,image=person_img, command=person_click)
person_btn.place(x=250, y=330)
 
#人狼羊菜圖片

#boat_canvas = bg_canvas.create_image(250,100,image=boat_img) #船
wolf_canvas = bg_canvas.create_image(30,100,image=wolf_img) #狼
sheep_canvas = bg_canvas.create_image(80,100,image=sheep_img) #羊
vegetable_canvas = bg_canvas.create_image(130,100,image=vegetable_img) #菜
person_canvas = bg_canvas.create_image(180,100,image=person_img) #人

      

root.mainloop()
