import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk()
root.title("test register 3 buttons")
root.geometry('800x800')
root.configure(bg='grey')


I_button = PhotoImage(file="Invincible.png")
VR_button = PhotoImage(file="Vowel.png")
LE_button = PhotoImage(file="Letter Eraser.png")
play_btn = PhotoImage(file= "Button-2.png")


I_button_reg = tk.Button(root, image=I_button, command=lambda: button_click('Invincibility'))
VR_button_reg = tk.Button(root, image=VR_button, command=lambda: button_click('Vowel Reveal'))
LE_button_reg = tk.Button(root, image=LE_button, command=lambda: button_click('Letter Eraser'))
play_btn_reg = tk.Button(root, image=play_btn, command=lambda: button_click('select diff'))


def hover_click(event):
    play_btn_reg.config(borderwidth=7, highlightbackground="white", highlightcolor="white")
   
def leave(event):
     play_btn_reg.config(borderwidth=0)
     
play_btn_reg.bind("<Enter>", hover_click)
play_btn_reg.bind("<Leave>", leave)


def hover_click(event):
    I_button_reg.config(borderwidth=7, highlightbackground="white", highlightcolor="white", text="invincibility")
   
def leave(event):
     I_button_reg.config(borderwidth=0, text="")
     
I_button_reg.bind("<Enter>", hover_click)
I_button_reg.bind("<Leave>", leave)

def hover_click2(event):
    VR_button_reg.config(borderwidth=7, highlightbackground="white", highlightcolor="white")
   
def leave2(event):
     VR_button_reg.config(borderwidth=0)
     
VR_button_reg.bind("<Enter>", hover_click2)
VR_button_reg.bind("<Leave>", leave2)

def hover_click3(event):
    LE_button_reg.config(borderwidth=7, highlightbackground="white", highlightcolor="white")
   
def leave3(event):
     LE_button_reg.config(borderwidth=0)
     
LE_button_reg.bind("<Enter>", hover_click3)
LE_button_reg.bind("<Leave>", leave3)



def button_click(button_name):
   
    print(f"{button_name} power up clicked")
I_button_reg.pack(pady=10, padx=90, side="top", anchor="ne")
VR_button_reg.pack(pady=10, padx=90, side="top", anchor="ne")
LE_button_reg.pack(pady=10, padx=90, side="top", anchor="ne")
play_btn_reg.pack(pady=10, padx=90, side="top", anchor="c")

#pop up box still in progress



root.mainloop()



#info box
#outline color still in progress

''''
import tkinter as tk
from tkinter import PhotoImage


root = tk.Tk()
root.title("border test")
I_button = PhotoImage(file="Invincible.png")

class HoverButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        tk.Button.__init__(self, master, **kwargs)
        self.tooltip = None
        self.bind("<Enter>", self.hovered)
        self.bind("<Leave>", self.not_hovered)

    def hovered(self, event):
        if not self.tooltip:
            x, y, _, _ = self.bbox("insert")
            x += self.winfo_rootx() + 50
            y += self.winfo_rooty() + 50

            self.tooltip = tk.Toplevel(self)
            self.tooltip.wm_overrideredirect(True)
            self.tooltip.wm_geometry(f"+{x}+{y}")

            label = tk.Label(self.tooltip, text="this can save you from losing an attempt", borderwidth=8, bg='gray', highlightbackground='white', highlightcolor='white')
            label.pack(ipadx=20, ipady=20)

    def not_hovered(self, event):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None
hover_button = HoverButton(root, image=I_button, highlightcolor='gray')
hover_button.pack(pady=10)


root.mainloop()
''''
