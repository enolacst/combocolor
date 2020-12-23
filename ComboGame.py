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
    #self.reset(config)
    self.scores=[[0,0], [0,0], [0,0], [0,0]]
    #[[AR,MR], [AG,MG], [AB,MB], [AY,MY]]
  # ----------------------------------------------------------------------------
##  def __repr__(self):
##    """return object representation for 'self'"""
##    return "%s(config=%r)" % (type(self).__name__, self.config)
##  # ----------------------------------------------------------------------------
##  def __str__(self):
##    """return string representation for 'self'"""
##    return ' '.join(list(self.board)).replace(': ', '\n')
##  # ----------------------------------------------------------------------------
##  def reset(self, config=''):
##    """reset the board and set game configuration according to 'config'"""
##  # ----------------------------------------------------------------------------
##  def clear(self):
##    self[:,:]=self.none; return self()
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
      self.scores[i][1]+=tags[1] # sinon c'est une multiplication, on met dans M

    AR=self.scores[0][0]#attribution
    MR=self.scores[0][1]
    AB=self.scores[2][0]
    MB=self.scores[2][1]
    if AR==0 and MR==0 and AB==0 and MB==0 : A=0 #si tout est = 0
    else : # pour ne pas avoir de multiplication par 0
      if AR==0 : AR=1 
      if MR==0 : MR=1
      if AB==0 : AB=1
      if MB==0 : MB=1
      A = (AR*MR*AB*MB)#calcul final A, produit des scores rouge et bleu
    
    AG=self.scores[1][0]
    MG=self.scores[1][1]
    AY=self.scores[3][0]
    MY=self.scores[3][1]
    if AG==0 and MG==0 and AY==0 and MY==0 : B=0 #si tout est = 0
    else : # pour ne pas avoir de multiplication par 0
      if AG==0 : AG=1 
      if MG==0 : MG=1
      if AY==0 : AY=1
      if MY==0 : MY=1
      B = (AG*MG*AY*MY)#calcul final B, produit des scores vert et jaune
    #print([[AR,MR], [AG,MG], [AB,MB], [AY,MY]])
    print([A,B])
    return [A,B]
  # --------------------------------------------------------------------------
  #def gagnant(sel):
  # -------------------------------------------------------------------------- 
  def texte(self,coordx,coordy,color,file_name):
    """lecture du fichier texte"""
    self.color=color
    txt = read_blk(file_name+'.txt')#lecture du fichier texte associé a la grille
    #print(txt[coordy][coordx])
    return self.score(txt[coordy][coordx])
# ==============================================================================
if __name__ == "__main__": # testcode for class 'ComboGame'
  code = r'''
'''; testcode(code)
