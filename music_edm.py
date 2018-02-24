from tkinter import *
from tkinter import ttk
from pyvirtualdisplay import Display
from termcolor import colored
from selenium import webdriver
import webbrowser
import random
import math
import time,sys

#import required modules 
root = Tk()
def move_window(event):
  root.geometry('+{0}+{1}'.format(event.x_root,event.y_root))

def executor():
 try:
  while(True):
    j =1
    #time.sleep(4)
    edm_collection.implicitly_wait(6)

    song = edm_collection.find_elements_by_class_name('pl-video-title-link.yt-uix-tile-link.yt-uix-sessionlink.spf-link')
    x1 = random.randint(0,39)
    x = x1

    if x>=4:
     edm_collection.execute_script("return arguments[0].scrollIntoView();", song[x-4])
    time.sleep(1)
    song[x].click()
    edm_collection.implicitly_wait(5)

    try:
       skip_ad2 = edm_collection.execute_script("document.getElementById('movie_player').getElementsByClassName('videoAdUiSkipButton')[0].click()")
       edm_collection.execute_script("document.getElementById('movie_player').mute()")
    except Exception:
       j =1
    try :
       title = edm_collection.find_element_by_id('eow-title')
    except Exception:
       print(colored("sorry Network Error.....Try again","red"))
       display.stop()
       edm_collection.quit()
       break
    title1 = title.text
    title2 = title1.replace("(Official Video)"," ")
    title2 = title2.replace("(Official Music Video)"," ")
    title2 = title2.replace("(OFFICIAL MUSIC VIDEO)"," ")
    title2 = title2.replace("[OFFICIAL MUSIC VIDEO]"," ")
    title2 = title2.replace("(Official Lyrics Video)"," ")
    title2 = title2.replace("[Official Video]"," ")
    title2 = title2.replace("(Lyrics Video)"," ")
    title2 = title2.replace("(Lyric)"," ")

    sty = "PLAYING: " + title2
    str_length = len(sty)
    space = ""
    for i in range(70 - str_length):
       space = space + " "
    edm_collection.execute_script("document.getElementById('movie_player').setPlaybackQuality('small')")
    global dur
    dur = edm_collection.execute_script("return document.getElementById('movie_player').getDuration()")
    str_dur = 'Duration : ' + str(math.floor(dur/60)) + ':' + str(math.floor(dur) - math.floor(dur/60)*60)
    Track_description.delete(1.0,END)
    sty = sty + space + str_dur
    Track_description.insert(INSERT,sty)
    Track_description.tag_add("here", "1.0", "1.8")
    Track_description.tag_add("start","1.70","1.78")
    Track_description.tag_config("here", background="green2", foreground="blue2")
    Track_description.tag_config("start", foreground="SkyBlue3")

    while(True):
      root.update()
      try:
          skip_ad = edm_collection.execute_script("document.getElementById('movie_player').getElementsByClassName('videoAdUiSkipButton')[0].click()")
          edm_collection.execute_script("document.getElementById('movie_player').mute()")
      except Exception:
          edm_collection.execute_script("document.getElementById('movie_player').unMute()")
      player_status = edm_collection.execute_script("return document.getElementById('movie_player').getPlayerState()")
      tim = edm_collection.execute_script("return document.getElementById('movie_player').getCurrentTime()")
      amount_loaded = edm_collection.execute_script("return document.getElementById('movie_player').getVideoLoadedFraction()")
      buffer_progress["value"] = amount_loaded
      track_progress["value"] = (tim/dur)

      if(player_status == 0):
          Track_description.delete(1.0,END)
          edm_collection.back()
          edm_collection.back()
          break
 except Exception:
     Track_description.delete(1.0,END)
     edm_collection.quit()
     Track_description.insert(INSERT,"Network Error...Try again")

def seek(x):
    y = (x-6)/245
    try:
     y = y*dur
     y = round(y)
     st = str(y)
     edm_collection.execute_script("""var v = '"""+st+"""';
                                   document.getElementById('movie_player').seekTo(v,true);""",st)
    except Exception:
     print("")

def get_mouse(event):
    x, y = root.winfo_pointerx()-root.winfo_rootx(),root.winfo_pointery()-root.winfo_rooty()
    if x>=6 and x<=251 and y>=51 and y<=64:
       seek(x)

def center(toplevel):
        toplevel.update_idletasks()
        w = toplevel.winfo_screenwidth()
        h = toplevel.winfo_screenheight()
        size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
        x = w/2 - size[0]/2
        y = h/2 - size[1]/2
        toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

def play_pause(event):
 try:
  staten = edm_collection.execute_script("return document.getElementById('movie_player').getPlayerState()")
  if staten == 1:
        button4.config(image = photo5)
        edm_collection.execute_script('document.getElementsByTagName("video")[0].pause()')

  elif staten == 2:
        button4.config(image = photo4)
        edm_collection.execute_script('document.getElementsByTagName("video")[0].play()')
 except Exception:
        print("")

