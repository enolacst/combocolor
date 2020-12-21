# ==============================================================================
"""ComboGame : kernel class for the Combocolor game"""
# ==============================================================================
__author__  = "Constanceau Enola & Panetier Camille"
__version__ = "2.0"
__date__    = "2020-12-23"
# ------------------------------------------------------------------------------
from ezCLI import testcode
from random import randrange as rr
# ------------------------------------------------------------------------------
class ComboGame(object):
  """ComboGame class for the combocolor game"""
  # ----------------------------------------------------------------------------
  def __init__(self, config='full'):
    """initialize 'self' by creating the board with chosen game configuration"""
    self.reset(config)
  # ----------------------------------------------------------------------------
  def __repr__(self):
    """return object representation for 'self'"""
    return "%s(config=%r)" % (type(self).__name__, self.config)
  # ----------------------------------------------------------------------------
  def __str__(self):
    """return string representation for 'self'"""
    return ' '.join(list(self.board)).replace(': ', '\n')
  # ----------------------------------------------------------------------------
  def reset(self, config=''):
    """reset the board and set game configuration according to 'config'"""
  # ----------------------------------------------------------------------------
  def clear(self):
    self[:,:]=self.none; return self()
  # ----------------------------------------------------------------------------
  #dictionnaire :
  zones = {'A':(1,0), 'B':(1,0),'C':(1,0),'D':(1,0),'E':(2,0), 'F':(2,0),'G':(2,0),'H':(2,0),
  'I':(3,0), 'J':(3,0),'K':(3,0),'L':(4,0),'M':(4,0),'N':(-2,0), 'O':(-2,0),'P':(-2,0),
  'Q':(-4,0),'R':(-4,0),'S':(-6,0),'T':(-6,0),'U':(0,2), 'V':(0,2),'W':(0,3),'X':(0,3)}  
  # ----------------------------------------------------------------------------
  def score(self):
    """calcul score"""
    #A=somme des tags additifs et soustractif
    #M=somme des tags multiplicatifs
    #[[AR,MR], [AG,MG], [AB,MB], [AY,MY]]
    #A = AR*MR*AB*MB
    #B = AG*MG*AY*MY
# ==============================================================================
if __name__ == "__main__": # testcode for class 'ComboGame'
  code = r'''
'''; testcode(code)
