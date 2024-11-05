#!/bin/bash
start_time=$(date +%s)
export SCRAM_ARCH=slc7_amd64_gcc700
source /cvmfs/cms.cern.ch/cmsset_default.sh

cd /eos/user/z/zhjie/CMSSW_10_2_13/src/
eval `scram runtime -sh`


d0='_2017_M125_pythia8_gghh.root'
d1='_2018_M125_pythia8_gghh.root'
d2='_2016pre_M125_pythia8_gghh.root'
d3='_2016post_M125_pythia8_gghh.root'
m='_gghh'
c0='_cat0'
c1='_cat1'
c2='_cat2'


path='/eos/cms/store/group/phys_higgs/cmshgg/zhjie/output/output_1000/opt/data'
cd /eos/user/z/zhjie/CMSSW_10_2_13/src/flashggFinalFit/Trees2WS
  ###
python trees2ws.py --inputConfig config_sys.py --inputTreeFile /eos/cms/store/group/phys_higgs/cmshgg/zhjie/output/output_1000/opt/2017/root/addsys/output_NMSSM_XToYHTo2B2G_MX-1000_MY-400_cat0_2017_M125_pythia8_gghh.root --inputMass 125 --productionMode gghh --year 2017 --jetmass 400 --low 150 --high 560  --doSystematics
python trees2ws.py --inputConfig config_sys.py --inputTreeFile /eos/cms/store/group/phys_higgs/cmshgg/zhjie/output/output_1000/opt/2018/root/addsys/output_NMSSM_XToYHTo2B2G_MX-1000_MY-400_cat0_2018_M125_pythia8_gghh.root --inputMass 125 --productionMode gghh --year 2018 --jetmass 400 --low 150 --high 560  --doSystematics
python trees2ws.py --inputConfig config_sys.py --inputTreeFile /eos/cms/store/group/phys_higgs/cmshgg/zhjie/output/output_1000/opt/2016pre/root/addsys/output_NMSSM_XToYHTo2B2G_MX-1000_MY-400_cat0_2016pre_M125_pythia8_gghh.root --inputMass 125 --productionMode gghh --year 2016pre --jetmass 400 --low 150 --high 560  --doSystematics
python trees2ws.py --inputConfig config_sys.py --inputTreeFile /eos/cms/store/group/phys_higgs/cmshgg/zhjie/output/output_1000/opt/2016post/root/addsys/output_NMSSM_XToYHTo2B2G_MX-1000_MY-400_cat0_2016post_M125_pythia8_gghh.root --inputMass 125 --productionMode gghh --year 2016post --jetmass 400 --low 150 --high 560  --doSystematics
python trees2ws_data.py --inputConfig config_simple.py --inputTreeFile /eos/cms/store/group/phys_higgs/cmshgg/zhjie/output/output_1000/opt/data/root/data_400_cat0.root --jetmass 400 --low 150 --high 560
cd  /eos/cms/store/group/phys_higgs/cmshgg/zhjie/output/output_1000/opt/2017/root/addsys
mkdir -p ws_gghh_cat0_400
mv ws_gghh/output_NMSSM_XToYHTo2B2G_MX-1000_MY-400_cat0_2017_M125_pythia8_gghh_gghh.root  ws_gghh_cat0_400/output_NMSSM_XToYHTo2B2G_MX-1000_MY-400_cat0_2017_M125_pythia8_gghh.root
cd  /eos/cms/store/group/phys_higgs/cmshgg/zhjie/output/output_1000/opt/2018/root/addsys
mkdir -p ws_gghh_cat0_400
mv ws_gghh/output_NMSSM_XToYHTo2B2G_MX-1000_MY-400_cat0_2018_M125_pythia8_gghh_gghh.root  ws_gghh_cat0_400/output_NMSSM_XToYHTo2B2G_MX-1000_MY-400_cat0_2018_M125_pythia8_gghh.root
cd  /eos/cms/store/group/phys_higgs/cmshgg/zhjie/output/output_1000/opt/2016pre/root/addsys
mkdir -p ws_gghh_cat0_400
mv ws_gghh/output_NMSSM_XToYHTo2B2G_MX-1000_MY-400_cat0_2016pre_M125_pythia8_gghh_gghh.root  ws_gghh_cat0_400/output_NMSSM_XToYHTo2B2G_MX-1000_MY-400_cat0_2016pre_M125_pythia8_gghh.root
cd  /eos/cms/store/group/phys_higgs/cmshgg/zhjie/output/output_1000/opt/2016post/root/addsys
mkdir -p ws_gghh_cat0_400
mv ws_gghh/output_NMSSM_XToYHTo2B2G_MX-1000_MY-400_cat0_2016post_M125_pythia8_gghh_gghh.root  ws_gghh_cat0_400/output_NMSSM_XToYHTo2B2G_MX-1000_MY-400_cat0_2016post_M125_pythia8_gghh.root
cd  /eos/cms/store/group/phys_higgs/cmshgg/zhjie/output/output_1000/opt/data/root/
mkdir -p ws_cat0_400
mv ws/data_400_cat0.root ws_cat0_400/allData.root 
cd /eos/user/z/zhjie/CMSSW_10_2_13/src/flashggFinalFit/Signal
python RunSignalScripts.py --inputConfig allsys/2017_1000/config_1000_2017_400_cat0.py --mode 'fTest'
python RunSignalScripts.py --inputConfig allsys/2017_1000/config_1000_2017_400_cat0.py  --mode calcPhotonSyst
python RunSignalScripts.py --inputConfig allsys/2017_1000/config_1000_2017_400_cat0.py --mode 'signalFit'
python RunSignalScripts.py --inputConfig allsys/2018_1000/config_1000_2018_400_cat0.py --mode 'fTest'
python RunSignalScripts.py --inputConfig allsys/2018_1000/config_1000_2018_400_cat0.py  --mode calcPhotonSyst
python RunSignalScripts.py --inputConfig allsys/2018_1000/config_1000_2018_400_cat0.py --mode 'signalFit'
python RunSignalScripts.py --inputConfig allsys/2016pre_1000/config_1000_2016pre_400_cat0.py --mode 'fTest'
python RunSignalScripts.py --inputConfig allsys/2016pre_1000/config_1000_2016pre_400_cat0.py  --mode calcPhotonSyst
python RunSignalScripts.py --inputConfig allsys/2016pre_1000/config_1000_2016pre_400_cat0.py --mode 'signalFit'
python RunSignalScripts.py --inputConfig allsys/2016post_1000/config_1000_2016post_400_cat0.py --mode 'fTest'
python RunSignalScripts.py --inputConfig allsys/2016post_1000/config_1000_2016post_400_cat0.py  --mode calcPhotonSyst
python RunSignalScripts.py --inputConfig allsys/2016post_1000/config_1000_2016post_400_cat0.py --mode 'signalFit'
python RunPackager.py --cats resolved_cat0 --exts dcb_resolved_M1000_M400_cat0_2017,dcb_resolved_M1000_M400_cat0_2018,dcb_resolved_M1000_M400_cat0_2016pre,dcb_resolved_M1000_M400_cat0_2016post --batch local  --massPoints 125 --mergeYears --outputExt packaged_mergeyears_resolved_M1000_M400_cat0
python RunPlotter.py --procs all --cats resolved_cat0 --years 2017,2018,2016pre,2016post  --ext packaged_mergeyears_resolved_M1000_M400_cat0
file0=`ls outdir_packaged_mergeyears_resolved_M1000_M400_cat0/*.root`
cp $file0  outdir_packaged_mergeyears_resolved_M1000_M400_cat0/CMS-HGG_sigfit_packaged_resolved_cat0.root
cd /eos/user/z/zhjie/CMSSW_10_2_13/src/flashggFinalFit/Background
python RunBackgroundScripts.py --inputConfig allsys/data_all_1000/config_all_cat0_400.py --mode fTestParallel
