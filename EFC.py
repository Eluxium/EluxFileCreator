import os
import sys, getopt

def main(argv):
    inputfile = None
    iconfile = None
    opts, args = getopt.getopt(argv,"hi:o:",["ifile=","icofile="])
    for opt, arg in opts:
        if opt == '-h':
            print ('pyinstaller.py -i <inputfile> -ico <iconfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-ico", "--icofile"):
            iconfile = arg
    print ('Input file is ', inputfile)
    print ('Output file is ', iconfile)
    hip = "--hidden-import"
    exeicon = "Elux"
    filename = "Elux"
    if inputfile != None:
        filename = inputfile
    if iconfile != None:
        exeicon = iconfile
        
    ha = "python "+"-m "+"PyInstaller "+"--onefile "+"--clean "+"--upx-dir=./tools "+"--distpath=./ --icon ./"+exeicon+f".ico ./{filename}.py"
    print(ha)
    os.system(ha)


if __name__ == "__main__":
   main(sys.argv[1:])
