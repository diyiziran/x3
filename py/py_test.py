#!/usr/bin/env python
# -*- coding: utf-8 -*-
#


print ([x*x for x in range(1,10) if x%2==0])


def count(m):
    fs = []
    for i in range(1, m):
        def f():
             return i*i
        fs.append(f)
    return fs

print (count(6))


http://f.apiplus.net/ssq.json