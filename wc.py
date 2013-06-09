import sys
import re

optW = False  # -a Option Flag

argvs = sys.argv

for argv in sys.argv:
  if argv.startswith("-"):
      if argv.find("w") != -1:
        optW = True
      argvs.remove(argv)

argc = len(argvs)

if argc == 1: 
    f = sys.stdin
elif argc == 2:
    try:
        f = open(sys.argv[1], "rU")
    except IOError:
        print >>sys.stderr, "wc: %s: No such file or directory" % (sys.argv[1])
        sys.exit()
else:
    print >>sys.stderr, "usage: wc [file]"
    sys.exit()

s = f.read()
f.close()

words = s.split()

d = {}

p = re.compile(r'[a-z|A-Z]+')

for word in words:
    tmp = p.search(word)
    if tmp == None:
        continue
    w = tmp.group().lower()
    if w == "":
        continue
    if d.has_key(w):
        d[w] += 1
    else: 
        d[w] = 1

if optW:
    sorted_keys = sorted(d.keys())
else:
    sorted_keys = sorted(d.keys(), key = lambda x: d[x], reverse = True)

print "all: %d" % len(d)

i = 0
for k in sorted_keys:
    if i == 20:
        break
    print k, ": ", d[k]
    i += 1
