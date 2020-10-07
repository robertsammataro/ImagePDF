import os
from os import *
import shutil
import tkinter as tk
from tkinter import ttk 
from tkinter import *
from PIL import ImageTk,Image
from datetime import datetime
from tkinter import filedialog
from tkinter import messagebox
from fpdf import FPDF

def mergePDF(inp, out, png, jpg, jpeg, gif, bmp, sortChoice):
    
    ##################################
    # Converts .png files with Alpha #
    #     Values to Strictly RGB     #
    ##################################
    
    compressList = []
    
    for file in os.listdir(inp):
        if(file.split('.')[-1] == 'png'):
            compressList.append(file)
    for image in compressList:
        im1 = Image.open(inp+"\\"+image)
        im1 = im1.convert('RGB')
        im1.save(inp+"\\"+image.split(".")[0]+".png")
 
 
 
 
    #################################
    #  Sorts filenames based of of  #
    #    method from main screen    #
    #################################
 
 
    if(sortChoice == "Date Created"):
        x=0
        inp_list = os.listdir(inp)
        while(x < len(inp_list)):
            inp_list[x] = (inp + "\\" + inp_list[x])
            x = x+1
        inp_list.sort(key=os.path.getctime)
        
        x=0
        
         
    if(sortChoice == "Date Modified"):
        x=0
        inp_list = os.listdir(inp)
        while(x < len(inp_list)):
            inp_list[x] = (inp + "\\" + inp_list[x])
            x = x+1
        inp_list.sort(key=os.path.getctime)
        
        
    if(sortChoice == "File Size"):
        x=0
        inp_list = os.listdir(inp)
        while(x < len(inp_list)):
            inp_list[x] = (inp + "\\" + inp_list[x])
            x = x+1
        inp_list.sort(key=os.path.getsize)
        
    else:
        x=0
        inp_list = os.listdir(inp)
        while(x < len(inp_list)):
            inp_list[x] = (inp + "\\" + inp_list[x])
            x = x+1

    #####################################
    # Filters out unselected filetypes  #
    #####################################

            
    fileList = []
    
    for file in inp_list:
        if(png == 1 and file.split('.')[-1] == 'png'):
            fileList.append(file)
        elif(jpg == 1 and file.split('.')[-1] == 'jpg'):
            fileList.append(file)
        elif(jpeg == 1 and file.split('.')[-1] == 'jpeg'):
            fileList.append(file)
        elif(gif == 1 and file.split('.')[-1] == 'gif'):
            fileList.append(file)
        elif(bmp == 1 and file.split('.')[-1] == 'bmp'):
            fileList.append(file)
    
    
    image = Image.open(fileList[0])
    width, height = image.size
    
    
    ##################################
    #  Add Images To New Page of pdf #
    ##################################
    
    
    pdf = FPDF('P', 'pt', (width,height))
    for file in fileList:
        pdf.add_page()
        pdf.image((file),0,0,width,height)
        print("Successfully processed",file)
        
        
    ###################################
    #  Saves PDF in Output Directory  #
    #  Note: If User Put in a Custom  #
    #  Filename on the main screen it #
    #  Will Save with that filename   #
    ###################################
    
    
    if("." in out and out.split(".")[-1] == "pdf"):
        pdf.output(out, "F")
        outputFile = out
    else:
        pdf.output(out+"\\"+"output.pdf", "F")
        outputFile = (out+"/"+"output.pdf")
    
    root = Tk()
    root.withdraw()
    messagebox.showinfo(title="Info", message="PDF Created At:\n"+str(outputFile))
    quit()
    


