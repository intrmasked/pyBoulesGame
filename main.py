from tk import *                  # imports tk
from tkinter import *            # imports tkinter
from tk import *
import time                     # imports time library
from Player1_Balls import  *  # imports the classes/functions inside Player1_Balls
from Player2_Balls import *   # imports the classes/functions inside Player2 Balls
import sys
from socket import *
from threading import *

global ScoreStorePlayer1       #used as data storage
ScoreStorePlayer1 = 0           #initial points for player 1
global ScoreStorePlayer2        #used as data storage
ScoreStorePlayer2 = 0          #initial points for player 2


class window():   # maskes the main window

    def __init__(self,master): #__init__ is basically used as an initializer in a class
        self.master = master  # used to set master value
        self.btn = Button(master,text = "Start Game" , command = self.command)  #makes a button on the main menu
        self.btn.place( x = 640 , y = 360 )     #used for the position of the button






    def command(self):
        self.master.withdraw()         #connects the window to the games's main window
        toplevel = Toplevel(self.master)     #used to close the previous window
        toplevel.geometry("1280x720")   #size / resolution of the main window
        app  = Main_Window(toplevel)   # variable to call the class in













class Main_Window:                #class with the components of the main window
    def __init__(self,master):
        self.master = master        #assigs master its value
        self.canvas = Canvas(master, width = 1280, height = 920)     #canvas is used for the animation of the objects

        self.canvas.pack()                  #used to pack the animation in the window
        
        

        """set of the buttons used in  the main window"""
        self.bt1 = Button(self.canvas,text = "Player1 Ball1", command = self.movePlayer1Ball1)   #button to control first ball
        self.bt1.place(x = 2, y= 48)
        
        self.bt2 = Button(self.canvas,text = "Player1 Ball1" , command = self.movePlayer1Ball2) #button to control second ball
        self.bt2.place(x = 2, y= 136)
        
        self.bt3 = Button(self.canvas,text = "Player1 Ball3", command = self.movePlayer1Ball3)  #button to control third ball
        self.bt3.place(x = 2, y= 243)

        self.bt4 = Button(self.canvas,text = "Player2 Ball1" , command = self.movePlayer2Ball1) #button to control fourth ball
        self.bt4.place(x = 1200, y= 48)

        self.bt5 = Button(self.canvas,text = "Player2 Ball2" , command = self.movePlayer2Ball2) #button to control fifth ball
        self.bt5.place(x = 1200, y= 136)

        self.bt6 = Button(self.canvas,text = "Player2 Ball3" , command = self.movePlayer2Ball3) #button to control sixth ball
        self.bt6.place(x = 1200, y= 243)

        self.bt7 = Button(self.canvas,text = "Result"  , command = self.Result)         #button to find the result
        self.bt7.place( x = 610 , y = 400 )

        self.bt7 = Button(self.canvas, text="View Score or Next Round", command=self.ScoreWin)         # button to find the winner
        self.bt7.place(x=600, y=450)



        self.bt8 = Button(self.canvas, text = "Player1 Ball 4", command = self.movePlayer1Ball0)
        self.bt8.place( x = 2 , y = 340)

        self.bt9 = Button(self.canvas,text = "Player2 Ball 4", command = self.movePlayer2Ball8)
        self.bt9.place( x = 1200, y = 340)





        if ScoreStorePlayer2 == 7 or ScoreStorePlayer1 == 7:
            self.label_ = Label(self.canvas, text = "1 Round Left")
            self.label_.place(x = 700 , y = 300)







       # initializing text boxes

        self.Player1Ball0Value = Entry(self.canvas)  # takes custom value for Player1Ball1
        self.Player1Ball0Value.place(x=2, y=400)


        self.Player1Ball1Value =  Entry(self.canvas)        #takes custom value for Player1Ball1
        self.Player1Ball1Value.place(x = 2, y = 93)


        self.Player1Ball2Value = Entry(self.canvas)         #takes custom value for Player1Ball2
        self.Player1Ball2Value.place(x=2, y=180)

        self.Player1Ball3Value = Entry(self.canvas)         #takes custom value for Player1Ball3
        self.Player1Ball3Value.place(x=2, y=297)


        self.Player2Ball1Value = Entry(self.canvas)         #takes custom value for Player2Ball1
        self.Player2Ball1Value.place(x=1190, y=93)


        self.Player2Ball2Value = Entry(self.canvas)         #takes custom value for Player2Ball2
        self.Player2Ball2Value.place(x=1190, y = 180)


        self.Player2Ball3Value =  Entry(self.canvas)        #takes custom value for Player2Ball3
        self.Player2Ball3Value.place(x=1190, y=297)

        self.Player2Ball4Value = Entry(self.canvas)  # takes custom value for Player1Ball1
        self.Player2Ball4Value.place(x=1190, y=400)

        self.xpositonOfCenterBall = 640
        self.ypositionOfCenterBall = 360
        self.CenterBall = Player1Balls(self.canvas,self.xpositonOfCenterBall,self.ypositionOfCenterBall,20,0,0,"purple")



        # player 1 Balls

                    #player1Balls(master,xposition,yposition,diameter,speed x axis, speed y axis, colour)
        self.ball0 = Player1Balls(self.canvas,240,20,20,0,1,"green")
        self.ball1 = Player1Balls(self.canvas,320,20,20,0,1,"green")    #to make balls on the screen
        self.ball2 = Player1Balls(self.canvas,400,20,20,0,1,"green")
        self.ball3 = Player1Balls(self.canvas,480,20,20,0,1,"green")





        # player 2 Balls

        self.ball4 = Player2Balls(self.canvas, 780,20,20,0,1,"blue")
        self.ball5 = Player2Balls(self.canvas, 860,20,20,0,1,"blue")
        self.ball6 = Player2Balls(self.canvas, 940,20,20,0,1,"blue")
        self.ball7 = Player2Balls(self.canvas,1020,20,20,0,1,"blue")


   # def Client(self):
    #    """Script for Tkinter GUI chat client."""
     #   from socket import AF_INET, socket, SOCK_STREAM
      #  from threading import Thread
       # import tkinter

        #def receive():
         #   """Handles receiving of messages."""
          #  while True:
           #     try:
            #        msg = client_socket.recv(BUFSIZ).decode("utf8")
             #       msg_list.insert(tkinter.END, msg)
              #  except OSError:  # Possibly client has left the chat.
               #     break

       # def send(event=None):  # event is passed by binders.
        #    """Handles sending of messages."""
         #   msg = my_msg.get()
          #  my_msg.set("")  # Clears input field.
          #  client_socket.send(bytes(msg, "utf8"))
          #  if msg == "{quit}":
           #     client_socket.close()
            #    top.quit()

        #def on_closing(event=None):
            # """This function is to be called when the window is closed."""
         #   my_msg.set("{quit}")
          #  send()

        #top = tkinter.Tk()
        #top.title("Chatter")

        #messages_frame = tkinter.Frame(top)
        #my_msg = tkinter.StringVar()  # For the messages to be sent.
        #my_msg.set("Type your messages here.")
        #scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
        # Following will contain the messages.
        #msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
        #scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        #msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
       # msg_list.pack()
       # messages_frame.pack()

       # entry_field = tkinter.Entry(top, textvariable=my_msg)
       # entry_field.bind("<Return>", send)
       # entry_field.pack()
       # send_button = tkinter.Button(top, text="Send", command=send)
       # send_button.pack()

       # top.protocol("WM_DELETE_WINDOW", on_closing)

        # ----Now comes the sockets part----
       # HOST = input('Enter host: ')
       # PORT = input('Enter port: ')
       # if not PORT:
        #    PORT = 33000
       # else:
        #    PORT = int(PORT)

        # BUFSIZ = 1024
         # ADDR = (HOST, PORT)

        # client_socket = socket(AF_INET, SOCK_STREAM)
        # client_socket.connect(ADDR)

        # receive_thread = Thread(target=receive)
        #receive_thread.start()
        #tkinter.mainloop()  # Starts GUI execution.





    def movePlayer1Ball0(self):
        x7 = 0

        Ball4ValueFromTextBox = int(self.Player1Ball0Value.get())
        while x7 <=Ball4ValueFromTextBox:
            self.ball0.movePlayer1()
            self.canvas.update()
            time.sleep(0.01)
            x7 = x7+1
        self.bt8.config(state = DISABLED)

    def movePlayer2Ball8(self):
        x8 = 0

        Ball8ValueFromTextBox = int(self.Player2Ball4Value.get())
        while x8 <= Ball8ValueFromTextBox:
            self.ball7.movePlayer2()
            self.canvas.update()
            time.sleep(0.01)
            x8 = x8 + 1
        self.bt9.config(state=DISABLED)



    def movePlayer1Ball1(self):             # function used for the animation of balls
        x = 0

        Ball1ValueFromTextBox =  int(self.Player1Ball1Value.get())
        while x <=Ball1ValueFromTextBox:
            self.ball1.movePlayer1()
            self.canvas.update()
            time.sleep(0.01)
            x = x+1
        self.bt1.config(state = DISABLED)

    def movePlayer1Ball2(self):             # function used for the animation of balls

        x2 = 0
        Ball2ValueFromTextBox = int(self.Player1Ball2Value.get())
        while x2 <=Ball2ValueFromTextBox:
            self.ball2.movePlayer1()
            self.canvas.update()
            time.sleep(0.01)
            x2 = x2 + 1
        self.bt2.config(state=DISABLED)


    def movePlayer1Ball3(self):             # function used for the animation of balls

        x3 = 0

        Ball3ValueFromTextBox = int(self.Player1Ball3Value.get())

        while x3 <= Ball3ValueFromTextBox:
            self.ball3.movePlayer1()
            self.canvas.update()
            time.sleep(0.01)
            x3 = x3 + 1

        self.bt3.config(state=DISABLED)




    def movePlayer2Ball1(self):         # function used for the animation of balls

        x4 = 0

        Ball4ValueFromTextBox = int(self.Player2Ball1Value.get())
        while x4 <= Ball4ValueFromTextBox:
            self.ball4.movePlayer2()
            self.canvas.update()
            time.sleep(0.01)
            x4 = x4 + 1

        self.bt4.config(state=DISABLED)

    def movePlayer2Ball2(self):         # function used for the animation of balls

        x5 = 0
        Ball5ValueFromTextBox = int(self.Player2Ball2Value.get())
        while x5 <= Ball5ValueFromTextBox:
            self.ball5.movePlayer2()
            self.canvas.update()
            time.sleep(0.01)
            x5 = x5 + 1
        self.bt5.config(state=DISABLED)

    def movePlayer2Ball3(self):         # function used for the animation of balls
        x6 = 0
        Ball6ValueFromTextBox = int(self.Player2Ball3Value.get())
        while x6 <= Ball6ValueFromTextBox:
            self.ball6.movePlayer2()
            self.canvas.update()
            time.sleep(0.01)
            x6 = x6 + 1

        self.bt6.config(state=DISABLED)


    def Result(self):           #function to find out who is the winner

        """global variables to store the points of the players"""
        global ScoreStorePlayer1
        global ScoreStorePlayer2

        """variables to convert the values from  the text boxes into int"""
        j  = int(self.Player1Ball3Value.get())      #4th ball
        k = int(self.Player2Ball1Value.get())       #5th ball
        if j <= 360  and j<k:       #used to check for the winner

            messageBox = Tk()     #used to make a window to indicate the wining player
            Result = Frame(messageBox)  #used to assign the frame
            Result.pack()           #packing the frame in the window
            lable = Label(Result, text="Player 2 Wins")     #used to produce a label to indidcate which player won
            lable.pack(side=LEFT)    # to place it on the form
            ScoreStorePlayer2 = ScoreStorePlayer2 + 1  #used to give a point to the winning player




        elif k <= 360 and  k<j:
            messageBox = Tk()
            Result = Frame(messageBox)
            Result.pack()
            lable = Label(Result, text="Player 1 Wins")
            lable.pack(side = LEFT)
            ScoreStorePlayer1 = ScoreStorePlayer1 + 1





    def ScoreWin(self):                     #used to make a window for the transitions of rounds
        self.master.withdraw()              #used to close the previous window
        toplevel = Toplevel(self.master)
        toplevel.geometry("1280x720")
        app = ScoreWindow(toplevel)       #assigns the variable a function that will open the window







