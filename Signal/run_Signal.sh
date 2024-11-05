
# python RunSignalScripts.py --inputConfig config_check_650_2017_cat0.py --mode 'fTest' 
# python RunSignalScripts.py --inputConfig config_check_650_2017_cat0.py --mode 'signalFit' --modeOpts '--skipSystematics' 

# python RunSignalScripts.py --inputConfig config_check_650_2017_cat1.py --mode 'fTest' 
# python RunSignalScripts.py --inputConfig config_check_650_2017_cat1.py --mode 'signalFit' --modeOpts '--skipSystematics' 


# python RunSignalScripts.py --inputConfig config_check_650_2017_cat2.py --mode 'fTest' 
# python RunSignalScripts.py --inputConfig config_check_650_2017_cat2.py --mode 'signalFit' --modeOpts '--skipSystematics' 



# python RunSignalScripts.py --inputConfig config_check_650_2018_cat0.py --mode 'fTest' 
# python RunSignalScripts.py --inputConfig config_check_650_2018_cat0.py --mode 'signalFit' --modeOpts '--skipSystematics' 
# python RunSignalScripts.py --inputConfig config_check_650_2018_cat1.py --mode 'fTest' 
# python RunSignalScripts.py --inputConfig config_check_650_2018_cat1.py --mode 'signalFit' --modeOpts '--skipSystematics' 
# python RunSignalScripts.py --inputConfig config_check_650_2018_cat2.py --mode 'fTest' 
# python RunSignalScripts.py --inputConfig config_check_650_2018_cat2.py --mode 'signalFit' --modeOpts '--skipSystematics' 


# python RunSignalScripts.py --inputConfig config_check_650_2016pre_cat0.py --mode 'fTest' 
# python RunSignalScripts.py --inputConfig config_check_650_2016pre_cat0.py --mode 'signalFit' --modeOpts '--skipSystematics' 
# python RunSignalScripts.py --inputConfig config_check_650_2016pre_cat1.py --mode 'fTest' 
# python RunSignalScripts.py --inputConfig config_check_650_2016pre_cat1.py --mode 'signalFit' --modeOpts '--skipSystematics' 
# python RunSignalScripts.py --inputConfig config_check_650_2016pre_cat2.py --mode 'fTest' 
# python RunSignalScripts.py --inputConfig config_check_650_2016pre_cat2.py --mode 'signalFit' --modeOpts '--skipSystematics' 


# python RunSignalScripts.py --inputConfig config_check_650_2016post_cat0.py --mode 'fTest' 
# python RunSignalScripts.py --inputConfig config_check_650_2016post_cat0.py --mode 'signalFit' --modeOpts '--skipSystematics' 
# python RunSignalScripts.py --inputConfig config_check_650_2016post_cat1.py --mode 'fTest' 
# python RunSignalScripts.py --inputConfig config_check_650_2016post_cat1.py --mode 'signalFit' --modeOpts '--skipSystematics' 
# python RunSignalScripts.py --inputConfig config_check_650_2016post_cat2.py --mode 'fTest' 
# python RunSignalScripts.py --inputConfig config_check_650_2016post_cat2.py --mode 'signalFit' --modeOpts '--skipSystematics' 


python RunPackager.py --cats resolved_cat0 --exts dcb_2017_M650_90_res_cat0,dcb_2018_M650_90_res_cat0,dcb_2016pre_M650_90_res_cat0,dcb_2016post_M650_90_res_cat0 --batch local  --massPoints 125 --mergeYears --outputExt packaged_mergeyears_check_M659-90_res_cat0
python RunPackager.py --cats resolved_cat1 --exts dcb_2017_M650_90_res_cat1,dcb_2018_M650_90_res_cat1,dcb_2016pre_M650_90_res_cat1,dcb_2016post_M650_90_res_cat1 --batch local  --massPoints 125 --mergeYears --outputExt packaged_mergeyears_check_M659-90_res_cat1
python RunPackager.py --cats resolved_cat2 --exts dcb_2017_M650_90_res_cat2,dcb_2018_M650_90_res_cat2,dcb_2016pre_M650_90_res_cat2,dcb_2016post_M650_90_res_cat2 --batch local  --massPoints 125 --mergeYears --outputExt packaged_mergeyears_check_M659-90_res_cat2