# Rule 3.1.m: Each semicolon shall follow the statement it terminates without a precceding space

for filename in vera.getSourceFileNames():
    file = open(filename, 'rb');
    lineCounter = 1;
    lines = file.readlines();

    for line in lines:
        pos = line.find(';');

        if pos != -1:
            if line[pos-1] == ' ':
                vera.report(filename, lineCounter, ''.join(['White space before semicolon detected at position ', str(pos)]));

        lineCounter = lineCounter + 1;

    file.close();