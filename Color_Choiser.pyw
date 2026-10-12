
# -*- coding: utf-8 -*-
#!/usr/bin/env python

'''
Tomado del Video de la Plataforma en la Pataforma de YouTube

Creado con la Tecnologia de: Tkinter
Desarrollado en: Python 3.8.3 (En este Ejemplo - Modificado)

Nombre del Video:
Create Image Color Detection Software with Python _ GUI Tkinter Color Finder Project(480P)

Modificado por: Cristian M. Veliz Cano
Ejemplo sobre las Librerias: -|colorthief|- y otras Librerias
Mi aporte es solamente, la Modificación

Con esta Magnifica libreria (colorthief), podremos Obtener una Lista de 10 Opciones para poder escoger
entre 10 Obciones en Colores, Tomadas desde una Imagen que sea de nuestra Preferencia, Pudiendo tener
Cualquier Dimención (Tamaño), o Formato de Imagen (*.Formato de Imagen)

Creditos a su o sus DESARROLLADORES Originales
=========================================================

Color Picker From Image es una aplicación de escritorio desarrollada en Python con
Tkinter que permite extraer automáticamente los colores dominantes de cualquier
imagen y obtener sus valores en formato hexadecimal para uso en diseño, desarrollo
web o proyectos gráficos.

La aplicación analiza una imagen seleccionada por el usuario y genera una paleta
de hasta 10 colores principales, mostrándolos visualmente junto con su código hexadecimal
correspondiente.

Características principales
Selección de cualquier imagen desde el sistema
Extracción automática de 10 colores dominantes
Visualización de la paleta de colores en tiempo real
Mostrar valores de color en formato HEX
Copiar un color al portapapeles con un solo clic
Vista previa de la imagen cargada dentro de la aplicación
Opción para abrir la imagen original en el visor del sistema
Botón para limpiar y restaurar la aplicación
Interfaz gráfica simple y ligera
Tecnologías utilizadas
Python
Tkinter (interfaz gráfica)
Pillow (procesamiento de imágenes)
ColorThief (extracción de paletas de color)
AwesomeTkinter (mejoras visuales para la interfaz)
Uso del programa
Selecciona una imagen desde tu computadora.
El programa analizará la imagen automáticamente.
Se generará una paleta con los colores principales.
Haz clic sobre el código HEX para copiarlo al portapapeles.
Aplicaciones
Esta herramienta es útil para:
Diseñadores gráficos
Desarrolladores web
Creación de paletas de color
Identificación de colores en fotografías
Inspiración para diseño visual
'''
##===============================================================================================
##===============================================================================================

from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

from PIL import Image, ImageTk
from colorthief import ColorThief

import os
import webbrowser as wb
import awesometkinter as atk

from Tool_Tip import ToolTip
from tooltips import CreateToolTip

##===============================================================================================
##===============================================================================================

class Path():
    def resource_path(relative_path):
        """Get absolute path to resource, works for dev and for pyinstaller"""
        try:
            #PyInstaller Create a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

##===============================================================================================
##===============================================================================================

root = Tk()
self = root
root.title("Color Picker From Image")

##===============================================================================================
##===============================================================================================

##Ajustando Geometry de App:

app_width = 800
app_height = 470

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

##===============================================================================================
##===============================================================================================

# Variables Globales
filename = ""
Color_str = ""
color1, color2, color3, color4, color5 = "", "", "", "", ""
color6, color7, color8, color9, color10 = "", "", "", "", ""

## Style Configure Button´s
style = ttk.Style()
style.configure('TButton', font = 'arial 16 bold')

## Color Label (Tool_Tip) and (tooltips)
self.background = "#14aaf5"
texto_tolltip = f'Copy To Clipboard\n        Clic Here.'

##===============================================================================================
##===============================================================================================

# Configuración para el Color en App
root.configure(bg = '#e4e8eb')
# Configuración para que no sea Redimencionable
root.resizable(False, False)

#Icon App
ico_app = Path.resource_path('Icon\\icon.png')
image_icon = PhotoImage(file = ico_app)
root.iconphoto(False, image_icon)

