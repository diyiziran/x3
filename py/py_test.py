#!/usr/bin/env python
# -*- coding: utf-8 -*-
#


print [x*x for x in xrange(1,10) if x%2==0]


def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

counter=4
print counter


