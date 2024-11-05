##############################################################################
# Abraham Tishelman-Charny
# 11 March 2020
#
# The purpose of this python module is to plot limits for the HHWWgg analysis 
############################################################################## 

# Example usage:
#
# python plot_limits.py -AC # compare to ATLAS 2016 semileptonic result 
# python plot_limits.py -CMSC # compare to CMS 2016 results 
# python plot_limits.py -SM # standard model point only 

import ROOT
from ROOT import TFile, TTree, TCanvas, TGraph, TMultiGraph, TGraphErrors, TLegend, kBlack, TLatex, gPad, TH1F, TGraphAsymmErrors
import CMS_lumi, tdrstyle
import subprocess # to execute shell command
from array import array 
import sys
import glob
import re
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-AC","--atlas_compare", action="store_true", default=False, help="Display limits in way to compare to ATLAS HHWWgg limits", required=False)
parser.add_argument("-CMSC","--CMS_compare", action="store_true", default=False, help="Display limits in way to compare to CMS HH limits", required=False)
parser.add_argument("-a","--All_Points", action="store_true", default=False, help="Display limits for all mass points produced", required=False)
parser.add_argument("-r","--Ratio", action="store_true", default=False, help="Plot Ratio of two limits. For example, with systematics / without systematics.", required=False)
parser.add_argument("-SM","--SM_Point",action="store_true", default=False, help="Display SM limits", required=False)
parser.add_argument("-s","--systematics",action="store_true", default=False, help="Display SM limits", required=False)
parser.add_argument("-l","--HHWWggCatLabel",type=str, default="UnLabeled", help="Category Label to find files", required=False)
parser.add_argument("-sl","--SecondHHWWggCatLabel",type=str, default="SecondUnLabeled", help="Category Label to find second set of files. Used for ratio plots", required=False)
parser.add_argument("-g","--Grid",action="store_true", default=False, help="Plot grid of limits", required=False)
parser.add_argument("-gl", "--GridLabels", type=str, nargs='+',default="", help="Labels to add to grid", required=False)
parser.add_argument("--campaign",type=str, default="", help="Campaign name used to find limit root files", required=False)
parser.add_argument("--resultType",type=str, default="", help="Result type to choose which BR's to apply", required=True) # Ex: WWgg, HH
parser.add_argument("--unit",type=str, default="", help="Result unit: fb or pb", required=True)
parser.add_argument("--ymin",type=float, default=0, help="Y minimum", required=True)
parser.add_argument("--ymax",type=float, default=0, help="Y maximum", required=True)
parser.add_argument("--yboost",type=float, default=0, help="Y boost of legend. Ex: -0.2, 0.090", required=True)
parser.add_argument("--EFT",action="store_true", default=False, help="EFT results", required=False)
parser.add_argument("--NMSSM",action="store_true", default=False, help="NMSSM results", required=False)
parser.add_argument("--lumiRescale",type=str, default="", help="Rescale limit by luminosity", required=False)
parser.add_argument("--year",type=str, default="", help="Year. 2016, 2017, 2016post or Run2", required=True) 
# parser.add_argument("--year",type=str, default="", help="Year. 2016, 2017, 2016post or Run2", required=True) 
parser.add_argument("--campaignOne",type=str, default="UnLabeled", help="Campaign of first limits in ratio", required=False)
parser.add_argument("--campaignTwo",type=str, default="UnLabeled", help="Campaign of second limits in ratio", required=False)

args = parser.parse_args()
#ol = '/afs/cern.ch/user/z/zhenxuan/CMSSW_10_6_20/src/flashggFinalFit/Plots/FinalResults/'
ol = '/eos/user/z/zhjie/CMSSW_10_2_13/src/flashggFinalFit/Plots/output'
# GET limits from root file
def getLimits(file_name):

    # print'file_name = ',file_name 
    file = TFile(file_name)
    tree = file.Get("limit")
 
    limits = [ ]
    for quantile in tree:
        if(args.unit == "fb"):
            limits.append(tree.limit) # value is already in fb because multiplied by arb. XS = 1fb 
        elif(args.unit == "pb"):
            limits.append(tree.limit * 1000.) # pb
        elif(args.SM_Point):
            limits.append(tree.limit)
 
    return limits[:6]
 
 
