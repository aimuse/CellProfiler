#!/usr/bin/env python

"""
Writes source code for a python module that contains the raw contents
of one or more files.  The contents of each file is assigned to a
variable named after the file.  Characters in the filename that are
not allowed in Python identifiers are replaced by underscores.
"""

from __future__ import with_statement

import os.path
import sys
import re
import base64

print "# Generated by %s.  Do no edit."%(os.path.basename(sys.argv[0]))
print
print "import base64"

for filename in sys.argv[1:]:
    with open(filename) as f:
        data = f.read()
    encoded = base64.b64encode(data)
    name = re.sub(r'[^a-zA-Z0-9_]', '_', filename)
    print
    print '%s = base64.b64decode("%s")'%(name, encoded)
