

#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n8306699
#    Student name: Thomas Feldman
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files may be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  The Top Ten of Everything 
#
#  In this task you will combine your knowledge of HTMl/XML mark-up
#  languages with your skills in Python scripting, pattern matching
#  and Graphical User Interface design to produce a useful
#  application for accessing online data.  See the instruction
#  sheet accompanying this template for full details.
#
#--------------------------------------------------------------------#



#--------------------------------------------------------------------#
#
#  Import the modules needed for this assignment.  You may not import
#  any other modules or rely on any other files.  All data and images
#  needed for your solution must be sourced from the Internet.
#

# Import the function for downloading web pages
from urllib import urlopen

# Import the regular expression function
from re import findall

# Import the Tkinter functions
from Tkinter import *

# Import Python's HTML parser
from HTMLParser import *

# Import SQL to connect to db
from sqlite3 import *

#--------------------------------------------------------------------#
#
#  Utility function:
#  Given the raw byte stream of a GIF image, return a Tkinter
#  PhotoImage object suitable for use as the 'image' attribute
#  in a Tkinter Label widget or any other such widget that
#  can display images.
#
def gif_to_PhotoImage(gif_image):

    # Encode the byte stream as a base-64 character string
    # (MIME Base 64 format)
    characters = gif_image.encode('base64', 'strict')

    # Return the result as a Tkinter PhotoImage
    return PhotoImage(data = characters)



#--------------------------------------------------------------------#
#
#  Utility function:
#  Given the raw byte stream of a JPG or PNG image, return a
#  Tkinter PhotoImage object suitable for use as the 'image'
#  attribute in a Tkinter Label widget or any other such widget
#  that can display images.  If positive integers are supplied for
#  the width and height (in pixels) the image will be resized
#  accordingly.
#
def image_to_PhotoImage(image, width = None, height = None):

    # Import the Python Imaging Library, if it exists
    try:
        from PIL import Image, ImageTk
    except:
        raise Exception, 'Python Imaging Library has not been installed properly!'

    # Import StringIO for character conversions
    from StringIO import StringIO

    # Convert the raw bytes into characters
    image_chars = StringIO(image)

    # Open the character string as a PIL image, if possible
    try:
        pil_image = Image.open(image_chars)
    except:
        raise Exception, 'Cannot recognise image given to "image_to_Photoimage" function\n' + \
                         'Confirm that image was downloaded correctly'
    
    # Resize the image, if a new size has been provided
    if type(width) == int and type(height) == int and width > 0 and height > 0:
        pil_image = pil_image.resize((width, height), Image.ANTIALIAS)

    # Return the result as a Tkinter PhotoImage
    return ImageTk.PhotoImage(pil_image)



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by putting your solution below.
#
##### DEVELOP YOUR SOLUTION HERE #####
# Create a window
Top_10_window = Tk()

# Give the window a title
Top_10_window.title('Top 10 things I care about')
# Gives the window a picture from the url using the img function provided
url_home = urlopen('http://www.christmasfilm.com/topten.gif').read()
img = image_to_PhotoImage(url_home)


