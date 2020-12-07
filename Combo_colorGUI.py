# ==============================================================================
"""ComboColor: GUI (graphical user interface) class for the combocolor game"""
# ==============================================================================
__author__  = "Constanceau Enola & Panetier Camille"
__version__ = "1.0"
__date__    = "2020-11-20"
# ==============================================================================
from ezTK import *
from ezCLI import *
from PIL import Image,ImageDraw,ImageTk
from random import randrange as rr
from ComboGame import ComboGame
# ------------------------------------------------------------------------------
class ComboColor(Win):
  """Gui class for the combocolor game"""
  # ----------------------------------------------------------------------------
  def __init__(self):
    """create the main window and pack the widgets"""
    self.game = ComboGame() # create an instance of the kernel class
    Win.__init__(self, title='ComboColor', op=5, click=self.on_click)
    # --------------------------------------------------------------------------
    #grille=[Image(file=f"board{name}.png") for name in 'ABCDEF']
    self.frame1=Frame(self,grow=False, op=0)
    Label(self.frame1, text='Choix de la grille de jeu', font='Arial 18 bold italic')
    self.frame2 = Frame(self, op=0)
    Button(self.frame2, text='Grille A',fg="cyan",font='Arial 18 bold', command=self.grid)
    Button(self.frame2, text='Grille B',fg="red",font='Arial 18 bold')
    Button(self.frame2, text='Grille C',fg="pink",font='Arial 18 bold')
    Button(self.frame2, text='Grille D',fg="orange",font='Arial 18 bold')
    Button(self.frame2, text='Grille E',fg="purple",font='Arial 18 bold')
    Button(self.frame2, text='Grille F',fg="grey",font='Arial 18 bold')
    self.frame3=Frame(self, op=0)
    Button(self.frame3, text='Règle du jeu',font='Arial 15',command=self.rules)
    # --------------------------------------------------------------------------
    self.loop()
    #self.reset();
     # ----------------------------------------------------------------------------
  def rules(self):
    win=Win(title='Règles du jeu', font='Courier 15')
    txt = read_txt('rules_game.txt')
    Label(win, text=txt,grow=False)
# --------------------------------------------------------------------------
    self.loop()
# --------------------------------------------------------------------------
  def grid(self,width=699,height=699):
    #self.win=Win(title='Grille',fold=1,grow=True)
    self.frame=Frame(self,grow=False, op=0)
    self.board= Image.new('RGB',(width,height))
    self.image= ImageTk.PhotoImage(self.board)
    Label(self.frame, text='grille de jeu', font='Arial 18 bold italic',image=self.image)
    #self.label=Label(self,image=self.image)
    self.width, self.height = width, height
    self.afficher(); self.loop
    #self.label['image'] = self.image = ImageTk.PhotoImage(self.board)
##    for loop in range (rows*cols):
##      Brick(win,height=size, width=size)
    
  def afficher(self):
    image=self.board
    level=Image.open('images/boardA.png')
    image.paste(level)
    self.image.paste(image)
# -------------------------------------------------------------------------- 
  def on_click(self, widget, code, mods):
    """apply floodfiil """
    widget.state=1
##    if widget != self.label: return # only click on board are processed
##    x = (widget.winfo_pointerx() - widget.winfo_rootx()) # get x coord for mouse 
##    y = (widget.winfo_pointery() - widget.winfo_rooty()) # get y coord for mouse
##    colors = ((255,0,0), (0,255,0), (0,0,255), (255,255,0)) # define RGB colorset
##    if self.board.getpixel((x,y)) != (255,255,255):
##      return # no floodfill when color of seed pixel is not white
##    color = colors[rr(4)] # select random color from colorset
##    ImageDraw.floodfill(self.board, (x,y), color, thresh=128) # apply floodfill
##    self.label['image'] = self.image = ImageTk.PhotoImage(self.board) # update
  


    
    
# ----------------------------------------------------------------------------
  #def grid(self):
    
# ==============================================================================
if __name__ == "__main__": # testcode for class 'PegGUI'
  ComboColor()
# ==============================================================================
