
import tkinter
from tkinter import font
#import tkFont
import PIL
from PIL import Image, ImageTk



WIDTH = 800
HEIGHT = 600
PROGRAM_NAME = 'Cidadela do Caos'
PROGRAM_ICON = './img/castle_01.ico'
IMAGE_LIST = ['./img/space01.png','./img/citadel_01.png',\
			 './img/citadel_04_c.png', './img/citadel_05.png']
BUTTON_BG_COLOR = "#ADD8E6"
BUTTON_FG_COLOR = "#B22222"
BUTTON_FONT = ("Verdana", 12,  "bold")
BUTTON_relx = 0.02
#BUTTON_FONT = tkinter.font(family = "Verdana", size = 20, weight = 'bold')
BACKGROUND_IMAGE = IMAGE_LIST[2]

root = tkinter.Tk()
root.title(PROGRAM_NAME)
root.iconbitmap(PROGRAM_ICON)
root.geometry(f'{WIDTH}x{HEIGHT}+{10}+{10}')


canvas = tkinter.Canvas(root, width = WIDTH, height = HEIGHT)
canvas.pack()


#TODO: criar uma função pra isso
imagem = PIL.Image.open(BACKGROUND_IMAGE)
#resized_image = imagem.resize((WIDTH, HEIGHT))
resized_image = imagem
resized_image_tk = ImageTk.PhotoImage(resized_image)

bg_image = tkinter.PhotoImage(file = BACKGROUND_IMAGE)
bg_label = tkinter.Label(root, image = resized_image_tk)
bg_label.place(relwidth=1, relheight=1)

btn_start = tkinter.Button(root, text = "New Game", bg = BUTTON_BG_COLOR,
	font = BUTTON_FONT, 	fg = BUTTON_FG_COLOR,
	command = lambda : print("Botão Start"))
btn_start.place(relx = BUTTON_relx, rely = 0.2)#pack(side = tkinter.LEFT)

btn_load = tkinter.Button(root, text = "Load Game", bg = BUTTON_BG_COLOR,
	font = BUTTON_FONT, 	fg = BUTTON_FG_COLOR,
	command = lambda : print("Botão load game"))
btn_load.place(relx = BUTTON_relx, rely = 0.3)

btn_quit = tkinter.Button(root, text = "Quit", bg = BUTTON_BG_COLOR,
	font = BUTTON_FONT, 	fg = BUTTON_FG_COLOR,
	command = lambda : quit())
btn_quit.place(relx = BUTTON_relx, rely = 0.4)


#mainFrame = tkinter.Frame(root, bg = 'blue', bd = 5)
#mainFrame.pack()


#print('root keys:\n',root.configure().keys())
#print('/===============================================')
#print('root properties:\n', dir(tkinter.Tk))
#print('/===============================================')
#print('canvas keys:\n', canvas.configure().keys())
print('/===============================================')
print('PhotoImage: \n', dir(tkinter.PhotoImage))
print('/===============================================')


root.mainloop()



print('End.')