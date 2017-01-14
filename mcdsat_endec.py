#!/usr/bin/python

import sys, getopt, re


def merge_dicts(*dict_args):
    """
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    """
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result


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


def generate_mappings(filename, mappings):
    """
    Generate all mappings for encoding from the views file
    """
    ifile = open(filename, 'r')
    mappings = open(mappings, 'w')
    
    # Get all function names and arguments
    allmatches = []
    for line in ifile:
        allmatches.append(explode(line))

    views = []
    funcs = []
    args = []
    for match in allmatches:
        for idx, pair in enumerate(match):
            if pair[0] not in funcs:
                if idx == 0:
                    views.append(pair[0])
                else:
                    funcs.append(pair[0])
            for arg in pair[1].split(','):
                if arg not in args:
                    args.append(arg)

    # Produce the mappings for all functions and arguments
    viewmappings = {}
    for idx, view in enumerate(views):
        viewmappings[view] = 'v' + str(idx)

    funcmappings = {}
    for idx, func in enumerate(funcs):
        funcmappings[func] = 'r' + str(idx + 1)

    argmappings = {}
    for idx, arg in enumerate(args):
        argmappings[arg] = 'X' + str(idx + 1)

    # Merge all dictionaries
    allmappings = merge_dicts(viewmappings, funcmappings, argmappings)
    
    # Write all mappings to a file
    for k, v in allmappings.iteritems():
        mappings.write(v + '=' + k + '\n')

    # Close files
    ifile.close()
    mappings.close()


def transform_file(inputf, mappings, outputf, encode=True):
    """
    Decode or encode files to be used with mcdsat
    """
    ifile = open(inputf, 'r')
    mappings = open(mappings, 'r')

    allmappings = dict(line.strip().split('=') for line in mappings)

    # Read views vile
    filedata = None
    with open(inputf, 'r') as file :
        filedata = file.read()

    # Replace all strings
    for k, v in allmappings.iteritems():
        if encode:
            filedata = filedata.replace(v, k)
        else:
            filedata = filedata.replace(k, v)

    # Write the file for mcdsat
    with open(outputf, 'aw') as file:
        file.write(filedata)
        file.close()

    # Close files
    ifile.close()
    mappings.close()


# Main method
def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"ha:i:m:o:",["action=","ifile=","mfile=","ofile="])
    except getopt.GetoptError:
        print 'mcdsat_endec.py -a <action> -i <inputfile> -m <mappings> -o <outputfile>'
        sys.exit(2)
   
    for opt, arg in opts:
        if opt == '-h':
            print 'mcdsat_endec.py -a <generate|encode|decode> -i <inputfile> -m <mappings> -o <outputfile>'
            sys.exit()
        elif opt in ("-a", "--action"):
            action = arg
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-m", "--mfile"):
            mappingsfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    if action == 'generate':
        generate_mappings(inputfile, mappingsfile)
    elif action == 'encode':
        transform_file(inputfile, mappingsfile, outputfile)
    elif action == 'decode':
        transform_file(inputfile, mappingsfile, outputfile, False)

if __name__ == "__main__":
   main(sys.argv[1:])





