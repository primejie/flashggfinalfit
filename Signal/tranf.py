import os, sys
from optparse import OptionParser
from collections import OrderedDict as od
import importlib
import sys
print(sys.path)
def get_options():
  parser = OptionParser()
  # Take inputs from config file
  parser.add_option('--inputConfig', dest='inputConfig', default='', help="Name of input config file (if specified will ignore other options)")
  return parser.parse_args()
(opt,args) = get_options()
config=opt.inputConfig
config=config.replace("/",".")
print(config)
config = os.path.splitext(config)[0]
module = importlib.import_module(config)

cfg=module.signalScriptCfg
print(cfg['inputWSDir'])
print(cfg['procs'])
print(cfg['cats'])
print(cfg['ext'])
print(cfg['analysis'])
print(cfg['year'])
print(cfg['massPoints'])
print(cfg['scales'])
print(cfg['scalesCorr'])
print(cfg['scalesGlobal'])
print(cfg['smears'])
print(cfg['batch'])
print(cfg['queue'])