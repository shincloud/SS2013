import os, sys, time, stat, pwd, grp

def get_mode(mode):
    if stat.S_ISDIR(mode): r = 'd'
    else:                  r = '-'
    mode = stat.S_IMODE(mode)
    for p in [mode >> 6, mode >> 3, mode]:
        p &= 7
        s = ['-'] * 3
        if p & 4: s[0] = 'r'
        if p & 2: s[1] = 'w'
        if p & 1: s[2] = 'x'
        r += ''.join(s)
    return r

def print_filename(f, p):
    if all == False and f[0] == '.':
        return

    st = os.stat(os.path.join(p, f))

    if inode: i = "%10d " % (st.st_ino)
    else:     i = ""

    if long:
        m = get_mode(st.st_mode)
        u = pwd.getpwuid(st.st_uid).pw_name
        g = grp.getgrgid(st.st_gid).gr_name
        t = time.strftime('%b %d %H:%m', time.localtime(st.st_mtime))
        print "%s%s %2d %8s %8s %8d %s %s" % (i, m, st.st_nlink, u, g, st.st_size, t, f)
    else: 
        print "%s%s" % (i, f)

def ls(p, v = False):
    if os.path.isdir(p):
        if v: print "%s:" % (p)
        filelist = os.listdir(p)
        for f in filelist:
            print_filename(f, p)
    elif os.path.isfile(p):
        print_filename(p, '')
    else:
        print >>sys.stderr, "%s: %s: No such file or directory" % (sys.argv[0], p)

all = inode = long = False
path = []
for a in sys.argv[1:]:
    if a[0] != '-':
        path.append(a)
    else: 
        if a.find('a') != -1: all = True
        if a.find('i') != -1: inode = True
        if a.find('l') != -1: long = True

n = len(path) 
if n == 0: ls('.')
if n == 1: ls(path[0])
else:
    for p in path: 
        ls(p, True)
