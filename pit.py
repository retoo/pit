#!/usr/bin/python

# Installation
#  Add ~/bin/ to your path 
#  ln -s $PATH_TO_PIT ~/bin/pci
#  ln -s $PATH_TO_PIT ~/bin/pup
#  ln -s $PATH_TO_PIT ~/bin/psh
#  ln -s $PATH_TO_PIT ~/bin/pst
#  ln -s $PATH_TO_PIT ~/bin/prc


# Usage:
#  pci <files>: commits changes and pushes the changes
#   -> if it aborts due to 'non-fastforward' erros do a `pup`, 
#      fix conflicts if any, and then `psh` the changes
#      IMPORTANT: do a `prc <conflict-files>` before you `psh` 
#                 if you had any conflict,
#         (git rebase --continue)
#  pup: updates the local working dir by rebasing any uncommited
#       changes to the lasted verson from the repo
#  psh: push all changes to the remote repo
#  prc: marks all conflicts as resolved

from subprocess import call
import os 
import sys

args = list(sys.argv)
command = os.path.basename(args.pop(0))

cmds = None

if command == "pci":
    ''' commits changes and pushes them'''
    cmds = [
        ['git', 'commit'] + args,
        ['git', 'push']]
elif command == "pup":
    ''' updates the working dir by rebasing local changes to upstream's head '''
    cmds = [
        ['git', 'pull', '--rebase'] + args]
elif command == "psh":
    cmds = [
        ['git', 'push']]
elif command == "pst":
    cmds = [
        ['git', 'status']]
elif command == "prc":
    if not args:
        print "Please specify which files have resolved conflicts (see `pst`)"
        sys.exit(99)
    cmds = [
        ['git', 'add'] + args
        ['git', 'rebase', '--continue']]
else:
    print "unknown cmd: '%s'" % repr(command)
    sys.exit(99)

for cmd in cmds:
    print " ".join(cmd)
    ret = call(cmd)

    if ret != 0:
        sys.exit(ret)

