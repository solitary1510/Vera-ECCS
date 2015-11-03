# Keywords goto, continue, and break shall not be used to create unconditional jumps
import re
string_check = re.compile('goto|continue|break');

for filename in vera.getSourceFileNames():
    file = open (filename, 'rb');
    lineCounter = 1;
    lines = file.readlines();

    for line in lines:
        iterator = re.finditer(string_check, line);
        if iterator != None:
            for mem in iterator:
                vera.report (filename, lineCounter, ''.join(['position ', str(mem.start())]));
        lineCounter = lineCounter + 1;
        
    file.close();
