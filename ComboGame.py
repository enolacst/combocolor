# ==============================================================================
"""ComboGame : kernel class for the Combocolor game"""
# ==============================================================================
__author__  = "Constanceau Enola & Panetier Camille"
__version__ = "1.0"
__date__    = "2020-11-20"
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
    
# ==============================================================================
if __name__ == "__main__": # testcode for class 'ComboGame'
  code = r'''
'''; testcode(code)