# Function to bring up a new window when the matching button on the main page is pressed
def itunes_top_ten():
    def Main():
        Itunes_window.withdraw()
    root = Toplevel()
    Itunes_window = root
    Itunes_window.title('Top Ten Itunes Singles')
    url2='http://www.vmusic.com.au/charts/itunes-top-50-singles-chart.aspx'
    url2_contents = urlopen(url2).read()
    url2_list= findall('<div id="Content_Content_Left_Tracklist_Tracklist_Album_[0-9]+">([a-zA-Z0-9]+.+)(?:</div>)', url2_contents)
    url_itunes_img=urlopen('https://ksedtech.wikispaces.com/file/view/itunes.gif/112819231/itunes.gif').read()
    itunes_img=image_to_PhotoImage(url_itunes_img)
    label = Label(Itunes_window, image = itunes_img)
    label.image=itunes_img
    label.pack()
    text = Text(Itunes_window)
    text.insert(INSERT,'1. '+url2_list[0])
    text.insert(INSERT,'\n2. '+url2_list[1])
    text.insert(INSERT,'\n3. '+url2_list[2])
    text.insert(INSERT,'\n4. '+url2_list[3])
    text.insert(INSERT,'\n5. '+url2_list[4])
    text.insert(INSERT,'\n6. '+url2_list[5])
    text.insert(INSERT,'\n7. '+url2_list[6])
    text.insert(INSERT,'\n8. '+url2_list[7])
    text.insert(INSERT,'\n9. '+url2_list[8])
    text.insert(INSERT,'\n10. '+url2_list[9])
    text.insert(INSERT,'\n'+'\n'+'\n'+'http://www.vmusic.com.au/charts/itunes-top-50-singles-chart.aspx')
    text.pack()
    # Function to call the database and save the list as above
    def savebutton():
        conn = connect(database = 'top_ten.db')
        conn.text_factory = str
        top_ten = conn.cursor()
        def Itunes_data_entry():
            conn.execute("DELETE FROM Top_Ten")
            Rank = ['1','2','3','4','5','6','7','8','9','10']
            for i in range(10):
                conn.execute('INSERT INTO Top_Ten(Rank, Description) VALUES(?, ?)',(Rank[i], url2_list[i]))
            conn.commit()
        Itunes_data_entry()      
    save_button=Button(Itunes_window, text='save to db', command=savebutton)
    save_button.pack()
    Itunes_window.mainloop()
    
# Function to bring up a new window when the matching button on the main page is pressed 
def nrl_top_ten():
    def Main():
        NRL_window.withdraw()
    # Creat New Window as Top Level to keep it infront (as I found it wont work as Tk() which i'm only 50% sure of why)
    root = Toplevel()
    # Rename the window for my benifit
    NRL_window = root
    # Give it a title
    NRL_window.title('Top Ten NRL Teams')
    # Call the url that will be used for this top list
    url3='https://www.nrl.com/draw/telstrapremiership/ladder/tabid/10251/default.aspx'
    # Read the contents of the web page as a string
    url3_contents = urlopen(url3).read()
    # Findall function that will collect the information i need to display the top 10 list
    url3_list= findall('&nbsp;</div>([a-zA-Z0-9\s]+)(?:</td>)', url3_contents)
    # url for the image
    url_nrl_img=urlopen('http://2.bp.blogspot.com/-THx7NtMisrQ/UT6aLVEjxFI/AAAAAAAAAQY/jwPcoQklRTY/s200/Current_NRL_Telstra_Premiership_Logo.png').read()
    # function given to display the image
    nrl_img=image_to_PhotoImage(url_nrl_img)
    # call the image as a label, name it, then pack
    label = Label(NRL_window, image = nrl_img)
    label.image=nrl_img
    label.pack()
    # Inserting the urlstring as individual items for the 1-10 top list (i tried a for i in range (10) but i couldn't get it to look like this so i left it simple)
    text = Text(NRL_window)
    text.insert(INSERT,'1. '+url3_list[i])
    text.insert(INSERT,'\n2. '+url3_list[1])
    text.insert(INSERT,'\n3. '+url3_list[2])
    text.insert(INSERT,'\n4. '+url3_list[3])
    text.insert(INSERT,'\n5. '+url3_list[4])
    text.insert(INSERT,'\n6. '+url3_list[5])
    text.insert(INSERT,'\n7. '+url3_list[6])
    text.insert(INSERT,'\n8. '+url3_list[7])
    text.insert(INSERT,'\n9. '+url3_list[8])
    text.insert(INSERT,'\n10. '+url3_list[9])
    text.insert(INSERT,'\n'+'\n'+'\n'+'https://www.nrl.com/draw/telstrapremiership/ladder/tabid/10251/default.aspx')
    # pack the text
    text.pack()
    # Function to call the database and save the list as above
    def savebutton():
        # connect to the db
        conn = connect(database = 'top_ten.db')
        # needed this line to actually get it too work, something about it not wanting 8-bit bytestrings. Otherwise i dont get this line at all
        conn.text_factory = str
        top_ten = conn.cursor()
        # Function for this specific list
        def NRL_data_entry():
            # Delete whats already in it
            conn.execute("DELETE FROM Top_Ten")
            # Rank column in db
            Rank = ['1','2','3','4','5','6','7','8','9','10']
            # Do it 10 times from urlstring
            for i in range(10):
                # put the string data into the db
                conn.execute('INSERT INTO Top_Ten(Rank, Description) VALUES(?, ?)',(Rank[i], url3_list[i]))
            # commit the changes
            conn.commit()
        # run the function
        NRL_data_entry()
    # Button to save the list to the db
    save_button=Button(NRL_window, text='save to db', command=savebutton)
    save_button.pack()
    # loop the window
    NRL_window.mainloop()

