from tkinter import *
from tkinter import filedialog
from color_generator import *
from PIL import ImageTk

def generate_palette():
    global picture
    cleanup()
    file = filedialog.askopenfilename(filetypes=[("JPEG", ".jpeg"), ("JPG", ".jpg"), ("PNG", ".png")])
    lower_res(file)
    new_image = Image.open('low_res.jpeg')
    picture = ImageTk.PhotoImage(new_image)
    color_list = get_palette()
    code_box.delete("1.0", "end")
    for color in color_list: code_box.insert('1.0', color + "   ")
    code_box.tag_add("center", "1.0", "end")
    canvas.itemconfig(current_picture, image=picture)
    canvas.itemconfig(color1, fill=color_list[0])
    canvas.itemconfig(color2, fill=color_list[1])
    canvas.itemconfig(color3, fill=color_list[2])
    canvas.itemconfig(color4, fill=color_list[3])
    canvas.itemconfig(color5, fill=color_list[4])

### UI ###
bg1 = 'white'
bg2 = 'black'

window = Tk()
window.resizable(False, False)
window.title('Color Palette Generator (supports: .jpg, .jpeg, .png)')
window.config(padx=10, pady=10, bg=bg2)

canvas = Canvas(window, height=450, width=400)
canvas.config(bg=bg1)
canvas.grid(row=1, column=0)

label = Label(text="Upload an image to generate color palette.", fg=bg1, bg=bg2)
label.grid(row=0, column=0)

lower_res('placeholder.jpeg')
placeholder = Image.open('low_res.jpeg')
picture = ImageTk.PhotoImage(placeholder)
current_picture = canvas.create_image(200, 200, image=picture)

code_box = Text(window, height=1, width=56)
code_box.config(fg=bg2, bg=bg1)
code_box.grid(row=2, column=0, pady=1)
code_box.tag_configure("center", justify="center")
color_list = get_palette()
for color in color_list: code_box.insert('1.0', color + "   ")
code_box.tag_add("center", "1.0", "end")

color1 = canvas.create_rectangle(27, 400, 77, 450, fill=color_list[0])
color2 = canvas.create_rectangle(97, 400, 147, 450, fill=color_list[1])
color3 = canvas.create_rectangle(167, 400, 217, 450, fill=color_list[2])
color4 = canvas.create_rectangle(237, 400, 287, 450, fill=color_list[3])
color5 = canvas.create_rectangle(307, 400, 357, 450, fill=color_list[4])

choose_file = Button(text="Choose File", pady=5, highlightthickness=0, command=generate_palette)
choose_file.grid(row=3, column=0, columnspan=2)


window.mainloop()
cleanup()