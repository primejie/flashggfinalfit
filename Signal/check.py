import importlib
import os
from optparse import OptionParser
import sys
sys.path.append('/eos/home-z/zhjie/CMSSW_10_2_13/src/flashggFinalFit/Signal/allsys')
def get_options():
  parser = OptionParser()
  # Take inputs from config file
  parser.add_option('--inputConfig', dest='inputConfig', default='', help="Name of input config file (if specified will ignore other options)")
  return parser.parse_args()
(opt,args) = get_options()


config=opt.inputConfig
config = os.path.splitext(config)[0]
# print(path_without_extension)
config=config.replace("/",".")
module = importlib.import_module(config)