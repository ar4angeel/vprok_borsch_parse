from tkinter import *
win = Tk()
photo = PhotoImage(file='example_icon.png')
pink = '#F99FA2'
skin_color = '#F1EBE4'
click_counter = 0


def counter_click():
    global click_counter
    click_counter += 1
    buttonie['text'] = f'click number: {click_counter}'
    print(click_counter)


win.title('Example! Test!')
win.iconphoto(False, photo)
win.geometry('700x300+45+700')
win.resizable(False, False)
win.config(background=pink)


def main_label_on():
    labule = Label(win, text='example label! test label!', bg=pink, relief=SUNKEN)
    return labule


main_label_on().pack(side='top')


def main_button_on():
    buttonie = Button(win, text='experiment button! test button!', bg=skin_color, relief=RAISED,)
    return buttonie


main_button_on().place(bordermode=OUTSIDE, x=239, y=50)


def main_lambda_button_add_label_technology(text):
    button_lambda_add_label = Button(
        win, text='add new label',
        command=lambda: Label(win, text=text).place(x=239, y=200)
    )
    return button_lambda_add_label


main_lambda_button_add_label_technology('test! test!').place(x=239, y=150)


buttonie = Button(win, text=f'count number: {click_counter}', command=counter_click)


buttonie.place(x=239, y=250)
win.mainloop()
