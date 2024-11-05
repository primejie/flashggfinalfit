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
import os
import math
import glob
import re
import numpy as np
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
ol = '/eos/user/z/zhjie/CMSSW_10_2_13/src/flashggFinalFit/Plots/combined'
# GET limits from root file
def getxy(medians,i):
    
    N = medians[i].GetN()  

    if N > 0:
        last_index = N - 1  
        last_x = ROOT.Double(0)  
        last_y = ROOT.Double(0)  
        
        medians[i].GetPoint(last_index, last_x, last_y) 


        y_min = 0.01 
        y_max = 10000000000  
        
        normalized_x = 0.85*(last_x - 60) /3300  +0.1
        normalized_y = (last_y - y_min) / (y_max - y_min)
        # log_texty = math.log10(normalized_y)
    
    return normalized_x,normalized_y
def getLimits(file_name):

    # print'file_name = ',file_name 
    file = TFile(file_name)
    tree = file.Get("limit")
    if not tree:
        return []
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
    mass=[1000,1800,2000,2400,2500,2600,2800,3000,3500,4000]
    nexp=len(mass)
    yellows={}
    greens={}
    medians={}
    year = args.year

    vals = []
    up2s = []
    nonBRvals = [] 
    for i in mass:
        N=len(labels[i])
        print("label",labels[i])
        yellows[i] = TGraph(2*N)    # yellow band
        greens[i] = TGraph(2*N)     # green band
        medians[i] = TGraph(N)
     
    factor=10**(nexp-1)
    for i in mass:
        N=len(labels[i])
        value=values[i]
        print("N",N)
        x_vals = []
        y_vals_yellow_up = []
        y_vals_yellow_down = []
        y_vals_green_up = []
        y_vals_green_down = []
        y_vals_median = []

        for j in range(N):
            file_name = '/eos/user/z/zhjie/CMSSW_10_2_13/src/flashggFinalFit/Datacard/ALL_'+str(i)+'/higgsCombineall_'+str(i)+'_M%s.AsymptoticLimits.mH125.root'%(values[i][j])
        
            limit= getLimits(file_name)
            
        
            if(resultType == "bbgg"): HHWWgg_factor = 1
            elif(resultType == "HY"): HHWWgg_factor = 1
           
        
      
       
            yellows[i].SetPoint(    j,    value[j], limit[4]*HHWWgg_factor*factor ) # + 2 sigma
            greens[i].SetPoint(     j,    value[j], limit[3]*HHWWgg_factor*factor ) # + 1 sigma
            medians[i].SetPoint(    j,    value[j], limit[2]*HHWWgg_factor*factor ) # median
            greens[i].SetPoint(  2*N-1-j, value[j], limit[1]*HHWWgg_factor*factor ) # - 1 sigma
            yellows[i].SetPoint( 2*N-1-j, value[j], limit[0]*HHWWgg_factor*factor ) # - 2 sigm
            

            # with open("limit_resolved_1000.txt","a") as f:
            #     f.write("Ymass: "+str(values[i][j])+"\n")
            # print("Ymass",values[i][j],limit[2]*0.0023)
        # HHWWgg_qqlnu_factor = campaignBRdict[args.campaign]
        factor=factor/10
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
    for i in mass:
        frame.GetXaxis().SetLimits(min(values[i]),max(values[i])+800)
    # frame.GetXaxis().SetLimits(min(values)-10,max(values)+10)
    c.SetLogy()
    factor=nexp-1
    texty=0.86
    for i in mass:
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
        medians[i].Draw('Psame')
        latex = ROOT.TLatex()
        latex.SetTextSize(0.04)  
        latex.SetNDC()
        textx,tty=getxy(medians,i)
        
        print(tty,"check")
        texty=texty-0.07
        if i >=3000:
            textx=textx-0.02
            texty=texty+0.005
        # text = "\$m_X$={}GeV(\$10^{}$)".format(i, factor) 
        text = "\$m_X={}GeV(10^{})$".format(i, factor)
        latex.SetTextSize(0.02)
        latex.DrawLatex(textx,texty, text)
        factor=factor-1



    CMS_lumi.CMS_lumi(c,4,11)
    ROOT.gPad.SetTicks(1,1)
    frame.Draw('sameaxis')
 
    yboost = args.yboost
    # x1 = 0.15
    x1=0.6
    x2=0.9
    # x2 = x1 + 0.24
    y2 = 0.9 + yboost
    y1 = 0.80 + yboost
    legend = TLegend(x1,y1,x2,y2)
    legend.SetFillStyle(0)
    legend.SetBorderSize(0)
    legend.SetTextSize(0.031)
    legend.SetTextFont(32)
    legend.AddEntry(medians[1000], "AsymptoticLimits CL_{s} expected",'L')
    legend.AddEntry(greens[1000], "#pm 1 std. deviation",'f')
#    legend.AddEntry(green, "AsymptoticLimits CL_{s} #pm 1 std. deviation",'f')
    legend.AddEntry(yellows[1000],"#pm 2 std. deviation",'f')
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
    # if(args.systematics): label.DrawLatex(0.7,0.7 + yboost,"SYST + STAT")
    # else: label.DrawLatex(0.7,0.7 + yboost,"Xmass=1000")
    
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
    c.SaveAs("%s_%s_%s_all_UpperLimit.pdf"%(outFile,args.lumiRescale,resultType))
    c.SaveAs("%s_%s_%s_all_UpperLimit.png"%(outFile,args.lumiRescale,resultType))
    c.SaveAs("%s_%s_%s_all_UpperLimit.C"%(outFile,args.lumiRescale,resultType))
    c.Close()
def getMXMY(filename):
    mx_my = re.search("combined_M(\d+)", filename)

    if mx_my:
        # mx = mx_my.group(1)
        my = mx_my.group(1)
        print(my)
    return int(my)
def main():
    mass=[1000,1800,2000,2400,2500,2600,2800,3000,3500,4000]
    values={}
    labels={}
    for j in mass:
        sigFiles=glob.glob('/eos/user/z/zhjie/CMSSW_10_2_13/src/flashggFinalFit/Datacard/ALL_'+str(j)+'/Datacard_sys*txt')
        value=[]
        label=[]
        print(sigFiles)
        for f in sigFiles:
            # print(f)
            y=getMXMY(f)
            value.append(y)
        value.sort()
    
        for i in value:
            l=str(i)
            l='M'+l
            label.append(l)
        values[j]=value
        labels[j]=label
    print(labels)

    resultType = args.resultType
    plotUpperLimits(labels,values,resultType)
if __name__ == '__main__':
    main()

#  'M60','M70','M80','M90',70,80,90,'M150','M170','M190','M250''M300','M350','M400',
