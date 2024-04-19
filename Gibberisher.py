import os
import time
import datetime
import string
import pickle
import tkinter as tk
import tkinter.font as tkFont
from os import system
from time import sleep

## NEXT-STEPS

## make sure we understand Controller() and controller object mycontroller, and that the usage throughout the code is consistent
        # it should tie each class together and probably be an attribute for each class
## get tkinter.Label to update text to show new readfilename
        # halfway working, see line 182
        # TypeError: App.updateLabel1() missing 1 required positional argument: 'x'
## get text input boxes working
        # create new frame for text input
## decompose classes into MVC files



## NEW IN THIS VERSION

# adding second App class (AppWindow_Input) and modifying it to have controller attribute
# trying to work on switching frames
# see: https://stackoverflow.com/questions/34301300/tkinter-understanding-how-to-switch-frames
# see: https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# https://coderslegacy.com/python/switching-between-tkinter-frames-with-tkraise/


## halfway implemented this tweak but didn't get it working yet

class Model():
    def __init__(self):
        self.name = "myDataModel"
        self.filename = "N/A"
        self.filedir=""
        self.readfilename = "N/A"
        self.base_words_array = []
        self.append_string_array = []
        self.allcharsarray = []
        self.ascii = string.ascii_letters
        self.digits = string.digits
        self.punct = string.punctuation
        self.array1 = []
        self.array2 = []
        self.array3 = []
        self.array1.extend(self.ascii)
        self.array2.extend(self.digits)
        self.array3.extend(self.punct)
        self.allcharsarray = self.array1 + self.array2 + self.array3
        self.outputwordlist_array = []

    ## May not be needed since calling mymodel.modelName is achieving this already
    def get_modelName(self):
        return self.name
    def get_filename(self):
        return self.filename
    def set_filename(self, x):
        self.filename = x
    def set_filedir(self, x):
        self.filedir = x
    def set_readfilename(self, x):
        self.readfilename = x
    def set_base_words_array(self, x):
        self.base_words_array = x
    def set_append_string_array(self, x):
        self.append_string_array = x
    def set_allcharsarray(self, x):
        self.allcharsarray = x




