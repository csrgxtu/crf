#!/usr/bin/env python
# coding=utf8
#
# Author: Archer Reilly
# Date: 12/Mar/2016
# File: PrepareTrainingData.py
# Desc: preparing the training data for CRF++
#
# Produced By CSRGXTU
import sys

from Utility import loadMatrixFromFile

if len(sys.argv) != 2:
  print 'Usage: PrepareTrainingData.py teamid'
  sys.exit(1)

teamid = sys.argv[1]

DATA_PATH = '../data/TeamRank/'

mat = loadMatrixFromFile(DATA_PATH + teamid + '.csv.sorted')

print mat[0]