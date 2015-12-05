# coding=utf-8
# All new structures, unions, and enumerations shall be named via a typedef
import re
typeDef = 'typedef ';
size_typeDef = 8;
string_check = re.compile('struct|union|enum');

for filename in vera.getSourceFileNames():
    file = open (filename, 'rb');
    lineCounter = 1;
    lines = file.readlines();

    for line in lines:
        iterator = re.finditer(string_check, line);
        if iterator != None:
            for mem in iterator:
                if mem.start() > size_typeDef:
                    if not re.match(line[(mem.start() - size_typeDef): mem.start() - 1], typeDef):
                        vera.report (filename, lineCounter, ''.join(['New structures, unions, and enumerations shall be named via a typedef at position ', str(mem.start() + 1)]));
                else:
                    vera.report (filename, lineCounter, ''.join(['New structures, unions, and enumerations shall be named via a typedef at position ', str(mem.start() + 1)]));
                
        lineCounter = lineCounter + 1;
        
    file.close();