root.clipboard_clear()

##===============================================================================================
##===============================================================================================

# Metodos <--------------------------------------------------------------------------------------

## Reseteamos las String-Glovals que contienen los Colores de cada Retangulo del Canvas, y las Lbl.
def Resete_Str_Colors():
	global color1, color2, color3, color4, color5, color6, color7, color8, color9, color10, Color_str

	## Limpiamos las String-Glovals
	color1, color2, color3, color4, color5 = "", "", "", "", ""
	color6, color7, color8, color9, color10, Color_str  = "", "", "", "", "", ""

	## Las Rellenamos Denuevo con los Colores Default de la App
	color1 = '#b8255f'
	color2 = '#db4035'
	color3 = '#ff9933'
	color4 = '#fad000'
	color5 = '#afb83b'

	color6 = '#7ecc49'
	color7 = '#299438'
	color8 = '#6accbc'
	color9 = '#158fad'
	color10 = '#14aaf5'

	return

# Cleaner All (Restore Defauld)
def Restore_From_Button(e = None):
	global filename

	# Variable que contiene la Ruta de la Imagen
	if filename == "":
		pass

	else:

		## Limpiamos el Clipboard
		root.clipboard_clear()
		## Reseteamos las Strin-Glovals de los Colores
		Resete_Str_Colors()
		## Restauramos
		Restore()

		# Colocamos nuestra Imagen Princial dentro del Visor Para las Imagens

		## LLamamos la uvicación (Definitiva) - Con la Clase especial para eso
		Image_Logo = Path.resource_path('Fondo\\Fondo.png')
		## La Ingresamos dentro de Pill para ser leida
		img1 = Image.open(Image_Logo)
		## La Redimencionamos (Puede ser de Cualquier Dimencion, y con casi cualquier formato de Imagen)
		imagen_02 = img1.resize((330,300), Image.Resampling.LANCZOS)
		## La ingresamos dentro del PhotoImage de ImageTk
		img = ImageTk.PhotoImage(imagen_02)

		## La Ingresamos dentro del Visor de Imagenes
		lbl.configure(image = img, width = 310, height = 270)
		## Confirmamos esa Imagen
		lbl.image = img
		## Evento Bind para su Invocación
		lbl.bind('<Button-1>', lambda e: Image_Ruta(e))

		## Reseteamos la Variable que contiene la Ruta de la Imagen
		filename = ""

# Cleaner All (Restore Defauld)
def Restore(e = None):
	global filename, color1, color2, color3, color4, color5, color6, color7, color8, color9, color10, Color_str

	if filename == "":
		pass

	else:

		## Limpiamos el Clipboard
		root.clipboard_clear()
		## Reseteamos las Strin-Glovals de los Colores
		Resete_Str_Colors()

		# Colocamos los Colores en Dicho Retangulo
		colors.itemconfig(id1, fill = color1)
		colors.itemconfig(id2, fill = color2)
		colors.itemconfig(id3, fill = color3)
		colors.itemconfig(id4, fill = color4)
		colors.itemconfig(id5, fill = color5)

		colors2.itemconfig(id6, fill = color6)
		colors2.itemconfig(id7, fill = color7)
		colors2.itemconfig(id8, fill = color8)
		colors2.itemconfig(id9, fill = color9)
		colors2.itemconfig(id10, fill = color10)

		# Y Colocamos cada Nombre en Exa Decimal Nuevamente dentro de Cada Lbl. para ese fin.
		hex1.configure(text = color1)
		hex2.configure(text = color2)
		hex3.configure(text = color3)
		hex4.configure(text = color4)
		hex5.configure(text = color5)
		hex6.configure(text = color6)
		hex7.configure(text = color7)
		hex8.configure(text = color8)
		hex9.configure(text = color9)
		hex10.configure(text = color10)

##===============================================================================================
##===============================================================================================

