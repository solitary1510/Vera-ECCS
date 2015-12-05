# coding=utf-8
# Comma should not be preceded by whitespace, but should be followed by one
import re
group_param_func = re.compile('\(.*\)');
comma_not_space_preceded_followed = re.compile('([\s],)|(,[^\s])');

for filename in vera.getSourceFileNames():
    file = open (filename, 'rb');
    lineCounter = 1;
    lines = file.readlines();

    for line in lines:
        pos = re.search(group_param_func, line);
        if pos != None:
            for mem in re.finditer(comma_not_space_preceded_followed, line):
                vera.report (filename, lineCounter, ''.join(['Comma should not be preceded by whitespace and should be followed by one at position ', str(mem.start() + 1)]));
        lineCounter = lineCounter + 1;
        
    file.close();
