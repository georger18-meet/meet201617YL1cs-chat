#2016-2017 PERSONAL PROJECTS: TurtleChat!
#WRITE YOUR NAME HERE!
"""GeorgeR"""
#####################################################################################
#                                   IMPORTS                                         #
#####################################################################################
#import the turtle module
import turtle
##from abc import ABCMeta , abstractmethod
#import the Client class from the turtle_chat_client module
from turtle_chat_client import Client 
#Finally, from the turtle_chat_widgets module, import two classes: Button and TextInput
from  turtle_chat_widgets import Button , TextInput 
#####################################################################################
#####################################################################################

#####################################################################################
#                                   TextBox                                         #
#####################################################################################
#Make a class called TextBox, which will be a subclass of TextInput.
class TextBox(TextInput):
#Because TextInput is an abstract class, you must implement its abstract
#methods.  There are two:
#
#draw_box\
    def draw_box(self):
        
        self.pos=(-200,-100)
        turtle.hideturtle()
        turtle.bgcolor("Orange")
        self.writer.hideturtle()
        self.writer=turtle.clone()
        self.writer.penup()
        self.writer.goto(self.pos)
        self.writer.color("Blue")
        self.writer.pendown()
        self.writer.goto(self.width,-100)
        self.writer.goto(self.width,self.height)
        self.writer.goto(-200,self.height)
        self.writer.goto(self.pos)
        self.writer.penup()


#write_msg      
    def write_msg(self):
        self.writer.penup()
        self.writer.write('')
        self.writer.goto(-180,self.height-30)
        self.writer.clear()
        self.writer.write(self.new_msg)


#Hints:
#1. in draw_box, you will draw (or stamp) the space on which the user's input
#will appear.
#
#2. All TextInput objects have an internal turtle called writer (i.e. self will
#   have something called writer).  You can write new text with it using code like
#
#   self.writer.write(a_string_variable)
#
#   and you can erase that text using
#
#   self.writer.clear()
#
#3. If you want to make a newline character (i.e. go to the next line), just add
#   \r to your string.  Test it out at the Python shell for practice
#####################################################################################
#####################################################################################

#####################################################################################
#                                  SendButton                                       #
#####################################################################################
#Make a class called SendButton, which will be a subclass of Button.
#Button is an abstract class with one abstract method: fun.
#fun gets called whenever the button is clicked.  It's jobs will be to
class SendButton(Button):
    def __init__(self,my_turtle=None,shape=None,pos=(0,-150),view=None):
        super(SendButton,self).__init__(my_turtle,shape,pos)
        self.view=view

        if shape is None:
            self.turtle.goto(pos)
            self.turtle.shape('square')
            self.turtle.shapesize(2,10)
            self.turtle.fillcolor("Purple3")

    def fun(self,x=None,y=None):
        self.view.send_msg()
            
        
# 1. send a message to the other chat participant - to do this,
#    you will need to call the send method of your Client instance
# 2. update the messages that you see on the screen
#
#HINT: You may want to override the __init__ method so that it takes one additional
#      input: view.  This will be an instance of the View class you will make next
#      That class will have methods inside of it to help
#      you send messages and update message displays.
#####################################################################################
#####################################################################################


##################################################################
#                             View                               #
##################################################################
#Make a new class called View.  It does not need to have a parent
#class mentioned explicitly.
#
#Read the comments below for hints and directions.
##################################################################
##################################################################
class View:
    _MSG_LOG_LENGTH=5 #Number of messages to retain in view
    _SCREEN_WIDTH=300
    _SCREEN_HEIGHT=600
    _LINE_SPACING=round(_SCREEN_HEIGHT/2/(_MSG_LOG_LENGTH+1))

    def __init__(self,username='Me',partner_name='Partner'):
        '''
        :param username: the name of this chat user
        :param partner_name: the name of the user you are chatting with
        '''
        ###
        #Store the username and partner_name into the instance.
        ###
        self.username=username
        self.partner_name=partner_name

        
        ###
        #Make a new client object and store it in this instance of View
        #(i.e. self).  The name of the instance should be my_client
        ###
        self.my_client=Client()
        ###
        #Set screen dimensions using turtle.setup
        #You can get help on this function, as with other turtle functions,
        #by typing
        #
        #   import turtle
        #   help(turtle.setup)
        #
        #at the Python shell.
        ###
        turtle.setup(width=0.5,height=0.75,startx=0,starty=0)

        ###
        #This list will store all of the messages.
        #You can add strings to the front of the list using
        #   self.msg_queue.insert(0,a_msg_string)
        #or at the end of the list using
        #   self.msg_queue.append(a_msg_string)
        self.msg_queue=[]
        ###


        ###
        #Create one turtle object for each message to display.
        #You can use the clear() and write() methods to erase
        #and write messages for each
        ###
