import ply.lex as lex
import ply.yacc as yacc
import sys
from lex import *
from yacc import *
from get_tree import *
from parse import *

file = open(sys.argv[1], 'r')
data = file.readlines()
data = ''.join(data)
tree = get_tree(data)

# file_tree = open("tree.txt",'w')
# write_tree(tree,file_tree)

file1 = open(sys.argv[2], 'w')
parse_tree(tree,file1)
file1.close()