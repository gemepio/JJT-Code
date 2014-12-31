#Alpha
import sqlite3
import Tkinter
from Tkinter import *
from pylab import *
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import math
from PIL import ImageTk, Image
def dependencies_for_myprogram():
    from scipy.sparse.csgraph import _validation
        
class Application(Frame):
        global funcsel
        def __init__(self, master):
        #Initialize the Frame 
                Frame.__init__(self, master)
                self.grid()
                self.create_widgets()
        
        def create_widgets(self):
                        
                self.img = ImageTk.PhotoImage(Image.open("JTT-Logo1.tiff"))
                self.panel = Label(self, image = self.img)
                self.panel.grid(row =1, column =1, columnspan =4)
                
                self.instruction = Label(self, text = "Company Name:")
                self.instruction.grid(row =7, column =0, columnspan =2, sticky = W)
                self.Name = Entry(self)
                self.Name.grid(row =7, column =2, sticky =E)
                
                self.instruction = Label(self, text = "Vessel Type:")
                self.instruction.grid(row =8, column =0, columnspan =2, sticky = W)
                self.Type = Entry(self)
                self.Type.grid(row =8, column =2, sticky =E)
                
                
                self.instruction = Label(self, text = "Shell Geometry:")
                self.instruction.grid(row =9, column =0, columnspan =2, sticky = W)
                self.OPTIONS = ["Vertical Plate","Horizontal Roof","Vertical Cylinder","Horizontal Cylinder"]
                self.SGvar = StringVar(self)
                self.SGvar.set(self.OPTIONS[0])
                self.SG = apply(OptionMenu, (self, self.SGvar) +tuple(self.OPTIONS))
                self.SG.grid(row =9, column =1, columnspan =2, sticky = E)
                
                
                self.instruction = Label(self, text = "Layers of Refractory")
                self.instruction.grid(row =11, column =0, columnspan =2, sticky = W)
                self.Layer = Entry(self)
                self.Layer.grid(row =11, column =2, sticky =E)
                
                self.btnLayer = Tkinter.Button(self, text = "Confirm/Edit", command = self.Toplevel)
                self.btnLayer.grid(row=11, column =4, sticky = E)               
                
                
                self.instruction = Label(self, text = "Operating Temp." )
                self.instruction.grid(row =12, column =0, columnspan =2, sticky = W)
                self.Ti = Entry(self)
                self.Ti.grid(row =12, column =2, sticky = E)
                
                self.instruction = Label(self, text = "Ambient Temp." )
                self.instruction.grid(row =13, column =0, columnspan =2, sticky = W)
                self.To = Entry(self)
                self.To.grid(row =13, column =2, sticky = E)

                #self.instruction = Label(self, text = "h1" )
                #self.instruction.grid(row =14, column =0, columnspan =2, sticky = W)
                #self.h1 = Entry(self)
                #self.h1.grid(row =14, column =2, sticky = E)

                #self.instruction = Label(self, text = "h2" )
                #self.instruction.grid(row =15, column =0, columnspan =2, sticky = W)
                #self.h2 = Entry(self)
                #self.h2.grid(row =15, column =2, sticky = E)

                self.btn1 = Tkinter.Button(self, text ="Calculate", command = self.reveal)
                self.btn1.grid(row = 13, column = 4, sticky = E)
                
                self.text =Tkinter.Text(self, width = 60, height = 5, wrap = WORD)
                self.text.grid(row = 17, column = 0, columnspan =4, sticky = W)
                self.text.configure(state='disabled')

        def updateoptions(self, *args):
            global w
            rows=[]
            CTsel=w.CTvar.get().strip("'(,)'")
            castable = sqlite3.connect("castable.db")
            castable.text_factory = str
            tb=castable.cursor()
            tb.execute("select name from " + CTsel)
            rows = tb.fetchall()
            
            w.MRvar.set(rows[0])
            #menu.append(w.MR_op_menu['menu'])
            menu = w.MR_op_menu['menu']
            menu.delete(0, END)
            for row in rows:
                menu.add_command(label=row, command=lambda row=row: w.MRvar.set(row))
        def updateoptions2(self, *args):
            global w
            rows=[]
            CTsel=w.CTvar2.get().strip("'(,)'")
            castable = sqlite3.connect("castable.db")
            castable.text_factory = str
            tb=castable.cursor()
            tb.execute("select name from " + CTsel)
            rows = tb.fetchall()
            
            w.MRvar2.set(rows[0])
            #menu.append(w.MR_op_menu['menu'])
            menu = w.MR_op_menu2['menu']
            menu.delete(0, END)
            for row in rows:
                menu.add_command(label=row, command=lambda row=row: w.MRvar2.set(row))
        def updateoptions3(self, *args):
            global w
            rows=[]
            CTsel=w.CTvar3.get().strip("'(,)'")
            castable = sqlite3.connect("castable.db")
            castable.text_factory = str
            tb=castable.cursor()
            tb.execute("select name from " + CTsel)
            rows = tb.fetchall()
            
            w.MRvar3.set(rows[0])
            #menu.append(w.MR_op_menu['menu'])
            menu = w.MR_op_menu3['menu']
            menu.delete(0, END)
            for row in rows:
                menu.add_command(label=row, command=lambda row=row: w.MRvar3.set(row))
        def updateoptions4(self, *args):
            global w
            rows=[]
            CTsel=w.CTvar4.get().strip("'(,)'")
            castable = sqlite3.connect("castable.db")
            castable.text_factory = str
            tb=castable.cursor()
            tb.execute("select name from " + CTsel)
            rows = tb.fetchall()
            
            w.MRvar4.set(rows[0])
            #menu.append(w.MR_op_menu['menu'])
            menu = w.MR_op_menu4['menu']
            menu.delete(0, END)
            for row in rows:
                menu.add_command(label=row, command=lambda row=row: w.MRvar4.set(row))
        def updateoptions5(self, *args):
            global w
            rows=[]
            CTsel=w.CTvar5.get().strip("'(,)'")
            castable = sqlite3.connect("castable.db")
            castable.text_factory = str
            tb=castable.cursor()
            tb.execute("select name from " + CTsel)
            rows = tb.fetchall()
            
            w.MRvar5.set(rows[0])
            #menu.append(w.MR_op_menu['menu'])
            menu = w.MR_op_menu5['menu']
            menu.delete(0, END)
            for row in rows:
                menu.add_command(label=row, command=lambda row=row: w.MRvar5.set(row))

        def MRmatch(self):
            global w
            CTsel=w.CTvar.get().strip("'(,)'")
            WRsel=w.MRvar.get().strip("'(,)'")
            if CTsel == "catalog":
                castable = sqlite3.connect("castable.db")
                castable.text_factory = str
                tb=castable.cursor()
                tb.execute("select id from catalog where name == ?", [WRsel])
                id = tb.fetchone()
            elif CTsel == "castable":
                castable = sqlite3.connect("castable.db")
                tb=castable.cursor()
                tb.execute("select id from castable where name == ?", [WRsel])
                id = tb.fetchone()
            elif CTsel == "brick":
                castable = sqlite3.connect("castable.db")
                tb=castable.cursor()
                tb.execute("select id from brick where name == ?", [WRsel])
                id = tb.fetchone()
            print id
            return id
            
        def MRmatch2(self):
            global w
            CTsel=w.CTvar2.get().strip("'(,)'")
            WRsel=w.MRvar2.get().strip("'(,)'")
            if CTsel == "catalog":
                castable = sqlite3.connect("castable.db")
                castable.text_factory = str
                tb=castable.cursor()
                tb.execute("select id from catalog where name == ?", [WRsel])
                id = tb.fetchone()
            elif CTsel == "castable":
                castable = sqlite3.connect("castable.db")
                tb=castable.cursor()
                tb.execute("select id from castable where name == ?", [WRsel])
                id = tb.fetchone()
            elif CTsel == "brick":
                castable = sqlite3.connect("castable.db")
                tb=castable.cursor()
                tb.execute("select id from brick where name == ?", [WRsel])
                id = tb.fetchone()
            print id
            return id
            
        def MRmatch3(self):
            global w
            CTsel=w.CTvar3.get().strip("'(,)'")
            WRsel=w.MRvar3.get().strip("'(,)'")
            if CTsel == "catalog":
                castable = sqlite3.connect("castable.db")
                castable.text_factory = str
                tb=castable.cursor()
                tb.execute("select id from catalog where name == ?", [WRsel])
                id = tb.fetchone()
            elif CTsel == "castable":
                castable = sqlite3.connect("castable.db")
                tb=castable.cursor()
                tb.execute("select id from castable where name == ?", [WRsel])
                id = tb.fetchone()
            elif CTsel == "brick":
                castable = sqlite3.connect("castable.db")
                tb=castable.cursor()
                tb.execute("select id from brick where name == ?", [WRsel])
                id = tb.fetchone()
            print id
            return id
            
        def MRmatch4(self):
            global w
            CTsel=w.CTvar4.get().strip("'(,)'")
            WRsel=w.MRvar4.get().strip("'(,)'")
            if CTsel == "catalog":
                castable = sqlite3.connect("castable.db")
                castable.text_factory = str
                tb=castable.cursor()
                tb.execute("select id from catalog where name == ?", [WRsel])
                id = tb.fetchone()
            elif CTsel == "castable":
                castable = sqlite3.connect("castable.db")
                tb=castable.cursor()
                tb.execute("select id from castable where name == ?", [WRsel])
                id = tb.fetchone()
            elif CTsel == "brick":
                castable = sqlite3.connect("castable.db")
                tb=castable.cursor()
                tb.execute("select id from brick where name == ?", [WRsel])
                id = tb.fetchone()
            print id
            return id
            
        def MRmatch5(self):
            global w
            CTsel=w.CTvar5.get().strip("'(,)'")
            WRsel=w.MRvar5.get().strip("'(,)'")
            if CTsel == "catalog":
                castable = sqlite3.connect("castable.db")
                castable.text_factory = str
                tb=castable.cursor()
                tb.execute("select id from catalog where name == ?", [WRsel])
                id = tb.fetchone()
            elif CTsel == "castable":
                castable = sqlite3.connect("castable.db")
                tb=castable.cursor()
                tb.execute("select id from castable where name == ?", [WRsel])
                id = tb.fetchone()
            elif CTsel == "brick":
                castable = sqlite3.connect("castable.db")
                tb=castable.cursor()
                tb.execute("select id from brick where name == ?", [WRsel])
                id = tb.fetchone()
            print id
            return id 
            
        def Toplevel(self):
                global Layer, w
                Layer = int(self.Layer.get())
                funcsel = self.SGvar.get()
                
                w = Toplevel()
                w.title("Input")
                #w.geometry("500x310")
                castable = sqlite3.connect("castable.db")
                castable.text_factory = str
                tb=castable.cursor()
                tb.execute("select tbl_name from sqlite_master where type='table'")
                TB_names = tb.fetchall()
                if funcsel == "Vertical Plate" or funcsel =="Horizontal Roof":
                    if Layer == 1:
                        instruction = Label(w, text = "L (Length/m)" )
                        instruction.grid(row =1, column =0, columnspan =2, sticky = W)
                        self.L = Entry(w)
                        self.L.grid(row =1, column =2, sticky = E)
                    
                        instruction = Label(w, text = "K (Thermal Conductivity)" )
                        instruction.grid(row =2, column =0, columnspan =2, sticky = W)
                        w.CTvar=Tkinter.StringVar(w)
                        w.MRvar=Tkinter.StringVar(w)
                        w.CTvar.trace('w',self.updateoptions)
                        w.CT_op_menu=Tkinter.OptionMenu(w, w.CTvar, *TB_names)
                        w.MR_op_menu=Tkinter.OptionMenu(w, w.MRvar, '')
                        w.CTvar.set(TB_names[0]) 
                        w.CT_op_menu.grid(row = 2, column =1, columnspan =2)
                        w.MR_op_menu.grid(row = 2, column =3, columnspan =2,sticky = E)
                        w.CT_op_menu.config(width=10)
                        w.MR_op_menu.config(width=20)
                        #self.K = Entry(w)
                        #self.K.grid(row =2, column =2, sticky = E)     
            
                        btnsave = Tkinter.Button(w, text="Save", command = self.save1)
                        btnsave.grid(row =3, column =2, sticky =E)              
                    elif Layer ==2:
                        instruction = Label(w, text = "L1 (Length/m)" )
                        instruction.grid(row =1, column =0, columnspan =2, sticky = W)
                        self.L1 = Entry(w)
                        self.L1.grid(row =1, column =2, sticky = E)
                    
                        instruction = Label(w, text = "K1 (Thermal Conductivity)" )
                        instruction.grid(row =2, column =0, columnspan =2, sticky = W)
                        w.CTvar=Tkinter.StringVar(w)
                        w.MRvar=Tkinter.StringVar(w)
                        w.CTvar.trace('w',self.updateoptions)
                        w.CT_op_menu=Tkinter.OptionMenu(w, w.CTvar, *TB_names)
                        w.MR_op_menu=Tkinter.OptionMenu(w, w.MRvar, '')
                        w.CTvar.set(TB_names[0]) 
                        w.CT_op_menu.grid(row = 2, column =1, columnspan =2)
                        w.MR_op_menu.grid(row = 2, column =3, columnspan =2,sticky = E)
                        w.CT_op_menu.config(width=10)
                        w.MR_op_menu.config(width=20)
            
                        instruction = Label(w, text = "L2 (Length/m)" )
                        instruction.grid(row =3, column =0, columnspan =2, sticky = W)
                        self.L2 = Entry(w)
                        self.L2.grid(row =3, column =2, sticky = E)
                    
                        instruction = Label(w, text = "K2 (Thermal Conductivity)" )
                        instruction.grid(row =4, column =0, columnspan =2, sticky = W)
                        w.CTvar2=Tkinter.StringVar(w)
                        w.MRvar2=Tkinter.StringVar(w)
                        w.CTvar2.trace('w',self.updateoptions2)
                        w.CT_op_menu2=Tkinter.OptionMenu(w, w.CTvar2, *TB_names)
                        w.MR_op_menu2=Tkinter.OptionMenu(w, w.MRvar2, '')
                        w.CTvar2.set(TB_names[0]) 
                        w.CT_op_menu2.grid(row = 4, column =1, columnspan =2)
                        w.MR_op_menu2.grid(row = 4, column =3, columnspan =2,sticky = E)
                        w.CT_op_menu2.config(width=10)
                        w.MR_op_menu2.config(width=20) 
            
                        btnsave = Tkinter.Button(w, text="Save", command = self.save2)
                        btnsave.grid(row =5, column =2, sticky =E)                                      
                    elif Layer ==3:
                        instruction = Label(w, text = "L1 (Length/m)" )
                        instruction.grid(row =1, column =0, columnspan =2, sticky = W)
                        self.L1 = Entry(w)
                        self.L1.grid(row =1, column =2, sticky = E)
                    
                        instruction = Label(w, text = "K1 (Thermal Conductivity)" )
                        instruction.grid(row =2, column =0, columnspan =2, sticky = W)
                        w.CTvar=Tkinter.StringVar(w)
                        w.MRvar=Tkinter.StringVar(w)
                        w.CTvar.trace('w',self.updateoptions)
                        w.CT_op_menu=Tkinter.OptionMenu(w, w.CTvar, *TB_names)
                        w.MR_op_menu=Tkinter.OptionMenu(w, w.MRvar, '')
                        w.CTvar.set(TB_names[0]) 
                        w.CT_op_menu.grid(row = 2, column =1, columnspan =2)
                        w.MR_op_menu.grid(row = 2, column =3, columnspan =2,sticky = E)
                        w.CT_op_menu.config(width=10)
                        w.MR_op_menu.config(width=20)
            
                        instruction = Label(w, text = "L2 (Length/m)" )
                        instruction.grid(row =3, column =0, columnspan =2, sticky = W)
                        self.L2 = Entry(w)
                        self.L2.grid(row =3, column =2, sticky = E)
                    
                        instruction = Label(w, text = "K2 (Thermal Conductivity)" )
                        instruction.grid(row =4, column =0, columnspan =2, sticky = W)
                        w.CTvar2=Tkinter.StringVar(w)
                        w.MRvar2=Tkinter.StringVar(w)
                        w.CTvar2.trace('w',self.updateoptions2)
                        w.CT_op_menu2=Tkinter.OptionMenu(w, w.CTvar2, *TB_names)
                        w.MR_op_menu2=Tkinter.OptionMenu(w, w.MRvar2, '')
                        w.CTvar2.set(TB_names[0]) 
                        w.CT_op_menu2.grid(row = 4, column =1, columnspan =2)
                        w.MR_op_menu2.grid(row = 4, column =3, columnspan =2,sticky = E)
                        w.CT_op_menu2.config(width=10)
                        w.MR_op_menu2.config(width=20)    
            
                        instruction = Label(w, text = "L3 (Length/m)" )
                        instruction.grid(row =5, column =0, columnspan =2, sticky = W)
                        self.L3 = Entry(w)
                        self.L3.grid(row =5, column =2, sticky = E)
                    
                        instruction = Label(w, text = "K3 (Thermal Conductivity)" )
                        instruction.grid(row =6, column =0, columnspan =2, sticky = W)
                        w.CTvar3=Tkinter.StringVar(w)
                        w.MRvar3=Tkinter.StringVar(w)
                        w.CTvar3.trace('w',self.updateoptions3)
                        w.CT_op_menu3=Tkinter.OptionMenu(w, w.CTvar3, *TB_names)
                        w.MR_op_menu3=Tkinter.OptionMenu(w, w.MRvar3, '')
                        w.CTvar3.set(TB_names[0]) 
                        w.CT_op_menu3.grid(row = 6, column =1, columnspan =2)
                        w.MR_op_menu3.grid(row = 6, column =3, columnspan =2,sticky = E)
                        w.CT_op_menu3.config(width=10)
                        w.MR_op_menu3.config(width=20)
    
                        btnsave = Tkinter.Button(w, text="Save", command = self.save3)
                        btnsave.grid(row =7, column =2, sticky =E)      
                    elif Layer ==4:
                        instruction = Label(w, text = "L1 (Length/m)" )
                        instruction.grid(row =1, column =0, columnspan =2, sticky = W)
                        self.L1 = Entry(w)
                        self.L1.grid(row =1, column =2, sticky = E)
                    
                        instruction = Label(w, text = "K1 (Thermal Conductivity)" )
                        instruction.grid(row =2, column =0, columnspan =2, sticky = W)
                        w.CTvar=Tkinter.StringVar(w)
                        w.MRvar=Tkinter.StringVar(w)
                        w.CTvar.trace('w',self.updateoptions)
                        w.CT_op_menu=Tkinter.OptionMenu(w, w.CTvar, *TB_names)
                        w.MR_op_menu=Tkinter.OptionMenu(w, w.MRvar, '')
                        w.CTvar.set(TB_names[0]) 
                        w.CT_op_menu.grid(row = 2, column =1, columnspan =2)
                        w.MR_op_menu.grid(row = 2, column =3, columnspan =2,sticky = E)
                        w.CT_op_menu.config(width=10)
                        w.MR_op_menu.config(width=20)
            
                        instruction = Label(w, text = "L2 (Length/m)" )
                        instruction.grid(row =3, column =0, columnspan =2, sticky = W)
                        self.L2 = Entry(w)
                        self.L2.grid(row =3, column =2, sticky = E)
                    
                        instruction = Label(w, text = "K2 (Thermal Conductivity)" )
                        instruction.grid(row =4, column =0, columnspan =2, sticky = W)
                        w.CTvar2=Tkinter.StringVar(w)
                        w.MRvar2=Tkinter.StringVar(w)
                        w.CTvar2.trace('w',self.updateoptions2)
                        w.CT_op_menu2=Tkinter.OptionMenu(w, w.CTvar2, *TB_names)
                        w.MR_op_menu2=Tkinter.OptionMenu(w, w.MRvar2, '')
                        w.CTvar2.set(TB_names[0]) 
                        w.CT_op_menu2.grid(row = 4, column =1, columnspan =2)
                        w.MR_op_menu2.grid(row = 4, column =3, columnspan =2,sticky = E)
                        w.CT_op_menu2.config(width=10)
                        w.MR_op_menu2.config(width=20)    
            
                        instruction = Label(w, text = "L3 (Length/m)" )
                        instruction.grid(row =5, column =0, columnspan =2, sticky = W)
                        self.L3 = Entry(w)
                        self.L3.grid(row =5, column =2, sticky = E)
                    
                        instruction = Label(w, text = "K3 (Thermal Conductivity)" )
                        instruction.grid(row =6, column =0, columnspan =2, sticky = W)
                        w.CTvar3=Tkinter.StringVar(w)
                        w.MRvar3=Tkinter.StringVar(w)
                        w.CTvar3.trace('w',self.updateoptions3)
                        w.CT_op_menu3=Tkinter.OptionMenu(w, w.CTvar3, *TB_names)
                        w.MR_op_menu3=Tkinter.OptionMenu(w, w.MRvar3, '')
                        w.CTvar3.set(TB_names[0]) 
                        w.CT_op_menu3.grid(row = 6, column =1, columnspan =2)
                        w.MR_op_menu3.grid(row = 6, column =3, columnspan =2,sticky = E)
                        w.CT_op_menu3.config(width=10)
                        w.MR_op_menu3.config(width=20)
    
            
                        instruction = Label(w, text = "L4 (Length/m)" )
                        instruction.grid(row =7, column =0, columnspan =2, sticky = W)
                        self.L4 = Entry(w)
                        self.L4.grid(row =7, column =2, sticky = E)
                    
                        instruction = Label(w, text = "K4 (Thermal Conductivity)" )
                        instruction.grid(row =8, column =0, columnspan =2, sticky = W)
                        w.CTvar4=Tkinter.StringVar(w)
                        w.MRvar4=Tkinter.StringVar(w)
                        w.CTvar4.trace('w',self.updateoptions4)
                        w.CT_op_menu4=Tkinter.OptionMenu(w, w.CTvar4, *TB_names)
                        w.MR_op_menu4=Tkinter.OptionMenu(w, w.MRvar4, '')
                        w.CTvar4.set(TB_names[0]) 
                        w.CT_op_menu4.grid(row = 8, column =1, columnspan =2)
                        w.MR_op_menu4.grid(row = 8, column =3, columnspan =2,sticky = E)
                        w.CT_op_menu4.config(width=10)
                        w.MR_op_menu4.config(width=20)
            
                        btnsave = Tkinter.Button(w, text="Save", command = self.save4)
                        btnsave.grid(row =9, column =2, sticky =E)      
                    elif Layer ==5:
                        instruction = Label(w, text = "L1 (Length/m)" )
                        instruction.grid(row =1, column =0, columnspan =2, sticky = W)
                        self.L1 = Entry(w)
                        self.L1.grid(row =1, column =2, sticky = E)
                    
                        instruction = Label(w, text = "K1 (Thermal Conductivity)" )
                        instruction.grid(row =2, column =0, columnspan =2, sticky = W)
                        w.CTvar=Tkinter.StringVar(w)
                        w.MRvar=Tkinter.StringVar(w)
                        w.CTvar.trace('w',self.updateoptions)
                        w.CT_op_menu=Tkinter.OptionMenu(w, w.CTvar, *TB_names)
                        w.MR_op_menu=Tkinter.OptionMenu(w, w.MRvar, '')
                        w.CTvar.set(TB_names[0]) 
                        w.CT_op_menu.grid(row = 2, column =1, columnspan =2)
                        w.MR_op_menu.grid(row = 2, column =3, columnspan =2,sticky = E)
                        w.CT_op_menu.config(width=10)
                        w.MR_op_menu.config(width=20)
            
                        instruction = Label(w, text = "L2 (Length/m)" )
                        instruction.grid(row =3, column =0, columnspan =2, sticky = W)
                        self.L2 = Entry(w)
                        self.L2.grid(row =3, column =2, sticky = E)
                    
                        instruction = Label(w, text = "K2 (Thermal Conductivity)" )
                        instruction.grid(row =4, column =0, columnspan =2, sticky = W)
                        w.CTvar2=Tkinter.StringVar(w)
                        w.MRvar2=Tkinter.StringVar(w)
                        w.CTvar2.trace('w',self.updateoptions2)
                        w.CT_op_menu2=Tkinter.OptionMenu(w, w.CTvar2, *TB_names)
                        w.MR_op_menu2=Tkinter.OptionMenu(w, w.MRvar2, '')
                        w.CTvar2.set(TB_names[0]) 
                        w.CT_op_menu2.grid(row = 4, column =1, columnspan =2)
                        w.MR_op_menu2.grid(row = 4, column =3, columnspan =2,sticky = E)
                        w.CT_op_menu2.config(width=10)
                        w.MR_op_menu2.config(width=20)    
            
                        instruction = Label(w, text = "L3 (Length/m)" )
                        instruction.grid(row =5, column =0, columnspan =2, sticky = W)
                        self.L3 = Entry(w)
                        self.L3.grid(row =5, column =2, sticky = E)
                    
                        instruction = Label(w, text = "K3 (Thermal Conductivity)" )
                        instruction.grid(row =6, column =0, columnspan =2, sticky = W)
                        w.CTvar3=Tkinter.StringVar(w)
                        w.MRvar3=Tkinter.StringVar(w)
                        w.CTvar3.trace('w',self.updateoptions3)
                        w.CT_op_menu3=Tkinter.OptionMenu(w, w.CTvar3, *TB_names)
                        w.MR_op_menu3=Tkinter.OptionMenu(w, w.MRvar3, '')
                        w.CTvar3.set(TB_names[0]) 
                        w.CT_op_menu3.grid(row = 6, column =1, columnspan =2)
                        w.MR_op_menu3.grid(row = 6, column =3, columnspan =2,sticky = E)
                        w.CT_op_menu3.config(width=10)
                        w.MR_op_menu3.config(width=20)
    
            
                        instruction = Label(w, text = "L4 (Length/m)" )
                        instruction.grid(row =7, column =0, columnspan =2, sticky = W)
                        self.L4 = Entry(w)
                        self.L4.grid(row =7, column =2, sticky = E)
                    
                        instruction = Label(w, text = "K4 (Thermal Conductivity)" )
                        instruction.grid(row =8, column =0, columnspan =2, sticky = W)
                        w.CTvar4=Tkinter.StringVar(w)
                        w.MRvar4=Tkinter.StringVar(w)
                        w.CTvar4.trace('w',self.updateoptions4)
                        w.CT_op_menu4=Tkinter.OptionMenu(w, w.CTvar4, *TB_names)
                        w.MR_op_menu4=Tkinter.OptionMenu(w, w.MRvar4, '')
                        w.CTvar4.set(TB_names[0]) 
                        w.CT_op_menu4.grid(row = 8, column =1, columnspan =2)
                        w.MR_op_menu4.grid(row = 8, column =3, columnspan =2,sticky = E)
                        w.CT_op_menu4.config(width=10)
                        w.MR_op_menu4.config(width=20)
            
            
                        instruction = Label(w, text = "L5 (Length/m)" )
                        instruction.grid(row =9, column =0, columnspan =2, sticky = W)
                        self.L5 = Entry(w)
                        self.L5.grid(row =9, column =2, sticky = E)
                    
                        instruction = Label(w, text = "K5 (Thermal Conductivity)" )
                        instruction.grid(row =10, column =0, columnspan =2, sticky = W)
                        w.CTvar5=Tkinter.StringVar(w)
                        w.MRvar5=Tkinter.StringVar(w)
                        w.CTvar5.trace('w',self.updateoptions5)
                        w.CT_op_menu5=Tkinter.OptionMenu(w, w.CTvar5, *TB_names)
                        w.MR_op_menu5=Tkinter.OptionMenu(w, w.MRvar5, '')
                        w.CTvar5.set(TB_names[0]) 
                        w.CT_op_menu5.grid(row = 10, column =1, columnspan =2)
                        w.MR_op_menu5.grid(row = 10, column =3, columnspan =2,sticky = E)
                        w.CT_op_menu5.config(width=10)
                        w.MR_op_menu5.config(width=20) 
            
                        btnsave = Tkinter.Button(w, text="Save", command = self.save5)
                        btnsave.grid(row =11, column =2, sticky =E)     
                                
                elif funcsel == "Vertical Cylinder"  or funcsel == "Horizontal Cylinder":       
                    if Layer == 1:
                        instruction = Label(w, text = "Distance from Center (Length/m)" )
                        instruction.grid(row =1, column =0, columnspan =2, sticky = W)
                        self.L = Entry(w)
                        self.L.grid(row =1, column =2, sticky = E)
                        
                        instruction = Label(w, text = "R (Length/m)" )
                        instruction.grid(row =2, column =0, columnspan =2, sticky = W)
                        self.R = Entry(w)
                        self.R.grid(row =2, column =2, sticky = E)
                        
                        instruction = Label(w, text = "K (Thermal Conductivity)" )
                        instruction.grid(row =3, column =0, columnspan =2, sticky = W)
                        w.CTvar=Tkinter.StringVar(w)
                        w.MRvar=Tkinter.StringVar(w)
                        w.CTvar.trace('w',self.updateoptions)
                        w.CT_op_menu=Tkinter.OptionMenu(w, w.CTvar, *TB_names)
                        w.MR_op_menu=Tkinter.OptionMenu(w, w.MRvar, '')
                        w.CTvar.set(TB_names[0]) 
                        w.CT_op_menu.grid(row = 3, column =1, columnspan =2)
                        w.MR_op_menu.grid(row = 3, column =3, columnspan =2,sticky = E)
                        w.CT_op_menu.config(width=10)
                        w.MR_op_menu.config(width=20)   
                
                        btnsave = Tkinter.Button(w, text="Save", command = self.save1)
                        btnsave.grid(row =4, column =2, sticky =E)              
                    elif Layer == 2:
                        instruction = Label(w, text = "Distance from Center (Length/m)" )
                        instruction.grid(row =1, column =0, columnspan =2, sticky = W)
                        self.L = Entry(w)
                        self.L.grid(row =1, column =2, sticky = E)
                        
                        instruction = Label(w, text = "R1 (Radius/m)" )
                        instruction.grid(row =2, column =0, columnspan =2, sticky = W)
                        self.R1 = Entry(w)
                        self.R1.grid(row =2, column =2, sticky = E)
                        
                        instruction = Label(w, text = "K1 (Thermal Conductivity)" )
                        instruction.grid(row =3, column =0, columnspan =2, sticky = W)
                        w.CTvar=Tkinter.StringVar(w)
                        w.MRvar=Tkinter.StringVar(w)
                        w.CTvar.trace('w',self.updateoptions)
                        w.CT_op_menu=Tkinter.OptionMenu(w, w.CTvar, *TB_names)
                        w.MR_op_menu=Tkinter.OptionMenu(w, w.MRvar, '')
                        w.CTvar.set(TB_names[0]) 
                        w.CT_op_menu.grid(row = 3, column =1, columnspan =2)
                        w.MR_op_menu.grid(row = 3, column =3, columnspan =2,sticky = E)
                        w.CT_op_menu.config(width=10)
                        w.MR_op_menu.config(width=20)   
                        
                        instruction = Label(w, text = "R2 (Radius/m)" )
                        instruction.grid(row =4, column =0, columnspan =2, sticky = W)
                        self.R2 = Entry(w)
                        self.R2.grid(row =4, column =2, sticky = E)
                        
                        instruction = Label(w, text = "K2 (Thermal Conductivity)" )
                        instruction.grid(row =5, column =0, columnspan =2, sticky = W)
                        w.CTvar2=Tkinter.StringVar(w)
                        w.MRvar2=Tkinter.StringVar(w)
                        w.CTvar2.trace('w',self.updateoptions2)
                        w.CT_op_menu2=Tkinter.OptionMenu(w, w.CTvar2, *TB_names)
                        w.MR_op_menu2=Tkinter.OptionMenu(w, w.MRvar2, '')
                        w.CTvar2.set(TB_names[0]) 
                        w.CT_op_menu2.grid(row = 5, column =1, columnspan =2)
                        w.MR_op_menu2.grid(row = 5, column =3, columnspan =2,sticky = E)
                        w.CT_op_menu2.config(width=10)
                        w.MR_op_menu2.config(width=20)    
                
                        btnsave = Tkinter.Button(w, text="Save", command = self.save2)
                        btnsave.grid(row =6, column =2, sticky =E)                     
                    elif Layer == 3:
                        instruction = Label(w, text = "Distance from Center (Length/m)" )
                        instruction.grid(row =1, column =0, columnspan =2, sticky = W)
                        self.L = Entry(w)
                        self.L.grid(row =1, column =2, sticky = E)
                        
                        instruction = Label(w, text = "R1 (Radius/m)" )
                        instruction.grid(row =2, column =0, columnspan =2, sticky = W)
                        self.R1 = Entry(w)
                        self.R1.grid(row =2, column =2, sticky = E)
                        
                        instruction = Label(w, text = "K1 (Thermal Conductivity)" )
                        instruction.grid(row =3, column =0, columnspan =2, sticky = W)
                        w.CTvar=Tkinter.StringVar(w)
                        w.MRvar=Tkinter.StringVar(w)
                        w.CTvar.trace('w',self.updateoptions)
                        w.CT_op_menu=Tkinter.OptionMenu(w, w.CTvar, *TB_names)
                        w.MR_op_menu=Tkinter.OptionMenu(w, w.MRvar, '')
                        w.CTvar.set(TB_names[0]) 
                        w.CT_op_menu.grid(row = 3, column =1, columnspan =2)
                        w.MR_op_menu.grid(row = 3, column =3, columnspan =2,sticky = E)
                        w.CT_op_menu.config(width=10)
                        w.MR_op_menu.config(width=20)   
                        
                        instruction = Label(w, text = "R2 (Radius/m)" )
                        instruction.grid(row =4, column =0, columnspan =2, sticky = W)
                        self.R2 = Entry(w)
                        self.R2.grid(row =4, column =2, sticky = E)
                        
                        instruction = Label(w, text = "K2 (Thermal Conductivity)" )
                        instruction.grid(row =5, column =0, columnspan =2, sticky = W)
                        w.CTvar2=Tkinter.StringVar(w)
                        w.MRvar2=Tkinter.StringVar(w)
                        w.CTvar2.trace('w',self.updateoptions2)
                        w.CT_op_menu2=Tkinter.OptionMenu(w, w.CTvar2, *TB_names)
                        w.MR_op_menu2=Tkinter.OptionMenu(w, w.MRvar2, '')
                        w.CTvar2.set(TB_names[0]) 
                        w.CT_op_menu2.grid(row = 5, column =1, columnspan =2)
                        w.MR_op_menu2.grid(row = 5, column =3, columnspan =2,sticky = E)
                        w.CT_op_menu2.config(width=10)
                        w.MR_op_menu2.config(width=20)    
                        
                        instruction = Label(w, text = "R3 (Radius/m)" )
                        instruction.grid(row =6, column =0, columnspan =2, sticky = W)
                        self.R3 = Entry(w)
                        self.R3.grid(row =6, column =2, sticky = E)
                        
                        instruction = Label(w, text = "K3 (Thermal Conductivity)" )
                        instruction.grid(row =7, column =0, columnspan =2, sticky = W)
                        w.CTvar3=Tkinter.StringVar(w)
                        w.MRvar3=Tkinter.StringVar(w)
                        w.CTvar3.trace('w',self.updateoptions3)
                        w.CT_op_menu3=Tkinter.OptionMenu(w, w.CTvar3, *TB_names)
                        w.MR_op_menu3=Tkinter.OptionMenu(w, w.MRvar3, '')
                        w.CTvar3.set(TB_names[0]) 
                        w.CT_op_menu3.grid(row = 7, column =1, columnspan =2)
                        w.MR_op_menu3.grid(row = 7, column =3, columnspan =2,sticky = E)
                        w.CT_op_menu3.config(width=10)
                        w.MR_op_menu3.config(width=20)
                
                        btnsave = Tkinter.Button(w, text="Save", command = self.save3)
                        btnsave.grid(row =8, column =2, sticky =E)              
                    elif Layer == 4:
                        instruction = Label(w, text = "Distance from Center (Length/m)" )
                        instruction.grid(row =1, column =0, columnspan =2, sticky = W)
                        self.L = Entry(w)
                        self.L.grid(row =1, column =2, sticky = E)
                        
                        instruction = Label(w, text = "R1 (Radius/m)" )
                        instruction.grid(row =2, column =0, columnspan =2, sticky = W)
                        self.R1 = Entry(w)
                        self.R1.grid(row =2, column =2, sticky = E)
                        
                        instruction = Label(w, text = "K1 (Thermal Conductivity)" )
                        instruction.grid(row =3, column =0, columnspan =2, sticky = W)
                        w.CTvar=Tkinter.StringVar(w)
                        w.MRvar=Tkinter.StringVar(w)
                        w.CTvar.trace('w',self.updateoptions)
                        w.CT_op_menu=Tkinter.OptionMenu(w, w.CTvar, *TB_names)
                        w.MR_op_menu=Tkinter.OptionMenu(w, w.MRvar, '')
                        w.CTvar.set(TB_names[0]) 
                        w.CT_op_menu.grid(row = 3, column =1, columnspan =2)
                        w.MR_op_menu.grid(row = 3, column =3, columnspan =2,sticky = E)
                        w.CT_op_menu.config(width=10)
                        w.MR_op_menu.config(width=20)   
                        
                        instruction = Label(w, text = "R2 (Radius/m)" )
                        instruction.grid(row =4, column =0, columnspan =2, sticky = W)
                        self.R2 = Entry(w)
                        self.R2.grid(row =4, column =2, sticky = E)
                        
                        instruction = Label(w, text = "K2 (Thermal Conductivity)" )
                        instruction.grid(row =5, column =0, columnspan =2, sticky = W)
                        w.CTvar2=Tkinter.StringVar(w)
                        w.MRvar2=Tkinter.StringVar(w)
                        w.CTvar2.trace('w',self.updateoptions2)
                        w.CT_op_menu2=Tkinter.OptionMenu(w, w.CTvar2, *TB_names)
                        w.MR_op_menu2=Tkinter.OptionMenu(w, w.MRvar2, '')
                        w.CTvar2.set(TB_names[0]) 
                        w.CT_op_menu2.grid(row = 5, column =1, columnspan =2)
                        w.MR_op_menu2.grid(row = 5, column =3, columnspan =2,sticky = E)
                        w.CT_op_menu2.config(width=10)
                        w.MR_op_menu2.config(width=20)    
                        
                        instruction = Label(w, text = "R3 (Radius/m)" )
                        instruction.grid(row =6, column =0, columnspan =2, sticky = W)
                        self.R3 = Entry(w)
                        self.R3.grid(row =6, column =2, sticky = E)
                        
                        instruction = Label(w, text = "K3 (Thermal Conductivity)" )
                        instruction.grid(row =7, column =0, columnspan =2, sticky = W)
                        w.CTvar3=Tkinter.StringVar(w)
                        w.MRvar3=Tkinter.StringVar(w)
                        w.CTvar3.trace('w',self.updateoptions3)
                        w.CT_op_menu3=Tkinter.OptionMenu(w, w.CTvar3, *TB_names)
                        w.MR_op_menu3=Tkinter.OptionMenu(w, w.MRvar3, '')
                        w.CTvar3.set(TB_names[0]) 
                        w.CT_op_menu3.grid(row = 7, column =1, columnspan =2)
                        w.MR_op_menu3.grid(row = 7, column =3, columnspan =2,sticky = E)
                        w.CT_op_menu3.config(width=10)
                        w.MR_op_menu3.config(width=20)
                        
                        instruction = Label(w, text = "R4 (Radius/m)" )
                        instruction.grid(row =8, column =0, columnspan =2, sticky = W)
                        self.R4 = Entry(w)
                        self.R4.grid(row =8, column =2, sticky = E)
                        
                        instruction = Label(w, text = "K4 (Thermal Conductivity)" )
                        instruction.grid(row =9, column =0, columnspan =2, sticky = W)
                        w.CTvar4=Tkinter.StringVar(w)
                        w.MRvar4=Tkinter.StringVar(w)
                        w.CTvar4.trace('w',self.updateoptions4)
                        w.CT_op_menu4=Tkinter.OptionMenu(w, w.CTvar4, *TB_names)
                        w.MR_op_menu4=Tkinter.OptionMenu(w, w.MRvar4, '')
                        w.CTvar4.set(TB_names[0]) 
                        w.CT_op_menu4.grid(row = 9, column =1, columnspan =2)
                        w.MR_op_menu4.grid(row = 9, column =3, columnspan =2,sticky = E)
                        w.CT_op_menu4.config(width=10)
                        w.MR_op_menu4.config(width=20)  
                
                        btnsave = Tkinter.Button(w, text="Save", command = self.save4)
                        btnsave.grid(row =10, column =2, sticky =E)             
                    elif Layer == 5:
                        instruction = Label(w, text = "Distance from Center (Length/m)" )
                        instruction.grid(row =1, column =0, columnspan =2, sticky = W)
                        self.L = Entry(w)
                        self.L.grid(row =1, column =2, sticky = E)
                        
                        instruction = Label(w, text = "R1 (Radius/m)" )
                        instruction.grid(row =2, column =0, columnspan =2, sticky = W)
                        self.R1 = Entry(w)
                        self.R1.grid(row =2, column =2, sticky = E)
                        
                        instruction = Label(w, text = "K1 (Thermal Conductivity)" )
                        instruction.grid(row =3, column =0, columnspan =2, sticky = W)
                        w.CTvar=Tkinter.StringVar(w)
                        w.MRvar=Tkinter.StringVar(w)
                        w.CTvar.trace('w',self.updateoptions)
                        w.CT_op_menu=Tkinter.OptionMenu(w, w.CTvar, *TB_names)
                        w.MR_op_menu=Tkinter.OptionMenu(w, w.MRvar, '')
                        w.CTvar.set(TB_names[0]) 
                        w.CT_op_menu.grid(row = 3, column =1, columnspan =2)
                        w.MR_op_menu.grid(row = 3, column =3, columnspan =2,sticky = E)
                        w.CT_op_menu.config(width=10)
                        w.MR_op_menu.config(width=20)   
                        
                        instruction = Label(w, text = "R2 (Radius/m)" )
                        instruction.grid(row =4, column =0, columnspan =2, sticky = W)
                        self.R2 = Entry(w)
                        self.R2.grid(row =4, column =2, sticky = E)
                        
                        instruction = Label(w, text = "K2 (Thermal Conductivity)" )
                        instruction.grid(row =5, column =0, columnspan =2, sticky = W)
                        w.CTvar2=Tkinter.StringVar(w)
                        w.MRvar2=Tkinter.StringVar(w)
                        w.CTvar2.trace('w',self.updateoptions2)
                        w.CT_op_menu2=Tkinter.OptionMenu(w, w.CTvar2, *TB_names)
                        w.MR_op_menu2=Tkinter.OptionMenu(w, w.MRvar2, '')
                        w.CTvar2.set(TB_names[0]) 
                        w.CT_op_menu2.grid(row = 5, column =1, columnspan =2)
                        w.MR_op_menu2.grid(row = 5, column =3, columnspan =2,sticky = E)
                        w.CT_op_menu2.config(width=10)
                        w.MR_op_menu2.config(width=20)    
                        
                        instruction = Label(w, text = "R3 (Radius/m)" )
                        instruction.grid(row =6, column =0, columnspan =2, sticky = W)
                        self.R3 = Entry(w)
                        self.R3.grid(row =6, column =2, sticky = E)
                        
                        instruction = Label(w, text = "K3 (Thermal Conductivity)" )
                        instruction.grid(row =7, column =0, columnspan =2, sticky = W)
                        w.CTvar3=Tkinter.StringVar(w)
                        w.MRvar3=Tkinter.StringVar(w)
                        w.CTvar3.trace('w',self.updateoptions3)
                        w.CT_op_menu3=Tkinter.OptionMenu(w, w.CTvar3, *TB_names)
                        w.MR_op_menu3=Tkinter.OptionMenu(w, w.MRvar3, '')
                        w.CTvar3.set(TB_names[0]) 
                        w.CT_op_menu3.grid(row = 7, column =1, columnspan =2)
                        w.MR_op_menu3.grid(row = 7, column =3, columnspan =2,sticky = E)
                        w.CT_op_menu3.config(width=10)
                        w.MR_op_menu3.config(width=20)
                        
                        instruction = Label(w, text = "R4 (Radius/m)" )
                        instruction.grid(row =8, column =0, columnspan =2, sticky = W)
                        self.R4 = Entry(w)
                        self.R4.grid(row =8, column =2, sticky = E)
                        
                        instruction = Label(w, text = "K4 (Thermal Conductivity)" )
                        instruction.grid(row =9, column =0, columnspan =2, sticky = W)
                        w.CTvar4=Tkinter.StringVar(w)
                        w.MRvar4=Tkinter.StringVar(w)
                        w.CTvar4.trace('w',self.updateoptions4)
                        w.CT_op_menu4=Tkinter.OptionMenu(w, w.CTvar4, *TB_names)
                        w.MR_op_menu4=Tkinter.OptionMenu(w, w.MRvar4, '')
                        w.CTvar4.set(TB_names[0]) 
                        w.CT_op_menu4.grid(row = 9, column =1, columnspan =2)
                        w.MR_op_menu4.grid(row = 9, column =3, columnspan =2,sticky = E)
                        w.CT_op_menu4.config(width=10)
                        w.MR_op_menu4.config(width=20)  
                        
                        instruction = Label(w, text = "R5 (Radius/m)" )
                        instruction.grid(row =10, column =0, columnspan =2, sticky = W)
                        self.R5 = Entry(w)
                        self.R5.grid(row =10, column =2, sticky = E)
                        
                        instruction = Label(w, text = "K5 (Thermal Conductivity)" )
                        instruction.grid(row =11, column =0, columnspan =2, sticky = W)
                        w.CTvar5=Tkinter.StringVar(w)
                        w.MRvar5=Tkinter.StringVar(w)
                        w.CTvar5.trace('w',self.updateoptions5)
                        w.CT_op_menu5=Tkinter.OptionMenu(w, w.CTvar5, *TB_names)
                        w.MR_op_menu5=Tkinter.OptionMenu(w, w.MRvar5, '')
                        w.CTvar5.set(TB_names[0]) 
                        w.CT_op_menu5.grid(row = 11, column =1, columnspan =2)
                        w.MR_op_menu5.grid(row = 11, column =3, columnspan =2,sticky = E)
                        w.CT_op_menu5.config(width=10)
                        w.MR_op_menu5.config(width=20) 
                
                        btnsave = Tkinter.Button(w, text="Save", command = self.save5)
                        btnsave.grid(row =12, column =2, sticky =E)             
                                        
        def save1(self):
                self.text.configure(state='normal')
                self.text.delete("1.0", END)
                global L, K, R
                funcsel = self.SGvar.get()
                if funcsel == "Vertical Plate" or funcsel == "Horizontal Roof":
                    L = float(self.L.get())
                    K = float(self.MRmatch()[0])
                    message1 = "| Layer 1 Material | K =" 
                    message2 = " | L ="
                    self.text.insert(END, message1)
                    self.text.insert(END, K)
                    self.text.insert(END, message2)
                    self.text.insert(END, L)
                    self.text.configure(state='disabled')
                    w.destroy()
                elif funcsel == "Vertical Cylinder" or funcsel == "Horizontal Cylinder":
                    L = float(self.L.get())
                    R = float(self.R.get())
                    K = float(self.MRmatch()[0])
                    message1 = "| Distance from center: "
                    message2 = "\n| Layer 1 Material | K =" 
                    message3 = " | R ="
                    self.text.insert(END, message1)
                    self.text.insert(END, L)
                    self.text.insert(END, message2)
                    self.text.insert(END, K)
                    self.text.insert(END, message3)
                    self.text.insert(END, R)
                    self.text.configure(state='disabled')
                    w.destroy()
        def save2(self):
                self.text.configure(state='normal')
                self.text.delete("1.0", END)
                global L, K1, K2, R1, R2, L1, L2
                funcsel = self.SGvar.get()
                if funcsel == "Vertical Plate" or funcsel == "Horizontal Roof":
                    L1 = float(self.L1.get())
                    K1 = float(self.MRmatch()[0])
                    L2 = float(self.L2.get())
                    K2 = float(self.MRmatch2()[0])
                    message1 = "| Layer 1 Material | K1 =" 
                    message2 = " | L1 ="
                    message3 = "\n| Layer 2 Material | K2 =" 
                    message4 = " | L2 ="
                    self.text.insert(END, message1)
                    self.text.insert(END, K1)
                    self.text.insert(END, message2)
                    self.text.insert(END, L1)
                    self.text.insert(END, message3)
                    self.text.insert(END, K2)
                    self.text.insert(END, message4)
                    self.text.insert(END, L2)
                    self.text.configure(state='disabled')
                    w.destroy()
                elif funcsel == "Vertical Cylinder" or funcsel == "Horizontal Cylinder":
                    L = float(self.L.get())
                    K1 = float(self.MRmatch()[0])
                    R1 = float(self.R1.get())
                    K2 = float(self.MRmatch2()[0])
                    R2 = float(self.R2.get())
                    message1 = "| Distance from center: "
                    message2 = "\n| Layer 1 Material | K1 =" 
                    message3 = " | R1 ="
                    message4 = "\n| Layer 2 Material | K2 =" 
                    message5 = " | R2 ="
                    self.text.insert(END, message1)
                    self.text.insert(END, L)
                    self.text.insert(END, message2)
                    self.text.insert(END, K1)
                    self.text.insert(END, message3)
                    self.text.insert(END, R1)
                    self.text.insert(END, message4)
                    self.text.insert(END, K2)
                    self.text.insert(END, message5)
                    self.text.insert(END, R2)
                    self.text.configure(state='disabled')
                    w.destroy()
        def save3(self):
                self.text.configure(state='normal')
                self.text.delete("1.0", END)
                global L, K1, K2, K3, R1, R2, R3, L1, L2, L3
                funcsel = self.SGvar.get()
                if funcsel == "Vertical Plate" or funcsel == "Horizontal Roof":
                    L1 = float(self.L1.get())
                    K1 = float(self.MRmatch()[0])
                    L2 = float(self.L2.get())
                    K2 = float(self.MRmatch2()[0])
                    L3 = float(self.L3.get())
                    K3 = float(self.MRmatch3()[0])
                    message1 = "| Layer 1 Material | K1 =" 
                    message2 = " | L1 ="
                    message3 = "\n| Layer 2 Material | K2 =" 
                    message4 = " | L2 ="
                    message5 = "\n| Layer 3 Material | K3 =" 
                    message6 = " | L3 ="
                    self.text.insert(END, message1)
                    self.text.insert(END, K1)
                    self.text.insert(END, message2)
                    self.text.insert(END, L1)
                    self.text.insert(END, message3)
                    self.text.insert(END, K2)
                    self.text.insert(END, message4)
                    self.text.insert(END, L2)
                    self.text.insert(END, message5)
                    self.text.insert(END, K3)
                    self.text.insert(END, message6)
                    self.text.insert(END, L3)
                    self.text.configure(state='disabled')
                    w.destroy()
                elif funcsel == "Vertical Cylinder" or funcsel == "Horizontal Cylinder": 
                    L = float(self.L.get())
                    K1 = float(self.MRmatch()[0])
                    R1 = float(self.R1.get())
                    K2 = float(self.MRmatch2()[0])
                    R2 = float(self.R2.get())
                    K3 = float(self.MRmatch3()[0])
                    R3 = float(self.R3.get())
                    message1 = "| Distance from center: "
                    message2 = "\n| Layer 1 Material | K1 =" 
                    message3 = " | R1 ="
                    message4 = "\n| Layer 2 Material | K2 =" 
                    message5 = " | R2 ="
                    message6 = "\n| Layer 3 Material | K3 =" 
                    message7 = " | R3 ="
                    self.text.insert(END, message1)
                    self.text.insert(END, L)
                    self.text.insert(END, message2)
                    self.text.insert(END, K1)
                    self.text.insert(END, message3)
                    self.text.insert(END, R1)
                    self.text.insert(END, message4)
                    self.text.insert(END, K2)
                    self.text.insert(END, message5)
                    self.text.insert(END, R2)
                    self.text.insert(END, message6)
                    self.text.insert(END, K3)
                    self.text.insert(END, message7)
                    self.text.insert(END, R3)
                    self.text.configure(state='disabled')
                    w.destroy()
        def save4(self):
                self.text.configure(state='normal')
                self.text.delete("1.0", END)
                global L, K1, K2, K3, K4, R1, R2, R3, R4,L1, L2, L3, L4
                funcsel = self.SGvar.get()
                if funcsel == "Vertical Plate" or funcsel == "Horizontal Roof":
                    L1 = float(self.L1.get())
                    K1 = float(self.MRmatch()[0])
                    L2 = float(self.L2.get())
                    K2 = float(self.MRmatch2()[0])
                    L3 = float(self.L3.get())
                    K3 = float(self.MRmatch3()[0])
                    L4 = float(self.L4.get())
                    K4 = float(self.MRmatch4()[0])
                    message1 = "| Layer 1 Material | K1 =" 
                    message2 = " | L1 ="
                    message3 = "\n| Layer 2 Material | K2 =" 
                    message4 = " | L2 ="
                    message5 = "\n| Layer 3 Material | K3 =" 
                    message6 = " | L3 ="
                    message7 = "\n| Layer 4 Material | K4 =" 
                    message8 = " | L4 ="
                    self.text.insert(END, message1)
                    self.text.insert(END, K1)
                    self.text.insert(END, message2)
                    self.text.insert(END, L1)
                    self.text.insert(END, message3)
                    self.text.insert(END, K2)
                    self.text.insert(END, message4)
                    self.text.insert(END, L2)
                    self.text.insert(END, message5)
                    self.text.insert(END, K3)
                    self.text.insert(END, message6)
                    self.text.insert(END, L3)
                    self.text.insert(END, message7)
                    self.text.insert(END, K4)
                    self.text.insert(END, message8)
                    self.text.insert(END, L4)
                    self.text.configure(state='disabled')
                    w.destroy()
                elif funcsel == "Vertical Cylinder" or funcsel == "Horizontal Cylinder": 
                    L = float(self.L.get())
                    K1 = float(self.MRmatch()[0])
                    R1 = float(self.R1.get())
                    K2 = float(self.MRmatch2()[0])
                    R2 = float(self.R2.get())
                    K3 = float(self.MRmatch3()[0])
                    R3 = float(self.R3.get())
                    K4 = float(self.MRmatch4()[0])
                    R4 = float(self.R4.get())
                    message1 = "| Distance from center: "
                    message2 = "\n| Layer 1 Material | K1 =" 
                    message3 = " | R1 ="
                    message4 = "\n| Layer 2 Material | K2 =" 
                    message5 = " | R2 ="
                    message6 = "\n| Layer 3 Material | K3 =" 
                    message7 = " | R3 ="
                    message8 = "\n| Layer 4 Material | K4 =" 
                    message9 = " | R4 ="
                    self.text.insert(END, message1)
                    self.text.insert(END, L)
                    self.text.insert(END, message2)
                    self.text.insert(END, K1)
                    self.text.insert(END, message3)
                    self.text.insert(END, R1)
                    self.text.insert(END, message4)
                    self.text.insert(END, K2)
                    self.text.insert(END, message5)
                    self.text.insert(END, R2)
                    self.text.insert(END, message6)
                    self.text.insert(END, K3)
                    self.text.insert(END, message7)
                    self.text.insert(END, R3)
                    self.text.insert(END, message8)
                    self.text.insert(END, K4)
                    self.text.insert(END, message9)
                    self.text.insert(END, R4)
                    self.text.configure(state='disabled')
                    w.destroy()
        def save5(self):
                self.text.configure(state='normal')
                self.text.delete("1.0", END)
                global L, K1, K2, K3, K4, K5,R1,R2,R3,R4,R5, L1, L2, L3,L4, L5
                funcsel = self.SGvar.get()
                if funcsel == "Vertical Plate" or funcsel == "Horizontal Roof":
                    L1 = float(self.L1.get())
                    K1 = float(self.MRmatch()[0])
                    L2 = float(self.L2.get())
                    K2 = float(self.MRmatch2()[0])
                    L3 = float(self.L3.get())
                    K3 = float(self.MRmatch3()[0])
                    L4 = float(self.L4.get())
                    K4 = float(self.MRmatch4()[0])
                    L5 = float(self.L5.get())
                    K5 = float(self.MRmatch5()[0])
                    message1 = "| Layer 1 Material | K1 =" 
                    message2 = " | L1 ="
                    message3 = "\n| Layer 2 Material | K2 =" 
                    message4 = " | L2 ="
                    message5 = "\n| Layer 3 Material | K3 =" 
                    message6 = " | L3 ="
                    message7 = "\n| Layer 4 Material | K4 =" 
                    message8 = " | L4 ="
                    message9 = "\n| Layer 5 Material | K5 =" 
                    message10 = " | L5 ="
                    self.text.insert(END, message1)
                    self.text.insert(END, K1)
                    self.text.insert(END, message2)
                    self.text.insert(END, L1)
                    self.text.insert(END, message3)
                    self.text.insert(END, K2)
                    self.text.insert(END, message4)
                    self.text.insert(END, L2)
                    self.text.insert(END, message5)
                    self.text.insert(END, K3)
                    self.text.insert(END, message6)
                    self.text.insert(END, L3)
                    self.text.insert(END, message7)
                    self.text.insert(END, K4)
                    self.text.insert(END, message8)
                    self.text.insert(END, L4)
                    self.text.insert(END, message9)
                    self.text.insert(END, K5)
                    self.text.insert(END, message10)
                    self.text.insert(END, L5)
                    self.text.configure(state='disabled')   
                    w.destroy()
                elif funcsel == "Vertical Cylinder" or funcsel == "Horizontal Cylinder": 
                    L = float(self.L.get())
                    K1 = float(self.MRmatch()[0])
                    R1 = float(self.R1.get())
                    K2 = float(self.MRmatch2()[0])
                    R2 = float(self.R2.get())
                    K3 = float(self.MRmatch3()[0])
                    R3 = float(self.R3.get())
                    K4 = float(self.MRmatch4()[0])
                    R4 = float(self.R4.get())
                    K5 = float(self.MRmatch5()[0])
                    R5 = float(self.R5.get())
                    message1 = "| Distance from center: "
                    message2 = "\n| Layer 1 Material | K1 =" 
                    message3 = " | R1 ="
                    message4 = "\n| Layer 2 Material | K2 =" 
                    message5 = " | R2 ="
                    message6 = "\n| Layer 3 Material | K3 =" 
                    message7 = " | R3 ="
                    message8 = "\n| Layer 4 Material | K4 =" 
                    message9 = " | R4 ="
                    message10 = "\n| Layer 5 Material | K5 =" 
                    message11 = " | R5 ="
                    self.text.insert(END, message1)
                    self.text.insert(END, L)
                    self.text.insert(END, message2)
                    self.text.insert(END, K1)
                    self.text.insert(END, message3)
                    self.text.insert(END, R1)
                    self.text.insert(END, message4)
                    self.text.insert(END, K2)
                    self.text.insert(END, message5)
                    self.text.insert(END, R2)
                    self.text.insert(END, message6)
                    self.text.insert(END, K3)
                    self.text.insert(END, message7)
                    self.text.insert(END, R3)
                    self.text.insert(END, message8)
                    self.text.insert(END, K4)
                    self.text.insert(END, message9)
                    self.text.insert(END, R4)
                    self.text.insert(END, message10)
                    self.text.insert(END, K5)
                    self.text.insert(END, message11)
                    self.text.insert(END, R5)
                    self.text.configure(state='disabled')
                    w.destroy()               
        def reveal(self):
                
                Ti = float(self.Ti.get())
                To = float(self.To.get())
                #h1 = float(self.h1.get())
                #h2 = float(self.h2.get())
                h1=2
                h2=4
                funcsel = self.SGvar.get()
                
                if funcsel == "Vertical Plate":
                    if Layer ==1:
                        x=arange(0,L,0.0001)
                        K10=2
                        gamma1=0.2
                        def equations(p1):
                            T1, Ts = p1
                            return (h1*(Ti-T1)-(K10/L)*((T1**(1-gamma1)-Ts**(1-gamma1))/(1-gamma1)), \
                                    h1*(Ti-T1)-h2*(Ts-To))
                        T1, Ts= fsolve(equations, (1,1))
                        q=h1*(Ti-T1)
                        TL1=((T1**(1-gamma1))-q*(1-gamma1)*x/K10)**(1/(1-gamma1))
                        plt.plot(x,TL1)
                        plt.show()
                    elif Layer ==2:
                        d1=L1
                        d2=L1+L2
                        x1=arange(0,d1,0.0001)
                        x2=arange(d1,d2,0.0001)
                        x22=arange(0,L2,0.0001)
                        K10=2.0
                        T10=293.0
                        gamma1=0.2
                        K20=2.0
                        T20=293.0
                        gamma2=0.2
                        def equations(p2):
                            T1, T2, Ts =p2
                            return(h1*(Ti-T1)-(K10/d1)*T10**(gamma1)*((T1**(1-gamma1)-T2**(1-gamma1))/(1-gamma1)), \
                                   h1*(Ti-T1)-(K20/(d2-d1))*T20**(gamma2)*((T2**(1-gamma2)-Ts**(1-gamma2))/(1-gamma2)), \
                                   h1*(Ti-T1)-h2*(Ts-To))
                        T1, T2, Ts= fsolve(equations,(1,1,1))
                        print T1, T2, Ts
                        q=h1*(Ti-T1)
                        TL1=( (1-x1/d1)*T1**(1-gamma1) +x1/d1*T2**(1-gamma1))**(1/(1-gamma1))
                        TL2=(1/(d2-d1)*((d2-x2)*T2**(1-gamma2)+(x2-d1)*Ts**(1-gamma2)))**(1/(1-gamma2))
                        plt.plot(x1,TL1)
                        plt.plot(x2,TL2)
                        plt.show()
                    elif Layer ==3:
                        d1=L1
                        d2=L1+L2
                        d3=L1+L2+L3
                        x1=arange(0,d1,0.0001)
                        x2=arange(d1,d2,0.0001)
                        x3=arange(d2,d3,0.0001)
                        K10=0.8
                        T10=293
                        gamma1=0.2
                        K20=0.57
                        T20=293
                        gamma2=0.2
                        K30=30
                        T30=293
                        gamma3=0.2
                        # epsilon1=0
