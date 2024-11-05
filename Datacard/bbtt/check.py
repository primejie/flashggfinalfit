import ROOT
import sys
from ROOT import TFile, TTree, TCanvas, TGraph, TMultiGraph, TGraphErrors, TLegend, kBlack, TLatex, gPad, TH1F, TGraphAsymmErrors

args=sys.argv

def getLimits(file_name):

    # print'file_name = ',file_name 
    file = TFile(file_name)
    limits = [ ]
    if file.GetListOfKeys().Contains("limit"):
        tree = file.Get("limit")
        
        for quantile in tree:
            limits.append(tree.limit) # value is already in fb because multiplied by arb. XS = 1fb 
        return limits[:6]
    else:
        print("no limit    ",file_name)
        return limits[:6]
 
   
 
 
# print(args[1])
limit=getLimits(args[1])

if len(limit)==0:
    print("failed",args[1])
else :
    print("sucessful!!!!!!!!!")
