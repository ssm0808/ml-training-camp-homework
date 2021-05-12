# distutils: language=c++
# coding:utf-8
# Author : Simon Shi
# FILE : target_encoding_cython.pyx
# DATE : 2021/5/1 13:40

#include <unordered_map>
#include <map>
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
cimport numpy as np

cpdef target_mean_v3(data, y_name, x_name):
    cdef long nrow = data.shape[0]
    cdef np.ndarray[double] result = np.asfortranarray(np.zeros(nrow), dtype=np.float64)
    cdef np.ndarray[double] y = np.asfortranarray(data[y_name], dtype=np.float64)
    cdef np.ndarray[double] x = np.asfortranarray(data[x_name], dtype=np.float64)

    target_mean_v3_impl(result, y, x, nrow)
    return result

cdef void target_mean_v3_impl(double[:] result, double[:] y, double[:] x, const long nrow):
    cdef dict value_dict = dict()
    cdef dict count_dict = dict()

    cdef long i
    for i in range(nrow):
        if x[i] not in value_dict.keys():
            value_dict[x[i]] = y[i]
            count_dict[x[i]] = 1
        else:
            value_dict[x[i]] += y[i]
            count_dict[x[i]] += 1

    i=0
    for i in range(nrow):
        result[i] = (value_dict[x[i]] - y[i])/(count_dict[x[i]]-1)


cpdef target_mean_v4(data, y_name, x_name):
    cdef int nrow = data.shape[0]
    cdef np.ndarray[float] result = np.asfortranarray(np.zeros(nrow), dtype=np.float32)
    cdef np.ndarray[float] y = np.asfortranarray(data[y_name], dtype=np.float32)
    cdef np.ndarray[int] x = np.asfortranarray(data[x_name], dtype=np.int32)

    target_mean_v4_impl(result, y, x, nrow)
    return result

cdef void target_mean_v4_impl(float[:] result, float[:] y, int[:] x, const int nrow):
    unordered_map<int, float> value_dict
    unordered_map<int, float> count_dict

    cdef int i
    for i from 0 <= i < nrow by 1:
        if x[i] not in value_dict.keys():
            value_dict[x[i]] = y[i]
            count_dict[x[i]] = 1
        else:
            value_dict[x[i]] += y[i]
            count_dict[x[i]] += 1

    i = 0
    for i from 0 <= i < nrow by 1:
        result[i] = (value_dict[x[i]] - y[i])/(count_dict[x[i]] - 1)


if __name__ == "__main__":
    pass

