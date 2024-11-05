WhichSamples=${1}


if [ ${WhichSamples} -eq 0 ]
  then
    python RunYields.py --inputWSDirMap 2017=/eos/user/z/zhjie/finlafit/ws_gghh_M1000_cat0 --sigModelWSDir /eos/user/z/zhjie/finlafit/ws_gghh_M1000_cat0 --bkgModelWSDir /eos/user/z/zhjie/finlafit/ws_cat0 --cats auto --procs auto --batch local --ext M1000_cat0 >M500_SL_yields.log 2>&1
    python RunYields.py --inputWSDirMap 2017=/eos/user/z/zhjie/finlafit/ws_gghh_M1500_cat0 --sigModelWSDir /eos/user/z/zhjie/finlafit/ws_gghh_M1500_cat0 --bkgModelWSDir /eos/user/z/zhjie/finlafit/ws_cat0 --cats auto --procs auto --batch local --ext M1500_cat0 >M500_SL_yields.log 2>&1
    python RunYields.py --inputWSDirMap 2017=/eos/user/z/zhjie/finlafit/ws_gghh_M2000_cat0 --sigModelWSDir /eos/user/z/zhjie/finlafit/ws_gghh_M2000_cat0 --bkgModelWSDir /eos/user/z/zhjie/finlafit/ws_cat0 --cats auto --procs auto --batch local --ext M2000_cat0 >M500_SL_yields.log 2>&1
    python RunYields.py --inputWSDirMap 2017=/eos/user/z/zhjie/finlafit/ws_gghh_M2500_cat0 --sigModelWSDir /eos/user/z/zhjie/finlafit/ws_gghh_M2500_cat0 --bkgModelWSDir /eos/user/z/zhjie/finlafit/ws_cat0 --cats auto --procs auto --batch local --ext M2500_cat0 >M500_SL_yields.log 2>&1
    python RunYields.py --inputWSDirMap 2017=/eos/user/z/zhjie/finlafit/ws_gghh_M3000_cat0 --sigModelWSDir /eos/user/z/zhjie/finlafit/ws_gghh_M3000_cat0 --bkgModelWSDir /eos/user/z/zhjie/finlafit/ws_cat0 --cats auto --procs auto --batch local --ext M3000_cat0 >M500_SL_yields.log 2>&1
    
    python RunYields.py --inputWSDirMap 2017=/eos/user/z/zhjie/finlafit/ws_gghh_M1000_cat1 --sigModelWSDir /eos/user/z/zhjie/finlafit/ws_gghh_M1000_cat1 --bkgModelWSDir /eos/user/z/zhjie/finlafit/ws_cat1 --cats auto --procs auto --batch local --ext M1000_cat1 >M500_SL_yields.log 2>&1
    python RunYields.py --inputWSDirMap 2017=/eos/user/z/zhjie/finlafit/ws_gghh_M1500_cat1 --sigModelWSDir /eos/user/z/zhjie/finlafit/ws_gghh_M1500_cat1 --bkgModelWSDir /eos/user/z/zhjie/finlafit/ws_cat1 --cats auto --procs auto --batch local --ext M1500_cat1 >M500_SL_yields.log 2>&1
    python RunYields.py --inputWSDirMap 2017=/eos/user/z/zhjie/finlafit/ws_gghh_M2000_cat1 --sigModelWSDir /eos/user/z/zhjie/finlafit/ws_gghh_M2000_cat1 --bkgModelWSDir /eos/user/z/zhjie/finlafit/ws_cat1 --cats auto --procs auto --batch local --ext M2000_cat1 >M500_SL_yields.log 2>&1
    python RunYields.py --inputWSDirMap 2017=/eos/user/z/zhjie/finlafit/ws_gghh_M2500_cat1 --sigModelWSDir /eos/user/z/zhjie/finlafit/ws_gghh_M2500_cat1 --bkgModelWSDir /eos/user/z/zhjie/finlafit/ws_cat1 --cats auto --procs auto --batch local --ext M2500_cat1 >M500_SL_yields.log 2>&1
    python RunYields.py --inputWSDirMap 2017=/eos/user/z/zhjie/finlafit/ws_gghh_M3000_cat1 --sigModelWSDir /eos/user/z/zhjie/finlafit/ws_gghh_M3000_cat1 --bkgModelWSDir /eos/user/z/zhjie/finlafit/ws_cat1 --cats auto --procs auto --batch local --ext M3000_cat1 >M500_SL_yields.log 2>&1
    
    python RunYields.py --inputWSDirMap 2017=/eos/user/z/zhjie/finlafit/ws_gghh_M1000_cat2 --sigModelWSDir /eos/user/z/zhjie/finlafit/ws_gghh_M1000_cat2 --bkgModelWSDir /eos/user/z/zhjie/finlafit/ws_cat2 --cats auto --procs auto --batch local --ext M1000_cat2 >M500_SL_yields.log 2>&1
    python RunYields.py --inputWSDirMap 2017=/eos/user/z/zhjie/finlafit/ws_gghh_M1500_cat2 --sigModelWSDir /eos/user/z/zhjie/finlafit/ws_gghh_M1500_cat2 --bkgModelWSDir /eos/user/z/zhjie/finlafit/ws_cat2 --cats auto --procs auto --batch local --ext M1500_cat2 >M500_SL_yields.log 2>&1
    python RunYields.py --inputWSDirMap 2017=/eos/user/z/zhjie/finlafit/ws_gghh_M2000_cat2 --sigModelWSDir /eos/user/z/zhjie/finlafit/ws_gghh_M2000_cat2 --bkgModelWSDir /eos/user/z/zhjie/finlafit/ws_cat2 --cats auto --procs auto --batch local --ext M2000_cat2 >M500_SL_yields.log 2>&1
    python RunYields.py --inputWSDirMap 2017=/eos/user/z/zhjie/finlafit/ws_gghh_M2500_cat2 --sigModelWSDir /eos/user/z/zhjie/finlafit/ws_gghh_M2500_cat2 --bkgModelWSDir /eos/user/z/zhjie/finlafit/ws_cat2 --cats auto --procs auto --batch local --ext M2500_cat2 >M500_SL_yields.log 2>&1
    python RunYields.py --inputWSDirMap 2017=/eos/user/z/zhjie/finlafit/ws_gghh_M3000_cat2 --sigModelWSDir /eos/user/z/zhjie/finlafit/ws_gghh_M3000_cat2 --bkgModelWSDir /eos/user/z/zhjie/finlafit/ws_cat2 --cats auto --procs auto --batch local --ext M3000_cat2 >M500_SL_yields.log 2>&1
    
    python RunYields.py --inputWSDirMap 2017=/eos/user/z/zhjie/finlafit/ws_gghh_M1000_cat3 --sigModelWSDir /eos/user/z/zhjie/finlafit/ws_gghh_M1000_cat3 --bkgModelWSDir /eos/user/z/zhjie/finlafit/ws_cat3 --cats auto --procs auto --batch local --ext M1000_cat3 >M500_SL_yields.log 2>&1
    python RunYields.py --inputWSDirMap 2017=/eos/user/z/zhjie/finlafit/ws_gghh_M1500_cat3 --sigModelWSDir /eos/user/z/zhjie/finlafit/ws_gghh_M1500_cat3 --bkgModelWSDir /eos/user/z/zhjie/finlafit/ws_cat3 --cats auto --procs auto --batch local --ext M1500_cat3 >M500_SL_yields.log 2>&1
    python RunYields.py --inputWSDirMap 2017=/eos/user/z/zhjie/finlafit/ws_gghh_M2000_cat3 --sigModelWSDir /eos/user/z/zhjie/finlafit/ws_gghh_M2000_cat3 --bkgModelWSDir /eos/user/z/zhjie/finlafit/ws_cat3 --cats auto --procs auto --batch local --ext M2000_cat3 >M500_SL_yields.log 2>&1
    python RunYields.py --inputWSDirMap 2017=/eos/user/z/zhjie/finlafit/ws_gghh_M2500_cat3 --sigModelWSDir /eos/user/z/zhjie/finlafit/ws_gghh_M2500_cat3 --bkgModelWSDir /eos/user/z/zhjie/finlafit/ws_cat3 --cats auto --procs auto --batch local --ext M2500_cat3 >M500_SL_yields.log 2>&1
    python RunYields.py --inputWSDirMap 2017=/eos/user/z/zhjie/finlafit/ws_gghh_M3000_cat3 --sigModelWSDir /eos/user/z/zhjie/finlafit/ws_gghh_M3000_cat3 --bkgModelWSDir /eos/user/z/zhjie/finlafit/ws_cat3 --cats auto --procs auto --batch local --ext M3000_cat3 >M500_SL_yields.log 2>&1
    
    python RunYields.py --inputWSDirMap 2017=/eos/user/z/zhjie/finlafit/ws_gghh_M1000_cat4 --sigModelWSDir /eos/user/z/zhjie/finlafit/ws_gghh_M1000_cat4 --bkgModelWSDir /eos/user/z/zhjie/finlafit/ws_cat4 --cats auto --procs auto --batch local --ext M1000_cat4 >M500_SL_yields.log 2>&1
    python RunYields.py --inputWSDirMap 2017=/eos/user/z/zhjie/finlafit/ws_gghh_M1500_cat4 --sigModelWSDir /eos/user/z/zhjie/finlafit/ws_gghh_M1500_cat4 --bkgModelWSDir /eos/user/z/zhjie/finlafit/ws_cat4 --cats auto --procs auto --batch local --ext M1500_cat4 >M500_SL_yields.log 2>&1
    python RunYields.py --inputWSDirMap 2017=/eos/user/z/zhjie/finlafit/ws_gghh_M2000_cat4 --sigModelWSDir /eos/user/z/zhjie/finlafit/ws_gghh_M2000_cat4 --bkgModelWSDir /eos/user/z/zhjie/finlafit/ws_cat4 --cats auto --procs auto --batch local --ext M2000_cat4 >M500_SL_yields.log 2>&1
    python RunYields.py --inputWSDirMap 2017=/eos/user/z/zhjie/finlafit/ws_gghh_M2500_cat4 --sigModelWSDir /eos/user/z/zhjie/finlafit/ws_gghh_M2500_cat4 --bkgModelWSDir /eos/user/z/zhjie/finlafit/ws_cat4 --cats auto --procs auto --batch local --ext M2500_cat4 >M500_SL_yields.log 2>&1
    python RunYields.py --inputWSDirMap 2017=/eos/user/z/zhjie/finlafit/ws_gghh_M3000_cat4 --sigModelWSDir /eos/user/z/zhjie/finlafit/ws_gghh_M3000_cat4 --bkgModelWSDir /eos/user/z/zhjie/finlafit/ws_cat4 --cats auto --procs auto --batch local --ext M3000_cat4 >M500_SL_yields.log 2>&1
    
    # python RunYields.py --inputWSDirMap 2017=/eos/user/z/zhjie/finlafit/ws_gghh_M1500 --sigModelWSDir /eos/user/z/zhjie/finlafit/ws_gghh_M1500 --bkgModelWSDir /eos/user/z/zhjie/finlafit/ws --cats auto --procs auto --batch local --ext M1500 >M1000_SL_yields.log 2>&1
    # python RunYields.py --inputWSDirMap 2017=/eos/user/z/zhjie/finlafit/ws_gghh_M2000 --sigModelWSDir /eos/user/z/zhjie/finlafit/ws_gghh_M2000 --bkgModelWSDir /eos/user/z/zhjie/finlafit/ws --cats auto --procs auto --batch local --ext M2000 >M2000_SL_yields.log 2>&1
    # python RunYields.py --inputWSDirMap 2017=/eos/user/z/zhjie/finlafit/ws_gghh_M2500 --sigModelWSDir /eos/user/z/zhjie/finlafit/ws_gghh_M2500 --bkgModelWSDir /eos/user/z/zhjie/finlafit/ws --cats auto --procs auto --batch local --ext M2500 >M3000_SL_yields.log 2>&1
    # python RunYields.py --inputWSDirMap 2017=/eos/user/z/zhjie/finlafit/ws_gghh_M3000 --sigModelWSDir /eos/user/z/zhjie/finlafit/ws_gghh_M3000 --bkgModelWSDir /eos/user/z/zhjie/finlafit/ws --cats auto --procs auto --batch local --ext M3000 >M3000_SL_yields.log 2>&1
   
