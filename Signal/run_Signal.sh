WhichSamples=${1}
if [ ${WhichSamples} -eq 0 ]
  then
    echo ${whichsample}
    # already saved different mass point root file into different directory
    # can't run parallel since some operation may have confliction attention
    python RunSignalScripts.py --inputConfig config_M500_SL_2017.py --mode 'fTest' >signal_ftest_M500_SL.log 2>&1 &
    python RunSignalScripts.py --inputConfig config_M1000_SL_2017.py --mode 'fTest' >signal_ftest_M1000_SL.log 2>&1 &
    python RunSignalScripts.py --inputConfig config_M2000_SL_2017.py --mode 'fTest' >signal_ftest_M2000_SL.log 2>&1 &
    python RunSignalScripts.py --inputConfig config_M3000_SL_2017.py --mode 'fTest' >signal_ftest_M3000_SL.log 2>&1 &
fi
if [ ${WhichSamples} -eq 1 ]
  then
    echo ${whichsample}
    # already saved different mass point root file into different directory
    # can't run parallel since some operation may have confliction attention
    # python RunSignalScripts.py --inputConfig config_M500_SL_2017.py --mode 'signalFit' --modeOpts "--skipSystematics" >signal_signalFit_M500_SL.log 2>&1 &
    python RunSignalScripts.py --inputConfig config_M1000_SL_2017.py --mode 'signalFit' --modeOpts "--skipSystematics" >signal_signalFit_M1000.log 2>&1
    python RunSignalScripts.py --inputConfig config_M2000_SL_2017.py --mode 'signalFit' --modeOpts "--skipSystematics" >signal_signalFit_M2000.log 2>&1 
    python RunSignalScripts.py --inputConfig config_M3000_SL_2017.py --mode 'signalFit' --modeOpts "--skipSystematics" >signal_signalFit_M3000.log 2>&1 
fi
if [ ${WhichSamples} -eq 2 ]
  then
    echo 'run doPlots'
    # already saved different mass point root file into different directory
    python RunSignalScripts.py --inputConfig config_M300_2017.py --mode 'signalFit' --modeOpts "--skipSystematics --doPlots --skipVertexScenarioSplit" >signal_signalFit_M300.log 2>&1 
    python RunSignalScripts.py --inputConfig config_M700_2017.py --mode 'signalFit' --modeOpts "--skipSystematics --doPlots --skipVertexScenarioSplit" >signal_signalFit_M700.log 2>&1 
    python RunSignalScripts.py --inputConfig config_M1250_2017.py --mode 'signalFit' --modeOpts "--skipSystematics --doPlots --skipVertexScenarioSplit" >signal_signalFit_M1250.log 2>&1 
    python RunSignalScripts.py --inputConfig config_M2000_2017.py --mode 'signalFit' --modeOpts "--skipSystematics --doPlots --skipVertexScenarioSplit" >signal_signalFit_M2000.log 2>&1 
    python RunSignalScripts.py --inputConfig config_M3000_2017.py --mode 'signalFit' --modeOpts "--skipSystematics --doPlots --skipVertexScenarioSplit" >signal_signalFit_M3000.log 2>&1 
fi
if [ ${WhichSamples} -eq 3 ]
  then
    echo 'run packaged'
    # already saved different mass point root file into different directory
    python RunPackager.py --cats RECO_untagged --exts dcb_2017_M500,  --batch local  --massPoints 125 --year 2017 --outputExt packaged_M500
    python RunPackager.py --cats RECO_untagged --exts dcb_2017_M1000,  --batch local  --massPoints 125 --year 2017 --outputExt packaged_M1000
    python RunPackager.py --cats RECO_untagged --exts dcb_2017_M2000,  --batch local  --massPoints 125 --year 2017 --outputExt packaged_M2000
    python RunPackager.py --cats RECO_untagged --exts dcb_2017_M3000,  --batch local  --massPoints 125 --year 2017 --outputExt packaged_M3000
fi
if [ ${WhichSamples} -eq 4 ]
  then
    echo 'run plotter'
    # already saved different mass point root file into different directory
    python RunPlotter.py --procs all --cats RECO_untagged --years 2017 --ext packaged_M500
    python RunPlotter.py --procs all --cats RECO_untagged --years 2017 --ext packaged_M1000
    python RunPlotter.py --procs all --cats RECO_untagged --years 2017 --ext packaged_M2000
    python RunPlotter.py --procs all --cats RECO_untagged --years 2017 --ext packaged_M3000
fi
if [ ${WhichSamples} -eq 5 ]
  then
  #attention: need to copy all the CMS_multipdf* to your workspace dir
    echo 'run copy'
    # cp outdir_dcb_2017_M500/signalFit/output/CMS-HGG_sigfit_dcb_2017_M500_gghh_2017_RECO_untagged.root /eos/user/z/zhenxuan/hhwwgg_root/hhwwgg_root_SL/ws_gghh_M500/CMS-HGG_sigfit_packaged_RECO_untagged_2017.root
    cp outdir_dcb_2017_M1000/signalFit/output/CMS-HGG_sigfit_dcb_2017_M1000_gghh_2017_RECO_untagged.root /eos/user/z/zhenxuan/hhwwgg_root/hhwwgg_root_SL/ws_gghh_M1000/CMS-HGG_sigfit_packaged_RECO_untagged_2017.root
    cp outdir_dcb_2017_M2000/signalFit/output/CMS-HGG_sigfit_dcb_2017_M2000_gghh_2017_RECO_untagged.root /eos/user/z/zhenxuan/hhwwgg_root/hhwwgg_root_SL/ws_gghh_M2000/CMS-HGG_sigfit_packaged_RECO_untagged_2017.root
    cp outdir_dcb_2017_M3000/signalFit/output/CMS-HGG_sigfit_dcb_2017_M3000_gghh_2017_RECO_untagged.root /eos/user/z/zhenxuan/hhwwgg_root/hhwwgg_root_SL/ws_gghh_M3000/CMS-HGG_sigfit_packaged_RECO_untagged_2017.root
fi

