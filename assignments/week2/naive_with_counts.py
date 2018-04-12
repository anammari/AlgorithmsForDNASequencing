#!/usr/bin/env python

"""naive_with_counts.py: naive exact matching with the number of character comparisons performed and the number of alignments tried."""

__author__ = "Ahmad Ammari"

def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            # ignore header line with genome information
            if not line[0] == '>':
                genome += line.rstrip()
    return genome
	
	
def naive_with_counts(p, t):
    occurrences = []
    num_alignments = len(t) - len(p) + 1
    num_character_comparisons = 0
    for i in range(len(t) - len(p) + 1):
        match = True
        for j in range(len(p)):
            num_character_comparisons += 1
            if t[i+j] != p[j]:
                match = False
                break
        if match:
          occurrences.append(i)
    return (occurrences, num_alignments, num_character_comparisons)
	

