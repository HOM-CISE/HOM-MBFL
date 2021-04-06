#!/usr/bin/env python3
# -*- coding: utf-8 -*-\

def _getnext(a,a_next):
    al = len(a)
    a_next[0] = -1
    k = -1
    j = 0
    while j < al-1:
        if k == -1 or a[j] == a[k]:
            j += 1
            k += 1
            a_next[j] = k
        else:
            k = a_next[k]

def _kmpSearchIndex(a,b,a_next):
    i = j = 0
    al = len(a)
    bl = len(b)
    while i < al and j < bl:
        if j == -1 or a[i] == b[j]:
            i += 1
            j += 1
        else:
            j = a_next[j]
    if j == bl:
        return True
    else:
        return False

def _kmpSearchList(a, b, a_next):
    i = j = 0
    al = len(a)
    bl = len(b)
    ans = []
    num = 0
    while i < al:
        j = 0;
        while i < al and j < bl:
            if j == -1 or a[i] == b[j]:
                i += 1
                j += 1
            else:
                j = a_next[j]

        if j == bl:
            i = i - j
            ans.append(i);
            i = i + 1
    return ans;

def isFind(a,b):
    '''

    :param a:(type:str) a is a main string.
    :param b:(type:str) b is a sub string.
    :return:(type:bool) return True if the search is successful, otherwise return False
    '''
    #a = 'ABABCABDABBGAFDSBVSABDABB'
    #b = 'E'

    #a=input()
    #b=input()
    a_next = [0]*len(b)
    _getnext(b,a_next)
    t = _kmpSearchIndex(a,b,a_next)
    return t

def findIndex(a, b):
    '''

    :param a:(type:str) a is a main string.
    :param b:(type:str) b is a sub string.
    :return:(type:list) return all matching indexes
    '''
    # a = 'ABABCABDABBGAFDSBVSABDABB'
    # b = 'ABDABB'
    a_next = [0] * len(b)
    _getnext(b, a_next)
    t = _kmpSearchList(a, b, a_next)

    return t

def replaceOnce(mainstr, substr, replace_str):
    '''

    :param mainstr:(type:str) mainstr is a main string.
    :param substr:(type:str) substr is a sub string.
    :param replace_str:(type:str) replace_str is a replace string.
    :return:(type:list) return all strings that have been replaced only once.
    '''
    result_list = []

    replace_index = findIndex(mainstr, substr)
    for index in replace_index:
        temp_list = [mainstr[:index], mainstr[index + len(substr):]]
        result_str = replace_str.join(temp_list)
        result_list.append(result_str)

    return result_list

# compare two file
def isFileEqual(filename1, filename2):
    first_file = open(filename1)
    second_file = open(filename2)

    first_data = first_file.readlines()
    second_data = second_file.readlines()

    f_data = str(first_data).split('\n')
    s_data = str(second_data).split('\n')
    if len(f_data) != len(s_data):
        return False
    else:
        for i in range(len(f_data)):
            if f_data[i] != s_data[i]:
                return False
    return True