#                         sigma1=5.67e-8
                        def equations(p3):
                            T1, T2, T3, Ts =p3
                            return(h1*(Ti-T1)-(K10/d1)*T10**(gamma1)*((T1**(1-gamma1)-T2**(1-gamma1))/(1-gamma1)), \
                                   h1*(Ti-T1)-(K20/(d2-d1))*T20**(gamma2)*((T2**(1-gamma2)-T3**(1-gamma2))/(1-gamma2)), \
                                   h1*(Ti-T1)-(K30/(d3-d2))*T30**(gamma3)*((T3**(1-gamma3)-Ts**(1-gamma3))/(1-gamma3)), \
                                   h1*(Ti-T1)-h2*(Ts-To))
                        T1, T2, T3, Ts= fsolve(equations, (1,1,1,1))
#                         q=h1*(Ti-T1)+epsilon1*sigma1*(Ti**4-T1**4)
                        TL1=( (1-x1/d1)*T1**(1-gamma1) +x1/d1*T2**(1-gamma1))**(1/(1-gamma1))
                        TL2=(1/(d2-d1)*((d2-x2)*T2**(1-gamma2)+(x2-d1)*T3**(1-gamma2)))**(1/(1-gamma2))
                        TL3=(1/(d3-d2)*((d3-x3)*T3**(1-gamma3)+(x3-d2)*Ts**(1-gamma3)))**(1/(1-gamma3))