# Capture Colores From Image
def FindColor():
	global filename, color1, color2, color3, color4, color5, color6, color7, color8, color9, color10, Color_str

	if filename == "":
		pass

	else:

		ct = ColorThief(filename)  # Esto nos debuelve una lista con 10 Colores a Escoger
		palette = ct.get_palette(color_count = 11)

		# Colocamos cada casia en su lugar (10 Colores a ser Tratados)
		rgb1 = palette[0]
		rgb2 = palette[1]
		rgb3 = palette[2]
		rgb4 = palette[3]
		rgb5 = palette[4]
		rgb6 = palette[5]
		rgb7 = palette[6]
		rgb8 = palette[7]
		rgb9 = palette[8]
		rgb10 = palette[9]

		# Tratamos esa lista para sacar el Hexa Decimal de cada Color (Nombre en Hexa Decimal)
		color1 = f'#{rgb1[0]:02x}{rgb1[1]:02x}{rgb1[2]:02x}'
		color2 = f'#{rgb2[0]:02x}{rgb2[1]:02x}{rgb2[2]:02x}'
		color3 = f'#{rgb3[0]:02x}{rgb3[1]:02x}{rgb3[2]:02x}'
		color4 = f'#{rgb4[0]:02x}{rgb4[1]:02x}{rgb4[2]:02x}'
		color5 = f'#{rgb5[0]:02x}{rgb5[1]:02x}{rgb5[2]:02x}'
		color6 = f'#{rgb6[0]:02x}{rgb6[1]:02x}{rgb6[2]:02x}'
		color7 = f'#{rgb7[0]:02x}{rgb7[1]:02x}{rgb7[2]:02x}'
		color8 = f'#{rgb8[0]:02x}{rgb8[1]:02x}{rgb8[2]:02x}'
		color9 = f'#{rgb9[0]:02x}{rgb9[1]:02x}{rgb9[2]:02x}'
		color10 = f'#{rgb10[0]:02x}{rgb10[1]:02x}{rgb10[2]:02x}'
		
		# Los (Colores), los ingresamos dentro de los Retangulos Creados con Canvas
		colors.itemconfig(id1, fill = color1)
		colors.itemconfig(id2, fill = color2)
		colors.itemconfig(id3, fill = color3)
		colors.itemconfig(id4, fill = color4)
		colors.itemconfig(id5, fill = color5)

		colors2.itemconfig(id6, fill = color6)
		colors2.itemconfig(id7, fill = color7)
		colors2.itemconfig(id8, fill = color8)
		colors2.itemconfig(id9, fill = color9)
		colors2.itemconfig(id10, fill = color10)

		# Colocamos cada Nombre de los colores en Hexa Decimal, y los colocamos dentro de las Lbs´s.
		hex1.configure(text = color1)
		hex2.configure(text = color2)
		hex3.configure(text = color3)
		hex4.configure(text = color4)
		hex5.configure(text = color5)
		hex6.configure(text = color6)
		hex7.configure(text = color7)
		hex8.configure(text = color8)
		hex9.configure(text = color9)
		hex10.configure(text = color10)

##===============================================================================================
##===============================================================================================

## Llamamos a los Colores para los Retangulos en el Canvas desde la Función (Resete_Str_Colors())
Resete_Str_Colors()

##===============================================================================================
##===============================================================================================

# Buscamos Cualquier Imagen, Para su extracción de la lista y colocar los colores en Hexa Decimal
def showimage():
	global filename

	#Primero Se Restaura todo
	Restore()
	#Luego Dejamos el Visor de las Imagenes sin nada y con color Negro
	lbl.configure(image = "", width = 310, height = 270)

	#Luego Procederemos a Uvicar que Imagen Deseeamos, con las Extenciones, Correctas (Ext.)
	#O con cualquier Extención (Ext), que sea de Imagen
	filename = fd.askopenfilename(initialdir = "/gui/desktop",
		title = 'Selectet Image File', defaultextension="*.*", filetypes = (("Files Ext.", "*.png; *.jpg"),
		("All Files", "*.*")))  # <----O Cualquier Imagen, (Recordatorio, este es solamente un Ejemplo)

	#Si en caso no se Escoge Nada
	if filename == "":

		#Restaura todo y Nuevamente Tendremos que escoger alguna Imagen
		filename = "Restore"
		Restore_From_Button()

	else:

		#Pero si escogemos una Imagen, se procedera a Tratarla

		img1 = Image.open(filename) #Primero la Abrimos con PIL
		#Luego la Redimencionamos, para que quepa en el Visor, (Lbl) - Puede ser una Imagen de Cualquier Tamaño
		imagen_02 = img1.resize((330,275), Image.Resampling.LANCZOS)
		img = ImageTk.PhotoImage(imagen_02) #Luego la Tratara PhotoImage de ImageTk

		#Luego se Procede a Colocarla en el Viso de Imagenes
		lbl.configure(image = img, width = 310, height = 270)
		lbl.image = img # Y Se Confirma que si se Ingrese

		# Luego la Trataremos con ColorThief
		FindColor()

