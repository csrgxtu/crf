#!/usr/bin/env python
# coding=utf8
#
# Author: Archer Reilly
# Date: 12/Mar/2016
# File: PrepareTrainingData.py
# Desc: preparing the training data for CRF++
#
# Produced By CSRGXTU
from Utility import loadSeasons, loadTeamIds

DATA_PATH = '../data/TeamRank/'

seasons = loadSeasons(DATA_PATH + 'seasons.csv')
# print seasons

teams = loadTeamIds(DATA_PATH + 'teamidshortname.csv')
# print teams

files = []
for team in teams:
  for season in seasons:
    files.append(DATA_PATH + team + '.csv.sorted.' + season + '.csv')

print files