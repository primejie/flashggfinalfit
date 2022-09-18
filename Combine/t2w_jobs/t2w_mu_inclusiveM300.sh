#!/bin/bash

cd /afs/cern.ch/user/z/zhenxuan/CMSSW_10_6_20/src/flashggFinalFit/Combine

eval `scramv1 runtime -sh`

text2workspace.py DatacardM300.txt -o DatacardM300_mu_inclusive.root -m 125 higgsMassRange=122,128 