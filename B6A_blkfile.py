# ==============================================================================
"""BLKFILE : demo for 'read_blk/write_blk' functions from the 'ezCLI' toolbox"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "1.0"
__date__    = "2015-07-01"
__usage__   = """
Simply press <ENTER> at each pause""" 
# ==============================================================================
from ezCLI import *
# ------------------------------------------------------------------------------
# Sample use cases for 'read_blk'
# ------------------------------------------------------------------------------
txt = read_txt('test-blk.txt')
pause(">>> read BLK file as a TXT file :\n%s" % txt)

blk = read_blk('test-blk.txt')
pause(">>> read BLK file as list of single-line blocks :\n%s" % blk)

blk = read_blk('test-blk.txt', sep='\n\n')
pause(">>> read BLK file as list of multi-line blocks :\n%s" % blk)

blk = read_blk('test-blk.txt', filters={' ':lambda s:s.strip()})
pause(">>> apply filter to strip space_indented blocks :\n%s" % blk)

# ------------------------------------------------------------------------------
# Sample use cases for 'write_blk'
# ------------------------------------------------------------------------------
items = 'aaa bbb ccc ddd eee'.split(' ')
pause(">>> sample sequence of blocks containing 5 strings :\n%s" % items)

blk = write_blk('test.txt', items)
pause(">>> write content of 'items' in file 'test.txt' :\n%s" % blk)

blk = write_blk('test.txt', '***\n***', 0)
pause(">>> insert new blocks at head :\n%s" % blk)

blk = write_blk('test.txt', ('***', '***'), -1)
pause(">>> insert new blocks at tail :\n%s" % blk)

blk = write_blk('test.txt', items[0], None, 3)
pause(">>> replace the first three blocks :\n%s" % blk)

blk = write_blk('test.txt', items[4], -3, None)
pause(">>> replace the last three blocks :\n%s" % blk)
# ==============================================================================
