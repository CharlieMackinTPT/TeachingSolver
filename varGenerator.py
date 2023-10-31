# Write the rows to a CSV file.
with open("permutations.csv", "w", encoding="utf-8") as f:
	f.write("big,medium,small,square,triangle,circle,smooth,rough,fuzzy,red,green,blue")
	f.write('\n')
	for a in range(0, 3):
		p1 = ""
		p2 = ""
		p3 = ""
		p4 = ""
		match a:
			case 0:
				p1 = "1,0,0"
			case 1:
				p1 =  "0,1,0"
			case 2:
				p1 =  "0,0,1"
		
		for b in range(0, 3):
			match b:
				case 0:
					p2 =  ",1,0,0"
				case 1:
					p2 =  ",0,1,0"
				case 2:
					p2 =  ",0,0,1"
					
			for c in range(0, 3):
				match c:
					case 0:
						p3 = ",1,0,0"
					case 1:
						p3 =  ",0,1,0"
					case 2:
						p3 =  ",0,0,1"
						
				for d in range(0, 3):
					match d:
						case 0:
							p4 = ",1,0,0"
						case 1:
							p4 = ",0,1,0"
						case 2:
							p4 =  ",0,0,1"
							
					f.write(p1+p2+p3+p4)
					f.write('\n')