# PLOT upper limits
def plotUpperLimits(labels,values,resultType):
    # see CMS plot guidelines: https://ghm.web.cern.ch/ghm/plots/
    yellows={}
    greens={}
    medians={}
    N = len(labels)
    yellow = TGraph(2*N)    # yellow band
    green = TGraph(2*N)     # green band
    median = TGraph(N)      # median line
    mass=[1000]
    for i in mass:
        i=str(i)
        yellows[i]=yellow
        greens[i]=green
        medians[i]=median
    year = args.year

    vals = []
    up2s = [ ]
    nonBRvals = [] 
    for j in mass:
        j=str(j)
        for i in range(N):
            file_name = "/eos/user/z/zhjie/CMSSW_10_2_13/src/flashggFinalFit/Datacard/X"+j+"/higgsCombineM1000_%s.AsymptoticLimits.mH125.root"%(values[i])
            print("file: ",file_name)
            limit = getLimits(file_name)
            
            print(limit)
            # up2s.append(limit[4])

            campaignBRdict = {
                "HHWWgg_v2-3": 3.4916, # (1 / BR) of qqlnu. Electron and Muon decays only 
                "HHWWgg_v2-7": 2.3079, # (1 / BR) of qqlnu. Electron, Muon, all Tau decays INCLUDED
                "HHWWgg_v3": 1, # (1 / BR) of qqqq. 
                # "HHWWgg_v2-7": 2.2779 # (1 / BR) of qqlnu. Electron, Muon, all Tau decays INCLUDED
            }

            # HHWWgg_qqlnu_factor = campaignBRdict[args.campaign]
            HHWWgg_qqqq_factor = 0.0023

            HHWWgg_WWgg_factor = 1030.7153 

            lumiRescaledict = {
                "default": 1,
                "2017_2016": 107517.  # rescale from 2017 to 2016 
            }

            HHWWgg_lumiRescaleFactor = lumiRescaledict['default']

            if(resultType == "bbgg"): HHWWgg_factor = HHWWgg_qqqq_factor*HHWWgg_lumiRescaleFactor
            elif(resultType == "HY"): HHWWgg_factor = 1
            
            yellows[j].SetPoint(    i,    values[i], limit[4]*HHWWgg_factor ) # + 2 sigma
            greens[j].SetPoint(     i,    values[i], limit[3]*HHWWgg_factor ) # + 1 sigma
            medians[j].SetPoint(    i,    values[i], limit[2]*HHWWgg_factor ) # median
            greens[j].SetPoint(  2*N-1-i, values[i], limit[1]*HHWWgg_factor ) # - 1 sigma
            yellows[j].SetPoint( 2*N-1-i, values[i], limit[0]*HHWWgg_factor ) # - 2 sigm

            # print("limit without HHWWgg_factor:",limit[2])
            # print("HHWWgg_factor:",HHWWgg_factor)
            nonBRvals.append(limit[2])
            # print("limit[2]*HHWWgg_factor:",limit[2]*HHWWgg_factor)
            vals.append(limit[2]*HHWWgg_factor)

    #print(vals)
    massvals = labels[:]
    mvals = []
    for m in massvals: 
      massval = m.split('_')[0]
      massval = massval.replace("X","")
      mvals.append(massval)
      
    print("masses:",mvals)
    print("nonBR vals:",nonBRvals)
    print("vals:",vals)
    # vals=vals*0.0023

    W = 800
    H  = 600
    T = 0.08*H
    B = 0.12*H
    L = 0.12*W
    R = 0.04*W
    c = TCanvas("c","c",100,100,W,H)
    # c.SetGridy()
    # c.SetLogy()
    c.SetFillColor(0)
    c.SetBorderMode(0)
    c.SetFrameFillStyle(0)
    c.SetFrameBorderMode(0)
    c.SetLeftMargin( L/W )
    c.SetRightMargin( R/W )
    c.SetTopMargin( T/H )
    c.SetBottomMargin( B/H )
    c.SetTickx(0)
    c.SetTicky(0)
    c.SetGrid()
    # c.SetGridy()
    # c.SetLogy()
    # gPad.SetLogy()
    # c.cd()
    # ROOT.gPad.SetLogy()
    # c.SetLogy()
    frame = c.DrawFrame(1.4,0.001, 4.1, 10)
    frame.GetYaxis().CenterTitle()
    frame.GetYaxis().SetTitleSize(0.05)
    frame.GetXaxis().SetTitleSize(0.05)
    frame.GetXaxis().SetLabelSize(0.04)
    frame.GetYaxis().SetLabelSize(0.04)
    frame.GetYaxis().SetTitleOffset(0.9)
    frame.GetXaxis().SetNdivisions(508)
    frame.GetYaxis().CenterTitle(True)
    # frame.GetYaxis().SetTitle("95% upper limit on #sigma / #sigma_{SM}")
    
    if(args.unit == "pb"):
        if(resultType == "bbgg"): frame.GetYaxis().SetTitle("95% CL limits on #sigma(gg#rightarrow X)#times B(X#rightarrow HH#rightarrow bb#gamma#gamma) [pb]")    
        # elif(resultType == "HH"): frame.GetYaxis().SetTitle("95% CL limits on #sigma(gg#rightarrow X)#times B(X#rightarrow HH) [pb]")    
        elif(resultType == "HY") :   frame.GetYaxis().SetTitle("95% CL limits on #sigma(gg#rightarrow X)#times B(X#rightarrow HH) [pb]") 
    elif(args.unit == "fb"):
        if(resultType == "bbgg"): frame.GetYaxis().SetTitle("95% CL limits on #sigma(gg#rightarrow X)#times B(X#rightarrow HY#rightarrow bb#gamma#gamma) [fb]")    
        # elif(resultType == "HH"): frame.GetYaxis().SetTitle("95% CL limits on #sigma(gg#rightarrow X)#times B(X#rightarrow HH) [fb]")    
        elif(resultType == "HY") :   frame.GetYaxis().SetTitle("95% CL limits on #sigma(gg#rightarrow X)#times B(X#rightarrow HY) [fb]") 
    if(resultType == "bbgg"): 
        frame.GetYaxis().SetTitleSize(0.04)
        frame.GetYaxis().SetTitleOffset(1.3)

    #frame.GetXaxis().Set
