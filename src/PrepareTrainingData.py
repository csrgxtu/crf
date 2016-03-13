#!/usr/bin/env python
# coding=utf8
#
# Author: Archer Reilly
# Date: 12/Mar/2016
# File: PrepareTrainingData.py
# Desc: preparing the training data for CRF++
#
# Format: each row is a token, consist of the following
# GameName HomeAway FGM FGA 3PM 3PA FTM FTA OREB DREB AST TOV STL BLK PF PTS WinLose
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

# print mat[0]
trainMat = []
for row in mat:
  tmp = []
  # GameName
  tmp.append()

  # HomeAway
  # FGM
  # FGA
  # 3PM
  # 3PA
  # FTM
  # FTA
  # OREB
  # DREB
  # AST
  # TOV
  # STL
  # BLK
  # PF
  # PTS
  # WinLose