from tkinter import *
from PIL import Image, ImageTk

"""Script that potrais images and lets the user sort the image to either POSE, CALM, OFFENSIVE or ANON 
categories. After images are all shown, a text file is created for later analysis. 
This is for a human computer interaction course"""

def tallenna_tulos(nimi, a):		#saves results in a file called taxonomy_A
    tiedosto = open(nimi, "a") 
    tiedosto.write("%s\n"   % (a))
    tiedosto.close()

lista = []			#list for the results

class App:
	def __init__(self, master, lista):
	
		self.master = master
		self.lista = lista
		self.a = 1
		self.kuukausi = "aug"		#starting month, ends in september
		self.kuva = 1				#number of the picture
		self.w = Label(master, text= self.a)
		self.w.grid(row = 0, column = 0)
		self.canvas = Canvas(master, width = 750, height = 500)
		self.canvas.grid(row = 1, column = 0)
		self.photo = Image.open('%s (%s).jpg' % (self.kuukausi, self.kuva)) 	#example, opens image aug(1).jpg
		self.photo = ImageTk.PhotoImage(self.photo)
		self.pic = self.canvas.create_image(375,250, image=self.photo)
		self.frame = Frame(master)
		self.frame.grid(row = 2, column = 0)
		
		self.nappi_a= Button(self.frame, text="Pose", command =self.nappi_A)
		self.nappi_a.pack(side=LEFT)
		
		self.nappi_b= Button(self.frame, text="Calm", command = self.nappi_B)
		self.nappi_b.pack(side=LEFT)
		
		self.nappi_c= Button(self.frame, text="Offensive", command = self.nappi_C)
		self.nappi_c.pack(side=LEFT)
		
		self.nappi_d= Button(self.frame, text="Anon", command = self.nappi_D)
		self.nappi_d.pack(side=LEFT)
	
	def nappi_A(self):		#if button a is pressed, decide what the next image is and anppend result with button number
		self.lista.append(1)
		if self.kuva < 29 and self.kuukausi =="aug":
			self.kuva = self.kuva +1
		elif self.kuukausi == "aug":
			self.kuukausi = "july"
			self.kuva = 1
		elif self.kuva < 23 and self.kuukausi =="july":
			self.kuva = self.kuva +1
		elif self.kuukausi == "july":
			self.kuukausi = "june"
			self.kuva = 1
		elif self.kuva < 87 and self.kuukausi =="june":
			self.kuva = self.kuva +1
		elif self.kuukausi == "june":
			self.kuukausi = "may"
			self.kuva = 1
		elif self.kuva < 31 and self.kuukausi =="may":
			self.kuva = self.kuva +1
		elif self.kuukausi == "may":
			self.kuukausi = "nov"
			self.kuva = 1
		elif self.kuva < 69 and self.kuukausi =="nov":
			self.kuva = self.kuva +1
		elif self.kuukausi == "nov":
			self.kuukausi = "oct"
			self.kuva = 1
		elif self.kuva < 98 and self.kuukausi =="oct":
			self.kuva = self.kuva +1
		elif self.kuukausi == "oct":
			self.kuukausi = "sep"
			self.kuva = 1
		elif self.kuva < 36 and self.kuukausi =="sep":
			self.kuva = self.kuva +1
		elif self.kuukausi == "sep":
			self.master.quit()	#no more pics
		self.a = self.a +1				
		self.w.config(text=self.a)
		self.photo = Image.open('%s (%s).jpg' % (self.kuukausi, self.kuva))		#loads the next image
		self.photo = ImageTk.PhotoImage(self.photo)
		self.canvas.itemconfig(self.pic, image = self.photo)
		
	def nappi_B(self):	#on button b click
		self.lista.append(2)
		if self.kuva < 29 and self.kuukausi =="aug":
			self.kuva = self.kuva +1
		elif self.kuukausi == "aug":
			self.kuukausi = "july"
			self.kuva = 1
		elif self.kuva < 23 and self.kuukausi =="july":
			self.kuva = self.kuva +1
		elif self.kuukausi == "july":
			self.kuukausi = "june"
			self.kuva = 1
		elif self.kuva < 87 and self.kuukausi =="june":
			self.kuva = self.kuva +1
		elif self.kuukausi == "june":
			self.kuukausi = "may"
			self.kuva = 1
		elif self.kuva < 31 and self.kuukausi =="may":
			self.kuva = self.kuva +1
		elif self.kuukausi == "may":
			self.kuukausi = "nov"
			self.kuva = 1
		elif self.kuva < 69 and self.kuukausi =="nov":
			self.kuva = self.kuva +1
		elif self.kuukausi == "nov":
			self.kuukausi = "oct"
			self.kuva = 1
		elif self.kuva < 98 and self.kuukausi =="oct":
			self.kuva = self.kuva +1
		elif self.kuukausi == "oct":
			self.kuukausi = "sep"
			self.kuva = 1
		elif self.kuva < 36 and self.kuukausi =="sep":
			self.kuva = self.kuva +1
		elif self.kuukausi == "sep":
			self.master.quit()
		self.a = self.a +1
		self.w.config(text=self.a)
		self.photo = Image.open('%s (%s).jpg' % (self.kuukausi, self.kuva))
		self.photo = ImageTk.PhotoImage(self.photo)
		self.canvas.itemconfig(self.pic, image = self.photo)
		
	def nappi_C(self):	#on button c click
		self.lista.append(3)
		if self.kuva < 29 and self.kuukausi =="aug":
			self.kuva = self.kuva +1
		elif self.kuukausi == "aug":
			self.kuukausi = "july"
			self.kuva = 1
		elif self.kuva < 23 and self.kuukausi =="july":
			self.kuva = self.kuva +1
		elif self.kuukausi == "july":
			self.kuukausi = "june"
			self.kuva = 1
		elif self.kuva < 87 and self.kuukausi =="june":
			self.kuva = self.kuva +1
		elif self.kuukausi == "june":
			self.kuukausi = "may"
			self.kuva = 1
		elif self.kuva < 31 and self.kuukausi =="may":
			self.kuva = self.kuva +1
		elif self.kuukausi == "may":
			self.kuukausi = "nov"
			self.kuva = 1
		elif self.kuva < 69 and self.kuukausi =="nov":
			self.kuva = self.kuva +1
		elif self.kuukausi == "nov":
			self.kuukausi = "oct"
			self.kuva = 1
		elif self.kuva < 98 and self.kuukausi =="oct":
			self.kuva = self.kuva +1
		elif self.kuukausi == "oct":
			self.kuukausi = "sep"
			self.kuva = 1
		elif self.kuva < 36 and self.kuukausi =="sep":
			self.kuva = self.kuva +1
		elif self.kuukausi == "sep":
			self.master.quit()
		self.a = self.a +1
		self.w.config(text=self.a)
		self.photo = Image.open('%s (%s).jpg' % (self.kuukausi, self.kuva))
		self.photo = ImageTk.PhotoImage(self.photo)
		self.canvas.itemconfig(self.pic, image = self.photo)
	
	def nappi_D(self):	#on button d click
		self.lista.append(4)
		if self.kuva < 29 and self.kuukausi =="aug":
			self.kuva = self.kuva +1
		elif self.kuukausi == "aug":
			self.kuukausi = "july"
			self.kuva = 1
		elif self.kuva < 23 and self.kuukausi =="july":
			self.kuva = self.kuva +1
		elif self.kuukausi == "july":
			self.kuukausi = "june"
			self.kuva = 1
		elif self.kuva < 87 and self.kuukausi =="june":
			self.kuva = self.kuva +1
		elif self.kuukausi == "june":
			self.kuukausi = "may"
			self.kuva = 1
		elif self.kuva < 31 and self.kuukausi =="may":
			self.kuva = self.kuva +1
		elif self.kuukausi == "may":
			self.kuukausi = "nov"
			self.kuva = 1
		elif self.kuva < 69 and self.kuukausi =="nov":
			self.kuva = self.kuva +1
		elif self.kuukausi == "nov":
			self.kuukausi = "oct"
			self.kuva = 1
		elif self.kuva < 98 and self.kuukausi =="oct":
			self.kuva = self.kuva +1
		elif self.kuukausi == "oct":
			self.kuukausi = "sep"
			self.kuva = 1
		elif self.kuva < 36 and self.kuukausi =="sep":
			self.kuva = self.kuva +1
		elif self.kuukausi == "sep":
			self.master.quit()
		self.a = self.a +1
		self.w.config(text=self.a)
		self.photo = Image.open('%s (%s).jpg' % (self.kuukausi, self.kuva))
		self.photo = ImageTk.PhotoImage(self.photo)
		self.canvas.itemconfig(self.pic, image = self.photo)
		
root = Tk()
app = App(root, lista)
root.mainloop()
tallenna_tulos("taxonomy_A", lista)