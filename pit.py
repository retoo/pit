#!/usr/bin/python

from subprocess import call
import os 
import sys

args = list(sys.argv)
command = os.path.basename(args.pop(0))

cmds = None

if command == "pci":
    ''' commits changes and pushes them'''
    cmds = [
        ['git', 'ci'] + args,
        ['git', 'push']]
elif command == "pup":
    ''' updates the working dir by rebasing local changes to upstream's head '''
    cmds = [
        ['git', 'pull', '--rebase'] + args]
else:
    print "unknown cmd: '%s'" % repr(command)
    sys.exit(99)


for cmd in cmds:
    print " ".join(cmd)
    ret = call(cmd)

    if ret != 0:
        sys.exit(ret)