class Controller():
    
    def savedata():
        readfilename = mymodel.readfilename
        base_words_array = mymodel.base_words_array
        with open('readfilesave.pkl','wb') as file:
            pickle.dump(mymodel.readfilename, file)
        with open('basesave.pkl','wb') as file:
            pickle.dump(mymodel.base_words_array, file)

    def retrievesavedata():
        readfilename = mymodel.readfilename
        base_words_array = mymodel.base_words_array
        try:
            with open('readfilesave.pkl','rb') as file:
                readfilename = str(pickle.load(file))
                mymodel.readfilename = readfilename
        except:
            print("Load save error, sorry...\n")
            time.sleep(1)
        try:
            with open('basesave.pkl','rb') as file:
                base_words_array = pickle.load(file)
                mymodel.base_words_array = base_words_array
        except:
            print("Load save error, sorry...\n")
            time.sleep(1)

    def mainmenu():
        while(True):
            readfilename = mymodel.readfilename
            Controller.savedata()
            os.system('cls')
            print("1. Set File Name")
            print("2. Generate Wordlist (Basic)")
            print("3. Set File Directory")
            print("4. Ingest Base Words")
            print("5. Debug Shortcut")
            print("\nCurrent Read File Name: " + mymodel.readfilename)
            option=input("\nSelect an option.\n: ")
            try:
                option = int(option)
            except ValueError:
                print("Please try a valid input.")
                sleep(1)
                continue
            if option == 1:
                Controller.setfilename()
            if option == 2:
                Controller.generatewordlist()
            if option == 3:
                Controller.setfiledir()
            if option == 4:
                Controller.ingestbasewords()
            if option == 5:
                Controller.generate_one_rand_char()
            else:
                print("Please try again.")

    def ingestbasewords():
        while(True):
            global readfilename
            global base_words_array
            readfilename = readfilename
            os.system('cls')
            print("Ingesting from '"+str(readfilename) + "'\n")
            with open(readfilename, 'r') as readfile:
                readfilearray = readfile.read().splitlines()
                for word in readfilearray:
                    base_words_array.append(word)
                print("\n")
                print(str(base_words_array))
            print("\nBase Words ingested.\n")
            time.sleep(1)
            Controller.mainmenu()
            
    def setfilename():
        while(True):
            option = ""
            ## We're referencing the Model class not a Model class object
            filename = mymodel.filename
            filedir = mymodel.filedir
            readfilename = mymodel.readfilename
            os.system('cls')
            print("Current filename: '"+filename+"'\n")
            option=input("Type filename: \n: ")
            try:
                option = str(option)
            except ValueError:
                print("Somehow, that's not a string.")
                sleep(1)
                continue
            mymodel.set_filename(option)
            readfilename = str(mymodel.filedir) + str(mymodel.filename)
            mymodel.set_readfilename(readfilename)
            print("set_filename: " + mymodel.readfilename)
            print("\nYour new filename is: '"+option+"'\n")
            sleep(1)
            print("Returning to main menu...")
            sleep(1)

            ### BIG BREAKTHROUGH
            ## THIS IS IS THE RIGHT SYNTAX TO REFERENCE A METHOD IN THE APP CLASS 
            App.updateLabel(app)

            Controller.savedata()
            Controller.mainmenu()
            ##
            ##        

    def setfiledir():
        while(True):
            filedir = mymodel.filedir
            filename = mymodel.filename
            readfilename = mymodel.readfilename
            os.system('cls')
            print("Current File Directory: '"+filedir+"'\n")
            option=input("Type absolute path to File Directory: \n: ")
            try:
                option = str(option)
            except ValueError:
                print("Somehow, that's not a string.")
                sleep(1)
                continue
            mymodel.filedir = option
            mymodel.readfilename = str(filedir) + str(filename)
            print("\nYour new File Directory is: '"+filedir+"'\n")
            sleep(1)
            print("Returning to main menu...")
            sleep(1)
            Controller.mainmenu()
            return filedir

    def generatewordlist():
        while(True):
            readfilename = mymodel.readfilename
            os.system('cls')
            print("Current read file: '"+readfilename+"'\n")
            print("1. Basic Wordlist")
            print("2. Moderate Wordlist")
            print("3. Complex Wordlist")
            option = input("\nPlease select an option.\n: ")
            try:
                option = int(option)
            except:
                print("Please try a valid input.")
                continue
            if option == 1:
                Controller.generatebasicwordlist()
            if option == 2:
                continue
            if option == 3:
                continue
            else:
                continue            

    def generatebasicwordlist():
        while(True):
            readfilename = mymodel.readfilename
            os.system('cls')
            Controller.generate_one_rand_char()

    def generate_one_rand_char():
        total_rand_chars = 0
        base_words_array = mymodel.base_words_array
        allcharsarray = mymodel.allcharsarray
        outputwordlist_array = mymodel.outputwordlist_array
        filedir = mymodel.filedir
        basewordsCounter = 0
        basewordsCount = len(base_words_array)
        while basewordsCounter < basewordsCount:
            #print("first while loop")
            char = 0
            print(basewordsCounter)
            while char < 69:
                #print("second while loop")
                print(char)
                appendstr1=str(allcharsarray[char])
                print("append")
                basestr1=str(base_words_array[basewordsCounter])
                print("base")
                newstring = basestr1 + appendstr1
                print("new")
                #print("basetr1: " + basestr1)
                #print("appendstr1: " + appendstr1)
                #print("newstring: " + newstring)
                outputwordlist_array.append(newstring)
                char = char + 1
            basewordsCounter = basewordsCounter + 1   
        print(outputwordlist_array)
        print(len(outputwordlist_array))
        with open(filedir + "outputfile.txt", 'w') as file:
            for word in outputwordlist_array:
                file.write("%s\n" % word)
        print("\nDebug: generate_one_rand_char() succeeded.\n")
        time.sleep(5)








