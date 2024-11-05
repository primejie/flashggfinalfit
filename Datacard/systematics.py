# Python file to store systematics: for STXS analysis

# Comment out all nuisances that you do not want to include

# THEORY SYSTEMATICS:

# For type:constant
#  1) specify same value for all processes
#  2) define process map json in ./theory_uncertainties (add process names where necessary!)

# For type:factory
# Tier system: adds different uncertainties to dataframe
#   1) shape: absolute yield of process kept constant, shape effects i.e. calc migrations across cats
#   2) ishape: as (1) but absolute yield for proc x cat is allowed to vary
#   3) norm: absolute yield of production mode (s0) kept constant but migrations across sub-processes e.g. STXS bins.Same value in each category.
#   4) inorm: as (3) but absolute yield of production mode (s0) can vary
#   5) inc: variations in production mode (s0), same value for each subprocess in each category
# Relations: shape = ishape/inorm
#            norm  = inorm/inc
# Specify as list in dict: e.g. 'tiers'=['inc','inorm','norm','ishape','shape']

theory_systematics = [
                # Normalisation uncertainties: enter interpretations
                {'name':'BR_hgg','title':'BR_hgg','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':"0.98/1.021"},
                # New scheme for ggH stage 1.2 
                
          
                {'name':'QCDscale_ggHH','title':'QCDscale','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':"0.950/1.022"},
                {'name':'pdf_Higgs_ggHH','title':'pdf_Higgs','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':"1.030"},
                {'name':'alphaS_ggH','title':'alphaS','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':"1.026"}
              
               
              ]
# PDF weight
# for i in range(1,60): theory_systematics.append( {'name':'pdfWeight_%g'%i, 'title':'CMS_hgg_pdfWeight_%g'%i, 'type':'factory','prior':'lnN','correlateAcrossYears':1,'tiers':['shape']} )

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# EXPERIMENTAL SYSTEMATICS
# correlateAcrossYears = 0 : no correlation
# correlateAcrossYears = 1 : fully correlated
# correlateAcrossYears = -1 : partially correlated

experimental_systematics = [
                # Updated luminosity partial-correlation scheme: 13/5/21 (recommended simplified nuisances)
                {'name':'lumi_13TeV_Uncorrelated','title':'lumi_13TeV_Uncorrelated','type':'constant','prior':'lnN','correlateAcrossYears':0,'value':{'2016pre':'1.010','2016post':'1.010','2017':'1.020','2018':'1.015'}},
                {'name':'lumi_13TeV_Correlated','title':'lumi_13TeV_Correlated','type':'constant','prior':'lnN','correlateAcrossYears':-1,'value':{'2016pre':'1.006','2016post':'1.006','2017':'1.009','2018':'1.020'}},
                {'name':'lumi_13TeV_Correlated_1718','title':'lumi_13TeV_Correlated_1718','type':'constant','prior':'lnN','correlateAcrossYears':-1,'value':{'2016pre':'-','2016post':'-','2017':'1.006','2018':'1.002'}},
                {'name':'photon_id_sf_Diphoton_Photon_','title':'CMS_hgg_MVASF','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'photon_presel_sf_Diphoton_Photon_','title':'CMS_hgg_PreselSF','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'electron_veto_sf_Diphoton_Photon_','title':'CMS_hgg_electronVetoSF','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'trigger_sf_','title':'CMS_hgg_TriggerWeight','type':'factory','prior':'lnN','correlateAcrossYears':0},
               
                {'name':'L1_prefiring_sf_','title':'CMS_hgg_prefire','type':'factory','prior':'lnN','correlateAcrossYears':0},
               
                {'name':'puWeight_','title':'CMS_hgg_puWeight','type':'factory','prior':'lnN','correlateAcrossYears':0},

                {'name':'btag_deepjet_sf_SelectedbJet_jes_','title':'CMS_hgg_btag_jes','type':'factory','prior':'lnN','correlateAcrossYears':1},
                {'name':'btag_deepjet_sf_SelectedbJet_lf_','title':'CMS_hgg_btag_lf','type':'factory','prior':'lnN','correlateAcrossYears':1},
                {'name':'btag_deepjet_sf_SelectedbJet_hfstats1_','title':'CMS_hgg_btag_hfstats1','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'btag_deepjet_sf_SelectedbJet_hfstats2_','title':'CMS_hgg_btag_hfstats2','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'btag_deepjet_sf_SelectedbJet_cferr1_','title':'CMS_hgg_btag_cferr1','type':'factory','prior':'lnN','correlateAcrossYears':1},
                {'name':'btag_deepjet_sf_SelectedbJet_cferr2_','title':'CMS_hgg_btag_cferr2','type':'factory','prior':'lnN','correlateAcrossYears':1},
                {'name':'btag_deepjet_sf_SelectedbJet_hf_','title':'CMS_hgg_btag_hf','type':'factory','prior':'lnN','correlateAcrossYears':1},
                {'name':'btag_deepjet_sf_SelectedbJet_lfstats1_','title':'CMS_hgg_btag_lfstats1','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'btag_deepjet_sf_SelectedbJet_lfstats2_','title':'CMS_hgg_btag_lfstats2','type':'factory','prior':'lnN','correlateAcrossYears':0},

                # {'name':'PNet_','title':'CMS_hgg_ParticalNet','type':'factory','prior':'lnN','correlateAcrossYears':0},

                {'name':'JES','title':'CMS_scale_j','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'JER','title':'CMS_res_j','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'FJER','title':'CMS_res_fj','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'FJES','title':'CMS_scale_fj','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'FJHEM','title':'CMS_FatjetHEM','type':'factory','prior':'lnN','correlateAcrossYears':0},
                {'name':'JetHEM','title':'CMS_JetHEM','type':'factory','prior':'lnN','correlateAcrossYears':0}

              ]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Shape nuisances: effect encoded in signal model
# mode = (other,scalesGlobal,scales,scalesCorr,smears): match the definition in the signal models

signal_shape_systematics = [
              
                {'name':'scale','title':'scale','type':'signal_shape','mode':'scales','mean':'0.0','sigma':'1.0'},
            
                {'name':'material','title':'material','type':'signal_shape','mode':'scalesCorr','mean':'0.0','sigma':'1.0'},

                {'name':'fnuf','title':'fnuf','type':'signal_shape','mode':'scalesCorr','mean':'0.0','sigma':'1.0'},
        
                {'name':'smear','title':'smear','type':'signal_shape','mode':'smears','mean':'0.0','sigma':'1.0'}
           
              ]
