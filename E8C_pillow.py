# ==============================================================================
"""PILLOW : demo program for the Pillow module"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "1.0"
__date__    = "2020-11-25"
# ==============================================================================
from ezTK import *
from PIL import Image, ImageTk, ImageDraw
from random import randrange as rr
# ------------------------------------------------------------------------------
class DemoPillow(Win):
  """demo program for the Pillow module"""
  # ----------------------------------------------------------------------------
  def __init__(self, width=512, height=512):
    """create the main window and pack the widgets"""
    Win.__init__(self, title='PILLOW', click=self.on_click, op=5, grow=False)
    self.board = Image.new('RGB', (width, height), '#FFF') # create PIL image
    self.image = ImageTk.PhotoImage(self.board) # create Tk image for display
    self.width, self.height = width, height # store image size as attributes
    # --------------------------------------------------------------------------
    info = 'Click anywhere on window to apply floodfill from that seed point'
    Label(self, text=info); self.label = Label(self, image=self.image)
    self.lines(); self.loop()
  # ----------------------------------------------------------------------------
  def lines(self):
    """draw a random set of black lines on image"""
    w, h = self.width, self.height # create local shortcut for image size
    board = ImageDraw.Draw(self.board) # create interactive image (for drawing)
    for loop in range(8): # draw 8 pairs of random lines on image
      xa, ya, xb, yb = rr(w), rr(h), rr(w), rr(h) # select random coordinates
      board.line((xa, 0, xb, h), width=2, fill='#000') # line from top to bottom
      board.line((0, ya, w, yb), width=2, fill='#000') # line from left to right
    self.label['image'] = self.image = ImageTk.PhotoImage(self.board) # update
  # ------------------------------------------------------------------------------
  def on_click(self, widget, code, mods):
    """apply floodfiil """
    if widget != self.label: return # only click on board are processed
    x = (widget.winfo_pointerx() - widget.winfo_rootx()) # get x coord for mouse 
    y = (widget.winfo_pointery() - widget.winfo_rooty()) # get y coord for mouse
    colors = ((255,0,0), (0,255,0), (0,0,255), (255,255,0)) # define RGB colorset
    if self.board.getpixel((x,y)) != (255,255,255):
      return # no floodfill when color of seed pixel is not white
    color = colors[rr(4)] # select random color from colorset
    ImageDraw.floodfill(self.board, (x,y), color, thresh=128) # apply floodfill
    self.label['image'] = self.image = ImageTk.PhotoImage(self.board) # update
# ==============================================================================
if __name__ == '__main__':
  DemoPillow()
# ==============================================================================
