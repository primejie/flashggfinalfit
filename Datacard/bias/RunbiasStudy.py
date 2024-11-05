#!/usr/bin/env python
# -*- coding: utf-8 -*-


## sample:
# python RunbiasStudy.py -d Datacard_sys_boost_masscut_combined_M100_cat2.root  -t

# python RunbiasStudy.py -d Datacard_sys_boost_masscut_combined_M100_cat2.root -f -c "--cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints   --rMin -5 --rMax 5  --freezeParameters MH"
# python RunbiasStudy.py -d Datacard_sys_boost_masscut_combined_M100_cat2.root -p --gaussianFit


from biasUtils import *
import matplotlib
from array import array
from os import *
import matplotlib.pyplot as plt
matplotlib.use('Agg')
from optparse import OptionParser
parser = OptionParser()
parser.add_option("-d","--datacard",default="Datacard.root")
parser.add_option("-w","--workspace",default="w")
parser.add_option("-t","--toys",action="store_true", default=False)
parser.add_option("-n","--nToys",default=2000,type="int")
parser.add_option("-f","--fits",action="store_true", default=False)
parser.add_option("-p","--plots",action="store_true", default=False)
parser.add_option("-e","--expectSignal",default=1,type="float")
parser.add_option("-m","--mH",default=125.,type="float")
parser.add_option("-c","--combineOptions",default="")
parser.add_option("-s","--seed",default=12345,type="int")
parser.add_option("--dryRun",action="store_true", default=False)
parser.add_option("--poi",default="r")
parser.add_option("--split",default=2000,type="int")
parser.add_option("--selectFunction",default=None)
parser.add_option("--gaussianFit",action="store_true", default=False)
(opts,args) = parser.parse_args()
print
if opts.nToys>opts.split and not opts.nToys%opts.split==0: raise RuntimeError('The number of toys %g needs to be smaller than or divisible by the split number %g'%(opts.nToys, opts.split))

import ROOT as r
r.gROOT.SetBatch(True)
r.gStyle.SetOptStat(2211)

sname=opts.datacard.split('.')[0]

ws = r.TFile(opts.datacard).Get(opts.workspace)

pdfs = rooArgSetToList(ws.allPdfs())
multipdfName = None
for pdf in pdfs:
    if pdf.InheritsFrom("RooMultiPdf"):
        if multipdfName is not None: raiseMultiError() 
        multipdfName = pdf.GetName()
        print 'Conduct bias study for multipdf called %s'%multipdfName
multipdf = ws.pdf(multipdfName)
print

varlist = rooArgSetToList(ws.allCats())
indexName = None
for var in varlist:
    if var.GetName().startswith('pdfindex'):
        if indexName is not None: raiseMultiError()
        indexName = var.GetName()
        print 'Found index called %s'%indexName
print

from collections import OrderedDict as od
indexNameMap = od()
for ipdf in range(multipdf.getNumPdfs()):
    if opts.selectFunction is not None:
        if not multipdf.getPdf(ipdf).GetName().count(opts.selectFunction): continue
    indexNameMap[ipdf] = multipdf.getPdf(ipdf).GetName()

