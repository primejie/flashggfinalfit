#!/bin/bash

cd /afs/cern.ch/user/z/zhjie/CMSSW_10_2_13/src/flashggFinalFit/Combine

eval `scramv1 runtime -sh`

text2workspace.py Datacard.txt -o Datacard_mu_inclusive.root -m 125 higgsMassRange=122,128 