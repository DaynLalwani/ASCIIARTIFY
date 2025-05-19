import tkinter.messagebox #import message box from tkinter
from PIL import Image #Import Pillow For Image Manuipilation
import os #import OS to clear terminal
import tkinter as t #import tkinter for GUI
def encodegui():#IMG To ASCII ART .Txt
    def continu(sh):#func to continue
        import tkinter.messagebox as msb#import messagebox
        if msb.askyesno("CONTINUE?","This May take time depending on hardware and size of image , check the command line for progress"):#Ask user if they want to continue
            encode(sh,False)#call the encode
    rot2 = t.Toplevel()#Make window for IMG to ASCII ART GUI
    t.Label(rot2,text="ASCII ARTIFIYER",font=("Helvetica",36,"bold")).pack()#Heading For Window
    t.Label(rot2,text="CLICK NEXT AFTER download.png IS In The Working Directory ( will save to output.txt)",font=("Helvetica",12,"bold")).pack()#Instructions For User
    t.Label(rot2,text="GREYSCALE Indentifier Value (default is 60)",font=("Helvetica",12,"bold")).pack()#Instructions For Greyscale Identifiyer
    w = t.Scale(rot2, from_=40, to=80, orient=t.HORIZONTAL,font=("Helvetica",12,"bold"),length=500)#Add Slider
    w.pack()#Make Slider Visible
    t.Button(rot2,text="NEXT",command= lambda : continu(w.get()),font=("Helvetica",12,"bold")).pack()#Create Button to continue
    rot2.mainloop()#Tinter ending
def encode(tew,climode):#Image To Txt ASCII ART FUNCTION
    if climode:#Check IF IN CLI Mode
        input("put input.png file in same directory as this script , ENTER to contine")#Instruct User to put file in dir
    original = Image.open('input.png').convert('L')#Open the Image And Convert to Greyscale
    pixels = list(original.getdata())# Put All Pixels on a list
    width, height = original.size # List width and height
    count = 0 # Counter ( will be used later)
    asciiart = [] #Output ascii art list (will be converted into string)
    h = 0#current height
    w = 0#Current Width
    for i in pixels:#Iterate over every pixel
        if w == width:#Check If is on last pixel of a row
            w = 0# Go to start of row
            h += 1 # go to next row
            asciiart.append("\n")#Newline in str
        if i>=tew:#Check if pixel is supposed to be black 
            asciiart.append(".")#Put fullstop for black
        else:
            asciiart.append("#")#put # for white
        count +=1#Add to counter (progress)
        w += 1#Go to next pixel in the row
        print(f"\rPROGRESS {count}/{len(pixels)} [{(int((count/len(pixels))*100000))/1000}%]",end="",flush=True)#Show the progress to the user
    result = ''.join(asciiart)#Make the ASCIIART list into a string
    with open("output.txt", "w") as f:#Open or make a file called output.txt
        f.write(str(result))#Save the ASCIIART to the file
    print("Saved in output.txt")#Tell The User That It HAs Been Saved
    if climode and (input("Back to Main Menu [Y/N]") == "Y"):#ask user if they want to go to main cli menu
        from main import cli
        cli()#go to main cli menu 