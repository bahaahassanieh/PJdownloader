import sys
import os
from socket import *
import getopt
try:
    import requests
except:
    print "Request library not found, please install it before proceeding\n"
    sys.exit()


print '''
                                                `/.
                                              `/hoho.
                                             .ohNMmys+-
                                           `/hdmdhhNMho.
                                         :yddmmmdhhdmMMNy+
                                       `/ydmdmmmy+oyhNhhhs/-
                                      -odddymhhmddNNmNsoss//+`
                                     `.-:+shhydNmmhmNhhhhdddhs/
                                     `-//:-`/yyh.d-:m+.`-..---`
                                               oo.h:s/`
                                             -+o//-::-/-


            `-    +:+  +`   --/.   `-:+s/   `:` .+   +:   `-./.     ./. . -    `+  `.   :
            :+`:  -d`  -s   `sy+sdNNdyo/:++oo/. yM+  mM-  oNsh/ -+oo/`  /d/    oMo  h  -M+
              ym+ :y:  +/:oymmhs+:`o` -+.   hy: -My  yMs  `   //:``y`   `d+    .Mh`.y+  Md
           -++- . .o`ohmhd/-`  ..  -` `      `.  N+  +M`  dd/ys   `ms   .o   ./oNmo/-   Mo
           ` yNyNh`o:/. +/    :dh   /NN.  :d.ss  yd  -M/  .NMh     :M.   o `d+:`+M` `o  mh
            ` -   --    mos        -d.oNdmdmNh.  /N  `My .d:oM: s`  d+  :.  :   .M. `+  hm
           `s y. oNMm.  +s-   -s.  omyhd:. `+    +h ` Nd shhNh` .   hd  do  .hNMMNhhhhhdhM`
           `y ` yd:`yNo:--:/smdmNdmmdMmN`  `ooydms``s dm  -o+    .omodmym+  `-/sdMMmho/./M.
            y+`yh -+ /ydmmds/`  --` .+h- `sdy+:.`-  - yy   oh+ohmd+`  :d:  -ymds/-`:`   -M.
             ods` y-     :myhm+ -//+.-y/sh:  -///`    o-   .oo+:`+ysd:.s.+hs: -d: /mh   -h
                  /.      :- -`       .:.   `.                   -/`-  :s/`    .        ``\n'''


def usage():
    comm = os.path.basename(sys.argv[0])
    if os.path.dirname(sys.argv[0]) == os.getcwd():
        comm = "./" + comm
    print "Usage: PJ downloader options \n"
    print "     -y: specify the year "
    print "     -i: specify the issue number "
    print "     -s: start page "
    print "     -e: end page "
    print "\nExamples:"
    print "        " + comm + " -y 2017 -i 35 -s 5928 -e 5942"


def start(argv):
    if len(sys.argv) < 4:
        usage()
        sys.exit()
    try:
        opts, args = getopt.getopt(argv, "y:i:s:e:")
    except getopt.GetoptError:
        usage()
        sys.exit()
    for opt, arg in opts:
        if opt == '-y':
            year = int(arg)
        elif opt == '-i':
            issue = int(arg)
        elif opt == '-s':
            startpage = int(arg)
        elif opt == '-e':
            endpage = int(arg)
    print "coping public journal (year: " + str(year) + " issue " + str(issue)+") from page:" + str(startpage) +" to page:"+ str(endpage) 
    for x in range(startpage, endpage):
        print "..."
        url = 'http://jo.pcm.gov.lb/j'+str(year)+'/j'+str(issue)+'/doc46/'+str(x)+'.gif'
        dir = "./issue " + str(issue) + "-" +str(year)
        if not os.path.exists(dir):
                os.makedirs(dir)
        with open(dir+"/"+str(x)+'.gif', 'wb') as f:
            f.write(requests.get(url).content)
    print "copied "+ str(endpage - startpage) + " pages :)"


if __name__ == "__main__":
    try:
        start(sys.argv[1:])
    except KeyboardInterrupt:
        print "Search interrupted by user.."
    except:
        sys.exit()