##===============================================================================================
##===============================================================================================

## Este metodo es solamente para Ver la Imagen Tamaño Real en el Visor de Windos con (webbrowser)
def Image_Ruta(e = None):
	global filename

	if filename == "":
		pass

	else:

		wb.open_new(filename)	#Abrimos la Imagen para su Visualización

##===============================================================================================
##===============================================================================================

# Cuadro para la Imagen
Label(root, width = 120, height = 10, bg = '#4272f9').pack()

# Un Frame para que contenga un Canvas (Lienzo), y poder meter los colores en Retangulos
frame = Frame(root, width = 700, height = 370, bg = '#fff')
frame.place(x=50, y = 50)

#Label Title
Label(frame, text = 'Color Finder', font = 'arial 25 bold', bg = 'white').place(x = 100, y = 20)

# color 1 --|Retangulo donde estaran los colores con el Canvas|--
colors = Canvas(frame, bg = '#fff', width = 150, height = 265, bd = 0)
colors.place(x=20, y = 90)
# Se Crean los Retangulos en el Canvas y los colocamos en el Frame por ID
id1 = colors.create_rectangle((10, 10, 50, 50), fill = color1)
id2 = colors.create_rectangle((10, 50, 50, 100), fill = color2)
id3 = colors.create_rectangle((10, 100, 50, 150), fill = color3)
id4 = colors.create_rectangle((10, 150, 50, 200), fill = color4)
id5 = colors.create_rectangle((10, 200, 50, 250), fill = color5)

## Creamos las Label´s para que contenga el Hexa Decimal de cada Color
hex1 = Label(colors, text = '#b8255f', fg = '#000', font = 'arial 12 bold', bg = 'white')
hex1.place(x = 60, y = 15)
hex1.bind('<Button-1>', lambda e: Color_To_Clipboard.Selected_Color_To_Clipboard_1(e))
ToolTip(hex1, texto_tolltip, background = self.background)

hex2 = Label(colors, text = '#db4035', fg = '#000', font = 'arial 12 bold', bg = 'white')
hex2.place(x = 60, y = 65)
hex2.bind('<Button-1>', lambda e: Color_To_Clipboard.Selected_Color_To_Clipboard_2(e))
ToolTip(hex2, texto_tolltip, background = self.background)

hex3 = Label(colors, text = '#ff9933', fg = '#000', font = 'arial 12 bold', bg = 'white')
hex3.place(x = 60, y = 115)
hex3.bind('<Button-1>', lambda e: Color_To_Clipboard.Selected_Color_To_Clipboard_3(e))
ToolTip(hex3, texto_tolltip, background = self.background)

hex4 = Label(colors, text = '#fad000', fg = '#000', font = 'arial 12 bold', bg = 'white')
hex4.place(x = 60, y = 165)
hex4.bind('<Button-1>', lambda e: Color_To_Clipboard.Selected_Color_To_Clipboard_4(e))
ToolTip(hex4, texto_tolltip, background = self.background)

hex5 = Label(colors, text = '#afb83b', fg = '#000', font = 'arial 12 bold', bg = 'white')
hex5.place(x = 60, y = 215)
hex5.bind('<Button-1>', lambda e: Color_To_Clipboard.Selected_Color_To_Clipboard_5(e))
ToolTip(hex5, texto_tolltip, background = self.background)

