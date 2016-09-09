# html-creating functions, from Piazza

# Create the start tag and end tag for any kind of element,
# optionally with attributes and content.
# From Kenny Chen's Piazza post 176, slightly modified
def element(newline, nIndents, tag, attributes, content):
    indent = ' ' * 4 * nIndents
    start = indent + '<' + tag
    start += ' ' + attributes
    start += '>'
    end = '</' + tag + '>'
    if newline:
        start += '\n'
        end = '\n' + indent + end
    return start + content + end

# Generic routines for the parts of a standards-conforming 
# html web page. 
# Structure from James Smith's contributions in Piazza post 208
# with tab characters converted to spaces by
# Notepad++ | Edit | Blank Operations | Tab to space
def htmlSetup():
    return '<!DOCTYPE html> \n <html>'

def titleSetup(title):
    return element( False, 1, 'title', '', title)

def headSetup(title, metadata):
    return element( True, 0, 'head', '', titleSetup(title))

def bodySetup( content):
    return element( True, 0, 'body', '', content)

def tableSetup(tableBorder, caption, rowsHtml):
    return element( True, 0, 'table', 
                    'border="' + tableBorder + '"', 
                    element( False, 2, 'caption', '', caption) + '\n'
                    + rowsHtml
                  )

# someday: replace the 2 html routines with a call to element 
def html_end():
    return '</html>\n'