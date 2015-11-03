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
                if iterator.start() > size_typeDef:
                    if not re.match(line[(iterator.start() - size_typeDef): iterator.start() - 1], typeDef):
                        vera.report (filename, lineCounter, ''.join(['New structures, unions, and enumerations shall be named via a typedef at position ', str(iterator.start())]));
                
        lineCounter = lineCounter + 1;
        
    file.close();
