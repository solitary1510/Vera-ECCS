for filename in vera.getSourceFileNames():
	file = open(filename, 'rb');
	lineCounter = 1;
	lines = file.readlines();
	
	for line in lines:
		pos = line.find('\r');
		
		if pos != -1 and pos != len(line) - 1:
			vera.report(filename, lineCounter, ''.join(['\\r (CR) detected in isolation at position ', str(pos)]));

		lineCounter = lineCounter + 1;

	file.close();