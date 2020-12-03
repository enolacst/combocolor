# ==============================================================================
"""ComboColor: GUI (graphical user interface) class for the combocolor game"""
# ==============================================================================
__author__  = "Constanceau Enola & Panetier Camille"
__version__ = "1.0"
__date__    = "2020-11-20"
# ==============================================================================
from ezTK import *
from ezCLI import *
from ComboGame import ComboGame
# ------------------------------------------------------------------------------
class ComboColor(Win):
  """Gui class for the combocolor game"""
  # ----------------------------------------------------------------------------
  def __init__(self):
    """create the main window and pack the widgets"""
    self.game = ComboGame() # create an instance of the kernel class
    Win.__init__(self, title='ComboColor', op=5)
    # --------------------------------------------------------------------------
    frame1=Frame(self,grow=False, op=0)
    #self.config= Frame(self, font='Arial 14', anchor='W')
    Label(frame1, text='Choix de la grille de jeu', font='Arial 18 bold italic')
    frame2 = Frame(self, op=0)
    Button(frame2, text='Grille A',fg="cyan",font='Arial 18 bold', command=grid)
    Button(frame2, text='Grille B',fg="red",font='Arial 18 bold')
    Button(frame2, text='Grille C',fg="pink",font='Arial 18 bold')
    Button(frame2, text='Grille D',fg="orange",font='Arial 18 bold')
    Button(frame2, text='Grille E',fg="purple",font='Arial 18 bold')
    Button(frame2, text='Grille F',fg="grey",font='Arial 18 bold')
    frame3=Frame(self, op=0)
    Button(frame3, text='Règle du jeu',font='Arial 15',command=self.rules)
    # --------------------------------------------------------------------------
    self.loop()
    #self.reset();
     # ----------------------------------------------------------------------------
##  def reset(self):
##    """callback function for the RESET button"""
##    self.game.reset(); self.show()
  # ----------------------------------------------------------------------------
  def rules(self):
    win=Win(title='Règles du jeu', font='Courier 15')
    txt = read_txt('rules_game.txt')
    Label(win, text=txt,grow=False)
# ----------------------------------------------------------------------------
  def grid(self):
    
# ==============================================================================
if __name__ == "__main__": # testcode for class 'PegGUI'
  ComboColor()
# ==============================================================================
