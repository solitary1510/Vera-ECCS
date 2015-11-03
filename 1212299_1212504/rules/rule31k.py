# Comma should not be preceded by whitespace, but should be followed by one
import re
group_param_func = re.compile('\(.*\)');
comma_not_space_followed = re.compile(',[^\s]');
comma_not_space_preceded = re.compile('[\s],');

for filename in vera.getSourceFileNames():
    file = open (filename, 'rb');
    lineCounter = 1;
    lines = file.readlines();

    for line in lines:
        pos = re.search(group_param_func, line);
        if pos != None:
            for mem in re.finditer(comma_not_space_followed, line):
                vera.report (filename, lineCounter, ''.join(['position ', str(mem.start())]));
            for mem in re.finditer (comma_not_space_preceded, line):
                vera.report (filename, lineCounter, ''.join(['position ', str(mem.start())]));
        lineCounter = lineCounter + 1;
        
    file.close();
