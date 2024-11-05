# Config file: options for signal fitting

backgroundScriptCfg = {
  
  # Setup
  'inputWSDir':'/eos/cms/store/group/phys_higgs/cmshgg/zhjie/output/output_2000/opt/data/root/ws_cat2_80', # location of 'allData.root' file
  'cats':'auto', # auto: automatically inferred from input ws
  'catOffset':2, # add offset to category numbers (useful for categories from different allData.root files)  
  'ext':'2000_M80', # extension to add to output directory
  'year':'combined', # Use combined when merging all years in category (for plots)

  # Job submission options
  'batch':'local', # [condor,SGE,IC,local]
  'queue':'hep.q' # for condor e.g. microcentury
  
}
