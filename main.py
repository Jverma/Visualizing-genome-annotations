# -*- coding: utf-8 -*-
# Parent-child CSV file for visualization.
# Author - Janu Verma
# jv367@cornell.edu
# @januverma

import sys
import csv
from gff_parser import gffParser


endChrom = int(sys.argv[1])
input_file = open(sys.argv[2])
out = gffParser(input_file)
with open('parentChild.csv', 'wb') as csvfile:
	chromWriter = csv.writer(csvfile)
	chromWriter.writerow(["name", "parent", "start", "end", "type"])
	chromWriter.writerow(["chromosomeI", "null", 1, endChrom, "chromosome"])
	genes = out.getGenes("chromosomeI")
	for gene in genes:
		if (gene['end'] > endChrom):
			break
		chromWriter.writerow([gene['Name'],"chromosomeI", gene['start'], gene['end'], "gene"])
		mRNA = out.getmRNA("chromosomeI", gene['Name'])
		for transcript in mRNA:
			chromWriter.writerow([transcript['Name'], gene['Name'], transcript['start'], transcript['end'], "transcript"])
			coding_regions = out.getCDS("chromosomeI", transcript['ID'])
			for cds in coding_regions:

				chromWriter.writerow([cds['ID'], transcript['Name'], cds['start'], cds['end'], "CDS"])
		
