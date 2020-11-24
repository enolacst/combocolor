# ==============================================================================
"""ComboColor: GUI (graphical user interface) class for the combocolor game"""
# ==============================================================================
__author__  = "Constanceau Enola & Panetier Camille"
__version__ = "1.0"
__date__    = "2020-11-20"
# ==============================================================================
from ezTK import *
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
    Button(frame2, text='Grille A')
    Button(frame2, text='Grille B')
    Button(frame2, text='Grille C')
    Button(frame2, text='Grille D')
    Button(frame2, text='Grille E')
    Button(frame2, text='Grille F')
    frame3=Frame(self, op=0)
    Button(frame3, text='Règle du jeu')
    # --------------------------------------------------------------------------
    self.reset();self.loop()
     # ----------------------------------------------------------------------------
  def reset(self):
    """callback function for the RESET button"""
    self.game.reset(); self.show()
  # ----------------------------------------------------------------------------
# ==============================================================================
if __name__ == "__main__": # testcode for class 'PegGUI'
  ComboColor()
# ==============================================================================
