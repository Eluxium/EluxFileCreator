import os
import sys, getopt

def main(argv):
    inputfile = None
    iconfile = None
    opts, args = getopt.getopt(argv,"hi:o:",["ifile=","icofile="])
    for opt, arg in opts:
        if opt == '-h':
            print ('EFC.py -i <inputfile> -ico <iconfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-ico", "--icofile"):
            iconfile = arg
    print ('Input file is ', inputfile)
    print ('Output file is ', iconfile)
    exeicon = "Elux"
    file = "./Elux.py"
    if inputfile != None:
        file = inputfile
    if iconfile != None:
        exeicon = iconfile
        
    
    ha = "python "+"-m "+"PyInstaller "+"--onefile "+"--clean "+"--upx-dir=./tools "+"--distpath=./ --icon ./"+exeicon+f".ico {file}"
    #CTK ha = "python "+"-m "+"PyInstaller "+"--onefile "+"--clean "+"--add-data \"%localappdata%/Programs/Python/Python310/Lib/site-packages/customtkinter;customtkinter/\" --upx-dir=./tools "+"--distpath=./ --icon ./"+exeicon+f".ico {file}"
    print(ha)
    os.system(ha)


if __name__ == "__main__":
   main(sys.argv[1:])
