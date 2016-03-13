#!/usr/bin/env python
# coding=utf8
#
# Author: Archer Reilly
# Date: 12/Mar/2016
# File: PrepareTrainingData.py
# Desc: preparing the training data for CRF++
#
# Produced By CSRGXTU
from Utility import loadSeasons

seasons = loadSeasons("../data/TeamRank/seasons.csv")
print seasons