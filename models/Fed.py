#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python version: 3.6

import copy

import torch


def FedAvg(w):
    # parameter w is a list of dict which includes different clients' parameters: key-value
    w_avg = copy.deepcopy(w[0])
    # for the same key, average directly ignoring the proportion of the data
    for k in w_avg.keys():
        for i in range(1, len(w)):
            w_avg[k] += w[i][k]
        w_avg[k] = torch.div(w_avg[k], len(w))
    return w_avg
