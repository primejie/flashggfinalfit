from optparse import OptionParser
from shanePalette import set_color_palette
from usefulStyle import drawCMS, drawEnPu, setCanvasCorr, formatHisto
from collections import OrderedDict as od
import ROOT
import json
import os
import re

def get_options():
  parser = OptionParser()
  parser.add_option('--inputJson', dest='inputJson', default='inputs.json', help="Input json file to define fits")
  parser.add_option('--mode', dest='mode', default='', help='Type of fit')
  parser.add_option('--ext', dest='ext', default='', help='If running with extension in datacard')
  parser.add_option('--translate', dest='translate', default='', help='Load translations for pois')
  parser.add_option('--dropTHQ', dest='dropTHQ', default=False, action="store_true", help='Drop r_tHq from the poi list')
  return parser.parse_args()
(opt,args) = get_options() 

def LoadTranslations(jsonfilename):
    with open(jsonfilename) as jsonfile:
        return json.load(jsonfile)

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetNumberContours(500)
lumi = 137

modes = od()

# Read json file and extract pois
with open( opt.inputJson ) as jsonfile: inputs = json.load(jsonfile)[opt.mode]
pois = inputs['pois'].split(",") 
if(opt.dropTHQ)&("r_tHq" in pois): pois.remove("r_tHq")
fit = inputs['fits'].split("+")[0]
name = "%s_%s"%(fit.split(":")[0],fit.split(":")[1])
modes[opt.mode] = pois
# Load translations
translate = {} if opt.translate is None else LoadTranslations(opt.translate)

for mode,pois in modes.iteritems():
  fileName = '%s/src/flashggFinalFit/Combine/runFits%s_%s/robustHesse_%s.root'%(os.environ['CMSSW_BASE'],opt.ext,opt.mode,name)
  inFile = ROOT.TFile(fileName,'READ')
  theMatrix = inFile.Get('h_correlation')
  theList   = inFile.Get('floatParsFinal')

  pars = od()
  for iPar,par in enumerate(theList):
    if iPar==len(theList)-1: break
    if not par.GetName().startswith('r_'): continue
    pars[par.GetName()] = iPar
  nPars = len(pars.keys())
  print 'Procesing the following %g parameters:'%nPars
  for par in pars.keys(): print par
  revPars = {i:name for name,i in pars.iteritems()}

  theHist = ROOT.TH2F('corr_%s'%mode, '', nPars, -0.5, nPars-0.5, nPars, -0.5, nPars-0.5)
  theMap = {}

  for iBin,iPar in enumerate(pars.values()):
    for jBin,jPar in enumerate(pars.values()):
      proc = theMatrix.GetXaxis().GetBinLabel(iPar+1)
      #print 'Got proc %s, expecting proc %s'%(proc, revPars[iPar])
      theVal = theMatrix.GetBinContent(iPar+1,jPar+1)
      #print 'Value for correlation between %s and %s is %.3f'%(revPars[iPar],revPars[jPar],theVal)
      theMap[(revPars[iPar],revPars[jPar])] = theVal

  for iBin,iPar in enumerate(pois):
    for jBin,jPar in enumerate(pois):
      theHist.GetXaxis().SetBinLabel(iBin+1, translate[iPar])
      theHist.GetYaxis().SetBinLabel(jBin+1, translate[jPar])
      #print 'Filling correlation for %s and %s of %.3f'%(iPar, jPar, theMap[(iPar,jPar)])
      theHist.Fill(iBin, jBin, theMap[(iPar,jPar)])

  print 'Final correlation map used is:'
  print theMap

  set_color_palette('frenchFlag')
  ROOT.gStyle.SetNumberContours(500)
  ROOT.gStyle.SetPaintTextFormat('1.2f')

  if mode.count('stage1p2'): canv = setCanvasCorr(stage='1p2')
  else: canv = setCanvasCorr()
  formatHisto(theHist)
  theHist.GetXaxis().SetTickLength(0.)
  theHist.GetXaxis().SetLabelSize(0.06)
  theHist.GetYaxis().SetTickLength(0.)
  theHist.GetYaxis().SetLabelSize(0.06)
  theHist.GetZaxis().SetRangeUser(-1.,1.)
  theHist.GetZaxis().SetTickLength(0.)
  if mode.count('stage1p2'): 
    theHist.GetXaxis().SetLabelSize(0.03)
    theHist.GetYaxis().SetLabelSize(0.03)
    theHist.GetXaxis().LabelsOption("v")
  else:
    theHist.SetMarkerSize(1.5)
  theHist.Draw('colz,text')
  drawCMS(True)
  drawEnPu(lumi='%2.0f fb^{-1}'%lumi)
  canv.Print('%s/src/flashggFinalFit/Combine/runFits%s_%s/Plots/corrMatrix_%s_%s%s.png'%(os.environ['CMSSW_BASE'],opt.ext,mode,mode,name.split("_")[-1],opt.ext))
  canv.Print('%s/src/flashggFinalFit/Combine/runFits%s_%s/Plots/corrMatrix_%s_%s%s.pdf'%(os.environ['CMSSW_BASE'],opt.ext,mode,mode,name.split("_")[-1],opt.ext))