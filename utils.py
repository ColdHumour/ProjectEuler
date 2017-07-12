# -*- coding: utf-8 -*-

"""
utils.py

Utility functions using to analysis and evaluate solutions
Function list:
    timepast
    memoize
    clear_cython_cache
    find_solution

@author: Jasper Wu
"""

import os
import shutil
import webbrowser


def timepast(func):
    import time

    def _deco(*args, **kwargs):
        t = time.time()
        ret = func(*args, **kwargs)
        print("Time consumed by {0}(): {1:.2f}s".format(func.__name__, time.time() - t))
        return ret
    return _deco


def memoize(cache=None, key=lambda x: x):
    if cache is None:
        raise ValueError("cache must be an existed dict!")

    def _deco1(func):
        def _deco2(*args, **kw):
            idx = key(args)
            if idx not in cache:
                cache[idx] = func(*args, **kw)
            return cache[idx]
        return _deco2
    return _deco1


def clear_cython_cache(url="C:\\Users\\wuyd\\.ipython\\cython"):
    if os.path.exists(url):
        for f in os.listdir(url):
            filepath = os.path.join(url, f)
            if '.' in f:
                os.remove(filepath)
            else:
                shutil.rmtree(filepath)
    else:
        raise ValueError("Bad cython cache URL!")


def find_solution(id):
    if id % 10 == 0:
        lid, rid = id-9, id
    else:
        lid, rid = id // 10 * 10 + 1, id // 10 * 10 + 10
    webbrowser.open('http://htmlpreview.github.io/?https://github.com/ColdHumour/ProjectEulerSolutions/blob/master/Solutions%20{}-{}.html#{}'.format(lid, rid, id))