#    frame.GetYaxis().SetTitle("95% upper limit on #sigma #times BR / (#sigma #times BR)_{SM}")
    # frame.GetXaxis().SetTitle("background systematic uncertainty [%]")
    if(args.SM_Point): frame.GetXaxis().SetTitle("Standard Model")
    else: frame.GetXaxis().SetTitle(" Mass (GeV)")
    # frame.SetMinimum(0)
    # frame.SetMinimum(1) # need Minimum > 0 for log scale 
    frame.SetMinimum(args.ymin) # need Minimum > 0 for log scale 

    frame.SetMaximum(args.ymax)
    frame.GetXaxis().SetLimits(min(values),max(values))
    # frame.GetXaxis().SetLimits(min(values)-10,max(values)+10)
    c.SetLogy()
    for i in mass:
        i=str(i)
        yellows[i].SetFillColor(ROOT.kOrange)
        yellows[i].SetLineColor(ROOT.kOrange)
        yellows[i].SetFillStyle(1001)
        yellows[i].Draw('F')
    
        greens[i].SetFillColor(ROOT.kGreen+1)
        greens[i].SetLineColor(ROOT.kGreen+1)
        greens[i].SetFillStyle(1001)
        greens[i].Draw('Fsame')
    
        medians[i].SetLineColor(1)
        medians[i].SetLineWidth(2)
        medians[i].SetLineStyle(2)
        medians[i].SetMarkerStyle(8)
        medians[i].Draw('PLsame')
        
        
    
    





    CMS_lumi.CMS_lumi(c,4,11)
    ROOT.gPad.SetTicks(1,1)
    frame.Draw('sameaxis')
 
    yboost = args.yboost
    x1 = 0.15
    x2 = x1 + 0.24
    y2 = 0.76 + yboost
    y1 = 0.60 + yboost
    legend = TLegend(x1,y1,x2,y2)
    legend.SetFillStyle(0)
    legend.SetBorderSize(0)
    legend.SetTextSize(0.041)
    legend.SetTextFont(42)
    legend.AddEntry(median, "AsymptoticLimits CL_{s} expected",'L')
    legend.AddEntry(green, "#pm 1 std. deviation",'f')
