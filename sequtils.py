#!/usr/bin/python
# vim: set fileencoding=utf-8 :

import itertools

"Reimplementation of some clojure-core functions"

def select_keys(dct, keys_to_extract):
  return dict([ (k,v) for k, v in dct.items() if k in keys_to_extract])

def select_values(dct, keys_to_extract):
  return [ v for k, v in dct.items() if k in keys_to_extract]

def remove_keys(dct, keys_to_extract):
  return dict([ (k,v) for k, v in dct.items() if k not in keys_to_extract])

def merge(*args):
  return dict([(k,v) for dct in args for k,v in dct.items()])

def translate_keys(dct, key_map):
  return dict([ (key_map.get(k,k), v) for k, v in dct.items() if k in key_map])

def select_and_translate_keys(dct, key_map):
  return translate_keys(select_keys(dct, key_map.keys()), key_map)

def nonempty(dct):
  return dict([ (k,v) for k,v in dct.items() if v or v == 0])

def no_empty_strings(dct):
  return dict([ (k,v) for k,v in dct.items() if v != ''])

def first(seq):
    return len(seq) > 0 and seq[0] or None

def last(seq):
    return len(seq) > 0 and seq[-1] or None

def different_keys(dct1, dct2):
  set1 = set(dct1.items())
  set2 = set(dct2.items())
  shared_keys = set1 & set2
  return set1.difference(set2) & set2.difference(set1)

def get_in(m, keys):
    if len(keys) == 1:
        return m[keys[0]]
    else:
        return get_in(m[keys[0]], keys[1:])

def makelist(x):
    """
    If list is passed it returns unchanged argument,
    otherwise creates list containing passed item
    """
    return isinstance(x, list) and x or [x]

def flatten(seq):
    """
    Returns list of slists fčattened as single level sequence
    """
    return list(itertools.chain.from_iterable(seq))
