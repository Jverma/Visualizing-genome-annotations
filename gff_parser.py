# -*- coding: utf-8 -*-
# Parsing annotations file to extract data to be used for other purposes.
# Author - Janu Verma
# jv367@cornell.edu
# @januverma


import sys
import json


class gffParser:
    """ GFF Parser Class.
        Extracts the relevant information and stores it in a way
        which facilitates quick access and processing.

        Parameters
        ----------
        input_file : path to the gff file. 

        Example
        -------
        >>> from gff import gffParser
        >>> import sys
        
        >>> input_file = sys.argv[1]
        >>> out = gffParser(input_file)
        >>> out.getGenes("1")
    """
    def __init__(self, input_file):
        self.data = {}
        for line in input_file:
            record = line.strip().split("\t")
            sequence_name = record[0]
            source = record[1]
            feature = record[2]
            start = int(record[3])
            end = int(record[4])
            if (record[5] != '.'):
                score = record[5]
            else:
                score = None
            if (record[6] == '+'):
                strand = 1
            else:
                strand = -1
            if (record[7] != '.'):
                frame = record[7]
            else:
                frame = None
            attributes = record[8].split(';')
            attributes = {x.split('=')[0] : x.split('=')[1] for x in attributes if '=' in x}
            if not(sequence_name in self.data):self.data[sequence_name] = []
            alpha = {'source':source, 'feature':feature, 'start':start, 'end':end, 'score':score, 'strand':strand, 'frame':frame}
            for k,v in attributes.iteritems(): alpha[k] = v
            self.data[sequence_name].append(alpha)

    
    

    def getChromosomes(self):
        """Gets all the chromosomes in the gff file.

        Returns
        -------
        A list of chromosomes in the input GFF file.
        """
        return self.data.keys()
    

    
    def getGenes(self, Id):
        """ Gets all the genes for a chromosomes with all the relevant information.

            Parameters
            ----------
            Id : The identifier for the sequence. e.g. 9, 1, 2 in our file.
            
            Returns
            -------
            A list of dictionaries where each dictionary corresponds to a gene in the sequence.
        """
        genes_list = []
        chromosome = self.data[Id]
        for x in chromosome:
            if (x['feature'] == 'gene'):
                gene_info = x
                genes_list.append(gene_info)
        return genes_list
    


    
    def getmRNA(self, seq_name, Id):
        """ Gets all the mRNAs (transcripts) for a given gene.

            Arguments
            ---------
            seq_name : The name/identifier of the sequence.
            Id : The identifier/name of the gene we are interested in.
            
            Returns
            -------
            A list of dictionaries where each dictionary contains 
            information about an mRNA for the gene.
            """
        mRNA_list = []
        for x in self.data[seq_name]:
            if (x['feature'] == 'mRNA') and (x['Parent'] == Id):
                mRNA_info = x
                mRNA_list.append(mRNA_info)
        return mRNA_list
    
    
    def getCDS(self, seq_name, Id):
        """ Gets all the CDS for a given transcript (mRNA).

            Parameters
            ----------
            seq_name : Name/identifier of the sequence.
            Id : Identifier of the mRNA.
            
            Returns
            -------
            A list of dictionaries where each dictionary contains the 
            informations about an CDS for the transcript.
            """
        cds_list = []
        for x in self.data[seq_name]:
            if (x['feature'] == 'CDS') and (x['Parent'] == Id):
                cds_info =  x
                cds_list.append(cds_info)
        return cds_list


    def getFivePrimeUTR(self, seq_name, Id):
        """ Gets all the five prime UTRs for a given transcript. 

            Parameters
            ----------
            seq_name : Name/identifier of the sequence.
            Id : Identifier of the mRNA.

            Returns
            -------
            A list of dictionaries where each dictionary contains the 
            informations about an 5'-UTR for the transcript.

        """
        fivePrimeUTR_list =[]
        for x in self.data[seq_name]:
            if (x['feature'] == 'five_prime_UTR') and (x['Parent'] == Id):
                fivePrimeUTR_info = x
                fivePrimeUTR_list.append(fivePrimeUTR_info)
        return fivePrimeUTR_list



    def getThreePrimeUTR(self, seq_name,Id):
        """ Gets all the three prime UTRs for a given trancript. 

            Parameters
            ----------
            seq_name : Name/identifier of the sequence.
            Id : Identifier of the mRNA.

            Returns
            -------
            A list of dictionaries where each dictionary contains the 
            informations about an 3'-UTR for the transcript.
        """
        threePrimeUTR_list = []
        for x in self.data[seq_name]:
            if (x['feature'] == 'three_prime_UTR') and (x['Parent'] == Id):
                threePrimeUTR_info = x
                threePrimeUTR_list.append(fivePrimeUTR_info)
        return threePrimeUTR_list



    def child_parent_dict(self):
        """ Gets parents of a child transcript.

        Returns
        -------
        A dictionary containing transcripts as keys and lists containing
        the parent gene, chromosome and strand as values. 
        """
        child_parent_dict = {}
        for x in self.data.keys():
            y = self.data[x]
            for z in y:
                if (z['feature'] == 'mRNA'):
                    mRNA_id = z['ID']
                    parent_gene = z['Parent']
                    strand = z['strand']
                    child_parent_dict[mRNA_id] = [parent_gene, x, strand]
        return child_parent_dict