def change(event):
 try:
  edm_collection.execute_script('document.getElementsByTagName("video")[0].pause()')
  edm_collection.back()
  edm_collection.back()
  executor()
 except Exception:
  print("")

def exit():
  try:
      edm_collection.quit()
  except Exception:
      print("")

  try :
      root.destroy()
  except Exception:
      print("")


def close_player():

  try:
      edm_collection.quit()
  except Exception:
      print("")




def player_on(event):
  global display
  display = Display(visible=0, size=(800, 600))
  display.start()
  global edm_collection
  edm_collection = webdriver.Firefox()
  edm_collection.get("https://www.youtube.com/playlist?list=PL7-4xVu8FNDDuvU24R1t1PjVADO7DKk4u")
  executor()

entry_value = StringVar(root, value="")
root.title('My App')
root.geometry("257x208")
root.resizable(width=False, height=False)
global style
style2 = ttk.Style()
style1 = ttk.Style()
ttk.Style().theme_use('clam')

x = 0

style1.configure("SkyBlue3.Horizontal.TProgressbar",
                 padding = 3,
                 background = "turquoise2",
                 foreground = "SkyBlue3",
                 troughcolor = "black",
                 lightcolor  = "SkyBlue3",
                 darkcolor = "SkyBlue3",
                 bordercolor = "blue"

                     )
style2.configure("Blue4.Horizontal.TProgressbar",
                 padding = 3,
                 background = "Blue4",
                 foreground = "Blue2",
                 troughcolor = "black",
                 lightcolor  = "Blue2",
                 darkcolor = "Blue2",
                 bordercolor = "Blue2"

                     )

Track_description = Text(relief = FLAT,height = 3,width = 35,fg ="lawn green" ,bg = "black",bd =0,highlightbackground = "blue",wrap = WORD,)
Track_description.grid(row = 0,column = 1,columnspan = 3,pady = 0, padx =3,sticky =W)

track_progress = ttk.Progressbar(root,style = "SkyBlue3.Horizontal.TProgressbar",orient = HORIZONTAL,length = 249,mode = "determinate",maximum =1,value = 0)
track_progress.grid(row = 1,column = 1,columnspan = 3,padx =3,pady = 2,sticky =W)
track_progress.configure(style = "SkyBlue3.Horizontal.TProgressbar")

photo1 = PhotoImage(file="~/app/mus_images/arent.png")
photo2 = PhotoImage(file = "~/app/mus_images/trx1.png")
photo3 = PhotoImage(file = "~/app/mus_images/c123.png")
global photo4
global photo5
photo4 = PhotoImage(file = "~/app/mus_images/pause12.png")
photo5 = PhotoImage(file = "~/app/mus_images/play12.png")
photo6 = PhotoImage(file = "~/app/mus_images/SJ.gif")



button2 = Button(image = photo3,background = "blue",width = 50, height = 34,relief = GROOVE,overrelief = GROOVE,anchor = "center",activebackground = "DeepSkyBlue2",highlightbackground = "blue")
button2.place(relx = 0.715, rely =0.65,anchor = "center" )
button3 = Button(image = photo2,background = "blue",width = 50,height = 38,relief = GROOVE,overrelief = GROOVE,command = close_player,anchor = "center",activebackground = "DeepSkyBlue2",highlightbackground = "blue")
button3.place(relx = 0.5,rely = 0.85,anchor = "center")
global button4
button4 = Button(image = photo4,background = "blue",width = 50,height = 34,relief = GROOVE,overrelief = GROOVE,anchor = "center",activebackground = "DeepSkyBlue2",highlightbackground = "blue")
button4.place(relx = 0.287,rely = 0.648,anchor = "center")

button6 = Button(image = photo6, background = "black", height = 130, width = 40, relief = FLAT,highlightthickness=0,bd =0,activebackground = "black",command = exit)
button6.place(relx = 0.06, rely = 0.67 ,anchor = "center")

button7 = Button(image = photo6, background = "black", height = 130, width = 40, relief = FLAT,highlightthickness=0,bd = 0,activebackground = "black",command = exit)
button7.place(relx = 0.92, rely = 0.67 ,anchor = "center")

buffer_progress = ttk.Progressbar(root,style = "Blue4.Horizontal.TProgressbar",orient = HORIZONTAL,length = 249,mode = "determinate",maximum =1,value = 0)
buffer_progress.grid(row = 2,column = 1,columnspan = 3,padx =3,pady = 0,sticky =W)

button1 = Button(image = photo1,background = "blue",width = 50,height =38 ,relief = GROOVE,overrelief = GROOVE,anchor = "center",activebackground = "DeepSkyBlue2",highlightbackground = "blue")
button1.place(relx = 0.5,rely = 0.45,anchor = "center")
button1.bind("<Button-1>",player_on)
button4.bind("<Button-1>",play_pause)
button2.bind("<Button-1>",change)
#center(root)
root.bind('<B1-Motion>',move_window)
root.overrideredirect(1)
root.update_idletasks()
root.bind('<Button-1>',get_mouse)
root.configure(background = "black")
root.wm_attributes('-alpha',0.88)
root.mainloop()
