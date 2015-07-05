# Visualizing-genome-annotations
D3 JavaScript interactive visualization of genome feature (gff) files

This introduces a framework to create an interative and informative visualization of a [genome feature file](http://www.ensembl.org/info/website/upload/gff.html)(GFF). 

**General Feature Format (GFF)** also known as *Gene-Finding Format* is a file format which describes the features of genomic and protein sequences. A GFF file is a tab delimited text file where each feature is described on a single line. 

More information about GFF format can be found at <a href="http://www.sanger.ac.uk/resources/software/gff/">Wellcome Trust Sanger Institute</a>.

e.g. for maize, the GFF file I used looks like -

    9	ensembl	chromosome	1	156750706	.	.	.	ID=9;Name=chromosome:AGPv2:9:1:156750706:1
    9	ensembl	gene	66347	68582	.	-	.	ID=GRMZM2G354611;Name=GRMZM2G354611;biotype=protein_coding
    9	ensembl	mRNA	66347	68582	.	-	.	ID=GRMZM2G354611_T01;Parent=GRMZM2G354611;Name=GRMZM2G354611_T01;biotype=protein_coding
    9	ensembl	intron	68433	68561	.	-	.	Parent=GRMZM2G354611_T01;Name=intron.1

This uses JavaScript framework [D3.js](https://github.com/mbostock/d3). 


**Usage:**

- We need to create a CSV file containing the relevent information. This uses a python script to parse GFF file. This is taken from [GFF Parser](https://github.com/Jverma/GFF-Parser). We have written a script ```main.py``` which will create a CSV file named ```parentChild.csv```. Choose the chromosome and the segment of the chromosome to explore. e.g - 

        python main.py 5000 50000 chromosomeI sample1.gff
  
- Launch the ```gffTree.html``` into any browser. This will contain the tree visualization. 

- Ih short, the main script here is ```main.py```. After running this as above, we can directly open the HTML file to view the tree.


**Exploration:**

- The visualization is a tree encoding parent-child relationship of the genomic annotations e.g. for each chromosom, we have several genes and each gene, in turn, his composed of one or more transcripts, which are further divided into coding regions. 
- Each node in the tree represents an annotations e.g chromosome, gene, transcript, CDS.
- Each node is collapsibale, meaning the children will collapse into the node on click. 
- Each node contains the information about the type of annotation it is encoding, and it's start & end. This can be accessed by moving the mouse over to the name (text) of the node. The values will pop-up on the screen. 

See the visualization in action at [bl.ocks](http://bl.ocks.org/Jverma/4d8d73ad5f2bb39bab53)


