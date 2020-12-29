# ==============================================================================
"""ComboGame : kernel class for the Combocolor game"""
# ==============================================================================
__author__  = "Constanceau Enola & Panetier Camille"
__version__ = "2.0"
__date__    = "2020-12-23"
# ------------------------------------------------------------------------------
from ezCLI import *
from random import randrange as rr
# ------------------------------------------------------------------------------
class ComboGame(object):
  """ComboGame class for the combocolor game"""
  # ----------------------------------------------------------------------------
  def __init__(self, config='full'):
    """initialize 'self' by creating the board with chosen game configuration"""
    self.scores=[[0,1], [0,1], [0,1], [0,1]]
    self.countColors=0
  # ----------------------------------------------------------------------------
  def score(self,lettre):
    """calcul score"""
    #dictionnaire :
    zones = {'A':(1,0), 'B':(1,0),'C':(1,0),'D':(1,0),'E':(2,0), 'F':(2,0),'G':(2,0),'H':(2,0),
             'I':(3,0), 'J':(3,0),'K':(3,0),'L':(4,0),'M':(4,0),'N':(-2,0), 'O':(-2,0),'P':(-2,0),
             'Q':(-4,0),'R':(-4,0),'S':(-6,0),'T':(-6,0),'U':(0,2), 'V':(0,2),'W':(0,3),'X':(0,3)}  
    colors = {(255,0,0):0,(0,255,0):1,(0,0,255):2,(255,255,0):3} #dictionnaire de couleurs
    i=colors.get(self.color)#indice de la couleur dans dic
    tags=zones.get(lettre)

    if tags[0]!=0 : #si la première partie est différente de 0 alors on met dans A
      self.scores[i][0]+=tags[0]
    else :
      self.scores[i][1]*=tags[1] # sinon c'est une multiplication, on met dans M

    AR=self.scores[0][0]#attribution
    MR=self.scores[0][1]
    AB=self.scores[2][0]
    MB=self.scores[2][1]
    if AR==0 and MR==0 and AB==0 and MB==0 : A=0 #si tout est = 0
    else : # pour ne pas avoir de multiplication par 0
      if AR==0 : AR=1 
      if AB==0 : AB=1
      A = (AR*MR*AB*MB)#calcul final A, produit des scores rouge et bleu
    
    AG=self.scores[1][0]
    MG=self.scores[1][1]
    AY=self.scores[3][0]
    MY=self.scores[3][1]
    if AG==0 and MG==0 and AY==0 and MY==0 : B=0 #si tout est = 0
    else : # pour ne pas avoir de multiplication par 0
      if AG==0 : AG=1 
      if AY==0 : AY=1
      B = (AG*MG*AY*MY)#calcul final B, produit des scores vert et jaune

    self.countColors+=1 #on rajoute une case colorée
    
    if self.countColors==24 :
      self.scores=[[0,1], [0,1], [0,1], [0,1]] #partie finie on remet les score à 0
      self.countColors=0
      return [A,B,True] #savoir si toutes les cases sont coloriées
    return [A,B, False] #toutes les cases ne sont pas coloriée
  # -------------------------------------------------------------------------- 
  def texte(self,coordx,coordy,color,file_name):
    """lecture du fichier texte"""
    self.color=color
    txt = read_blk(file_name+'.txt')#lecture du fichier texte associé a la grille
    return self.score(txt[coordy][coordx])
  # -------------------------------------------------------------------------- 
  def verifAdjacent(self,coordx,coordy,file_name, board):
    """vérification pour colorié une case adjacente à une case déjà coloriée"""
    txt = read_blk(file_name+'.txt')#lecture du fichier texte
    lettre = txt[coordy][coordx]#lettre qui correspond
    caseVerifie = [] #tableau des lettre que j'ai déjà vérifié
    caseAVerifie = [] #tableau des lettre à vérifier
    reponse = False 
    caseAVerifie.append([coordy,coordx])
    index = 0
    while len(caseAVerifie) > 0 and index < 50: #<50 pour sécurité, tant qu'il y a des cases a vérifier
      coord = caseAVerifie.pop()#sort coordonnées à vérifier
      coordy = coord[0]
      coordx = coord[1]
      #regarder si lettre au dessus/en dessous/à gauche/à droite est coloriée
      if coordy != 0: #vérifier case au dessus, si coordy=0 on est dans le coin 
        if [coordy-1,coordx] not in caseVerifie:#regarder si coordonée ne sont pas dans le tableau caseVerifie
          if txt[coordy-1][coordx] != lettre: #regarde si meme lettre donc meme case
            if self.verifCouleur((coordy-1)*63,coordx*63, board): #vérifie si lettre à coté est colorié ou non
              caseAVerifie = []#plus de case à vérifier  
              reponse = True #si on trouve une couleur
              break #casse boucle while, on sort
          else: #si même lettre je rajoute dans tableau à vérifier
            caseAVerifie.append([coordy-1,coordx])

      if coordy != 10: #case en dessous
        if [coordy+1,coordx] not in caseVerifie:
          if txt[coordy+1][coordx] != lettre:
            if self.verifCouleur((coordy+1)*63,coordx*63, board):
              caseAVerifie = []
              reponse = True
              break
          else:
            caseAVerifie.append([coordy+1,coordx])

      if coordx != 0: #case à gauche
        if [coordy,coordx-1] not in caseVerifie:
          if txt[coordy][coordx-1] != lettre:
            if self.verifCouleur(coordy*63,(coordx-1)*63, board):
              caseAVerifie = []
              reponse = True
              break
          else:
            caseAVerifie.append([coordy,coordx-1])

      if coordx != 10: #case à droite
        if [coordy,coordx+1] not in caseVerifie:
          if txt[coordy][coordx+1] != lettre:
            if self.verifCouleur(coordy*63,(coordx+1)*63, board):
              caseAVerifie = []
              reponse = True
              break
          else:
            caseAVerifie.append([coordy,coordx+1])

      caseVerifie.append([coordy,coordx])
      index += 1
    
    return reponse

# -------------------------------------------------------------------------- 
  def verifCouleur(self,coordy,coordx,board):
    """vérifier si bien blanc"""
    coordx+=10 #vrai coordonnée, on ajoute 10 pour ne pas se retrouver dans la bande noire (remultiplication par 63)
    coordy+=10
    if board.getpixel((coordx,coordy)) != (255,255,255):#différent de blanc
      return True 
    return False
# ==============================================================================
if __name__ == "__main__": # testcode for class 'ComboGame'
  code = r'''
'''; testcode(code)
