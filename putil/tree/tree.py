#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# a test for traverse directory

__author__ = 'AlbertS'

import os
import os.path


def tree(path, max_depth: int = None, dir_only=True, ignore: set = None, depth=1):
    if ignore is None:
        ignore = set()
    if max_depth is not None:
        if depth > max_depth:
            return
    if depth == 0:
        print("root:[" + path + "]")

    for item in os.listdir(path):
        # filter, complete matching
        if item in ignore:
            continue
        else:
            newitem = path + '/' + item
            if os.path.isdir(newitem):
                print("| " * depth + "+--" + item)
                tree(newitem, max_depth, dir_only, ignore, depth + 1)
            elif dir_only:
                pass
            else:  # print filename
                print("| " * depth + "+--" + item)


if __name__ == '__main__':
    ignore = open(r'tree_ignore.txt', 'r').read().split('\n')
    ignore = set(ignore)
    tree('.', 3, ignore=ignore)