fi
if [ ${WhichSamples} -eq 1 ]
  then
    python makeDatacard.py --years 2017 --prune --ext 'M1000_cat0' --output Datacard_M1000_cat0  >datacard.log 2>&1
    python makeDatacard.py --years 2017 --prune --ext 'M1000_cat1' --output Datacard_M1000_cat1  >datacard.log 2>&1
    python makeDatacard.py --years 2017 --prune --ext 'M1000_cat2' --output Datacard_M1000_cat2  >datacard.log 2>&1
    python makeDatacard.py --years 2017 --prune --ext 'M1000_cat3' --output Datacard_M1000_cat3  >datacard.log 2>&1
    python makeDatacard.py --years 2017 --prune --ext 'M1000_cat4' --output Datacard_M1000_cat4  >datacard.log 2>&1

    python makeDatacard.py --years 2017 --prune --ext 'M1500_cat0' --output Datacard_M1500_cat0  >datacard.log 2>&1
    python makeDatacard.py --years 2017 --prune --ext 'M1500_cat1' --output Datacard_M1500_cat1  >datacard.log 2>&1
    python makeDatacard.py --years 2017 --prune --ext 'M1500_cat2' --output Datacard_M1500_cat2  >datacard.log 2>&1
    python makeDatacard.py --years 2017 --prune --ext 'M1500_cat3' --output Datacard_M1500_cat3  >datacard.log 2>&1
    python makeDatacard.py --years 2017 --prune --ext 'M1500_cat4' --output Datacard_M1500_cat4  >datacard.log 2>&1

    python makeDatacard.py --years 2017 --prune --ext 'M2000_cat0' --output Datacard_M2000_cat0  >datacard.log 2>&1
    python makeDatacard.py --years 2017 --prune --ext 'M2000_cat1' --output Datacard_M2000_cat1  >datacard.log 2>&1
    python makeDatacard.py --years 2017 --prune --ext 'M2000_cat2' --output Datacard_M2000_cat2  >datacard.log 2>&1
    python makeDatacard.py --years 2017 --prune --ext 'M2000_cat3' --output Datacard_M2000_cat3  >datacard.log 2>&1
    python makeDatacard.py --years 2017 --prune --ext 'M2000_cat4' --output Datacard_M2000_cat4  >datacard.log 2>&1

    python makeDatacard.py --years 2017 --prune --ext 'M2500_cat0' --output Datacard_M2500_cat0  >datacard.log 2>&1
    python makeDatacard.py --years 2017 --prune --ext 'M2500_cat1' --output Datacard_M2500_cat1  >datacard.log 2>&1
    python makeDatacard.py --years 2017 --prune --ext 'M2500_cat2' --output Datacard_M2500_cat2  >datacard.log 2>&1
    python makeDatacard.py --years 2017 --prune --ext 'M2500_cat3' --output Datacard_M2500_cat3  >datacard.log 2>&1
    python makeDatacard.py --years 2017 --prune --ext 'M2500_cat4' --output Datacard_M2500_cat4  >datacard.log 2>&1

    python makeDatacard.py --years 2017 --prune --ext 'M3000_cat0' --output Datacard_M3000_cat0  >datacard.log 2>&1
    python makeDatacard.py --years 2017 --prune --ext 'M3000_cat1' --output Datacard_M3000_cat1  >datacard.log 2>&1
    python makeDatacard.py --years 2017 --prune --ext 'M3000_cat2' --output Datacard_M3000_cat2  >datacard.log 2>&1
    python makeDatacard.py --years 2017 --prune --ext 'M3000_cat3' --output Datacard_M3000_cat3  >datacard.log 2>&1
    python makeDatacard.py --years 2017 --prune --ext 'M3000_cat4' --output Datacard_M3000_cat4  >datacard.log 2>&1






    # python makeDatacard.py --years 2017 --prune --ext 'M1500' --output Datacard_M1500  >datacard.log 2>&1
    # python makeDatacard.py --years 2017 --prune --ext 'M2000' --output Datacard_M2000  >datacard.log 2>&1
    # python makeDatacard.py --years 2017 --prune --ext 'M2500' --output Datacard_M2500  >datacard.log 2>&1
    # python makeDatacard.py --years 2017 --prune --ext 'M3000' --output Datacard_M3000  >datacard.log 2>&1
    
