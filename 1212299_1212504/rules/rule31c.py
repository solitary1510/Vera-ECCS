# coding=utf-8
# Each of the binary operators +, -, *, /, %, <, <=, >, >=, ==, !=, <<, >>, &, |, ^, &&, and || shall always be preceded and followed by one space.
#
import re

operator = re.compile('[\+\-\*\/\%\<\>\&\|\^\=\!]'); # kiem tra them dau bang
operatorDouble = re.compile('[\&\|\<\>\=]') # kiem tra them double
for filename in vera.getSourceFileNames():
    file = open(filename, 'rb');
    lineCounter = 1;
    lines = file.readlines();
    
    for line in lines:
        iterator = re.finditer(operator, line);
        if iterator != None:
            for mem in iterator:
                # truoc khong co dau cach => bao loi
                if line[mem.start() - 1] != ' ':
                    vera.report (filename, lineCounter, ''.join(['Preceded non have one space at position ', str(mem.start() + 1)]));
                else: # Sau, kiem tra dau bang => khong co dau cach => bao loi
                    if (line[mem.start() + 1] == '=') and (line[mem.start() + 2] != ' '):
                        vera.report (filename, lineCounter, ''.join(['Followed non have one space at position ', str(mem.start() + 2)]));
                    else:  # if la mot trong cac ki tu double => kiem tra double=> khong co dau cach => bao loi
                        iterInOperaterDouble = re.search(operatorDouble, line[mem.start()]);
                        if iterInOperaterDouble != None:
                            if (line[mem.start() + 1] == line[mem.start()]) and (line[mem.start() + 2] != ' '):
                                vera.report (filename, lineCounter, ''.join(['Followed non have one space at position ', str(mem.start() + 2)]));
        lineCounter = lineCounter + 1;

    file.close();