if opts.toys:
    if not path.isdir('BiasToysn'): system('mkdir -p BiasToys')
    toyCmdBase = 'combine -m %.4f -d %s -M GenerateOnly  --toysNoSystematics --expectSignal %.4f -s %g --saveToys %s '%(opts.mH, opts.datacard, opts.expectSignal, opts.seed, opts.combineOptions)
    for ipdf,pdfName in indexNameMap.iteritems():
        name = shortName(pdfName)
        print("name: ",toyName(name))
        if opts.nToys > opts.split:
            for isplit in range(opts.nToys//opts.split):
                toyCmd = toyCmdBase + ' -t %g -n _%s_split%g --setParameters %s=%g --freezeParameters %s'%(opts.split, name, isplit, indexName, ipdf, indexName)
                run(toyCmd, dry=opts.dryRun)
                system('mv higgsCombine_%s* %s'%(name, toyName(name,split=isplit)))
        else: 
            toyCmd = toyCmdBase + ' -t %g -n _%s --setParameters %s=%g --freezeParameters %s'%(opts.nToys, name, indexName, ipdf, indexName)
            run(toyCmd, dry=opts.dryRun)
            system('mv higgsCombine_%s* %s'%(name, toyName(name)))
print

if opts.fits:
    if not path.isdir('BiasFits'): system('mkdir -p BiasFits')
    fitCmdBase = 'combine -m %.4f -d %s -M MultiDimFit -P %s --algo singles %s '%(opts.mH, opts.datacard, opts.poi, opts.combineOptions)
    for ipdf,pdfName in indexNameMap.iteritems():
        name = shortName(pdfName)
        if opts.nToys > opts.split:
            for isplit in range(opts.nToys//opts.split):
                fitCmd = fitCmdBase + ' -t %g -n _%s_split%g --toysFile=%s'%(opts.split, name, isplit, toyName(name,split=isplit))
                run(fitCmd, dry=opts.dryRun)
                system('mv higgsCombine_%s* %s'%(name, fitName(name,split=isplit)))
            run('hadd %s BiasFits/*%s*split*.root'%(fitName(name),name), dry=opts.dryRun)
        else:
            fitCmd = fitCmdBase + ' -t %g -n _%s --toysFile=%s'%(opts.nToys, name, toyName(name))
            run(fitCmd, dry=opts.dryRun)
            system('mv higgsCombine_%s* %s'%(name, fitName(name)))

if opts.plots:
    if not path.isdir('BiasPlots'): system('mkdir -p BiasPlots')
    pdfnames=[]
    means=[]
    mids=[]
    for ipdf,pdfName in indexNameMap.iteritems():
        name = shortName(pdfName)
        tfile = r.TFile(fitName(name))
        tree = tfile.Get('limit')
        pullHist = r.TH1F('pullsForTruth_%s'%name, 'Pull distribution using the envelope to fit %s'%name, 80, -4., 4.)
        pullHist.GetXaxis().SetTitle('Pull')
        pullHist.GetYaxis().SetTitle('Entries')
        plotentry=[]
        for itoy in range(opts.nToys):
            tree.GetEntry(3*itoy)
            if not getattr(tree,'quantileExpected')==-1: 
                raiseFailError(itoy,True) 
                continue
            bf = getattr(tree, 'r')
            tree.GetEntry(3*itoy+1)
            if not abs(getattr(tree,'quantileExpected')--0.32)<0.001: 
                raiseFailError(itoy,True) 
                continue
            lo = getattr(tree, 'r')
            tree.GetEntry(3*itoy+2)
            if not abs(getattr(tree,'quantileExpected')-0.32)<0.001: 
                raiseFailError(itoy,True) 
                continue
            hi = getattr(tree, 'r')
            diff = bf - opts.expectSignal
            unc = 0.5 * (hi-lo)
            if unc > 0.: 
                pullHist.Fill(diff/unc)
                plotentry.append(diff/unc)
        sorted_entry = sorted(plotentry)
        n = len(sorted_entry)
        print(n,"check n")
        if n % 2 == 1:
    
            median = sorted_entry[n // 2]
        else:
    
            middle1 = sorted_entry[n // 2 - 1]
            middle2 = sorted_entry[n // 2]
            median = (middle1 + middle2) / 2.0
        canv = r.TCanvas()
        pullHist.Draw()
        if opts.gaussianFit:
           r.gStyle.SetOptFit(111)
           pullHist.Fit('gaus')
           fit_result = pullHist.GetFunction("gaus")
           mean=fit_result.GetParameter(1)
        pdfnames.append(pdfName)
        means.append(mean)
        mids.append(median)
        canv.SaveAs('%s.pdf'%plotName(name))
        canv.SaveAs('%s.png'%plotName(name))
    # plt.scatter(pdfnames, means, label='mean',color='blue', marker='o')
    # plt.scatter(pdfnames, mids, label='median',color='red', marker='o')
    # plt.xlabel('pdf name')
    # plt.ylabel('bias')
    # plt.legend()
    # plt.savefig('bias.png')
    print(pdfnames)
    print(mids)
    canvas = r.TCanvas("canvas", "Scatter Plot", 800, 800)
    graph_mean = r.TGraph(len(pdfnames), array('d', range(1,len(pdfnames)+1)), array('d', means))
    graph_mean.SetMarkerStyle(20)
    graph_mean.SetMarkerColor(r.kBlue)
    

    graph_median = r.TGraph(len(pdfnames), array('d', range(1,len(pdfnames)+1)), array('d', mids))
    graph_median.SetMarkerStyle(20)
    graph_median.SetMarkerColor(r.kRed)

    graph_mean.Draw("AP")
    graph_median.Draw("P")

    graph_mean.GetYaxis().SetRangeUser(-0.5, 0.5)
    graph_mean.GetXaxis().Set(len(pdfnames),0,len(pdfnames))
   
        

    graph_median.GetYaxis().SetRangeUser(-0.5, 0.5)
    graph_median.GetXaxis().Set(len(pdfnames),0,len(pdfnames))
    for i, label in enumerate(pdfnames):
        graph_mean.GetXaxis().SetBinLabel(i+1, label)
        graph_median.GetXaxis().SetBinLabel(i+1, label)
    legend = r.TLegend(0.8, 0.8, 0.9, 0.9)
    legend.AddEntry(graph_mean, "mean", "p")
    legend.AddEntry(graph_median, "median", "p")
    legend.Draw()
    
    box1 = r.TBox(graph_mean.GetXaxis().GetXmin(), -0.2, graph_mean.GetXaxis().GetXmax(), 0.2)
    box1.SetFillColorAlpha(r.kGray, 0.3)  
    box1.Draw("same")  

    box2 = r.TBox(graph_mean.GetXaxis().GetXmin(), -0.14, graph_mean.GetXaxis().GetXmax(), 0.14)
    box2.SetFillColorAlpha(r.kGray+5, 0.3)  
    box2.Draw("same")    



    canvas.Update()
    canvas.SaveAs('%s.png'%sname)