fi
if [ ${WhichSamples} -eq 2 ]
  then
    python cleanDatacard.py --datacard Datacard_M1000_cat0.txt --factor 2 --removeDoubleSided >datacard.log 2>&1
    python cleanDatacard.py --datacard Datacard_M1000_cat1.txt --factor 2 --removeDoubleSided >datacard.log 2>&1
    python cleanDatacard.py --datacard Datacard_M1000_cat2.txt --factor 2 --removeDoubleSided >datacard.log 2>&1
    python cleanDatacard.py --datacard Datacard_M1000_cat3.txt --factor 2 --removeDoubleSided >datacard.log 2>&1
    python cleanDatacard.py --datacard Datacard_M1000_cat4.txt --factor 2 --removeDoubleSided >datacard.log 2>&1

    python cleanDatacard.py --datacard Datacard_M1500_cat0.txt --factor 2 --removeDoubleSided >datacard.log 2>&1
    python cleanDatacard.py --datacard Datacard_M1500_cat1.txt --factor 2 --removeDoubleSided >datacard.log 2>&1
    python cleanDatacard.py --datacard Datacard_M1500_cat2.txt --factor 2 --removeDoubleSided >datacard.log 2>&1
    python cleanDatacard.py --datacard Datacard_M1500_cat3.txt --factor 2 --removeDoubleSided >datacard.log 2>&1
    python cleanDatacard.py --datacard Datacard_M1500_cat4.txt --factor 2 --removeDoubleSided >datacard.log 2>&1

    python cleanDatacard.py --datacard Datacard_M2000_cat0.txt --factor 2 --removeDoubleSided >datacard.log 2>&1
    python cleanDatacard.py --datacard Datacard_M2000_cat1.txt --factor 2 --removeDoubleSided >datacard.log 2>&1
    python cleanDatacard.py --datacard Datacard_M2000_cat2.txt --factor 2 --removeDoubleSided >datacard.log 2>&1
    python cleanDatacard.py --datacard Datacard_M2000_cat3.txt --factor 2 --removeDoubleSided >datacard.log 2>&1
    python cleanDatacard.py --datacard Datacard_M2000_cat4.txt --factor 2 --removeDoubleSided >datacard.log 2>&1

    python cleanDatacard.py --datacard Datacard_M2500_cat0.txt --factor 2 --removeDoubleSided >datacard.log 2>&1
    python cleanDatacard.py --datacard Datacard_M2500_cat1.txt --factor 2 --removeDoubleSided >datacard.log 2>&1
    python cleanDatacard.py --datacard Datacard_M2500_cat2.txt --factor 2 --removeDoubleSided >datacard.log 2>&1
    python cleanDatacard.py --datacard Datacard_M2500_cat3.txt --factor 2 --removeDoubleSided >datacard.log 2>&1
    python cleanDatacard.py --datacard Datacard_M2500_cat4.txt --factor 2 --removeDoubleSided >datacard.log 2>&1

    python cleanDatacard.py --datacard Datacard_M3000_cat0.txt --factor 2 --removeDoubleSided >datacard.log 2>&1
    python cleanDatacard.py --datacard Datacard_M3000_cat1.txt --factor 2 --removeDoubleSided >datacard.log 2>&1
    python cleanDatacard.py --datacard Datacard_M3000_cat2.txt --factor 2 --removeDoubleSided >datacard.log 2>&1
    python cleanDatacard.py --datacard Datacard_M3000_cat3.txt --factor 2 --removeDoubleSided >datacard.log 2>&1
    python cleanDatacard.py --datacard Datacard_M3000_cat4.txt --factor 2 --removeDoubleSided >datacard.log 2>&1
    # python cleanDatacard.py --datacard Datacard_M1500.txt --factor 2 --removeDoubleSided >datacard.log 2>&1
    # python cleanDatacard.py --datacard Datacard_M2000.txt --factor 2 --removeDoubleSided >datacard.log 2>&1
    # python cleanDatacard.py --datacard Datacard_M2500.txt --factor 2 --removeDoubleSided >datacard.log 2>&1
    # python cleanDatacard.py --datacard Datacard_M3000.txt --factor 2 --removeDoubleSided >datacard.log 2>&1
    
