#!/usr/bin/env python2

"""
loghash.py - Basic tamper evidence for logs, written in python.
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

def hashLines(lines, previousHash=SALT):
    output = []
    for l in lines: 
        (newHash, formattedLine) = hashOneLine(previousHash, l)
        output.append(formattedLine + "\n")
        previousHash = newHash
    output.append(newHash + " -\n")
    return output

def hashFile(fInput='input.txt', fOutput='output.txt'): 
    fi = open(fInput)
    fo = open(fOutput, 'w')
    
    inputlines = fi.readlines()
    outputlines = hashLines(inputlines)
    fo.writelines(outputlines)
    fi.close()
    fo.close()


if __name__ == "__main__": 
    hashFile()

