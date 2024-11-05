# Config file: options for signal fitting

backgroundScriptCfg = {
  
  # Setup
  'inputWSDir':'/eos/cms/store/group/phys_higgs/cmshgg/zhjie/output/output_2500/opt/data/root/ws_cat1_1800', # location of 'allData.root' file
  'cats':'auto', # auto: automatically inferred from input ws
  'catOffset':1, # add offset to category numbers (useful for categories from different allData.root files)  
  'ext':'2500_M1800', # extension to add to output directory
  'year':'combined', # Use combined when merging all years in category (for plots)

  # Job submission options
  'batch':'local', # [condor,SGE,IC,local]
  'queue':'hep.q' # for condor e.g. microcentury
  
}
