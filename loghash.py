#!/usr/bin/env python2

"""
loghash.py - Basic tamper evidence for logs, written in python.
Copyright (C) 2017 Simon Brown
Under GPLv3; see LICENSE for license.
"""

import sha

SALT = '844cde87865f882399dcffcecb002e5397f9d177'

def hash_one_line(previous_hash, line):
    """ Given a previous hash and a line of text, defang the line,
    hash it, and return the hash and the formatted line. """
    formatted_line = previous_hash + ' ' + line.replace('\n', ' ')
    new_hash = sha.sha(formatted_line + SALT).hexdigest()
    return (new_hash, formatted_line)


def hashLines(lines, previous_hash=SALT):
    output = []
    for l in lines:
        (new_hash, formatted_line) = hash_one_line(previous_hash, l)
        output.append(formatted_line + "\n")
        previous_hash = new_hash
    output.append(new_hash + " -\n")
    return output


def hashFile(f_input='input.txt', f_output='output.txt'):
    fi = open(f_input)
    fo = open(f_output, 'w')

    inputlines = fi.readlines()
    outputlines = hashLines(inputlines)
    fo.writelines(outputlines)
    fi.close()
    fo.close()


if __name__ == "__main__":
    hashFile()