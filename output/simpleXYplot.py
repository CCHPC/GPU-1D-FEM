#!/usr/bin/python

import sys, getopt
import numpy as np
import matplotlib.pyplot as plt

def main(argv):

    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:o:t:h", ["help", "infile=","outfile=","tsv="])

        if len(opts) == 0:
            print ('usage: simpleXYplot.py -i <first xy plot file name> -i <second xy file> ... -t <tab separated data file> -o <plot file name>')
            sys.exit(2)
        
    except getopt.GetoptError as err:
        # print help information and exit:
        sys.stderr.write("%s: %s\n" % (sys.argv[0], "Unknown option"))
        sys.stderr.write("Usage: `%s -help' for more information\n" % sys.argv[0])
        sys.exit(2)

    infile = ''
    outfile = ''
    var = ''

    Exact = []

    for o, a in opts:
        if o in ("-h", "-help"):
            print( 'simpleXYplot.py -i <inputfile> -t <tab separated data file> -o <outputfile>')
            sys.exit(0)
        elif o in ("-i", "-infile"):
            infile = a
            varnameParts = a.split('.')
            var = varnameParts[0]
            print( 'Input file is: ', infile)

            # read the first line with the variable names for each column
            f  = open(infile)
            firstline = f.readline()
            f.close()
            varnames = firstline.split(' ')

            data = np.loadtxt(infile, skiprows=1)
            col = 1
            #print ( 'firstline: ', varnames[0], varnames[1], varnames[2])

            for column in data[:,1:].T:
                plt.plot(data[0:,0], column[0:], label=varnames[col])
                col = col + 1
        elif o in ("-t", "-tsv"):
            # Read Paraview exported tsv file; first line has var names
            infile = a
            f  = open(infile)
            firstline = f.readline()
            f.close()
            
            X, rho, E, FVE, Ind, mx = np.loadtxt(infile, unpack=True, skiprows=1)

            ux = mx/rho
            sie = E/rho - ux*ux/2
            P = (5./3. - 1.)*(E - rho*ux*ux/2.)
            
            plt.plot(X, rho, label='rho')
            plt.plot(X, E,   label='E')
            plt.plot(X, FVE, label='FVE')
            plt.plot(X, Ind, label='Ind')
            plt.plot(X, ux,  label='ux')
            plt.plot(X, sie, label='sie')
            plt.plot(X, P,   label='P')

        elif o in ("-o", "-outfile"):
            outfile = a
            print( 'Output file is: ', outfile)


    plt.xlabel(varnames[0])  
    plt.legend()
    
    if outfile != '':
        plt.savefig(outfile)  

    plt.show()
    
if __name__ == "__main__":
   main(sys.argv[1:])