#    legend.AddEntry(green, "AsymptoticLimits CL_{s} #pm 1 std. deviation",'f')
    legend.AddEntry(yellow,"#pm 2 std. deviation",'f')
    # legend.AddEntry("","STAT Only","")
#    legend.AddEntry(green, "AsymptoticLimits CL_{s} #pm 2 std. deviation",'f')
    legend.Draw()

    label = TLatex()
    label.SetNDC()
    label.SetTextAngle(0)
    label.SetTextColor(kBlack)
    label.SetTextFont(42)
    label.SetTextSize(0.045)
    label.SetLineWidth(2)
    if(args.systematics): label.DrawLatex(0.7,0.7 + yboost,"SYST + STAT")
    else: label.DrawLatex(0.7,0.7 + yboost,"STAT ONLY")
    
    # print (" ")
    
    outFile = ''
    outFile += ol + '/'
    if(args.CMS_compare):
        outFile += "CMS_Compare_"
    if(args.All_Points):
	    outFile += "All_Points_"

    if(args.atlas_compare): outFile += "atlas_Compare_"

    if(args.SM_Point): outFile += "SM_"
    outFile += args.HHWWggCatLabel + "_"

    # args.lumiRescale
    c.SaveAs("%s_%s_%s_UpperLimit.pdf"%(outFile,args.lumiRescale,resultType))
    c.SaveAs("%s_%s_%s_UpperLimit.png"%(outFile,args.lumiRescale,resultType))
    c.SaveAs("%s_%s_%s_UpperLimit.C"%(outFile,args.lumiRescale,resultType))
    c.Close()
def getMXMY(filename):
    mx_my = re.search("data_(\d+)", filename)

    if mx_my:
        # mx = mx_my.group(1)
        my = mx_my.group(1)
    return int(my)
def main():
    # labels = ['M1000','M1200','M1400','M1600','M1800','M2000','M2200','M2400','M2500','M2600','M2800','M3000']
    # values = [1000,1200,1400,1600,1800,2000,2200,2400,2500,2600,2800,3000]
    # labels = ['M1000','M1500','M2000','M2500','M3000']
    # values = [1000,1500,2000,2500,3000]
    # labels = ['combine_M80','combine_M100','combine_M125','combine_M150','combine_M170','combine_M190','combine_M250','combine_M300','combine_M350','combine_M400','combine_M450','combine_M500','combine_M550','combine_M700']
    # values = [80,100,125,150,170,190,250,300,350,400,450,500,550,700]
    # labels = ['M100','M300','M400','M700']
    # 'M150','M250','M300','M400','M500','
    # values = [100,300,400,700]
    # 150,250,300,400,500
    mass=[1000]
    values={}
    labels={}
    for j in mass:
        sigFiles=glob.glob('/eos/user/z/zhjie/output_all_'+str(j)+'/data_*.parquet')
        value=[]
        label=[]
        for f in sigFiles:
            y=getMXMY(f)
            value.append(y)
        value.sort()
        for i in value:
            l=str(i)
            l='M'+l
            label.append(l)
        values[j]=value
        labels[j]=label

    resultType = args.resultType
    plotUpperLimits(labels,values,resultType)
if __name__ == '__main__':
    main()

#  'M60','M70','M80','M90',70,80,90,'M150','M170','M190','M250''M300','M350','M400',
