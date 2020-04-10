import pandas as pd
import csv

filename = 'file2.csv'
outpath = 'output2.csv'
df = pd.read_csv(filename)


with open(outpath,'w', newline = '') as f:
	thewriter = csv.writer(f)

	thewriter.writerow(['paper_title','value'])
	for index, line in df.iterrows():
		print(index, line)
		
		# sent.append(line['paper_title'])
		sent = line['value'].lower().split('. ')
		for i, line1 in enumerate(sent):
			sent = (line['paper_title']+str(i), line1)
			# sent.append()
			thewriter.writerow(sent)
		
f.close()