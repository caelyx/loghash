#!/usr/bin/env python2

"""
verify.py - Basic tamper evidence for logs, written in python.
Copyright (C) 2017 Simon Brown
Under GPLv3; see LICENSE for license.
"""

import sha

SALT = '844cde87865f882399dcffcecb002e5397f9d177'

def hashOneLine(previousHash, line): 
    """ Given a previous hash and a line of text, defang the line,
    hash it, and return the hash and the formatted line. """
    formattedLine = previousHash + ' ' + line.replace('\n', ' ')
    newHash = sha.sha(formattedLine + SALT).hexdigest()
    return (newHash, formattedLine)

def verifyLines(lines):
    output = []
    for i in range(len(lines) - 1): 
        l = lines[i]
        (previousHash, lineText) = l.split(' ', 1)
        lineText = lineText[:-1]
        (proposedNewHash, formattedLine) = hashOneLine(previousHash, lineText)
        (newHash, nextline) = lines[i+1].split(' ', 1)
        if (proposedNewHash == newHash): 
            output.append("+ %s" % lineText)
        else:
            output.append("!!! %s" % lineText)
    return output

def verifyFile(fInput='output.txt', fOutput=None): 
    fi = open(fInput)
    if fOutput: 
        fo = open(fOutput, 'w')
    
    inputlines = fi.readlines()
    fi.close()
    outputlines = verifyLines(inputlines)
    if fOutput: 
        fo.writelines(outputlines)
        fo.close()
    else:
        import string
        print string.join(outputlines, '\n')

if __name__ == "__main__": 
    verifyFile()
