# coding=utf-8
# Rule 3.1.m: Each semicolon shall follow the statement it terminates without a precceding space
import re
semicolon_preceded_by_space = re.compile('([\s];)');

for filename in vera.getSourceFileNames():
    file = open(filename, 'rb');
    lineCounter = 1;
    lines = file.readlines();
    
    for line in lines:
        for mem in re.finditer(semicolon_preceded_by_space, line):
            vera.report(filename, lineCounter, ''.join(['White space before semicolon detected at position ', str(mem.start() + 1)]));

        lineCounter = lineCounter + 1;

    file.close();
