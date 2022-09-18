#!/bin/bash

cd /afs/cern.ch/user/z/zhenxuan/CMSSW_10_6_20/src/flashggFinalFit/Combine

eval `scramv1 runtime -sh`

text2workspace.py Datacard_M300.txt -o Datacard_M300_mu_inclusive.root -m 125 higgsMassRange=122,128 