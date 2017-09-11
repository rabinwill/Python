'''
NAME = Rabin William David
WSUID = J965V385
Python Programming Assignment

The program asks for friend, gift ideas to gift the frined and where we
can find  the gift along with the cost.
Then this programs asks us to Enter a persons name, say the person to whom we
want to give the gift and then using random library it picks a random gift and
saves the output to a file and also shows the output on the window.


PSEUDO CODE:
Inputs: Asks user to enter a persons name and then asks the user to enter the
        gift for the specifc peron follwed by the location to find the gift and
        lastly the price of the gift.
        Then later, it asks the user to look up a person to whom the user wants
        to give a gift.
        Lastly, the program asks the user to enter the file name to save the
        randomly picked gift for the entered person.

Output: Outputs the randomly picked gift, the location, price and the name of
        the person in a user entered named file and also displays the output
        at the end in a window.

importing the from tkinter import *. This imports every exposed object in Tkinter
importing collections. This mplements specialized container datatypes providing
        alternatives to Python’s general purpose built-in containers.
importing os.path. This module contains functions that deal with long filenames
        (path names) in various ways.
importing random. This generates random numbers.

class Gift:
    def __init__ constructor
    getter of the name
    getter of the location
    getter of the price

class Friend:
    def __init__ constructor
    appneding gift
    getter of the name
    getter of the gift

Class MyInputDialog:
    def__init__ constructor
    getter to the input entered by the user
    getter to the top frame of the dialog box
    
class MyInputDialog:
    constructor to set the dialog to get input from the
    if user clicks ok button save the input
    getter to the input entered by the user
    getter to the top frame of the dialog box

class MyMessageDialog:
    constructor to set the confirmation/Message
    if ok button clicked then save the boolean for the OK
    if the cancel button is clicked then save the cancel boolean
    get the ok and cancel flags

class GUI(Frame): (
    The main GUI class to setup the command buttons, provide action
    handling gets commands and acts accordingly
    setting up the GUI, lable, buttons and action listeners
    setting the main frame
    collecting the friends
    def initGUI(self):
    function to setup the gui that will be called inside constructor,
    add label, buttons action listeners
        frame features
        lable components
        first button component
        second button component
        quit button compoenent
    def quit(self):
    function; event hadler to exit the application
        destroy
        exit
    def getText(self, txt):
    fuction; to get a message
    def getConfirmation(self, txt):
    function; to get the confirmation
        If statement to check if MyMessageDialog is confirmed the return True
        else return false
    def addPerson(self):
    function; event handler to add a new friend with all the gifts
        getting the persons name and creating a friend
        While loop; adding more gifts as needed
            Adding the gift
            the location
            the price
            Adding to friend
            more gifts or no confirmation
    def lookupPerson(self):
    function; event handler to do a look up for a given friend by name.
    If friend found, display friend's data, and ask an option to save the file.
        Asking the friends name
        finding the friend in the list
        if statement; if the friend data is found setting the found flag
        if statement; if the frined is not found then notify the user
        else; write to the file
            if; saving the file ask the user to enter the file name
                if; the file exists then say file exists
                else; open file and write the output to the file
                    close file
                    confirmation saying the file is saved
            display the friends data in the dialog box

def main():
    setup the window
    loop till user exists
closeing main()
'''


from tkinter import *                           #importing the libraried needed
import collections
import os.path
import random

class Gift:                                     #Gift class represents a gift
    
    def __init__(self, name, location, price):  #constructor
        self.name = name
        self.location = location
        self.price = price
    
    def getName(self):                          #getter of name
        return self.name
    
    def getLocation(self):                      #getter of location
        return self.location
    
    def getPrice(self):                         #setter of price
        return self.price



class Friend:                                   #Friend class represents a Friend
    
    def __init__(self, name):                   #constructor
        self.name = name
        self.gifts = []
    def add(self, gift):
        self.gifts.append(gift)
    
    def getName(self):                          #getter of name
        return self.name
        
    def getGifts(self):                         #getter of gifts
        return self.gifts


class MyInputDialog:                            #Input dialog window

    def __init__(self, parent, txt):            #constructor to set the dialog to get input from the user
        self.text = ""
        top = self.top = Toplevel(parent)
        Label(top, text=txt).pack()
        self.e = Entry(top)
        self.e.pack(padx=5)
        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    
    def ok(self):                               #if user clicks ok button save the input
        self.text = self.e.get()
        self.top.destroy()

    
    def getText(self):                          #get the input entered by the user
        return self.text

    
    def getTop(self):                           #get top frame of the dialog box
        return self.top


