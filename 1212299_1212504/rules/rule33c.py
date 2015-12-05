# Rule 3.1.c: Each source file shall have a blank line at the end.
import re
blank_line = re.compile('[\r\n]');

for filename in vera.getSourceFileNames():
    file = open(filename, 'rb');
    lineCounter = 0;
    lines = file.readlines();
    
    for line in lines:
        lineCounter = lineCounter + 1;
    if re.search(blank_line, line) == None:
        vera.report(filename, lineCounter, 'Source file shall have a blank line at the end');

    file.close();