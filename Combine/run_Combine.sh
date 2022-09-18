WhichSamples=${1}


if [ ${WhichSamples} -eq 0 ]
  then
  python RunText2Workspace
fi
if [ ${WhichSamples} -eq 1 ]
  then
    python RunText2Workspace.py --mode mu_inclusive --batch local --ext _M300
fi
if [ ${WhichSamples} -eq 2 ]
  then
  python RunFits.py --inputJson inputs.json --mode mu_inclusive --batch condor
fi
if [ ${WhichSamples} -eq 3 ]
  then
   python CollectFits.py --inputJson inputs.json --mode mu_inclusive
fi
if [ ${WhichSamples} -eq 4 ]
  then
   python CollectFits.py --inputJson inputs.json --mode mu_inclusive
fi