# color 2  --|| Lo mismo que en el cuadro de colores anterior ||--
colors2 = Canvas(frame, bg = '#fff', width = 150, height = 265, bd = 0)
colors2.place(x=180, y = 90)

id6 = colors2.create_rectangle((10, 10, 50, 50), fill = color6)
id7 = colors2.create_rectangle((10, 50, 50, 100), fill = color7)
id8 = colors2.create_rectangle((10, 100, 50, 150), fill = color8)
id9 = colors2.create_rectangle((10, 150, 50, 200), fill = color9)
id10 = colors2.create_rectangle((10, 200, 50, 250), fill = color10)

hex6 = Label(colors2, text = '#7ecc49', fg = '#000', font = 'arial 12 bold', bg = 'white')
hex6.place(x = 60, y = 15)
hex6.bind('<Button-1>', lambda e: Color_To_Clipboard.Selected_Color_To_Clipboard_6(e))
CreateToolTip(hex6, texto_tolltip, background = self.background)

hex7 = Label(colors2, text = '#299438', fg = '#000', font = 'arial 12 bold', bg = 'white')
hex7.place(x = 60, y = 65)
hex7.bind('<Button-1>', lambda e: Color_To_Clipboard.Selected_Color_To_Clipboard_7(e))
CreateToolTip(hex7, texto_tolltip, background = self.background)

hex8 = Label(colors2, text = '#6accbc', fg = '#000', font = 'arial 12 bold', bg = 'white')
hex8.place(x = 60, y = 115)
hex8.bind('<Button-1>', lambda e: Color_To_Clipboard.Selected_Color_To_Clipboard_8(e))
CreateToolTip(hex8, texto_tolltip, background = self.background)

hex9 = Label(colors2, text = '#158fad', fg = '#000', font = 'arial 12 bold', bg = 'white')
hex9.place(x = 60, y = 165)
hex9.bind('<Button-1>', lambda e: Color_To_Clipboard.Selected_Color_To_Clipboard_9(e))
CreateToolTip(hex9, texto_tolltip, background = self.background)

hex10 = Label(colors2, text = '#14aaf5', fg = '#000', font = 'arial 12 bold', bg = 'white')
hex10.place(x = 60, y = 215)
hex10.bind('<Button-1>', lambda e: Color_To_Clipboard.Selected_Color_To_Clipboard_10(e))
CreateToolTip(hex10, texto_tolltip, background = self.background)

##=======================================================
##=======================================================

# Frame Button´s
selectetimage = atk.Frame3d(frame, style='TFrame', padding=0, bg = 'white')
selectetimage.place(x = 350, y = 10, width = 340, height = 350)

## Button´s forma Original
#Button(selectetimage, text = 'Selectet Image', width = 12, height = 1, font = 'arial 14 bold', command = showimage).place(x = 10, y = 300)
#Button(selectetimage, text = 'Clean', width = 12, height = 1, font = 'arial 14 bold', command = Restore_From_Button).place(x = 176, y = 300)

## Button´s forma Alterada con (awesometkinter)
btn1 = atk.Button3d(selectetimage, text = 'Selectet Image', style='TButton', bg = '#d6dee5', padding=0, command = showimage)
btn1.place(x = 9, y = 293, height=46, width=180, bordermode=OUTSIDE)
btn1.configure(text = 'Selectet Image')

btn2 = atk.Button3d(selectetimage, text = 'Clean', style='TButton', padding=0, bg = '#d6dee5', command = Restore_From_Button)
btn2.place(x = 200, y = 293, height=46, width=130, bordermode=OUTSIDE)
btn2.configure(text = 'Clean')

##=======================================================
##=======================================================

## Frame Logo
f = Frame(selectetimage, bd = 3, bg = 'black', width = '320', height = 280, relief = GROOVE)
f.place(x = 10, y = 10)

