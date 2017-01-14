#!/usr/bin/python

import sys, getopt, re
from itertools import chain, combinations


def powerset(iterable):
    xs = list(iterable)
    return chain.from_iterable(combinations(xs,n) for n in range(len(xs)+1))


def get_combinations(predicates):
    return list(powerset(set(predicates)))


def explode(s):
    """
    Get all function names and arguments
    """
    pattern = r'(\w[\w\d_]*)\((\w[\w\d,_]*)\)'
    match = re.findall(pattern, s)
    if match:
        return list(match)
    else:
        return []


def create_queries(filename):
    ifile = open(filename, 'r')
    
    # Get all function names and arguments
    allmatches = []
    for line in ifile:
        allmatches.append(explode(line))

    predicates = {}
    for match in allmatches:
        for idx, pair in enumerate(match):
            if pair[0] not in predicates.keys():
                if idx != 0:
                    predicates[pair[0]] = pair[1].split(',')

    # Close files
    ifile.close()

    return predicates


def write_query_files(predicates, filename):
    combinations = get_combinations(predicates.keys())
    for idx, combination in enumerate(combinations):
        qfile = open(filename + '_' + str(idx) + '.txt', 'w')
        # TODO: find how to write parameters
        qfile.write('q()' + ' :- ' + ','.join(combination))
        qfile.close()


# Main method
def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:m:o:",["ifile=","mfile=","ofile="])
    except getopt.GetoptError:
        print 'mcdsat_queries.py -i <inputfile> -m <mappings> -o <outputfile>'
        sys.exit(2)
   
    for opt, arg in opts:
        if opt == '-h':
            print 'mcdsat_endec.py -i <inputfile> -m <mappings> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-m", "--mfile"):
            mappingsfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

if __name__ == "__main__":
    main(sys.argv[1:])
