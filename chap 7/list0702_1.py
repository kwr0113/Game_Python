import tkinter

def click_btn():
    text.insert(tkinter.END, "몬스터가 나타났다!")


root = tkinter.Tk()
root.title("여러 행 텍스트 입력")
root.geometry("400x200")
button = tkinter.Button(text="메세지", command=click_btn)
button.pack()
text = tkinter.Text()
text.place(x=20, y=50, width=360, height=120)
text.pack()
root.mainloop()