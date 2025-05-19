import tkinter.messagebox #import message box from tkinter
from PIL import Image #Import Pillow For Image Manuipilation
import os #import OS to clear terminal
import tkinter as t #import tkinter for GUI
def decode(climode):#TEXT TO THE ASCII ART IN TERMINAL
    if climode:#Check if user is using cli
        input("put output.txt file in same directory as this script , ENTER to contine")#Ask user to check files
    with open("output.txt", "r") as file:#open file
        content = file.read()#Read Text in file
    print(content)#Show The ASCII ART
    if climode and input("Back to Main Menu [Y/N]") == "Y":#ask user to go to main menu if in cli mode
        from main import cli
        cli()# go to main menu
def decodegui():# GUI For DECODE
    def continu():#Function To Continue
        import tkinter.messagebox as msb# import Message box
        if msb.askyesno("CONTINUE?","ASCII ART WILL SHOW IN COMMAND LINE , ZOOM OUT TO FULLY SEE IT"): # ask user to continue
            decode(False)# IF yes Continue
    def continu2():#Function to continue ( to png)
        import tkinter.messagebox as msb# imporrt message pox
        if msb.askyesno("CONTINUE?","ASCII ART WILL SHOW IN A PHOTOS WINDOW AND BE SAVED TO output.png"):#ask user if they want to continue
            decodepng(False)#If yes call decodepng
    rot3 = t.Toplevel()#Make new window for DECODe
    t.Label(rot3,text="ASCII ARTIFIYER",font=("Helvetica",36,"bold")).pack()#Main Heading Label
    t.Label(rot3,text="CLICK NEXT AFTER output.txt IS In The Working Directory ",font=("Helvetica",12,"bold")).pack()#Tell User to add the file
    t.Button(rot3,text="NEXT ( Print To Terminal)",command= lambda : continu(),font=("Helvetica",12,"bold")).pack()#Button to continue to print
    t.Button(rot3,text="NEXT (Save As PNG)",command= lambda : continu2(),font=("Helvetica",12,"bold")).pack()# Button to continue to save as png
    rot3.mainloop()#tkinter ending
def decodepng(climode):#ASCII ART output.txt to IMG
    if climode:# Check if user is in climode 
        input("put output.txt file in same directory as this script , ENTER to contine")# Ask youser to put file
    with open("output.txt", "r") as file:# Read file
        content = file.read()#Save contents into variable
    width = 0#Width of image
    height = 0#height of image
    count = 0#counter
    #for loop to get height and width
    for i in content:
        if i == "\n":#check if it is at end of line
            if count > width:#set width
                width = count
            count = 0# reset current pixel
            height += 1#add 1 more to height
        else:
            count += 1#go to next pixel
    if count > 0:#check if is in middle of row
        height += 1#add 1 to hight
        if count > width:#make sure width is correct
            width = count
    img = Image.new('RGB', (width, height), color='white')#make new image
    w, h = 0, 0#set a counter for height and width
    for i in content:#loop over every pixel
        if i == "\n":#if at end of line go to first pixel of next row
            h += 1#go to next row
            w = 0#pixel at first
        else:#check pixel
            if i == "#":#check if it is a white pixel
                img.putpixel((w, h), (0, 0, 0))#set it to a white pixel
            else:#otherwise
                img.putpixel((w, h), (255, 255, 255))#set to black pixel
            w += 1#go to next pixel
        count += 1
        print(f"\rPROGRESS {count}/{height*width} [{(int((count/(height*width))*100000))/1000}%]",end="",flush=True)#Show user the progress

    img.show()#Show user the image
    img.save("output.png")#save image to working dir
    if climode and input("Back to Main Menu [Y/N]") == "Y":#ask user to return to cli main menu
        from main import cli
        cli()#go to main menu
