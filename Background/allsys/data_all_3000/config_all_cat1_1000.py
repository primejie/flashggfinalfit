# Config file: options for signal fitting

backgroundScriptCfg = {
  
  # Setup
  'inputWSDir':'/eos/cms/store/group/phys_higgs/cmshgg/zhjie/output/output_3000/opt/data/root/ws_cat1_1000', # location of 'allData.root' file
  'cats':'auto', # auto: automatically inferred from input ws
  'catOffset':1, # add offset to category numbers (useful for categories from different allData.root files)  
  'ext':'3000_M1000', # extension to add to output directory
  'year':'combined', # Use combined when merging all years in category (for plots)

  # Job submission options
  'batch':'local', # [condor,SGE,IC,local]
  'queue':'hep.q' # for condor e.g. microcentury
  
}