class ScoreWindow:               # the window that has the next round option
    def __init__(self,master):

        b1 = Button(master,text = " Next Round"  , command = NextRound(master))



class NextRound:            # the transition window
    def __init__(self, master):
        self.master = master
        self.btn = Button(master, text="Next Round" , command=self.command)
        self.btn.place(x=640, y=360)
        self.btn1 = Button(master,text = "ScoreBoard"  , command =self.Score)
        self.btn1.place(x = 640 , y = 400 )




    def command(self):  #used to transition back into the game



        if ScoreStorePlayer2 ==8 or ScoreStorePlayer1 == 8:
            print("Rounds are completed")
            sys.exit()

        else:
            self.master.withdraw()
            toplevel = Toplevel(self.master)
            toplevel.geometry("1280x720")
            app = Main_Window(toplevel)

    def Score(self):  #used to open the core board
        self.twe = Tk()
        self.frame = Canvas(self.twe)
        self.frame.config(width = 300 , height = 300)
        lbl  = Label(self.twe,text = "Player 1")
        lbl.place(x= 2 , y = 50)
        lbl1 = Label(self.twe, text = str(ScoreStorePlayer1))
        lbl1.place(x = 60 , y = 50 )
        lbl = Label(self.twe, text="Player 2")
        lbl.place(x=2, y=100)
        lbl1 = Label(self.twe, text=str(ScoreStorePlayer2))
        lbl1.place(x=60, y=100)






root = Tk()         # this acts as the master for all classes
root.geometry("1280x720") # this acts as the size for the game windwo
b = window(root)        # this acts as the variable the initializes the main menu of  the game

root.title("Boules Game")       # gives the title
root.resizable(width= False , height= False)    # fixes the screen size


root.mainloop()     #its an event that is used to control tkinter