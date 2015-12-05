# coding=utf-8
#Function-Like Macros:Surround the entire macro body with parentheses.
import re
parentheses_last = ')';
is_function_macros = re.compile ('#define (.*)(...)');


for filename in vera.getSourceFileNames():
    file = open (filename, 'rb');
    lineCounter = 1;
    lines = file.readlines();

    for line in lines:
        line = line.rstrip();
        is_function_MACROS = re.search(is_function_macros, line);
        if is_function_MACROS != None:
            if parentheses_last != line[len(line) - 1]:
                vera.report(filename, lineCounter, ''.join(['Surround the entire macro c.jpgdy with parentheses at line:', str(lineCounter)]));
        lineCounter = lineCounter + 1;
        
    file.close();
