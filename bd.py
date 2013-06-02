import sys
from datetime import datetime

def usage():
    print >>sys.stderr, "usage: %s [date]" % (sys.argv[0])
    sys.exit()

if len(sys.argv) == 1:
    usage()

birthday = ""
args = ' '.join(sys.argv[1:])
for f in ['%Y/%m/%d', '%Y-%m-%d', '%Y%m%d', '%d %B %Y', '%d %b %Y']:
    try:
        birthday = datetime.strptime(args, f)
    except ValueError:
        continue
    break

if birthday == "":
    print >>sys.stderr, "unsupported date format: %s" % (args)
    usage()

today = datetime.today()
y = ((today.year * 10000 + today.month * 100 + today.day) - (birthday.year * 10000 + birthday.month * 100 + birthday.day)) 
if y >= 0:
    months = (today.month - birthday.month) % 12
    years = y / 10000
    next_days = datetime(birthday.year + years + 1, birthday.month, birthday.day) - datetime(today.year, today.month, today.day)
    print "You are %d (and %d months) years old." % (years, months)
    print "Your next birthday is %d days later." % (next_days.days)
else:
    usage()

