import tkinter.messagebox #import message box from tkinter
from PIL import Image #Import Pillow For Image Manuipilation
import os #import OS to clear terminal
import tkinter as t #import tkinter for GUI
import encode2,decode2
def recode(tew,climode):# Function To Read Image , turn to Greyscale and output it as ASCII art 
    if climode:#Check If The Program Is In CLI MODE
        input("put input.png file in same directory as this script , ENTER to contine")#ASK The User To Put File In Working Directory
    original = Image.open('input.png').convert('L')#Load Image
    pixels = list(original.getdata())#get all pixels of Image
    width, height = original.size#git width and height of image
    count = 0#counter for progress
    asciiart = []#List of the individual Pixels which will be an ascii art
    h = 0#current height
    w = 0 # current width 
    for i in pixels:#Iterate over all pixels
        if w == width:#Check if on last pixel of row
            w = 0#go to first pixel
            h += 1#Go to next line 
            asciiart.append("\n")# put a newline to actually change line in print
        if i>=tew:#check if pixel is supposed to be black or white,tew is threshold of black or white
            asciiart.append(".")#Sets current pixel to . as it looks like black  
        else:
            asciiart.append("#")# sets current pixel to # it looks like white
        count +=1#add a count
        w += 1#go to next pixel
        print(f"\rPROGRESS {count}/{len(pixels)} [{(int((count/len(pixels))*100000))/1000}%]",end="",flush=True)#Show user the progress
    result = ''.join(asciiart)#Combine all the pixels into a string
    print(result)#print the string
    if climode and (input("Back to Main Menu [Y/N]") == "Y"):#ask user if they whant to re run 
        cli()#Rerun if yes
def cli():#CLI INTERFACE
    os.system('cls' if os.name == 'nt' else 'clear')#Clear Terminal
    print("What Do you want to do \n    1.Test Your Image \n    2.Encode img to text\n    3.Decode Text to terminal")#Ask youser what to do
    td = input("Choose option [1/2/3] : ")#get their input
    if td == "1":#check their option
        recode(60,True)#Call recode func
    elif td == "2":
        encode2.encode(60,True)#Call Encode Func
    elif td == "3":
        decode2.decode(True)#Call Decode Func
def imgtestgui():#GUI FOR RECODE
    def continu(sh):#ASK USER TO CONTINUE
        import tkinter.messagebox as msb# Import Message Box
        if msb.askyesno("CONTINUE?","This May take time depending on hardware and size of image , check the command line for progress"):#Show the user the message box
            recode(sh,False)#Call the Recode Command
    rot1 = t.Toplevel()#Make the GUI for the IMG TEST 
    t.Label(rot1,text="ASCII ARTIFIYER",font=("Helvetica",24,"bold")).pack()#Make a Label With the Name
    t.Label(rot1,text="CLICK NEXT AFTER download.png IS In The Working Directory",font=("Helvetica",12,"bold")).pack()#Make Label with instructions
    t.Label(rot1,text="GREYSCALE Indentifier Value (default is 60)",font=("Helvetica",12,"bold")).pack()
    w = t.Scale(rot1, from_=40, to=80, orient=t.HORIZONTAL,length=300,font=("Helvetica",12,"bold"))#Make Slider 
    w.pack()#Add Slider to GUI
    t.Button(rot1,text="NEXT",command= lambda : continu(w.get()),font=("Helvetica",12,"bold")).pack()#Make buttion to call command
    rot1.mainloop()#Ending For tkinter
def gui():#Main Menu GUI
    def SwitchtoGUI():#Function to switch To CLI
        root.destroy()#Close the Window
        cli()#call the CLI command
    root = t.Tk()#Make the MAIIN window
    t.Label(text="ASCII ARTIFIYER",font=("Helvetica",36,"bold")).pack()#Add Heading 
    t.Button(text="IMAGE TEST",command=imgtestgui,font=("Helvetica",12,"bold")).pack()#Make Button For Image Test
    t.Button(text="Image To ASCII ART .TXT",command=encode2.encodegui,font=("Helvetica",12,"bold")).pack()#Make button For Img to txt
    t.Button(text="ASCII ART .TXT to Terminal/PNG",command=decode2.decodegui,font=("Helvetica",12,"bold")).pack()# make button for Txt to terminal
    t.Button(text="SWITCH TO CLI",command=SwitchtoGUI,font=("Helvetica",12,"bold")).pack()#button to switch to CLI
    root.mainloop()#Ending for tkinter
gui()#Call GUI