count=0
if int(raw_input('Enter 1 to continue:'))==1:
	print('Welcome')
	if float(raw_input('7+9:'))==16: count=count+20
	if float(raw_input('9^0:'))==1: count=count+20
	if float(raw_input('2-9:'))==0-7: count=count+20
	if float(raw_input('88*8:'))==704: count=count+20
	if float(raw_input('123/3:'))==41: count=count+20
        if count==100: print 'Excellent!'
	print 'Your result is ',count
else:
	print('Bye')
	
