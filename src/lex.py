import ply.lex as lex

tokens = ['STARTTAG','ENDTAG','EMPTYTAG','COMMENT','TEXT','DOCTYPE','FILLER','ENDFILE']
t_STARTTAG = r'<[^\/!][^<>]*>'
t_ENDTAG = r'<\/[^<>\!\/]*>'
t_EMPTYTAG = r'<[^\/!][^<>]*\/>'
t_TEXT = r'(?=[^<>]+)[^\n<>]+'
t_COMMENT = r'<\!--[^!]+-->'
t_DOCTYPE = r'<\![^-][^<>*]+>'
t_FILLER = r'[ ]{2,}|[\n]+'
t_ENDFILE = r'<\/[Hh][Tt][Mm][Ll]>'
def t_error(t):
   raise TypeError("Unknown text '%s'" % (t.value))

lex.lex()