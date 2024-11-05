import ROOT
from ROOT import RooFit

file = ROOT.TFile("higgsCombine.generate_exp.GenerateOnly.mH125.123456.root", "READ")
directory = file.Get("toys")
c = ROOT.TCanvas("c","c",100,100,800,600)
stack = ROOT.THStack("stack", "Multiple Datasets")

for i in range(5):
    i=i+1
    dataset = directory.Get("toy_{}".format(i))
    x=ROOT.RooRealVar("CMS_hgg_mass","x",100,180)
    plot=x.frame()
    dataset.plotOn(plot)
    plot.Draw()
    c.Draw()
    c.SaveAs("test2_{}.png".format(i))
    # var = dataset.get().first()
    # hist = ROOT.TH1F("hist{}".format(i), "Dataset {}".format(i), 100, var.getMin(), var.getMax())
    # # hist.SetFillColor(colors[i])
    # dataset.fillHistogram(hist, ROOT.RooArgList(var))
    # stack.Add(hist)
    


    
   