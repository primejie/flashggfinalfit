import numpy as np
import ROOT
import json

from optparse import OptionParser


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
def get_options():

    parser = OptionParser()
    parser.add_option("--date",type='string',dest='date',default='18_02_2020_Mjj_merged_90GeV')  
    #parser.add_option("--date",type='string',dest='date',default='12_02_2020_mjjnorm')  
    parser.add_option("--mass",type='string',dest='mass',default='125') 
    parser.add_option("--inp-procs",type='string',dest='inp_procs',default='gghh')  
    parser.add_option("--inp-dir",type='string',dest="inp_dir",default='./Mjjgg/')
    #parser.add_option("--inp-dir-mjj",type='string',dest="inp_dir_mjj",default='/work/nchernya/DiHiggs/CMSSW_7_4_7/src/flashggFinalFit/Signal/output/mjj/18_02_2020_2D/')
    parser.add_option("--inp-dir-mjj",type='string',dest="inp_dir_mjj",default='/work/nchernya/DiHiggs/CMSSW_7_4_7/src/flashggFinalFit/Signal/output/mjj/18_02_2020_Mjj_merged_90GeV/')
    parser.add_option("--inp-file",type='string',dest="inp_file",default='CMS-HGG_sigfit_2016_2017_2018_18_02_2020.root')
    parser.add_option("--inp-file-mjj",type='string',dest="inp_file_mjj",default='workspace_out_mjj_18_02_2020_merged_90GeV.root')
    #parser.add_option("--inp-dir-mjj",type='string',dest="inp_dir_mjj",default='/work/nchernya/DiHiggs/CMSSW_7_4_7/src/flashggFinalFit/Signal/output/mjj/04_02_2020_v3/')
    #parser.add_option("--inp-file",type='string',dest="inp_file",default='CMS-HGG_sigfit_2016_2017_2018_04_02_2020.root')
    #parser.add_option("--inp-file-mjj",type='string',dest="inp_file_mjj",default='workspace_out_mjj_12_02_2020.root')
    parser.add_option("--out-dir",type='string',dest="out_dir",default='./Mjjgg/')
    #parser.add_option("--cats",type='string',dest="cats",default='DoubleHTag_0,DoubleHTag_1,DoubleHTag_2,DoubleHTag_3,DoubleHTag_4,DoubleHTag_5,DoubleHTag_6,DoubleHTag_7,DoubleHTag_8,DoubleHTag_9,DoubleHTag_10,DoubleHTag_11')
   # parser.add_option("--cats",type='string',dest="cats",default='DoubleHTag_0,DoubleHTag_1,DoubleHTag_2,DoubleHTag_3,DoubleHTag_4,DoubleHTag_5,DoubleHTag_6,DoubleHTag_7,DoubleHTag_8,DoubleHTag_9')
    parser.add_option("--cats",type='string',dest="cats",default='resolved_cat0')
    return parser.parse_args()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

(opt,args) = get_options()
cats = opt.cats.split(',')
input_procs = opt.inp_procs.split(',')

print(opt.inp_dir + opt.inp_file)

tfile = ROOT.TFile(opt.inp_file)
tfile_mjj = ROOT.TFile(opt.inp_file_mjj)
ws_mgg = tfile.Get("multipdf")
ws_mjj = tfile_mjj.Get("multipdf")
for num,f in enumerate(input_procs):
  for cat_num,cat in enumerate(cats) : 
  #for cat_num,cat in enumerate([cats[0]]) : 
    pdf_mjj = "CMS_hgg_%s_13TeV_bkgshape"%(cat)
    pdf_mgg = "CMS_hgg_%s_13TeV_bkgshape"%(cat)
    #ws_mjj.pdf(pdf_mjj).Print("v")
    print("pdf",pdf_mjj,pdf_mgg)
    pdfjj=ws_mjj.pdf(pdf_mjj)
    pdfjj.SetName("CMS_hjj_resolved_cat0_13TeV_bkgshape")
    getattr(ws_mgg, 'import')(pdfjj,ROOT.RooCmdArg())
    getattr(ws_mgg, 'import')(ws_mjj.var("Dijet_mass"),ROOT.RooCmdArg())
    prod_pdf = "CMS_hjjgg_%s_13TeV_bkgshape"%(cat)
    #print ws_mgg.pdf(pdf_mgg)
    #print ws_mjj.pdf(pdf_mjj)
    sig_prod_pdf = ROOT.RooProdPdf(prod_pdf,"",ws_mgg.pdf(pdf_mgg),pdfjj)
    #sig_prod_pdf.Print("v") 
    getattr(ws_mgg, 'import')(sig_prod_pdf,ROOT.RooFit.RecycleConflictNodes())
    #Save normalization for combine
    #sig_prod_pdf_norm = (ws_mgg.function(pdf_mgg+"_norm")).clone(prod_pdf+"_norm")
    sig_prod_pdf_norm = (ws_mjj.var(pdf_mjj+"_norm")).clone(prod_pdf+"_norm")  #take norm from mjj?
    getattr(ws_mgg, 'import')(sig_prod_pdf_norm,ROOT.RooFit.RecycleConflictNodes())
    ##Printing normalization
   # ws_mgg.var("MH").setVal(125.)  #just to check that the normalization is the same for Mgg and Mjj, it is of course.
  #  print 'mgg : ',ws_mgg.function(pdf_mgg+"_norm").getVal(),', mjj : ',ws_mjj.function(pdf_mjj+"_norm").getVal(), ", imported product : ",ws_mgg.function(prod_pdf+"_norm").getVal() #just to check that the normalization is the same for Mgg and Mjj, it is of course.
    
 
f_out = ROOT.TFile.Open(opt.out_dir+"CMS-HGG_multipdf_resolved_cat0_2016_2017_2018_%s_%s.root"%(opt.mass,opt.cats),"RECREATE")
ws_mgg.Write()
f_out.Close()
