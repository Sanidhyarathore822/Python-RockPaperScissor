from tkinter import *
from PIL import Image,ImageTk

#tkinter is a gui provided by python.
#PIL 


root=Tk()
root.title("Conquer")

root.configure(background="orange")

#picture

# rockImg=ImageTk.PhotoImage(Image.open("rock.jpeg"))
paperImg=ImageTk.PhotoImage(Image.open("paper.jpg"))
scisssorImg=ImageTk.PhotoImage(Image.open("rock.jpeg"))


#insert Picture

user_label=Label(root,image=scisssorImg)
comp_label=Label(root,image=scisssorImg)
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)



root.mainloop()

print("Jai Shri Krishna") 