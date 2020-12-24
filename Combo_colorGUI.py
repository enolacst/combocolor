# ==============================================================================
"""ComboColor: GUI (graphical user interface) class for the combocolor game"""
# ==============================================================================
__author__  = "Constanceau Enola & Panetier Camille"
__version__ = "2.0"
__date__    = "2020-12-23"
# ==============================================================================
from ezTK import *
from ezCLI import *
from PIL import Image,ImageDraw,ImageTk
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
    self.count=0
    self.frame1=Frame(self,grow=False, op=0)
    self.label=Label(self.frame1, text='Choix de la grille de jeu', font='Arial 15 bold italic')
    self.frame2 = Frame(self, op=0)
    Button(self.frame2, text='Grille A',fg="cyan",font='Arial 18 bold',command=lambda:self.grid('boardA'))
    Button(self.frame2, text='Grille B',fg="red",font='Arial 18 bold',command=lambda:self.grid('boardB'))
    Button(self.frame2, text='Grille C',fg="pink",font='Arial 18 bold',command=lambda:self.grid('boardC'))
    Button(self.frame2, text='Grille D',fg="orange",font='Arial 18 bold',command=lambda:self.grid('boardD'))
    Button(self.frame2, text='Grille E',fg="purple",font='Arial 18 bold',command=lambda:self.grid('boardE'))
    Button(self.frame2, text='Grille F',fg="grey",font='Arial 18 bold',command=lambda:self.grid('boardF'))
    self.frame3=Frame(self, op=0)
    Button(self.frame3, text='Règle du jeu',font='Arial 15',command=self.rules)
    # --------------------------------------------------------------------------
    self.loop();
    #self.reset();
    # ----------------------------------------------------------------------------
  def rules(self):
    self.win1=Win(title='Règles du jeu', font='Courier 15')#fenetre pour les règles du jeu
    self.txt = read_txt('rules_game.txt')#lecture texte
    Label(self.win1, text=self.txt,grow=False)
# --------------------------------------------------------------------------
  def grid(self,grid_name,width=699,height=699):
    """nouvelle fenetre pour l'image"""
    self.frame2.destroy()#on elève les bouttons
    self.label.destroy()#on enlève le text
    self.win=Win(self,title='Grille',fold=1,grow=True,click=self.on_click, op=5)
    self.label1=Label(self.win, text='SCORE', font='Arial 15 bold italic')#affichage du score joueur A
    self.label2=Label(self.win, text='SCORE', font='Arial 15 bold italic')#affichage du score joueur B
    self.board= Image.new('RGB',(width,height))#création image
    self.image= ImageTk.PhotoImage(self.board)
    self.label=Label(self.win, text='grille de jeu', font='Arial 18 bold italic',width=width,height=height,image=self.image)
    # --------------------------------------------------------------------------
    self.gridName=grid_name
    self.afficher(grid_name);#récupération nom de la grille
    #self.loop();
    # --------------------------------------------------------------------------
  def afficher(self,grid_name):
    """affichage de l'image selon la grille"""
    self.count=0
    self.grille=Image.open('images/'+grid_name+'.png')#ouverture de l'image
    self.board.paste(self.grille)
    self.image.paste(self.board)
    # --------------------------------------------------------------------------
    self.loop(); 
    # -------------------------------------------------------------------------
  def on_click(self, widget, code, mods):
    """apply floodfiil """
    if widget != self.label: return # only click on board are processed
    x = (widget.winfo_pointerx() - widget.winfo_rootx()) # get x coord for mouse 
    y = (widget.winfo_pointery() - widget.winfo_rooty()) # get y coord for mouse
    coordx=x//63 #carré de 63 par 63
    coordy=y//63
    colors = ((255,0,0),(0,255,0), (0,0,255),(255,255,0)) # define RGB colorset
    if self.board.getpixel((x,y)) != (255,255,255):
      return # no floodfill when color of seed pixel is not white
    
    
    # vérification des adjacentes
    estAdjacent = self.game.verifAdjacent(coordx,coordy,self.gridName, self.board)
    
    if estAdjacent:
      color = colors[self.count] #select color from colorset
      self.count=(self.count+1)%4 #couleur dans l'ordre
      ImageDraw.floodfill(self.board, (x,y), color, thresh=128) # apply floodfill
      self.label['image'] = self.image = ImageTk.PhotoImage(self.board) # update
      self.score = self.game.texte(coordx,coordy,color,self.gridName)
      self.label1['text']='Score joueur A : '+str(self.score[0]) #modification au fur et à mesure du score A
      self.label2['text']='Score joueur B : '+str(self.score[1]) #modification au fur et à mesure du score B

      print(self.score)
      if self.score[2] : #si toute la grille est remplie
        self.win2=Win(self,title='Gagnant',fold=1,grow=True, op=5) # fenetre finale
        if self.score[0]>self.score[1]:
          Label(self.win2,text='Le joueur A remporte la partie', font='Arial 20 bold')
          Button(self.win2,tet='Retour au menu', font='Arial 20 bold')
        elif self.score[0]<self.score[1]:
          Label(self.win2,text='Le joueur B remporte la partie', font='Arial 20 bold')
          Button(self.win2,tet='Retour au menu', font='Arial 20 bold')
        else :
          Label(self.win2,text='Les joueurs sont à égalité', font='Arial 20 bold')
          Button(self.win2,tet='Retour au menu', font='Arial 20 bold')
    # --------------------------------------------------------------------------
    self.loop();
# ==============================================================================
if __name__ == "__main__": # testcode for class combo
  ComboColor()
# ==============================================================================
