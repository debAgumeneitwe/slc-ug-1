#!/usr/bin/env python
#-*-coding: utf-8 -*-

def words(file):
    word_count = {}
    for word in file.split():
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
    
     
    
    