def beginWindow():
    
    def getLocation(entryBox):
        
        ###################################
        #  Opens File Explorer for User   #
        #  To Select Source/Dest Folder   #
        ###################################
        
        
        path = filedialog.askdirectory()
        entryBox.delete(0,END)
        entryBox.insert(0,path)
        
        
    ######################
    #  Home Menu Script  #
    ######################
    
    mainWindow = Tk()
    mainWindow.title("ImagePDF")
    mainWindow.geometry("275x450")
    mainWindow.iconbitmap("imgsort.ico")
    mainWindow.resizable(False,False)
    
    logo_img = ImageTk.PhotoImage(Image.open("logo.png").resize((250,50),Image.ANTIALIAS))
    logo_label = Label(mainWindow, image=logo_img, width = 300, height = 50)
    logo_label.place(anchor="n", relx=.5, rely=.025)
    
    copyrightLabel = Label(mainWindow, text="© 2020 Robert Sammataro")
    copyrightLabel.configure(font=("Arial",9), borderwidth=1, bg="white", padx=5, relief='sunken')
    copyrightLabel.place(anchor='sw',x=0, rely=1)
    
    licenseLabel = Label(mainWindow, text="Free for home use")
    licenseLabel.configure(font=("Arial",9), borderwidth=1, bg="white", padx=6, relief='sunken')
    licenseLabel.place(anchor='se',x=275, rely=1)
    
    sourceEntry = Entry(mainWindow, width=31)
    sourceEntry.config(font=("Arial",9))
    sourceEntry.place(anchor='nw', x=20, y=80)
    
    image = Image.open("browse.png")
    image = image.resize((12,12), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(image=image)
    sourceExplorer = Button(mainWindow, image=img1, width=15, height=15, command=lambda:getLocation(sourceEntry))
    sourceExplorer.place(anchor="nw", x=235, y=80)
    
    sourceLabel = Label(mainWindow, text="Source Directory")
    sourceLabel.place(anchor='nw', x=20, y=100)
    
    outputEntry = Entry(mainWindow, width=31)
    outputEntry.config(font=("Arial",9))
    outputEntry.place(anchor='nw', x=20, y=130)
    
    outputExplorer = Button(mainWindow, image=img1, width=15, height=15, command=lambda:getLocation(outputEntry))
    outputExplorer.place(anchor="nw", x=235, y=130)
    
    outputLabel = Label(mainWindow, text="Output Directory")
    outputLabel.place(anchor='nw', x=20, y=150)
    
    fileFormats = LabelFrame(mainWindow, text="Included File Formats", pady=7)
    fileFormats.place(anchor="n", relx=.5, y=180)
    
    pngVar = IntVar()
    jpgVar = IntVar()
    jpegVar = IntVar()
    gifVar = IntVar()
    bmpVar = IntVar()
    
    ###############################
    #  Will show a warning when   #
    #  png file box is selected   #
    ###############################
    
    def showPngWarning(count):
        if(count == 1):
            messagebox.showwarning(title="Compress existing .png?", message='.png files in the source directory will be\ncompressed. Ensure originals are backed\nup before continuing.')
    
    pngButton = Checkbutton(fileFormats, text='.png', variable=pngVar, command=lambda:showPngWarning(pngVar.get()))
    pngButton.grid(row = 0, column = 0, padx=30)
    
    jpgButton = Checkbutton(fileFormats, text='.jpg', variable=jpgVar)
    jpgButton.grid(row = 0, column = 1, padx=30)
    
    jpegButton = Checkbutton(fileFormats, text='.jpeg', variable=jpegVar)
    jpegButton.grid(row = 1, column = 0, padx=30)
    
    gifButton = Checkbutton(fileFormats, text='.gif', variable=gifVar)
    gifButton.grid(row = 1, column = 1, padx=30)
    
    bmpButton = Checkbutton(fileFormats, text='.bmp', variable=bmpVar)
    bmpButton.grid(row = 2, column = 0, padx=30)
    
    sortLabel = tk.StringVar()
    sortChoice = ttk.Combobox(mainWindow, values=['Alphanumeric','Date Created','Date Modified','File Size'], width = 27, textvariable = sortLabel)
    sortChoice.configure(state='readonly')
    sortChoice.set('Alphanumeric')
    sortChoice.place(anchor='center',relx=.5,y=325)
    
    sortChoiceLabel = Label(mainWindow, text='Source Image Sort Method')
    sortChoiceLabel.place(anchor="nw",x=43, y=336)
    
    beginButton = Button(mainWindow, text="Begin", padx=15, pady=5, command=lambda:mergePDF(sourceEntry.get(),
                                                                                            outputEntry.get(),
                                                                                            pngVar.get(),
                                                                                            jpgVar.get(),
                                                                                            jpegVar.get(),
                                                                                            gifVar.get(),
                                                                                            bmpVar.get(),
                                                                                            sortChoice.get()))
    beginButton.place(anchor='w', x=175, y=400)

    mainWindow.mainloop()

if __name__ == '__main__':
    beginWindow()