class App:
    def __init__(self, root, controller):

        Controller.retrievesavedata() 
        #var = StringVar()



        self.controller = controller

        #setting title
        root.title("Gibberisher 1.3")
        #setting window size
        width=1200
        height=800
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        ## create canvas which lets us set background img
        canvas1 = tk.Canvas(root,width=1200,height=800)
        canvas1.pack()
        canvas1.create_image(0,0,image=bg_img,anchor='nw')
        canvas1.place(relx=0,rely=0)


       
        ## frame switch
        mainframe = tk.Frame(root)
        mainframe.pack(padx=10,pady=10,fill='both',expand=1)
        self.windowNum=0

        self.framelist = []
        self.framelist.append(PageOne(mainframe))
        self.framelist.append(PageTwo(mainframe))
        self.framelist[1].forget()

        bottomframe = tk.Frame(root)
        bottomframe.pack(padx=10,pady=10)

        switch = tk.Button(bottomframe,text="Switch", command=self.switchWindows)
        switch.pack(padx=10,pady=10)
        ## frame switch




        GButton_855=tk.Button(root)
        GButton_855["anchor"] = "center"
        GButton_855["bg"] = "#b0ffab"
        ft = tkFont.Font(family='Times',size=10)
        GButton_855["font"] = ft
        GButton_855["fg"] = "#000000"
        GButton_855["justify"] = "center"
        GButton_855["text"] = "Set File Name"
        GButton_855["relief"] = "raised"
        GButton_855.place(x=330,y=160,width=557,height=30)
        GButton_855["command"] = self.GButton_855_command

        GButton_804=tk.Button(root)
        GButton_804["bg"] = "#90ee90"
        ft = tkFont.Font(family='Times',size=10)
        GButton_804["font"] = ft
        GButton_804["fg"] = "#000000"
        GButton_804["justify"] = "center"
        GButton_804["text"] = "Set File Directory"
        GButton_804.place(x=330,y=200,width=557,height=30)
        GButton_804["command"] = self.GButton_804_command

        GButton_371=tk.Button(root)
        GButton_371["bg"] = "#bcffff"
        ft = tkFont.Font(family='Times',size=10)
        GButton_371["font"] = ft
        GButton_371["fg"] = "#000000"
        GButton_371["justify"] = "center"
        GButton_371["text"] = "Ingest Base Words"
        GButton_371.place(x=330,y=260,width=556,height=30)
        GButton_371["command"] = self.GButton_371_command

        GButton_75=tk.Button(root)
        GButton_75["bg"] = "#ef9918"
        ft = tkFont.Font(family='Times',size=10)
        GButton_75["font"] = ft
        GButton_75["fg"] = "#000000"
        GButton_75["justify"] = "center"
        GButton_75["text"] = "Generate Wordlist"
        GButton_75.place(x=330,y=320,width=555,height=30)
        GButton_75["command"] = self.GButton_75_command

        GButton_924=tk.Button(root)
        GButton_924["bg"] = "#cda0f4"
        ft = tkFont.Font(family='Times',size=10)
        GButton_924["font"] = ft
        GButton_924["fg"] = "#000000"
        GButton_924["justify"] = "center"
        GButton_924["text"] = "Debug Shortcut"
        GButton_924.place(x=330,y=550,width=552,height=30)
        GButton_924["command"] = self.GButton_924_command

        GLabel_388=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_388["font"] = ft
        GLabel_388["fg"] = "#333333"
        GLabel_388["justify"] = "center"
        GLabel_388["text"] = "Current Read File (File Name + File Directory):"
        GLabel_388.place(x=330,y=400,width=553,height=37)

        ##
        ##
        ## READFILENAME LABEL
        self.readfilenameVar = str(mymodel.readfilename)
        self.string_variable = tk.StringVar(root, self.readfilenameVar)

        GLabel_85=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_85["font"] = ft
        GLabel_85["fg"] = "#333333"
        GLabel_85["justify"] = "center"
        GLabel_85["textvariable"] = str(self.string_variable)
        GLabel_85.place(x=330,y=430,width=554,height=42)



    def switchWindows(self):
        self.framelist[self.windowNum].forget()
        self.windowNum = (self.windowNum + 1) % len(self.framelist)
        self.framelist[self.windowNum].tkraise()
        self.framelist[self.windowNum].pack(padx=10,pady=10)


    def GButton_855_command(self):
        Controller.setfilename()
    def GButton_804_command(self):
        Controller.setfiledir()
    def GButton_371_command(self):
        Controller.ingestbasewords()
    def GButton_75_command(self):
        Controller.generatewordlist()
    #DEBUG
    def GButton_924_command(self):
        self.show_frame("PageOne")
    #DEBUG

    # now WORKING WORKING WORKING WORKING
    # https://stackoverflow.com/questions/47878587/python-accessing-widget-items-from-outside-of-a-class
    # solution: create string_variable with "self." prefix to make it an attribute of the App class
    def updateLabel(self):
        self.string_variable.set(str(mymodel.readfilename))




class PageOne(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        PageOnelabel1 = tk.Label(self, text="This is Page One")
        PageOnelabel1.pack(side="top",fill="x",pady=10)

class PageTwo(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        PageTwolabel1 = tk.Label(self, text="This is Page Two")
        PageTwolabel1.pack(side="top",fill="x",pady=10)






## Create instance of Model and Controller?
mycontroller = Controller()
mymodel = Model()

Controller.retrievesavedata()
print(mymodel.readfilename)

## Create "root" window from Tkinter module
root = tk.Tk()
##Create bg image (Notably, outside of the main App class so it doesn't get 'blown away' after we leave that __init__ method)
bg_img = tk.PhotoImage(file="C:\\Users\\Spooky\\Documents\\PyCharm\\img3.png")
## Create "app" instance of Tkinter class for view
app = App(root, mycontroller)
## Run the "root" window in a loop to capture user input and display GUI
root.mainloop()

