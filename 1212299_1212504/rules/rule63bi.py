#Function-Like Macros:Surround the entire macro body with parentheses.
import re
parentheses_last = re.compile('\)$');
is_function_macros = re.compile ('#define (.*)(...)');


for filename in vera.getSourceFileNames():
    file = open (filename, 'rb');
    lineCounter = 1;
    lines = file.readlines();

    for line in lines:
        is_function_MACROS = re.search(is_function_macros, line);
        if is_function_MACROS != None:
            have_surround = re.match(parentheses_last, line);
            if have_surround == None:
                vera.report (filename, lineCounter, ''.join(['Surround the entire macro c.jpgdy with parentheses at line:', str(lineCounter)]));
        lineCounter = lineCounter + 1;
        
    file.close();
