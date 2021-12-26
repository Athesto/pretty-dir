#!/usr/bin/python3
"""
pdir is a pretty print function for the dir() command
"""
from cmd import Cmd
from re import match
import os


def pdir(data=None, opt=""):
    '''
    NAME:
        pdir - a pretty print for dir() command

    SYNOPSIS:
        pdir(data, [opt])

    ARGS:
        @data: is any object
        @opt: it could be None, 'public', 'privated', 'dunder'/'magic'
            or 'protected'. it set a blue color for dunder function and
            a light blue for protected function

    RETURN:
        It will print the dir command as ls in the shell
    '''

    if data is None:
        print("welcome to pdir, please use this syntax pdir(data, [opt])")
        return

    if type(opt) is not str:
        print("opt must be a string")

    re_public = r"^[^_].*"
    re_protec = r"^[_][^_].*"
    re_dunder = r"^[_][_].*[_][_]$|_"
    re_privat = r"^[_][_].*[^_][^_]$"

    public, private, protected, dunder, other = ([] for _ in range(5))

    list_dir = dir(data)
    for element in list_dir:
        if (match(re_public, element)):
            public.append(element)
        elif (match(re_privat, element)):
            private.append(element)
        elif (match(re_protec, element)):
            protected.append(element)
        elif (match(re_dunder, element)):
            dunder.append(element)
        else:
            other.append(element)

    a = list_dir
    b = public + protected + private + dunder
    if len(a) != len(b):
        print("regex error")
        print(sorted(a))
        print(sorted(b))
        print(other)
        print("len a: ", len(a))
        print("len b: ", len(b))
        return

    public = ["\033[{}m{}\033[m".format(00, x) for x in public]
    private = ["\033[{}m{}\033[m".format(00, x) for x in private]
    protected = ["\033[{}m{}\033[m".format(94, x) for x in protected]
    dunder = ["\033[{}m{}\033[m".format(34, x) for x in dunder]

    if opt == 'public':
        out = public
    elif opt == 'private':
        out = private
    elif opt == 'protected':
        out = protected
    elif opt in ('dunder', 'magic'):
        out = dunder
    elif opt == "":
        out = dunder + private + protected + public
    else:
        print("please use [public, private, protected, dunder/magic] as str")
        return

    rows, columns = os.popen('stty size', 'r').read().split()
    columns = int(columns)
    terminal = Cmd()
    terminal.columnize(out, displaywidth=columns)