class MyMessageDialog:                          #Message dialog window

    def __init__(self, parent, txt):            #constructor to set the confirmation/Message dialog
        self.ok = False
        self.cancel = False
        top = self.top = Toplevel(parent)
        Label(top, text=txt).pack()
        #self.e = Entry(top)
        #self.e.pack(padx=5)
        b = Button(top, text="OK", command=self.doOk)
        b.pack(pady=5)

        c = Button(top, text="CANCEL", command=self.doCancel)
        c.pack(pady=5)

    def doOk(self):                         #if ok button clicked, save the boolean for the OK
        self.ok = True
        self.cancel = False
        self.top.destroy()

    
    def doCancel(self):                     #if cancel button is clicked then save the cancel boolean
        self.ok = False
        self.cancel = True
        self.top.destroy()

    
    def getOk(self):                        #get ok flag
        return self.ok

    
    def getCancel(self):                    #get cancel flag
        return self.cancel


class GUI(Frame):                           #Main GUI class to setup the command buttons, provides action handling
                                            #get commands and act appropriately.
    def __init__(self, parent):             #setup GUI, lable, buttons and action listeners

        Frame.__init__(self, parent)        #main frame setting
        self.parent = parent
        self.initGUI()

        self.friends = collections.deque()  #collection for friends

    def initGUI(self):                      #function to setup the gui will be called inside
                                            #constructor, add label, buttons action listeners

        self.parent.title("Transcript")     #frame features
        frame = Frame(self, relief=RAISED, borderwidth=10, bg="cyan")
        frame.pack(fill=BOTH, expand=1, padx=15, pady=15)
        self.pack(fill=BOTH, expand=1)

        label = Label(frame, text="MAIN MENU", fg="red", bg="white")    #lable components
        label.pack(padx=5, pady=5)

        button1 = Button(frame, text="Add New Person and Gift", command=self.addPerson) #first button component
        button1.pack(padx=5, pady=5)

        button2 = Button(frame, text="Look up Person and gift", command=self.lookupPerson) #second button component
        button2.pack(padx=5, pady=5)

        button3 = Button(frame, text="Quit", fg="red", command=self.quit)               #quit button component
        button3.pack(padx=5, pady=5)

    
    def quit(self):                                         #event handler to exit the application
        self.destroy()
        exit(0)

    def getText(self, txt):                                 #helper function to get a message
        d = MyInputDialog(self, txt)
        self.wait_window(d.top)
        text = d.getText()
        return text
    
    def getConfirmation(self, txt):                         #helper function to get Confirmation
        d = MyMessageDialog(self, txt)
        self.wait_window(d.top)
        if d.getOk():
            return True
        else:
            return False

    def addPerson(self):                                    #event handler to add a new friend with all his/her gifts to the system.
    
        friendName = self.getText("Enter person's name:")   #get person name, and create friend
        friend = Friend(friendName)

        more = True

        
        while more:                                         #add as many gifts as needed

            giftName = self.getText("Enter the Gift")
            location = self.getText("Enter the location")
            price = self.getText("Enter the price")
            gift = Gift(giftName, location, price)

            friend.add(gift)                                #add to friend

            more = self.getConfirmation("Wanna enter more gifts for " + friendName) #confirmation to get more gift or exist

        self.friends.append(friend)

    
    def lookupPerson(self):                      #event handler to do a look up for a given friend by name
                                                #if friend found, display friend data, and ask an option
                                                # to save data to the file.

        friendName = self.getText("Enter the person's name: ")              #friend name being asked
        found = False
        aFriend = None
        index = 0
        txt = ""

        for friend in self.friends:                                          # find friend in list
            print(friend.getName() == friendName)

            if friend.getName() == friendName:                              #if found, save friend data, set found flag
                txt = "Friend's Data\nName: " + friendName + "\n"
                index = random.randint(0, len(friend.getGifts()) - 1)
                gift = friend.getGifts()[index]
                txt = txt + "Gift Name: " + gift.getName() + "\n"
                txt = txt + "Gift Location: " + gift.getLocation() + "\n"
                txt = txt + "Gift Price: " + gift.getPrice() + "\n"
                found = True
                aFriend = friend
                break

        if not found:                                                        #if friend not found, notify user
            self.getConfirmation("Person not Found with Name: " + friendName)
        else:

            asking = self.getConfirmation("Person Data Found! Do you want to Save to file?")        # write to file

            if asking:                                                      #if need to save to the file, ask file name and save data
                filename = self.getText("Enter file name: ")

                if os.path.isfile(filename):                                # find exists
                    self.getConfirmation("File is existing!")
                else:
                    f = open(filename, 'w')
                    f.write("Name: " + aFriend.getName() + "\n")
                    gift = friend.getGifts()[index]
                    f.write(gift.getName() + "\n")
                    f.write(gift.getLocation() + "\n")
                    f.write(gift.getPrice() + "\n")
                    f.write("\n")

                    f.close()                                               # close file
                    self.getConfirmation("Data Saved to File")

            self.getConfirmation(txt)                                       #display found friend's data in a dialog box

def main():                                                                 #main method, setup the window, and loop till user exists
    root = Tk()
    root.geometry("300x300+300+300")
    app = GUI(root)
    root.mainloop()

main()


