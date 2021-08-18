import tkinter
root = tkinter.Tk()
root.title('첫 번째 라벨')
root.geometry('800x600')
label = tkinter.Label(root, text='라벨 문자열', font=('궁서체', 12))
label.place(x=200, y=100)
root.mainloop()