#                         print q, epsilon1*sigma1*(Ti**4-T1**4)
                        plt.plot(x1,TL1)
                        plt.plot(x2,TL2)
                        plt.plot(x3,TL3)
                        plt.show()
                    elif Layer ==4:
                        d1=L1
                        d2=L1+L2
                        d3=L1+L2+L3
                        d4=L1+L2+L3+L4
                        x1=arange(0,d1,0.0001)
                        x2=arange(d1,d2,0.0001)
                        x3=arange(d2,d3,0.0001)
                        x4=arange(d3,d4,0.0001)
                        K10=0.8
                        T10=293
                        gamma1=0.2
                        K20=0.57
                        T20=293
                        gamma2=0.2
                        K30=30
                        T30=293
                        gamma3=0.2
                        K40=5
                        T40=293
                        gamma4=0.1
                        def equations(p4):
                            T1, T2, T3, T4, Ts =p4
                            return(h1*(Ti-T1)-(K10/d1)*T10**(gamma1)*((T1**(1-gamma1)-T2**(1-gamma1))/(1-gamma1)), \
                                   h1*(Ti-T1)-(K20/(d2-d1))*T20**(gamma2)*((T2**(1-gamma2)-T3**(1-gamma2))/(1-gamma2)), \
                                   h1*(Ti-T1)-(K30/(d3-d2))*T30**(gamma3)*((T3**(1-gamma3)-T4**(1-gamma3))/(1-gamma3)), \
                                   h1*(Ti-T1)-(K40/(d4-d3))*T40**(gamma4)*((T4**(1-gamma4)-Ts**(1-gamma4))/(1-gamma4)), \
                                   h1*(Ti-T1)-h2*(Ts-To))
                        T1, T2, T3, T4, Ts= fsolve(equations, (1,1,1,1,1))
                        q=h1*(Ti-T1)
                        TL1=( (1-x1/d1)*T1**(1-gamma1) +x1/d1*T2**(1-gamma1))**(1/(1-gamma1))
                        TL2=(1/(d2-d1)*((d2-x2)*T2**(1-gamma2)+(x2-d1)*T3**(1-gamma2)))**(1/(1-gamma2))
                        TL3=(1/(d3-d2)*((d3-x3)*T3**(1-gamma3)+(x3-d2)*T4**(1-gamma3)))**(1/(1-gamma3))
                        TL4=(1/(d4-d3)*((d4-x4)*T4**(1-gamma4)+(x4-d3)*Ts**(1-gamma4)))**(1/(1-gamma4))
                        plt.plot(x1,TL1)
                        plt.plot(x2,TL2)
                        plt.plot(x3,TL3)
                        plt.plot(x4,TL4)
                        plt.show()
                    elif Layer ==5:
                        d1=L1
                        d2=L1+L2
                        d3=L1+L2+L3
                        d4=L1+L2+L3+L4
                        d5=L1+L2+L3+L4+L5
                        x1=arange(0,d1,0.0001)
                        x2=arange(d1,d2,0.0001)
                        x3=arange(d2,d3,0.0001)
                        x4=arange(d3,d4,0.0001)
                        x5=arange(d4,d5,0.0001)
                        K10=0.8
                        T10=293
                        gamma1=0.2
                        K20=0.57
                        T20=293
                        gamma2=0.2
                        K30=30
                        T30=293
                        gamma3=0.2
                        K40=5
                        T40=293
                        gamma4=0.1
                        K50=6
                        T50=293
                        gamma5=0.15
                        def equations(p5):
                            T1, T2, T3, T4, T5, Ts =p5
                            return(h1*(Ti-T1)-(K10/d1)*T10**(gamma1)*((T1**(1-gamma1)-T2**(1-gamma1))/(1-gamma1)), \
                                   h1*(Ti-T1)-(K20/(d2-d1))*T20**(gamma2)*((T2**(1-gamma2)-T3**(1-gamma2))/(1-gamma2)), \
                                   h1*(Ti-T1)-(K30/(d3-d2))*T30**(gamma3)*((T3**(1-gamma3)-T4**(1-gamma3))/(1-gamma3)), \
                                   h1*(Ti-T1)-(K40/(d4-d3))*T40**(gamma4)*((T4**(1-gamma4)-T5**(1-gamma4))/(1-gamma4)), \
                                   h1*(Ti-T1)-(K50/(d5-d4))*T50**(gamma5)*((T5**(1-gamma5)-Ts**(1-gamma5))/(1-gamma5)), \
                                   h1*(Ti-T1)-h2*(Ts-To))
                        T1, T2, T3, T4, T5, Ts= fsolve(equations, (1,1,1,1,1,1))
                        q=h1*(Ti-T1)
                        TL1=( (1-x1/d1)*T1**(1-gamma1) +x1/d1*T2**(1-gamma1))**(1/(1-gamma1))
                        TL2=(1/(d2-d1)*((d2-x2)*T2**(1-gamma2)+(x2-d1)*T3**(1-gamma2)))**(1/(1-gamma2))
                        TL3=(1/(d3-d2)*((d3-x3)*T3**(1-gamma3)+(x3-d2)*T4**(1-gamma3)))**(1/(1-gamma3))
                        TL4=(1/(d4-d3)*((d4-x4)*T4**(1-gamma4)+(x4-d3)*T5**(1-gamma4)))**(1/(1-gamma4))
                        TL5=(1/(d5-d4)*((d5-x5)*T5**(1-gamma5)+(x5-d4)*Ts**(1-gamma5)))**(1/(1-gamma5))
                        plt.plot(x1,TL1)
                        plt.plot(x2,TL2)
                        plt.plot(x3,TL3)
                        plt.plot(x4,TL4)
                        plt.plot(x5,TL5)
                        plt.show()
                elif funcsel == "Horizontal Roof":
                    if Layer ==1:
                        x=arange(0,L,0.0001)
                        K10=2
                        gamma1=0.2
                        def equations(p1):
                            T1, Ts = p1
                            return (h1*(Ti-T1)-(K10/L)*((T1**(1-gamma1)-Ts**(1-gamma1))/(1-gamma1)), \
                                    h1*(Ti-T1)-h2*(Ts-To))
                        T1, Ts= fsolve(equations, (1,1))
                        q=h1*(Ti-T1)
                        TL1=((T1**(1-gamma1))-q*(1-gamma1)*x/K10)**(1/(1-gamma1))
                        plt.plot(x,TL1)
                        plt.show()
                    elif Layer ==2:
                        d1=L1
                        d2=L1+L2
                        x1=arange(0,d1,0.0001)
                        x2=arange(d1,d2,0.0001)
                        x22=arange(0,L2,0.0001)
                        K10=2.0
                        T10=293.0
                        gamma1=0.2
                        K20=2.0
                        T20=293.0
                        gamma2=0.2
                        def equations(p2):
                            T1, T2, Ts =p2
                            return(h1*(Ti-T1)-(K10/d1)*T10**(gamma1)*((T1**(1-gamma1)-T2**(1-gamma1))/(1-gamma1)), \
                                   h1*(Ti-T1)-(K20/(d2-d1))*T20**(gamma2)*((T2**(1-gamma2)-Ts**(1-gamma2))/(1-gamma2)), \
                                   h1*(Ti-T1)-h2*(Ts-To))
                        T1, T2, Ts= fsolve(equations,(1,1,1))
                        print T1, T2, Ts
                        q=h1*(Ti-T1)
                        TL1=( (1-x1/d1)*T1**(1-gamma1) +x1/d1*T2**(1-gamma1))**(1/(1-gamma1))
                        TL2=(1/(d2-d1)*((d2-x2)*T2**(1-gamma2)+(x2-d1)*Ts**(1-gamma2)))**(1/(1-gamma2))
                        plt.plot(x1,TL1)
                        plt.plot(x2,TL2)
                        plt.show()
                    elif Layer ==3:
                        d1=L1
                        d2=L1+L2
                        d3=L1+L2+L3
                        x1=arange(0,d1,0.0001)
                        x2=arange(d1,d2,0.0001)
                        x3=arange(d2,d3,0.0001)
                        K10=0.8
                        T10=293
                        gamma1=0.2
                        K20=0.57
                        T20=293
                        gamma2=0.2
                        K30=30
                        T30=293
                        gamma3=0.2
                        # epsilon1=0
