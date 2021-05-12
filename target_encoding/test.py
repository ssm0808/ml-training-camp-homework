# coding:utf-8
# Author : Simon Shi
# FILE : test.py
# DATE : 2021/5/1 14:20

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import time
import numpy as np
import pandas as pd
from target_encoding_v1 import target_mean_v1
from target_encoding_v1 import target_mean_v2
from target_encoding_cython import target_mean_v3
from target_encoding_cython import target_mean_v4


def main():
    y = np.random.randint(2, size=(5000, 1))
    x = np.random.randint(10, size=(5000, 1))
    data = pd.DataFrame(np.concatenate([y, x], axis=1), columns=['y', 'x'])

    # v1
    start = time.time()
    result1 = target_mean_v1(data, 'y', 'x')
    print("result1: {0}".format(result1))
    end = time.time()
    time_v1 = end - start
    print("target_mean_v1 using time: {}s".format(time_v1))

    # v2
    start = time.time()
    result2 = target_mean_v2(data, 'y', 'x')
    print("result2: {0}".format(result2))
    end = time.time()
    time_v2 = end - start
    # print("target_mean_v2 using time: {0}s".format(time_v2))
    print("target_mean_v2 using time: {0}s, speed up: {1} with v1".format(time_v2, time_v1/time_v2))

    # # v3
    start = time.time()
    result3 = target_mean_v3(data, 'y', 'x')
    print("result3: {0}".format(result3))
    end = time.time()
    time_v3 = end - start
    print("target_mean_v3 using time: {0}s, speed up: {1} with v2".format(time_v3, time_v2/time_v3))

    # v4
    start = time.time()
    result4 = target_mean_v4(data, 'y', 'x')
    print("result4: {0}".format(result4))
    end = time.time()
    time_v4 = end - start
    print("target_mean_v4 using time: {0}s,speed up: {1} with v2".format(time_v4, time_v2/time_v4))

if __name__ == "__main__":
    main()

