import random
import argparse
#TODO: csv-to-line-by-line txt

parser = argparse.ArgumentParser(description = 'Random word selection. ')
parser.add_argument("-f", "--file", help="A txt or csv file of words you wish to select from")
parser.add_argument("-i", "--iter", help="The number of words you wish to select", type=int)
args = parser.parse_args()

if args.file == None:
    f=open("base.txt", "r")
else:
    try: 
        f = open(args.file, "r")
    except:
        print "Please provide a valid file in the same directory."
        print "Currently supported formats: txt, csv."
        quit()

if args.iter == None:
    j=1
else:
    j=args.iter
    
dex = list(f.read().splitlines())
f.close()

#Generate random number between 0 and len(dex)-1
i = 0
while i < j and len(dex)>0:
    x = random.choice(dex)
    print x
    dex.remove(x)
    i+=1
