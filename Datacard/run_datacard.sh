WhichSamples=${1}


if [ ${WhichSamples} -eq 0 ]
  then
    python RunYields.py --inputWSDirMap 2017=/eos/user/z/zhenxuan/hhwwgg_root/hhwwgg_root_SL/ws_gghh_M500 --sigModelWSDir /eos/user/z/zhenxuan/hhwwgg_root/hhwwgg_root_SL/ws_gghh_M500 --bkgModelWSDir /eos/user/z/zhenxuan/hhwwgg_root/hhwwgg_root_SL/ws --cats auto --procs auto --batch local --ext M500 >M500_SL_yields.log 2>&1
    python RunYields.py --inputWSDirMap 2017=/eos/user/z/zhenxuan/hhwwgg_root/hhwwgg_root_SL/ws_gghh_M1000 --sigModelWSDir /eos/user/z/zhenxuan/hhwwgg_root/hhwwgg_root_SL/ws_gghh_M1000 --bkgModelWSDir /eos/user/z/zhenxuan/hhwwgg_root/hhwwgg_root_SL/ws --cats auto --procs auto --batch local --ext M1000 >M1000_SL_yields.log 2>&1
    python RunYields.py --inputWSDirMap 2017=/eos/user/z/zhenxuan/hhwwgg_root/hhwwgg_root_SL/ws_gghh_M2000 --sigModelWSDir /eos/user/z/zhenxuan/hhwwgg_root/hhwwgg_root_SL/ws_gghh_M2000 --bkgModelWSDir /eos/user/z/zhenxuan/hhwwgg_root/hhwwgg_root_SL/ws --cats auto --procs auto --batch local --ext M2000 >M2000_SL_yields.log 2>&1
    python RunYields.py --inputWSDirMap 2017=/eos/user/z/zhenxuan/hhwwgg_root/hhwwgg_root_SL/ws_gghh_M3000 --sigModelWSDir /eos/user/z/zhenxuan/hhwwgg_root/hhwwgg_root_SL/ws_gghh_M3000 --bkgModelWSDir /eos/user/z/zhenxuan/hhwwgg_root/hhwwgg_root_SL/ws --cats auto --procs auto --batch local --ext M3000 >M3000_SL_yields.log 2>&1
   
fi
if [ ${WhichSamples} -eq 1 ]
  then
    python makeDatacard.py --years 2017 --prune --ext 'M500' --output Datacard_M500_SL
    python makeDatacard.py --years 2017 --prune --ext 'M1000' --output Datacard_M1000_SL
    python makeDatacard.py --years 2017 --prune --ext 'M2000' --output Datacard_M2000_SL
    python makeDatacard.py --years 2017 --prune --ext 'M3000' --output Datacard_M3000_SL
    
fi
if [ ${WhichSamples} -eq 2 ]
  then
    python cleanDatacard.py --datacard Datacard_M500_SL.txt --factor 2 --removeDoubleSided
    python cleanDatacard.py --datacard Datacard_M1000_SL.txt --factor 2 --removeDoubleSided
    python cleanDatacard.py --datacard Datacard_M2000_SL.txt --factor 2 --removeDoubleSided
    python cleanDatacard.py --datacard Datacard_M3000_SL.txt --factor 2 --removeDoubleSided
    
fi
if [ ${WhichSamples} -eq 3 ]
  then
    combineCards.py Datacard_M500_SL.txt > Datacard_combined_M500_SL.txt
    combineCards.py Datacard_M1000_SL.txt > Datacard_combined_M1000_SL.txt
    combineCards.py Datacard_M2000_SL.txt > Datacard_combined_M2000_SL.txt
    combineCards.py Datacard_M3000_SL.txt > Datacard_combined_M3000_SL.txt

fi
if [ ${WhichSamples} -eq 4 ]
  then
    combine -M AsymptoticLimits -m 125 -n M500 -t -1 --expectSignal=1 Datacard_M500_SL.txt >datacard_limits_M500.log 2>&1 
    combine -M AsymptoticLimits -m 125 -n M1000 -t -1 --expectSignal=1 Datacard_M1000_SL.txt >datacard_limits_M1000.log 2>&1 
    combine -M AsymptoticLimits -m 125 -n M2000 -t -1 --expectSignal=1 Datacard_M2000_SL.txt >datacard_limits_M2000.log 2>&1 
    combine -M AsymptoticLimits -m 125 -n M3000 -t -1 --expectSignal=1 Datacard_M3000_SL.txt >datacard_limits_M3000.log 2>&1 
    
fi
if [ ${WhichSamples} -eq 5 ]
  # move limit root file to eos to further analysis 
  then
    mv higgsCombineM500.AsymptoticLimits.mH125.root /eos/user/z/zhenxuan/hhwwgg_root/hhwwgg_root_SL/
    mv higgsCombineM1000.AsymptoticLimits.mH125.root /eos/user/z/zhenxuan/hhwwgg_root/hhwwgg_root_SL/
    mv higgsCombineM2000.AsymptoticLimits.mH125.root /eos/user/z/zhenxuan/hhwwgg_root/hhwwgg_root_SL/
    mv higgsCombineM3000.AsymptoticLimits.mH125.root /eos/user/z/zhenxuan/hhwwgg_root/hhwwgg_root_SL/
    
fi