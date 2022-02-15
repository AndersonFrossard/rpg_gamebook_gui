
import tkinter
from tkinter import font
#import tkFont
import PIL
from PIL import Image, ImageTk



class lord_of_the_pages(tkinter.Tk):
	def __init__(self, *args, **kwargs):
		tkinter.Tk.__init__(self, *args, **kwargs)
		container = tkinter.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)
		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)
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

		BACKGROUND_IMAGE = IMAGE_LIST[2]
		self.geometry(f'{WIDTH}x{HEIGHT}+{10}+{10}')
		self.title(PROGRAM_NAME)
		self.iconbitmap(PROGRAM_ICON)
		self.frames = dict()

		for F in (Startpage, Gamepage, Loadgame):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row = 00, column = 0, sticky = "news")
		self.show_frame(Startpage)
		print('Lord of the pages created')

	def show_frame(self, controller):
		frame = self.frames[controller]
		frame.tkraise()

class Startpage(tkinter.Frame):
	global LARGE_FONT
	def __init__(self, parent, controller):
		tkinter.Frame.__init__(self, parent)
		#TODO: criar uma função pra isso

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

		imagem = PIL.Image.open(BACKGROUND_IMAGE)
		#resized_image = imagem.resize((WIDTH, HEIGHT))
		resized_image = imagem
		resized_image_tk = ImageTk.PhotoImage(resized_image)

		bg_image = tkinter.PhotoImage(file = BACKGROUND_IMAGE)
		bg_label = tkinter.Label(self, image = resized_image_tk)
		bg_label.image = resized_image_tk
		bg_label.place(relwidth=1, relheight=1)

		btn_start = tkinter.Button(self, text = "New Game", bg = BUTTON_BG_COLOR,
			font = BUTTON_FONT, 	fg = BUTTON_FG_COLOR,
			command = lambda : controller.show_frame(Gamepage))
		btn_start.place(relx = BUTTON_relx, rely = 0.2)#pack(side = tkinter.LEFT)

		btn_load = tkinter.Button(self, text = "Load Game", bg = BUTTON_BG_COLOR,
			font = BUTTON_FONT, 	fg = BUTTON_FG_COLOR,
			command = lambda : controller.show_frame(Loadgame))
		btn_load.place(relx = BUTTON_relx, rely = 0.3)

		btn_quit = tkinter.Button(self, text = "Quit", bg = BUTTON_BG_COLOR,
			font = BUTTON_FONT, 	fg = BUTTON_FG_COLOR,
			command = lambda : quit())
		btn_quit.place(relx = BUTTON_relx, rely = 0.4)		

class Loadgame(tkinter.Frame):
	global LARGE_FONT
	def __init__(self, parent, controller):
		tkinter.Frame.__init__(self, parent)
		PROGRAM_NAME = 'Cidadela do Caos'
		PROGRAM_ICON = './img/castle_01.ico'
		IMAGE_LIST = ['./img/space01.png','./img/citadel_01.png',\
					 './img/citadel_04_c.png', './img/citadel_05.png']
		BUTTON_BG_COLOR = "#ADD8E6"
		BUTTON_FG_COLOR = "#B22222"
		BUTTON_FONT = ("Verdana", 12,  "bold")
		BUTTON_relx = 0.02
		#BUTTON_FONT = tkinter.font(family = "Verdana", size = 20, weight = 'bold')
		BACKGROUND_IMAGE = IMAGE_LIST[3]
		
		imagem = PIL.Image.open(BACKGROUND_IMAGE)
		#resized_image = imagem.resize((WIDTH, HEIGHT))
		resized_image = imagem
		resized_image_tk = ImageTk.PhotoImage(resized_image)

		bg_image = tkinter.PhotoImage(file = BACKGROUND_IMAGE)
		bg_label = tkinter.Label(self, image = resized_image_tk)
		bg_label.image = resized_image_tk
		bg_label.place(relwidth=1, relheight=1)

		btn_start = tkinter.Button(self, text = "New Game", bg = BUTTON_BG_COLOR,
			font = BUTTON_FONT, 	fg = BUTTON_FG_COLOR,
			command = lambda : controller.show_frame(Gamepage))
		btn_start.place(relx = BUTTON_relx, rely = 0.2)#pack(side = tkinter.LEFT)

		btn_load = tkinter.Button(self, text = "Load Game", bg = BUTTON_BG_COLOR,
			font = BUTTON_FONT, 	fg = BUTTON_FG_COLOR,
			command = lambda : controller.show_frame(Loadgame))
		btn_load.place(relx = BUTTON_relx, rely = 0.3)

		btn_quit = tkinter.Button(self, text = "Quit", bg = BUTTON_BG_COLOR,
			font = BUTTON_FONT, 	fg = BUTTON_FG_COLOR,
			command = lambda : quit())
		btn_quit.place(relx = BUTTON_relx, rely = 0.4)		