##        object1=turtle.clone()
##        self.object1=object1
##
##        object2=turtle.clone()
##        self.object2=object2
##
##        object3=turtle.clone()
##        self.object3=object3
##
##        object4=turtle.clone()
##        self.object4=object4

        object_list=[]
        self.object_list=object_list
        for i in range(3):
            self.object_list.insert(0,turtle.clone())

        ###
        #Create a TextBox instance and a SendButton instance and
        #Store them inside of this instance
        ###
        self.textbox=TextBox()

        self.sendbutton=SendButton(view=self)
                                   

        ###
        #Call your setup_listeners() function, if you have one,
        #and any other remaining setup functions you have invented.
        ###

    def send_msg(self):
        self.my_client.send(self.textbox.new_msg)
        self.msg_queue.insert(0,self.textbox.new_msg)
        self.textbox.clear_msg()
        self.display_msg()
        '''
        You should implement this method.  It should call the
        send() method of the Client object stored in this View
        instance.  It should also update the list of messages,
        self.msg_queue, to include this message.  It should
        clear the textbox text display (hint: use the clear_msg method).
        It should call self.display_msg() to cause the message
        
        display to be updated.
        '''
        

    def get_msg(self):
        return self.textbox.get_msg()

    

    def setup_listeners(self):
        self.send_button.fun()
        turtle.listen() 
        '''
        Set up send button - additional listener, in addition to click,
        so that return button will send a message.
        To do this, you will use the turtle.onkeypress function.
        The function that it will take is
        self.send_btn.fun
        where send_btn is the name of your button instance

        Then, it can call turtle.listen()
        '''


    def msg_received(self,msg):
        self.msg_queue.insert(0,msg)
        self.display_msg()
        
        '''
        This method is called when a new message is received.
        It should update the log (queue) of messages, and cause
        the view of the messages to be updated in the display.

        :param msg: a string containing the message received
                    - this should be displayed on the screen
        '''
        print(msg) #Debug - print message
        show_this_msg=self.partner_name+' says:\r'+ msg
        #Add the message to the queue either using insert (to put at the beginning)
        #or append (to put at the end).
        #
        #Then, call the display_msg method to update the display

    def display_msg(self):
        for i in range(3):
            self.object_list[i].goto(-150,100+i*self._LINE_SPACING)
            self.object_list[i].pendown()
            self.object_list[i].write(self.msg_queue[i])
            
        
        '''
        This method should update the messages displayed in the screen.
        You can get the messages you want from self.msg_queue
        '''
        pass


    def get_client(self):
        return self.my_client
##############################################################
##############################################################


#########################################################
#Leave the code below for now - you can play around with#
#it once you have a working view, trying to run you chat#
#view in different ways.                                #
#########################################################
if __name__ == '__main__':
    my_view=View()
    _WAIT_TIME=200 #Time between check for new message, ms
    def check() :
        #msg_in=my_view.my_client.receive()
        msg_in=my_view.get_client().receive()
        if not(msg_in is None):
            if msg_in==Client._END_MSG:
                print('End message received')
                sys.exit()
            else:
                my_view.msg_received(msg_in)
        turtle.ontimer(check,_WAIT_TIME) #Check recursively
    check()
    turtle.mainloop()