## Logo  --|Ingresamos la Imagen que tenemos para ese Fin|-- desde la Carpeta Fondo (Fondo.png)
Image_Logo = Path.resource_path('Fondo\\Fondo.png')
img1 = Image.open(Image_Logo)
imagen_02 = img1.resize((330,300), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(imagen_02)

lbl = Label(f, bg = 'black')  ## Creamos el Visor con desde esta Label
lbl.place(x = 0, y = 0)

lbl.configure(image = img, width = 310, height = 270)## Ingresamos La Imagen
lbl.image = img  ## La Ingresamos (Y Confirmamos)
lbl.bind('<Button-1>', lambda e: Image_Ruta(e)) # Evento Virtual que Invoca a la Imagen

##===============================================================================================
##===============================================================================================

## Evento Para Cerrar la App. con la Tecla en el KeyBoard-Escape (ESC).
root.bind('<Escape>', lambda e: root.quit())

##===============================================================================================
##===============================================================================================

# Clase para Copiar al Portapapeles (Clipboard), el Color Escogido, dentro de las 10 Opciones de color

class Color_To_Clipboard():

	def __init__(self):
		super().__init__()
	'''
	Cada Lbl, Invoca Segun que LABEL con un CLIC (NORMAL), y segun que COLOR contenga al igual que el
	Retangulo Creado en Canvas
	'''

	## Lbl (hex1)
	def Selected_Color_To_Clipboard_1(e = None):
		global color1, Color_str

		self.clipboard_clear()
		Color_str = color1
		self.background = Color_str

		self.clipboard_clear()
		self.clipboard_append(string=Color_str)

	## Lbl (hex2)
	def Selected_Color_To_Clipboard_2(e = None):
		global color2, Color_str

		self.clipboard_clear()
		Color_str = color2
		self.background = Color_str

		self.clipboard_clear()
		self.clipboard_append(string=Color_str)

	## Lbl (hex3)
	def Selected_Color_To_Clipboard_3(e = None):
		global color3, Color_str

		self.clipboard_clear()
		Color_str = color3
		self.background = Color_str

		self.clipboard_clear()
		self.clipboard_append(string=Color_str)

	## Lbl (hex4)
	def Selected_Color_To_Clipboard_4(e = None):
		global color4, Color_str

		self.clipboard_clear()
		Color_str = color4
		self.background = Color_str

		self.clipboard_clear()
		self.clipboard_append(string=Color_str)

	## Lbl (hex5)
	def Selected_Color_To_Clipboard_5(e = None):
		global color5, Color_str

		self.clipboard_clear()
		Color_str = color5
		self.background = Color_str

		self.clipboard_clear()
		self.clipboard_append(string=Color_str)

	## Lbl (hex6)
	def Selected_Color_To_Clipboard_6(e = None):
		global color6, Color_str

		self.clipboard_clear()
		Color_str = color6
		self.background = Color_str

		self.clipboard_clear()
		self.clipboard_append(string=Color_str)

	## Lbl (hex7)
	def Selected_Color_To_Clipboard_7(e = None):
		global color7, Color_str

		self.clipboard_clear()
		Color_str = color7
		self.background = Color_str

		self.clipboard_clear()
		self.clipboard_append(string=Color_str)

	## Lbl (hex8)
	def Selected_Color_To_Clipboard_8(e = None):
		global color8, Color_str

		self.clipboard_clear()
		Color_str = color8
		self.background = Color_str

		self.clipboard_clear()
		self.clipboard_append(string=Color_str)

	## Lbl (hex9)
	def Selected_Color_To_Clipboard_9(e = None):
		global color9, Color_str

		self.clipboard_clear()
		Color_str = color9
		self.background = Color_str

		self.clipboard_clear()
		self.clipboard_append(string=Color_str)

	## Lbl (hex10)
	def Selected_Color_To_Clipboard_10(e = None):
		global color10, Color_str

		self.clipboard_clear()
		Color_str = color10
		self.background = Color_str

		self.clipboard_clear()
		self.clipboard_append(string=Color_str)

##===============================================================================================
##===============================================================================================

## Inniciamos el Loop (Bukle) en nuestra App.-
root.mainloop()

##===============================================================================================
##===============================================================================================