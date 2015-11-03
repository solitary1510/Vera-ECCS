# Rule 3.1.m: The left and right brackets of the array subscript operator ([ and ]) shall always be without surrounding spaces.
import re
semicolon_preceded_by_space = re.compile('([\s]\])|(\][\s])|([\s]\[)|(\[[\s])');

for filename in vera.getSourceFileNames():
    file = open(filename, 'rb');
    lineCounter = 1;
    lines = file.readlines();
    
    for line in lines:
        for mem in re.finditer(semicolon_preceded_by_space, line):
            vera.report(filename, lineCounter, ''.join(['White space surrounding brackets of the array subscript operator detected at position ', str(mem.start() + 1)]));

        lineCounter = lineCounter + 1;

    file.close();
