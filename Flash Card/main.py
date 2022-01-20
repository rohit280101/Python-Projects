BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
from random import choice
import pandas

current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")

    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
def next_card():
    global current_card,flip_timer
    current_card = choice(to_learn)
    window.after_cancel(flip_timer)


    canvas.itemconfig(card_title, text="French",fill="black")
    canvas.itemconfig(card_word, text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=logo_img)
    flip_timer =window.after(3000, func=flip_card)

def flip_card():

    canvas.itemconfig(card_title, text="English",fill="white")
    canvas.itemconfig(card_word, text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=back_logo)


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()





window =  Tk()
window.title("Flashy")
window.config(padx=50, pady=50,bg="#B1DDC6")
flip_timer = window.after(2000,func=flip_card)


canvas =Canvas(width=800,height=526 )
logo_img = PhotoImage(file="images/card_front.png")
card_background =canvas.create_image(400, 263, image=logo_img)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
back_logo =PhotoImage(file="images/card_back.png")
card_title =canvas.create_text(400,163,text="",font=("areil",40,"italic"))
card_word =canvas.create_text(400,263,text="",font=("areil",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)


logo_img1 = PhotoImage(file="images/right.png")
unk = Button(image=logo_img1,command=is_known)
unk.config(bg=BACKGROUND_COLOR,highlightthickness=0)
unk.grid(row=1, column=0)

logo_img2 = PhotoImage(file="images/wrong.png")
unk1 =Button(image=logo_img2,command=next_card)
unk1.config(bg=BACKGROUND_COLOR ,highlightthickness=0)
unk1.grid(row=1, column=1)
next_card()
window.mainloop()