class Gamepage(tkinter.Frame):
	global LARGE_FONT
	def __init__(self, parent, controller ):
		tkinter.Frame.__init__(self, parent)
		
		mainFrame = tkinter.Frame(self, bg = "yellow")
		mainFrame.pack(fill="both", expand = True)

		frame_a = tkinter.Frame(mainFrame, bg = "red")
		frame_b = tkinter.Frame(mainFrame, bg = "green")
		frame_c = tkinter.Frame(mainFrame, bg = "blue")
		frame_a.grid(row = 0, column = 0, rowspan = 9, columnspan = 9,sticky = "nsew")#side = "left", fill="x", expand = True)#place(relwidth=1, relheight=1) #(relx = BUTTON_relx, rely = 0.4)
		frame_b.grid(row = 0, column = 9, rowspan = 9, columnspan = 1,sticky = "nsew")#side = "left", fill="y",expand = True)
		frame_c.grid(row = 9, column = 0, rowspan = 1, columnspan = 10,sticky = "nsew")#side = "bottom", fill="x", expand = True)#grid(row = 1, column = 0)

		lbl = tkinter.Label(frame_b, text = "STATUS ",
						 font = LARGE_FONT, bg = "green", fg = "yellow")
		lbl.pack(expand = True, fill="both", padx = 2, pady = 2)
		
		btn = tkinter.Button(frame_c, text = "return to MAIN",	font = LARGE_FONT,
		 command = lambda : controller.show_frame(Startpage))
		btn.pack(side = "left", padx = 2, pady = 2)

		btn2 = tkinter.Button(frame_c, text = "Quit",
			command = lambda : quit())
		btn2.pack(side = "left", padx = 2, pady = 2)
	
				

		IMAGE_LIST = ['./img/space01.png','./img/citadel_01.png',\
					 './img/citadel_03.png',				
					 './img/citadel_04_c.png', './img/citadel_05.png']
		BUTTON_BG_COLOR = "#ADD8E6"
		BUTTON_FG_COLOR = "#B22222"
		BUTTON_FONT = ("Verdana", 12,  "bold")
		BUTTON_relx = 0.02
		#BUTTON_FONT = tkinter.font(family = "Verdana", size = 20, weight = 'bold')
		BACKGROUND_IMAGE = IMAGE_LIST[2]

		imagem = ImageTk.PhotoImage(Image.open(IMAGE_LIST[2]))
		lbl3 = tkinter.Label(frame_a, text = "Ilustração", font = LARGE_FONT)
		lbl3.image = imagem
		lbl3.configure(image = imagem)
		lbl3.pack(side = tkinter.LEFT,fill="both", expand = True, padx = 2, pady = 2)

		livro = Book()
		lbl4 = tkinter.Label(frame_a, text = livro.get_page(), anchor = "nw", justify = "left")
		lbl4.pack(side = tkinter.LEFT, fill = "both", expand = True, padx = 15, pady = 15)


class Book():
	def __init__(self):
		print('Livro inicializado')
	def get_page(page_id):
		text = '''Você  ouve  grunhidos  abafados  ao  se  aproximar,
e  vê  duas criaturas de aparência absurda. Do lado esquerdo
está uma criatura horrível, com a cabeça de um cachorro e
o corpo de um grande macaco, flexionando seus braços fortíssimos.
Do outro lado encontra-se de fato o seu oposto, com a cabeça
de um macaco no corpo de um cachorro grande. Este último guarda
se aproxima nas suas quatro patas. Pára a alguns metros de diante
de você, ergue-se sobre as patas traseiras e lhe dirige  a palavra.'''
		return text


"""
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


"""


#mainFrame = tkinter.Frame(root, bg = 'blue', bd = 5)
#mainFrame.pack()


#print('root keys:\n',root.configure().keys())
#print('/===============================================')
#print('root properties:\n', dir(tkinter.Tk))
#print('/===============================================')
#print('canvas keys:\n', canvas.configure().keys())
#print('/===============================================')
#print('PhotoImage: \n', dir(tkinter.PhotoImage))
#print('/===============================================')


#root.mainloop()

#/==================================
#/
#/  Main Program
#/
#/==================================


global LARGE_FONT
LARGE_FONT = ("Verdana", 12)
app = lord_of_the_pages()
app.mainloop()




print('End.')