fi
if [ ${WhichSamples} -eq 3 ]
  then
    combineCards.py Datacard_M1000_cat0.txt Datacard_M1000_cat1.txt Datacard_M1000_cat2.txt Datacard_M1000_cat3.txt Datacard_M1000_cat4.txt > Datacard_combined_M1000.txt  
    combineCards.py Datacard_M1500_cat0.txt Datacard_M1500_cat1.txt Datacard_M1500_cat2.txt Datacard_M1500_cat3.txt Datacard_M1500_cat4.txt > Datacard_combined_M1500.txt
    combineCards.py Datacard_M2000_cat0.txt Datacard_M2000_cat1.txt Datacard_M2000_cat2.txt Datacard_M2000_cat3.txt Datacard_M2000_cat4.txt > Datacard_combined_M2000.txt
    combineCards.py Datacard_M2500_cat0.txt Datacard_M2500_cat1.txt Datacard_M2500_cat2.txt Datacard_M2500_cat3.txt Datacard_M2500_cat4.txt > Datacard_combined_M2500.txt
    combineCards.py Datacard_M3000_cat0.txt Datacard_M3000_cat1.txt Datacard_M3000_cat2.txt Datacard_M3000_cat3.txt Datacard_M3000_cat4.txt > Datacard_combined_M3000.txt

    
   
    # combineCards.py Datacard_M1500.txt > Datacard_combined_M1500.txt
    # combineCards.py Datacard_M2000.txt > Datacard_combined_M2000.txt
    # combineCards.py Datacard_M2500.txt > Datacard_combined_M2500.txt
    # combineCards.py Datacard_M3000.txt > Datacard_combined_M3000.txt