#                         sigma1=5.67e-8
                        def equations(p3):
                            T1, T2, T3, Ts =p3
                            return(h1*(Ti-T1)-(K10/d1)*T10**(gamma1)*((T1**(1-gamma1)-T2**(1-gamma1))/(1-gamma1)), \
                                   h1*(Ti-T1)-(K20/(d2-d1))*T20**(gamma2)*((T2**(1-gamma2)-T3**(1-gamma2))/(1-gamma2)), \
                                   h1*(Ti-T1)-(K30/(d3-d2))*T30**(gamma3)*((T3**(1-gamma3)-Ts**(1-gamma3))/(1-gamma3)), \
                                   h1*(Ti-T1)-h2*(Ts-To))
                        T1, T2, T3, Ts= fsolve(equations, (1,1,1,1))
#                         q=h1*(Ti-T1)+epsilon1*sigma1*(Ti**4-T1**4)
                        TL1=( (1-x1/d1)*T1**(1-gamma1) +x1/d1*T2**(1-gamma1))**(1/(1-gamma1))
                        TL2=(1/(d2-d1)*((d2-x2)*T2**(1-gamma2)+(x2-d1)*T3**(1-gamma2)))**(1/(1-gamma2))
                        TL3=(1/(d3-d2)*((d3-x3)*T3**(1-gamma3)+(x3-d2)*Ts**(1-gamma3)))**(1/(1-gamma3))