# Function to bring up a new window when the matching button on the main page is pressed
def steam_top_ten():
    def Main():
        steam_window.withdraw()
    root = Toplevel()
    steam_window = root
    steam_window.title('Top Ten Best Selling Steam Games')
    url_steam_img=urlopen('http://www.gamasutra.com/db_area/images/news/2012/Aug/175572/steam.gif').read()
    steam_img=image_to_PhotoImage(url_steam_img)
    label = Label(steam_window, image = steam_img)
    label.image=steam_img
    label.pack()
    url1='http://store.steampowered.com/search/?filter=topsellers'
    url1_contents = urlopen(url1).read()
    url1_list= findall('<span class="title">([a-zA-Z0-9]+.+)(?:</span>)', url1_contents)
    text = Text(steam_window)
    text.insert(INSERT,'1. '+url1_list[0])
    text.insert(INSERT,'\n2. '+url1_list[1])
    text.insert(INSERT,'\n3. '+url1_list[2])
    text.insert(INSERT,'\n4. '+url1_list[3])
    text.insert(INSERT,'\n5. '+url1_list[4])
    text.insert(INSERT,'\n6. '+url1_list[5])
    text.insert(INSERT,'\n7. '+url1_list[6])
    text.insert(INSERT,'\n8. '+url1_list[7])
    text.insert(INSERT,'\n9. '+url1_list[8])
    text.insert(INSERT,'\n10. '+url1_list[9])
    text.insert(INSERT,'\n'+'\n'+'\n'+'http://store.steampowered.com/search/?filter=topsellers')
    text.pack()
    # Function to call the database and save the list as above
    def savebutton():
        conn = connect(database = 'top_ten.db')
        conn.text_factory = str
        top_ten = conn.cursor()
        def Steam_data_entry():
            conn.execute("DELETE FROM Top_Ten")
            Rank = ['1','2','3','4','5','6','7','8','9','10']
            for i in range(10):
                conn.execute('INSERT INTO Top_Ten(Rank, Description) VALUES(?, ?)',(Rank[i], url1_list[i]))
            conn.commit()
        Steam_data_entry()      
    save_button=Button(steam_window, text='save to db', command=savebutton)
    save_button.pack()
    steam_window.mainloop()
   
# Create the buttons which will bring up the top ten lists in seperate windows
the_button1 = Button(Top_10_window, text = 'Itunes \nTop Ten', command = itunes_top_ten)
the_button2 = Button(Top_10_window, text = 'NRL \nTop Ten', command = nrl_top_ten)
the_button3 = Button(Top_10_window, text = 'Steam \nTop Ten', command = steam_top_ten)
# Creates the img in the window
the_label = Label(Top_10_window, image = img)

# Call the geometry manager to "pack" the widgets onto
# the window (with a blank margin around the widgets)
margin_size = 5
the_label.grid( column = 1)
the_button1.grid(pady = margin_size, row = 1, column = 1, sticky = 'e' )
the_button2.grid(pady = margin_size, row = 1, column = 1,)
the_button3.grid(pady = margin_size, row = 1, column = 1, sticky = 'w')
# Start the event loop to react to user inputs
Top_10_window.mainloop()
                 