fi
if [ ${WhichSamples} -eq 4 ]
  then
    combine -M AsymptoticLimits -m 125 -n M1000  Datacard_combined_M1000.txt --run expected  >dd2.log 2>&1
    combine -M AsymptoticLimits -m 125 -n M1500  Datacard_combined_M1500.txt --run expected  >dd2.log 2>&1
    combine -M AsymptoticLimits -m 125 -n M2000  Datacard_combined_M2000.txt --run expected  >dd3.log 2>&1
    combine -M AsymptoticLimits -m 125 -n M2500  Datacard_combined_M2500.txt --run expected  >dd4.log 2>&1
    combine -M AsymptoticLimits -m 125 -n M3000  Datacard_combined_M3000.txt --run expected  >dd5.log 2>&1
    
fi
if [ ${WhichSamples} -eq 5 ]
  # move limit root file to eos to further analysis 
  then
    mv higgsCombineM1000.AsymptoticLimits.mH125.root /eos/user/z/zhjie/datacard
    mv higgsCombineM1500.AsymptoticLimits.mH125.root /eos/user/z/zhjie/datacard
    mv higgsCombineM2000.AsymptoticLimits.mH125.root /eos/user/z/zhjie/datacard
    mv higgsCombineM2500.AsymptoticLimits.mH125.root /eos/user/z/zhjie/datacard
    mv higgsCombineM3000.AsymptoticLimits.mH125.root /eos/user/z/zhjie/datacard
    
fi