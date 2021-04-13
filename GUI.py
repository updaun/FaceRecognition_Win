from tkinter import *
import tkinter.font

from dir_make import make
from face_shot import shot
from train_model import train
from face_lock import lock
from file_remove import remove


def isEnglishOrKorean(input_s):
    k_count = 0
    e_count = 0
    for c in input_s:
        if ord('가') <= ord(c) <= ord('힣'):
            k_count += 1
        elif ord('a') <= ord(c.lower()) <= ord('z'):
            e_count += 1
    return "k" if k_count > 1 else "e"


root = Tk()
root.geometry("480x640+850+0")
root.resizable(False, False)
root.configure(bg='#FFFFDE')
root.title("스마트 도어 시스템")
#root.title("Smart Door System")


#font=tkinter.font.Font(family="돋움", size=20, slant="italic")
font = tkinter.font.Font(family="KoPubWorld돋움체 Medium",
                         size=15, weight=tkinter.font.BOLD)  # 버튼 폰트
font1 = tkinter.font.Font(family="KoPubWorld돋움체 Medium", size=11)  # 설명 폰트
font2 = tkinter.font.Font(
    family="KoPubWorld돋움체 Medium", size=18)  # TEXT 박스, CI 폰트


# btn1 = Button(root, text = "체험자 폴더 생성", width=25, height=1, font = font, foreground='white', background='#2f3640', command=lambda: make(textExample.get(1.0, END+"-1c")))
btn1 = Button(root, text="체험자 폴더 생성", width=20, height=1, font=font,
              foreground='white', background='#2f3640', command=lambda: make(textExample.get()))
btn2 = Button(root, text="데이터 촬영", width=20, height=1, font=font, foreground='white',
              background='#2f3640', command=lambda: shot(textExample.get()))
btn3 = Button(root, text="인공지능 학습", width=20, height=1, font=font,
              foreground='white', background='#2f3640', command=train)
btn4 = Button(root, text="스마트 도어 작동", width=20, height=1, font=font,
              foreground='white', background='#2f3640', command=lock)
btn5 = Button(root, text="체험자 이미지 삭제", width=20, height=1, font=font,
              foreground='white', background='#2f3640', command=remove)


label1 = Label(root, text='- 체험자의 이름을 영어로 입력하세요.', anchor="sw",
               width=40, height=2, font=font1, background='#FFFFDE')

label2 = Label(root, text='- 스페이스 바를 눌러 사진을 촬영하세요.(종료 - ESC)',
               anchor="sw", width=40, height=2, font=font1, background='#FFFFDE')

label3 = Label(root, text='- 사진 개수에 따라 학습 시간이 다릅니다.', anchor="sw",
               width=40, height=2, font=font1, background='#FFFFDE')

label4 = Label(root, text='- 학습된 스마트 도어가 작동합니다.(종료 - ESC)',
               anchor="sw", width=40, height=2, font=font1, background='#FFFFDE')

label5 = Label(root, text='- 체험을 종료하고, 사진을 삭제합니다.', anchor="sw",
               width=40, height=2, font=font1, background='#FFFFDE')

ci = Label(root, text='(주)한국공학기술연구원', anchor="s", width=40,
           height=3, font=font2, background='#FFFFDE')


label1.pack()

textExample = Entry(root, width=17, font=font2, background='azure')
textExample.pack()

btn1.pack()

label2.pack()

btn2.pack()

label3.pack()

btn3.pack()

label4.pack()

btn4.pack()

label5.pack()

btn5.pack()

ci.pack()

root.mainloop()