#                         print q, epsilon1*sigma1*(Ti**4-T1**4)
                        plt.plot(x1,TL1)
                        plt.plot(x2,TL2)
                        plt.plot(x3,TL3)
                        plt.show()
                    elif Layer ==4:
                        d1=L1
                        d2=L1+L2
                        d3=L1+L2+L3
                        d4=L1+L2+L3+L4
                        x1=arange(0,d1,0.0001)
                        x2=arange(d1,d2,0.0001)
                        x3=arange(d2,d3,0.0001)
                        x4=arange(d3,d4,0.0001)
                        K10=0.8
                        T10=293
                        gamma1=0.2
                        K20=0.57
                        T20=293
                        gamma2=0.2
                        K30=30
                        T30=293
                        gamma3=0.2
                        K40=5
                        T40=293
                        gamma4=0.1
                        def equations(p4):
                            T1, T2, T3, T4, Ts =p4
                            return(h1*(Ti-T1)-(K10/d1)*T10**(gamma1)*((T1**(1-gamma1)-T2**(1-gamma1))/(1-gamma1)), \
                                   h1*(Ti-T1)-(K20/(d2-d1))*T20**(gamma2)*((T2**(1-gamma2)-T3**(1-gamma2))/(1-gamma2)), \
                                   h1*(Ti-T1)-(K30/(d3-d2))*T30**(gamma3)*((T3**(1-gamma3)-T4**(1-gamma3))/(1-gamma3)), \
                                   h1*(Ti-T1)-(K40/(d4-d3))*T40**(gamma4)*((T4**(1-gamma4)-Ts**(1-gamma4))/(1-gamma4)), \
                                   h1*(Ti-T1)-h2*(Ts-To))
                        T1, T2, T3, T4, Ts= fsolve(equations, (1,1,1,1,1))
                        q=h1*(Ti-T1)
                        TL1=( (1-x1/d1)*T1**(1-gamma1) +x1/d1*T2**(1-gamma1))**(1/(1-gamma1))
                        TL2=(1/(d2-d1)*((d2-x2)*T2**(1-gamma2)+(x2-d1)*T3**(1-gamma2)))**(1/(1-gamma2))
                        TL3=(1/(d3-d2)*((d3-x3)*T3**(1-gamma3)+(x3-d2)*T4**(1-gamma3)))**(1/(1-gamma3))
                        TL4=(1/(d4-d3)*((d4-x4)*T4**(1-gamma4)+(x4-d3)*Ts**(1-gamma4)))**(1/(1-gamma4))
                        plt.plot(x1,TL1)
                        plt.plot(x2,TL2)
                        plt.plot(x3,TL3)
                        plt.plot(x4,TL4)
                        plt.show()
                    elif Layer ==5:
                        d1=L1
                        d2=L1+L2
                        d3=L1+L2+L3
                        d4=L1+L2+L3+L4
                        d5=L1+L2+L3+L4+L5
                        x1=arange(0,d1,0.0001)
                        x2=arange(d1,d2,0.0001)
                        x3=arange(d2,d3,0.0001)
                        x4=arange(d3,d4,0.0001)
                        x5=arange(d4,d5,0.0001)
                        K10=0.8
                        T10=293
                        gamma1=0.2
                        K20=0.57
                        T20=293
                        gamma2=0.2
                        K30=30
                        T30=293
                        gamma3=0.2
                        K40=5
                        T40=293
                        gamma4=0.1
                        K50=6
                        T50=293
                        gamma5=0.15
                        def equations(p5):
                            T1, T2, T3, T4, T5, Ts =p5
                            return(h1*(Ti-T1)-(K10/d1)*T10**(gamma1)*((T1**(1-gamma1)-T2**(1-gamma1))/(1-gamma1)), \
                                   h1*(Ti-T1)-(K20/(d2-d1))*T20**(gamma2)*((T2**(1-gamma2)-T3**(1-gamma2))/(1-gamma2)), \
                                   h1*(Ti-T1)-(K30/(d3-d2))*T30**(gamma3)*((T3**(1-gamma3)-T4**(1-gamma3))/(1-gamma3)), \
                                   h1*(Ti-T1)-(K40/(d4-d3))*T40**(gamma4)*((T4**(1-gamma4)-T5**(1-gamma4))/(1-gamma4)), \
                                   h1*(Ti-T1)-(K50/(d5-d4))*T50**(gamma5)*((T5**(1-gamma5)-Ts**(1-gamma5))/(1-gamma5)), \
                                   h1*(Ti-T1)-h2*(Ts-To))
                        T1, T2, T3, T4, T5, Ts= fsolve(equations, (1,1,1,1,1,1))
                        q=h1*(Ti-T1)
                        TL1=( (1-x1/d1)*T1**(1-gamma1) +x1/d1*T2**(1-gamma1))**(1/(1-gamma1))
                        TL2=(1/(d2-d1)*((d2-x2)*T2**(1-gamma2)+(x2-d1)*T3**(1-gamma2)))**(1/(1-gamma2))
                        TL3=(1/(d3-d2)*((d3-x3)*T3**(1-gamma3)+(x3-d2)*T4**(1-gamma3)))**(1/(1-gamma3))
                        TL4=(1/(d4-d3)*((d4-x4)*T4**(1-gamma4)+(x4-d3)*T5**(1-gamma4)))**(1/(1-gamma4))
                        TL5=(1/(d5-d4)*((d5-x5)*T5**(1-gamma5)+(x5-d4)*Ts**(1-gamma5)))**(1/(1-gamma5))
                        plt.plot(x1,TL1)
                        plt.plot(x2,TL2)
                        plt.plot(x3,TL3)
                        plt.plot(x4,TL4)
                        plt.plot(x5,TL5)
                        plt.show()
                elif funcsel == "Horizontal Cylinder":
                    if Layer ==1:
                        r1=L
                        r2=L+R
                        x=arange(r1,r2,0.0001)
                        K10=2
                        gamma1=0.2
                        T10=293
                        def equations(p1):
                                T1, Ts = p1
                                return (r1*h1*(Ti-T1)-r2*h2*(Ts-To),\
                                        r1*h1*(Ti-T1)-K10*(T10**gamma1)*(T1**(1-gamma1)-Ts**(1-gamma1))/((log(r2/r1))*(1-gamma1)))
                        T1, Ts= fsolve(equations, (1,1))
                        print T1, Ts
                        T=(T1**(1-gamma1)+(log(r1)-log(x))*(T1**(1-gamma1)-Ts**(1-gamma1))/log(r2/r1))**(1/(1-gamma1))
                        plt.plot(x,T)
                        plt.show()
                    elif Layer ==2:
                        r1=L
                        r2=R1+L
                        r3=R1+R2+L
                        x1=arange(r1,r2,0.0001)
                        x2=arange(r2,r3,0.0001)
                        K10=2
                        gamma1=0.2
                        T10=293
                        K20=2
                        gamma2=0.2
                        T20=293
                        def equations(p2):
                                T1, T2, Ts =p2
                                return(r1*h1*(Ti-T1)-r3*h2*(Ts-To),\
                                       r1*h1*(Ti-T1)-K10*(T10**gamma1)*(T1**(1-gamma1)-T2**(1-gamma1))/((log(r2/r1))*(1-gamma1)),\
                                       r1*h1*(Ti-T1)-K20*(T20**gamma2)*(T2**(1-gamma2)-Ts**(1-gamma2))/((log(r3/r2))*(1-gamma2)))
                        T1, T2, Ts= fsolve(equations, (1,1,1))
                        TL1=(T1**(1-gamma1)+(log(r1)-log(x1))*(T1**(1-gamma1)-T2**(1-gamma1))/log(r2/r1))**(1/(1-gamma1))
                        TL2=(T2**(1-gamma2)+(log(r2)-log(x2))*(T2**(1-gamma2)-Ts**(1-gamma2))/log(r3/r2))**(1/(1-gamma2))
                        plt.plot(x1,TL1)
                        plt.plot(x2,TL2)
                        plt.show()
                    elif Layer ==3:
                        r1=L
                        r2=R1+L
                        r3=R1+R2+L
                        r4=R1+R2+R3+L
                        x1=arange(r1,r2,0.0001)
                        x2=arange(r2,r3,0.0001)
                        x3=arange(r3,r4,0.0001)
                        K10=2
                        gamma1=0.2
                        T10=293
                        K20=2
                        gamma2=0.2
                        T20=293
                        K30=2
                        gamma3=0.2
                        T30=293
                        def equations(p3):
                                T1, T2, T3, Ts =p3
                                return(r1*h1*(Ti-T1)-r4*h2*(Ts-To),\
                                       r1*h1*(Ti-T1)-K10*(T10**gamma1)*(T1**(1-gamma1)-T2**(1-gamma1))/((log(r2/r1))*(1-gamma1)),\
                                       r1*h1*(Ti-T1)-K20*(T20**gamma2)*(T2**(1-gamma2)-T3**(1-gamma2))/((log(r3/r2))*(1-gamma2)),\
                                       r1*h1*(Ti-T1)-K30*(T30**gamma3)*(T3**(1-gamma3)-Ts**(1-gamma3))/((log(r4/r3))*(1-gamma3)))
                        T1, T2, T3, Ts= fsolve(equations, (1,1,1,1))
                        TL1=(T1**(1-gamma1)+(log(r1)-log(x1))*(T1**(1-gamma1)-T2**(1-gamma1))/log(r2/r1))**(1/(1-gamma1))
                        TL2=(T2**(1-gamma2)+(log(r2)-log(x2))*(T2**(1-gamma2)-T3**(1-gamma2))/log(r3/r2))**(1/(1-gamma2))
                        TL3=(T3**(1-gamma3)+(log(r3)-log(x3))*(T3**(1-gamma3)-Ts**(1-gamma3))/log(r4/r3))**(1/(1-gamma3))
                        plt.plot(x1,TL1)
                        plt.plot(x2,TL2)
                        plt.plot(x3,TL3)
                        plt.show()
                    elif Layer ==4:
                        r1=L
                        r2=R1+L
                        r3=R1+R2+L
                        r4=R1+R2+R3+L
                        r5=R1+R2+R3+R4+L
                        x1=arange(r1,r2,0.0001)
                        x2=arange(r2,r3,0.0001)
                        x3=arange(r3,r4,0.0001)
                        x4=arange(r4,r5,0.0001)
                        K10=2
                        gamma1=0.2
                        T10=293
                        K20=2
                        gamma2=0.2
                        T20=293
                        K30=2
                        gamma3=0.2
                        T30=293
                        K40=2
                        gamma4=0.2
                        T40=293
                        def equations(p4):
                                T1, T2, T3, T4, Ts =p4
                                return(r1*h1*(Ti-T1)-r5*h2*(Ts-To),\
                                       r1*h1*(Ti-T1)-K10*(T10**gamma1)*(T1**(1-gamma1)-T2**(1-gamma1))/((log(r2/r1))*(1-gamma1)),\
                                       r1*h1*(Ti-T1)-K20*(T20**gamma2)*(T2**(1-gamma2)-T3**(1-gamma2))/((log(r3/r2))*(1-gamma2)),\
                                       r1*h1*(Ti-T1)-K30*(T30**gamma3)*(T3**(1-gamma3)-T4**(1-gamma3))/((log(r4/r3))*(1-gamma3)),\
                                       r1*h1*(Ti-T1)-K40*(T40**gamma4)*(T4**(1-gamma4)-Ts**(1-gamma4))/((log(r5/r4))*(1-gamma4)))
                        T1, T2, T3, T4, Ts= fsolve(equations, (1,1,1,1,1))
                        TL1=(T1**(1-gamma1)+(log(r1)-log(x1))*(T1**(1-gamma1)-T2**(1-gamma1))/log(r2/r1))**(1/(1-gamma1))
                        TL2=(T2**(1-gamma2)+(log(r2)-log(x2))*(T2**(1-gamma2)-T3**(1-gamma2))/log(r3/r2))**(1/(1-gamma2))
                        TL3=(T3**(1-gamma3)+(log(r3)-log(x3))*(T3**(1-gamma3)-T4**(1-gamma3))/log(r4/r3))**(1/(1-gamma3))
                        TL4=(T4**(1-gamma4)+(log(r4)-log(x4))*(T4**(1-gamma4)-Ts**(1-gamma4))/log(r5/r4))**(1/(1-gamma4))
                        plt.plot(x1,TL1)
                        plt.plot(x2,TL2)
                        plt.plot(x3,TL3)
                        plt.plot(x4,TL4)
                        plt.show()
                    elif Layer ==5:
                        r1=L
                        r2=R1+L
                        r3=R1+R2+L
                        r4=R1+R2+R3+L
                        r5=R1+R2+R3+R4+L
                        r6=R1+R2+R3+R4+R5+L
                        x1=arange(r1,r2,0.0001)
                        x2=arange(r2,r3,0.0001)
                        x3=arange(r3,r4,0.0001)
                        x4=arange(r4,r5,0.0001)
                        x5=arange(r5,r6,0.0001)
                        K10=2
                        gamma1=0.2
                        T10=293
                        K20=2
                        gamma2=0.2
                        T20=293
                        K30=2
                        gamma3=0.2
                        T30=293
                        K40=2
                        gamma4=0.2
                        T40=293
                        K50=2
                        gamma5=0.2
                        T50=293
                        def equations(p5):
                                T1, T2, T3, T4, T5, Ts =p5
                                return(r1*h1*(Ti-T1)-r6*h2*(Ts-To),\
                                       r1*h1*(Ti-T1)-K10*(T10**gamma1)*(T1**(1-gamma1)-T2**(1-gamma1))/((log(r2/r1))*(1-gamma1)),\
                                       r1*h1*(Ti-T1)-K20*(T20**gamma2)*(T2**(1-gamma2)-T3**(1-gamma2))/((log(r3/r2))*(1-gamma2)),\
                                       r1*h1*(Ti-T1)-K30*(T30**gamma3)*(T3**(1-gamma3)-T4**(1-gamma3))/((log(r4/r3))*(1-gamma3)),\
                                       r1*h1*(Ti-T1)-K40*(T40**gamma4)*(T4**(1-gamma4)-T5**(1-gamma4))/((log(r5/r4))*(1-gamma4)),\
                                       r1*h1*(Ti-T1)-K50*(T50**gamma5)*(T5**(1-gamma5)-Ts**(1-gamma5))/((log(r6/r5))*(1-gamma5)))
                        T1, T2, T3, T4, T5, Ts= fsolve(equations, (1,1,1,1,1,1))
                        TL1=(T1**(1-gamma1)+(log(r1)-log(x1))*(T1**(1-gamma1)-T2**(1-gamma1))/log(r2/r1))**(1/(1-gamma1))
                        TL2=(T2**(1-gamma2)+(log(r2)-log(x2))*(T2**(1-gamma2)-T3**(1-gamma2))/log(r3/r2))**(1/(1-gamma2))
                        TL3=(T3**(1-gamma3)+(log(r3)-log(x3))*(T3**(1-gamma3)-T4**(1-gamma3))/log(r4/r3))**(1/(1-gamma3))
                        TL4=(T4**(1-gamma4)+(log(r4)-log(x4))*(T4**(1-gamma4)-T5**(1-gamma4))/log(r5/r4))**(1/(1-gamma4))
                        TL5=(T5**(1-gamma5)+(log(r5)-log(x5))*(T5**(1-gamma5)-Ts**(1-gamma5))/log(r6/r5))**(1/(1-gamma5))
                        plt.plot(x1,TL1)
                        plt.plot(x2,TL2)
                        plt.plot(x3,TL3)
                        plt.plot(x4,TL4)
                        plt.plot(x5,TL5)
                        plt.show()
                elif funcsel == "Vertical Cylinder":
                    if Layer ==1:
                        r1=L
                        r2=L+R
                        x=arange(r1,r2,0.0001)
                        K10=2
                        gamma1=0.2
                        T10=293
                        def equations(p1):
                                T1, Ts = p1
                                return (r1*h1*(Ti-T1)-r2*h2*(Ts-To),\
                                        r1*h1*(Ti-T1)-K10*(T10**gamma1)*(T1**(1-gamma1)-Ts**(1-gamma1))/((log(r2/r1))*(1-gamma1)))
                        T1, Ts= fsolve(equations, (1,1))
                        print T1, Ts
                        T=(T1**(1-gamma1)+(log(r1)-log(x))*(T1**(1-gamma1)-Ts**(1-gamma1))/log(r2/r1))**(1/(1-gamma1))
                        plt.plot(x,T)
                        plt.show()
                    elif Layer ==2:
                        r1=L
                        r2=R1+L
                        r3=R1+R2+L
                        x1=arange(r1,r2,0.0001)
                        x2=arange(r2,r3,0.0001)
                        K10=2
                        gamma1=0.2
                        T10=293
                        K20=2
                        gamma2=0.2
                        T20=293
                        def equations(p2):
                                T1, T2, Ts =p2
                                return(r1*h1*(Ti-T1)-r3*h2*(Ts-To),\
                                       r1*h1*(Ti-T1)-K10*(T10**gamma1)*(T1**(1-gamma1)-T2**(1-gamma1))/((log(r2/r1))*(1-gamma1)),\
                                       r1*h1*(Ti-T1)-K20*(T20**gamma2)*(T2**(1-gamma2)-Ts**(1-gamma2))/((log(r3/r2))*(1-gamma2)))
                        T1, T2, Ts= fsolve(equations, (1,1,1))
                        TL1=(T1**(1-gamma1)+(log(r1)-log(x1))*(T1**(1-gamma1)-T2**(1-gamma1))/log(r2/r1))**(1/(1-gamma1))
                        TL2=(T2**(1-gamma2)+(log(r2)-log(x2))*(T2**(1-gamma2)-Ts**(1-gamma2))/log(r3/r2))**(1/(1-gamma2))
                        plt.plot(x1,TL1)
                        plt.plot(x2,TL2)
                        plt.show()
                    elif Layer ==3:
                        r1=L
                        r2=R1+L
                        r3=R1+R2+L
                        r4=R1+R2+R3+L
                        x1=arange(r1,r2,0.0001)
                        x2=arange(r2,r3,0.0001)
                        x3=arange(r3,r4,0.0001)
                        K10=2
                        gamma1=0.2
                        T10=293
                        K20=2
                        gamma2=0.2
                        T20=293
                        K30=2
                        gamma3=0.2
                        T30=293
                        def equations(p3):
                                T1, T2, T3, Ts =p3
                                return(r1*h1*(Ti-T1)-r4*h2*(Ts-To),\
                                       r1*h1*(Ti-T1)-K10*(T10**gamma1)*(T1**(1-gamma1)-T2**(1-gamma1))/((log(r2/r1))*(1-gamma1)),\
                                       r1*h1*(Ti-T1)-K20*(T20**gamma2)*(T2**(1-gamma2)-T3**(1-gamma2))/((log(r3/r2))*(1-gamma2)),\
                                       r1*h1*(Ti-T1)-K30*(T30**gamma3)*(T3**(1-gamma3)-Ts**(1-gamma3))/((log(r4/r3))*(1-gamma3)))
                        T1, T2, T3, Ts= fsolve(equations, (1,1,1,1))
                        TL1=(T1**(1-gamma1)+(log(r1)-log(x1))*(T1**(1-gamma1)-T2**(1-gamma1))/log(r2/r1))**(1/(1-gamma1))
                        TL2=(T2**(1-gamma2)+(log(r2)-log(x2))*(T2**(1-gamma2)-T3**(1-gamma2))/log(r3/r2))**(1/(1-gamma2))
                        TL3=(T3**(1-gamma3)+(log(r3)-log(x3))*(T3**(1-gamma3)-Ts**(1-gamma3))/log(r4/r3))**(1/(1-gamma3))
                        plt.plot(x1,TL1)
                        plt.plot(x2,TL2)
                        plt.plot(x3,TL3)
                        plt.show()
                    elif Layer ==4:
                        r1=L
                        r2=R1+L
                        r3=R1+R2+L
                        r4=R1+R2+R3+L
                        r5=R1+R2+R3+R4+L
                        x1=arange(r1,r2,0.0001)
                        x2=arange(r2,r3,0.0001)
                        x3=arange(r3,r4,0.0001)
                        x4=arange(r4,r5,0.0001)
                        K10=2
                        gamma1=0.2
                        T10=293
                        K20=2
                        gamma2=0.2
                        T20=293
                        K30=2
                        gamma3=0.2
                        T30=293
                        K40=2
                        gamma4=0.2
                        T40=293
                        def equations(p4):
                                T1, T2, T3, T4, Ts =p4
                                return(r1*h1*(Ti-T1)-r5*h2*(Ts-To),\
                                       r1*h1*(Ti-T1)-K10*(T10**gamma1)*(T1**(1-gamma1)-T2**(1-gamma1))/((log(r2/r1))*(1-gamma1)),\
                                       r1*h1*(Ti-T1)-K20*(T20**gamma2)*(T2**(1-gamma2)-T3**(1-gamma2))/((log(r3/r2))*(1-gamma2)),\
                                       r1*h1*(Ti-T1)-K30*(T30**gamma3)*(T3**(1-gamma3)-T4**(1-gamma3))/((log(r4/r3))*(1-gamma3)),\
                                       r1*h1*(Ti-T1)-K40*(T40**gamma4)*(T4**(1-gamma4)-Ts**(1-gamma4))/((log(r5/r4))*(1-gamma4)))
                        T1, T2, T3, T4, Ts= fsolve(equations, (1,1,1,1,1))
                        TL1=(T1**(1-gamma1)+(log(r1)-log(x1))*(T1**(1-gamma1)-T2**(1-gamma1))/log(r2/r1))**(1/(1-gamma1))
                        TL2=(T2**(1-gamma2)+(log(r2)-log(x2))*(T2**(1-gamma2)-T3**(1-gamma2))/log(r3/r2))**(1/(1-gamma2))
                        TL3=(T3**(1-gamma3)+(log(r3)-log(x3))*(T3**(1-gamma3)-T4**(1-gamma3))/log(r4/r3))**(1/(1-gamma3))
                        TL4=(T4**(1-gamma4)+(log(r4)-log(x4))*(T4**(1-gamma4)-Ts**(1-gamma4))/log(r5/r4))**(1/(1-gamma4))
                        plt.plot(x1,TL1)
                        plt.plot(x2,TL2)
                        plt.plot(x3,TL3)
                        plt.plot(x4,TL4)
                        plt.show()
                    elif Layer ==5:
                        r1=L
                        r2=R1+L
                        r3=R1+R2+L
                        r4=R1+R2+R3+L
                        r5=R1+R2+R3+R4+L
                        r6=R1+R2+R3+R4+R5+L
                        x1=arange(r1,r2,0.0001)
                        x2=arange(r2,r3,0.0001)
                        x3=arange(r3,r4,0.0001)
                        x4=arange(r4,r5,0.0001)
                        x5=arange(r5,r6,0.0001)
                        K10=2
                        gamma1=0.2
                        T10=293
                        K20=2
                        gamma2=0.2
                        T20=293
                        K30=2
                        gamma3=0.2
                        T30=293
                        K40=2
                        gamma4=0.2
                        T40=293
                        K50=2
                        gamma5=0.2
                        T50=293
                        def equations(p5):
                                T1, T2, T3, T4, T5, Ts =p5
                                return(r1*h1*(Ti-T1)-r6*h2*(Ts-To),\
                                       r1*h1*(Ti-T1)-K10*(T10**gamma1)*(T1**(1-gamma1)-T2**(1-gamma1))/((log(r2/r1))*(1-gamma1)),\
                                       r1*h1*(Ti-T1)-K20*(T20**gamma2)*(T2**(1-gamma2)-T3**(1-gamma2))/((log(r3/r2))*(1-gamma2)),\
                                       r1*h1*(Ti-T1)-K30*(T30**gamma3)*(T3**(1-gamma3)-T4**(1-gamma3))/((log(r4/r3))*(1-gamma3)),\
                                       r1*h1*(Ti-T1)-K40*(T40**gamma4)*(T4**(1-gamma4)-T5**(1-gamma4))/((log(r5/r4))*(1-gamma4)),\
                                       r1*h1*(Ti-T1)-K50*(T50**gamma5)*(T5**(1-gamma5)-Ts**(1-gamma5))/((log(r6/r5))*(1-gamma5)))
                        T1, T2, T3, T4, T5, Ts= fsolve(equations, (1,1,1,1,1,1))
                        TL1=(T1**(1-gamma1)+(log(r1)-log(x1))*(T1**(1-gamma1)-T2**(1-gamma1))/log(r2/r1))**(1/(1-gamma1))
                        TL2=(T2**(1-gamma2)+(log(r2)-log(x2))*(T2**(1-gamma2)-T3**(1-gamma2))/log(r3/r2))**(1/(1-gamma2))
                        TL3=(T3**(1-gamma3)+(log(r3)-log(x3))*(T3**(1-gamma3)-T4**(1-gamma3))/log(r4/r3))**(1/(1-gamma3))
                        TL4=(T4**(1-gamma4)+(log(r4)-log(x4))*(T4**(1-gamma4)-T5**(1-gamma4))/log(r5/r4))**(1/(1-gamma4))
                        TL5=(T5**(1-gamma5)+(log(r5)-log(x5))*(T5**(1-gamma5)-Ts**(1-gamma5))/log(r6/r5))**(1/(1-gamma5))
                        plt.plot(x1,TL1)
                        plt.plot(x2,TL2)
                        plt.plot(x3,TL3)
                        plt.plot(x4,TL4)
                        plt.plot(x5,TL5)
                        plt.show()


root = Tk()
root.title("Beta")
root.geometry("600x500")
app = Application(root)
root.mainloop()

