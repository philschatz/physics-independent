#!/usr/bin/env python
import os
import subprocess

#
# Please enter the location of your local validator here.
converterPath = "../../cnxml-validator/tohtml.py"
TextbookSpecPath = "TextbookHTML-spec.xml"

#
#
if __name__ == "__main__":
    # find all cnxmlplus files in this folder:
    cnxmlplusfiles = [f for f in os.listdir(os.curdir) if (f.endswith('.cnxmlplus')) and ('.' != f[0])]
    cnxmlplusfiles.sort()
    for cnxmlplusfile in cnxmlplusfiles:
        with open('%s.html'%cnxmlplusfile, "w") as fout:
#           command = ["python","%s --spec %s %s" % (converterPath, TextbookSpecPath, cnxmlplusfile)]
            command = ['python', converterPath, '--spec ', TextbookSpecPath, cnxmlplusfile]
            result = subprocess.call(command, stdout=fout)
            print cnxmlplusfile,'.'*(60-len(cnxmlplusfile)), 
            if result == 0:
                print "ok"
            else:
                print "Conversion Failed"


