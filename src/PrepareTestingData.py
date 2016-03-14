#!/usr/bin/env python
# coding=utf8
#
# Author: Archer Reilly
# File: PrepareTestingData.py
# Date: 14/Mar/2016
# Desc: prepare testing data from the train file temply
#
# Produced By CSRGXTU
import sys
from Utility import loadCrfMatrixFromFile, saveCrfMatrix

if len(sys.argv) != 2:
  print 'Usage: PrepareTestingData.py teamid'
  sys.exit(1)

teamid = sys.argv[1]

DATA_PATH = '../data/TeamRank/'

mat = loadCrfMatrixFromFile(DATA_PATH + teamid + '.train.csv')

saveCrfMatrix(DATA_PATH + teamid + '.test.csv', mat[-63:])