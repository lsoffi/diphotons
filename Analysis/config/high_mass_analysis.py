#!/usr/bin/env cmsRun

import FWCore.ParameterSet.Config as cms
import FWCore.Utilities.FileUtils as FileUtils

process = cms.Process("Analysis")

#
# general stuff
#
process.load("FWCore.MessageService.MessageLogger_cfi")

process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
from Configuration.AlCa.GlobalTag import GlobalTag

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32( 1000 )

process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
                                                   highMassCorrectedDiphotonsMC = cms.PSet(initialSeed = cms.untracked.uint32(664)),
                                                  )


### process.genGravitons = cms.EDProducer("GenParticlePruner",
###                                     src = cms.InputTag("flashggPrunedGenParticles"),
###                                     select = cms.vstring("drop  *  ", # this is the default
###                                                          "keep pdgId = 5100039",
###                                                          )
###                                     )
### if "Grav" in customize.datasetName():
###     bookCandViewNtProducer(process,"genGr","genGravitons")
###     addGloabalFloat(diphotonDumper.globalVariables,process,"genGr","genVtxZ","vertex.z")
### 

#
# load job options
#
from diphotons.MetaData.JobConfig import customize
customize.setDefault("maxEvents",10000)
customize.setDefault("targetLumi",1.e+3)

## 80mb 1.7/fb
## customize.setDefault("puTarget",
##                       '4.98e+04,3.4e+05,3.94e+05,4.15e+05,6.23e+05,7.74e+05,1.27e+06,4e+06,2.08e+07,7.66e+07,1.64e+08,2.42e+08,2.8e+08,2.74e+08,2.29e+08,1.62e+08,9.64e+07,4.8e+07,2.02e+07,7.33e+06,2.36e+06,7.07e+05,2.09e+05,6.58e+04,2.34e+04,9.84e+03,4.85e+03,2.63e+03,1.46e+03,803,428,220,108,51.2,23.3,10.1,4.24,1.7,0.655,0.242,0.0859,0.0292,0.00954,0.00299,0.0009,0.00026,7.19e-05,1.91e-05,4.88e-06,1.19e-06,2.81e-07,6.33e-08'
## )

### ## 69mb 2.4/fb
### customize.setDefault("puTarget",
###                       '1.435e+05,6.576e+05,8.781e+05,1.304e+06,2.219e+06,5.052e+06,1.643e+07,6.709e+07,1.975e+08,3.527e+08,4.44e+08,4.491e+08,3.792e+08,2.623e+08,1.471e+08,6.79e+07,2.748e+07,1.141e+07,5.675e+06,3.027e+06,1.402e+06,5.119e+05,1.467e+05,3.53e+04,8270,2235,721.3,258.8,97.27,36.87,13.73,4.932,1.692,0.5519,0.1706,0.04994,0.01383,0.003627,0.0008996,0.0002111,4.689e-05,9.854e-06,1.959e-06,3.686e-07,6.562e-08,1.105e-08,1.762e-09,2.615e-10,4.768e-11,0,0,0'
### )

## Modiond 16
## customize.setDefault("puTarget",
##                    "1.34e+05,6.34e+05,8.42e+05,1.23e+06,2.01e+06,4.24e+06,1.26e+07,4.88e+07,1.56e+08,3.07e+08,4.17e+08,4.48e+08,4.04e+08,3.05e+08,1.89e+08,9.64e+07,4.19e+07,1.71e+07,7.85e+06,4.2e+06,2.18e+06,9.43e+05,3.22e+05,8.9e+04,2.16e+04,5.43e+03,1.6e+03,551,206,80.1,31.2,11.9,4.38,1.54,0.518,0.165,0.0501,0.0144,0.00394,0.00102,0.000251,5.87e-05,1.3e-05,2.74e-06,5.47e-07,1.04e-07,1.86e-08,3.18e-09,5.16e-10,9.35e-11")

# # Spring16 2016 0.2/fb
# customize.setDefault("puTarget",
#                      "1.109e-08,1.277e-05,8.702e-05,0.0001387,0.000164,0.0002515,0.0001906,0.0005275,0.0008447,0.001411,0.002905,0.006861,0.02123,0.05716,0.09932,0.1283,0.1471,0.1517,0.1324,0.09691,0.06379,0.0402,0.02412,0.0132,0.006383,0.002693,0.0009978,0.0003421,0.0001291,7.043e-05,5.531e-05,4.97e-05,4.545e-05,4.136e-05,3.762e-05,3.449e-05,3.209e-05,3.039e-05,2.924e-05,2.846e-05,2.786e-05,2.727e-05,2.661e-05,2.582e-05,2.486e-05,2.372e-05,2.243e-05,2.1e-05,1.947e-05,1.788e-05")

# ## Spring16 2016 0.6/fb
# customize.setDefault("puTarget",
#                      "2.699e-08,2.225e-05,9.239e-05,0.0001369,0.0002404,0.0003861,0.000503,0.001261,0.003494,0.01008,0.02443,0.04579,0.07122,0.102,0.1304,0.1456,0.1417,0.1154,0.07907,0.04912,0.03089,0.02043,0.01319,0.007653,0.003846,0.001661,0.0006239,0.0002155,8.165e-05,4.459e-05,3.503e-05,3.147e-05,2.878e-05,2.619e-05,2.382e-05,2.184e-05,2.032e-05,1.924e-05,1.852e-05,1.802e-05,1.764e-05,1.727e-05,1.685e-05,1.635e-05,1.574e-05,1.502e-05,1.42e-05,1.33e-05,1.233e-05,1.132e-05")

# ## Spring16 2016 2/fb
# customize.setDefault("puTarget",
#                     "2.7e-08,2.225e-05,9.24e-05,0.0001369,0.0002404,0.0003862,0.000503,0.001261,0.003494,0.01008,0.02443,0.0458,0.07122,0.102,0.1304,0.1456,0.1417,0.1154,0.07907,0.04912,0.03088,0.02042,0.01319,0.007654,0.003846,0.001661,0.000624,0.0002156,8.165e-05,4.46e-05,3.503e-05,3.148e-05,2.879e-05,2.62e-05,2.382e-05,2.184e-05,2.033e-05,1.925e-05,1.852e-05,1.802e-05,1.764e-05,1.727e-05,1.686e-05,1.635e-05,1.574e-05,1.502e-05,1.42e-05,1.33e-05,1.233e-05,1.132e-05")


## Spring16 2016 2.55/fb, but many runs missing from pu json
customize.setDefault("puTarget",
                     "1.369e-06,1.549e-05,4.233e-05,9.232e-05,0.0001865,0.0002974,0.0007702,0.005968,0.01452,0.01918,0.02569,0.03709,0.05417,0.07408,0.0928,0.1055,0.1095,0.1042,0.09134,0.07505,0.05881,0.04434,0.03206,0.02198,0.01415,0.008512,0.004783,0.002515,0.001241,0.0005762,0.0002533,0.0001068,4.449e-05,1.956e-05,1.006e-05,6.499e-06,5.098e-06,4.461e-06,4.107e-06,3.879e-06,3.722e-06,3.607e-06,3.514e-06,3.427e-06,3.337e-06,3.236e-06,3.119e-06,2.984e-06,2.833e-06,2.666e-06")

import FWCore.ParameterSet.VarParsing as VarParsing
customize.options.register ('selection',
                            "diphoton", # default value
                            VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                            VarParsing.VarParsing.varType.string,          # string, int, or float
                            "selection")
customize.options.register ('massCut',
                            "200", # default value
                            VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                            VarParsing.VarParsing.varType.string,          # string, int, or float
                            "massCut")
customize.options.register ('ptLead',
                            100, # default value
                            VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                            VarParsing.VarParsing.varType.float,          # string, int, or float
                            "ptLead")
customize.options.register ('ptSublead',
                            100, # default value
                            VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                            VarParsing.VarParsing.varType.float,          # string, int, or float
                            "ptSublead")
customize.options.register ('scaling',
                            False, # default value
                            VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                            VarParsing.VarParsing.varType.bool,          # string, int, or float
                            "scaling")
customize.options.register ('doeleId',
                            False, # default value
                            VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                            VarParsing.VarParsing.varType.bool,          # string, int, or float
                            "doeleId")
customize.options.register ('eleId',
                            "passLooseId", # default value
                            VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                            VarParsing.VarParsing.varType.string,          # string, int, or float
                            "eleId")
customize.options.register ('trigger',
                            "", # default value
                            VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                            VarParsing.VarParsing.varType.string,          # string, int, or float
                            "trigger")
customize.options.register ('mctrigger',
                            "", # default value
                            VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                            VarParsing.VarParsing.varType.string,          # string, int, or float
                            "mctrigger")
customize.options.register ('dohltMatch',
                            False, # default value
                            VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                            VarParsing.VarParsing.varType.bool,          # string, int, or float
                            "dohltMatch")
customize.options.register ('dol1Match',
                            False, # default value
                            VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                            VarParsing.VarParsing.varType.bool,          # string, int, or float
                            "dol1Match")
customize.options.register ('idversion',
                            "V2", # default value
                            VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                            VarParsing.VarParsing.varType.string,          # string, int, or float
                            "idversion")
customize.options.register ('applyDiphotonCorrections',
                            True, # default value
                            VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                            VarParsing.VarParsing.varType.bool,          # string, int, or float
                            "applyDiphotonCorrections")
customize.options.register ('diphotonCorrectionsVersion',
                            "", # default value
                            VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                            VarParsing.VarParsing.varType.string,          # string, int, or float
                            "diphotonCorrectionsVersion")
customize.options.register ('useVtx0',
                            False, # default value
                            VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                            VarParsing.VarParsing.varType.bool,          # string, int, or float
                            "useVtx0")
customize.options.register ('addRegressionInput',
                            False, # default value
                            VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                            VarParsing.VarParsing.varType.bool,          # string, int, or float
                            "addRegressionInput")
customize.options.register ('histosOnly',
                            False, # default value
                            VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                            VarParsing.VarParsing.varType.bool,          # string, int, or float
                            "histosOnly")
customize.options.register ('extraActvity',
                            False, # default value
                            VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                            VarParsing.VarParsing.varType.bool,          # string, int, or float
                            "extraActvity")


customize.parse()


from Configuration.AlCa.autoCond import autoCond
if customize.options.processType == "data":
    process.GlobalTag = GlobalTag(process.GlobalTag, autoCond['run2_data'].replace("::All","") )
else:
    process.GlobalTag = GlobalTag(process.GlobalTag, autoCond['run2_mc'].replace("::All",""))



#
# analysis configuration
#
dataTriggers=[]
mcTriggers=[]
doSinglePho=False
doDoublePho=True
doDoublePho0T=False
invertEleVeto=False
## dumpBits=["HLT_DoublePhoton60","HLT_DoublePhoton85","HLT_Photon250_NoHE","HLT_Photon165_HE","HLT_ECALHT800"]
dumpBits=["HLT_DoublePhoton60","HLT_ECALHT800"]
askTriggerOnMc=False
extraSysModules=[]

# parse selection and trigger config options
if customize.selection == "diphoton":
    mcTriggers=["HLT_DoublePhoton85*","HLT_Photon250_NoHE*","HLT_DoublePhoton60*"] ## ,
    dataTriggers=mcTriggers
elif customize.selection == "photon":
    dataTriggers=["HLT_Photon165*"]
    mcTriggers=dataTriggers
    doSinglePho=True
    doDoublePho=False
elif customize.selection == "electron":
    dataTriggers=["HLT_Ele27_eta2p1_WPLoose_Gsf_v*"]
    ## mcTriggers=["HLT_Ele27_eta2p1_WP75_Gsf_v*"]
    mcTriggers=dataTriggers
    askTriggerOnMc=True
    invertEleVeto=True
elif customize.selection == "dielectron":
    dataTriggers=["*"]
    mcTriggers=dataTriggers
    if customize.options.trigger == "":
        sys.exit("please complete dielectron selection",-1)
        invertEleVeto=True
elif customize.selection == "dielectron0T":
    invertEleVeto=True
    doDoublePho0T=True
    mcTriggers=[]
    askTriggerOnMc=False

if customize.options.trigger != "":
    dataTriggers = customize.options.trigger.split(",")
    mcTriggers = [] ## dataTriggers
    dumpBits.extend( map(lambda x: x.rstrip("*"), dataTriggers)  )
    askTriggerOnMc=False

if customize.options.mctrigger != "":
    mcTriggers = customize.options.mctrigger.split(",")
dumpBits=set(dumpBits)

#
# define minitrees and histograms
#
from flashgg.Taggers.diphotonDumper_cfi import diphotonDumper 
from flashgg.Taggers.photonDumper_cfi import photonDumper 
import flashgg.Taggers.dumperConfigTools as cfgTools

sourceDiphotons = "flashggDiPhotons"

# Track count vertex
if "0T" in customize.idversion:
    sourceDiphotons = "flashggDiPhotonsTrkCount"

if customize.useVtx0:
    from flashgg.MicroAOD.flashggDiPhotons_cfi import flashggDiPhotonsLite
    process.flashggDiPhotonsVtx0 = flashggDiPhotonsLite.clone(VertexSelectorName="FlashggZerothVertexSelector",whichVertex=cms.uint32(0))
    sourceDiphotons = "flashggDiPhotonsVtx0"

diphotonDumper.processId = "test"
diphotonDumper.dumpTrees = False
diphotonDumper.dumpWorkspace = False
diphotonDumper.quietRooFit = True
diphotonDumper.maxCandPerEvent=1
diphotonDumper.nameTemplate = "$PROCESS_$SQRTS_$LABEL_$SUBCAT"
diphotonDumper.throwOnUnclassified = cms.bool(False)

# import default dumper configuration
import diphotons.Analysis.dumperConfig as dumpCfg

variables, histograms, variablesSinglePho, histogramsSinglePho = dumpCfg.getDefaultConfig()

# add extra variables if needed
if customize.addRegressionInput:
    dumpCfg.addRegressionInput(variables)

if (customize.selection=="diphoton" or customize.selection=="photon"):
    dumpCfg.addRandomCones(variables,variablesSinglePho,histograms,histogramsSinglePho)

if customize.extraActvity:
    from diphotons.Analysis.extraActivityConfig import addGlobalVariables
    addGlobalVariables(process,diphotonDumper)

# HLT matching
if customize.processType == "data" and customize.dohltMatch:
    extraSysModules.append(
        cms.PSet( PhotonMethodName = cms.string("FlashggPhotonHLTMatch"),
                  MethodName = cms.string("FlashggDiPhotonFromPhoton"),
                  Label = cms.string("hltMatch"),
                  NSigmas = cms.vint32(),
                  ApplyCentralValue = cms.bool(True),
                  trgBitsSrc = cms.InputTag("TriggerResults","","HLT"),
                  trgObjectsSrc = cms.InputTag("selectedPatTrigger"),
                  pathNames = cms.vstring(dumpBits),
                  deltaRmax = cms.double(0.3),
                  )
        )
    for bit in dumpBits:
        variables.extend( [ "lead%sMatch   := leadingPhoton.userInt('%s')"                                                    % (bit,bit),
                            "lead%sDr      := ?leadingPhoton.userInt('%s')==1?leadingPhoton.userFloat('%sCandDR'):999."       % (bit,bit,bit),
                            "lead%sPt      := ?leadingPhoton.userInt('%s')==1?leadingPhoton.userFloat('%sCandPt'):0."         % (bit,bit,bit),
                            "sublead%sMatch:= subLeadingPhoton.userInt('%s')"                                                 % (bit,bit),
                            "sublead%sDr   := ?subLeadingPhoton.userInt('%s')==1?subLeadingPhoton.userFloat('%sCandDR'):999." % (bit,bit,bit),
                            "sublead%sPt   := ?subLeadingPhoton.userInt('%s')==1?subLeadingPhoton.userFloat('%sCandPt'):0."   % (bit,bit,bit),
                            ] )
    
# L1 matching
if customize.processType == "data" and customize.dol1Match:
    extraSysModules.append(
        cms.PSet( PhotonMethodName = cms.string("FlashggPhotonL1Match"),
                  MethodName = cms.string("FlashggDiPhotonFromPhoton"),
                  Label = cms.string("l1Match"),
                  NSigmas = cms.vint32(),
                  ApplyCentralValue = cms.bool(True),
                  l1EgmSrc = cms.InputTag("caloStage2Digis:EGamma"),
                  ## l1JetSrc = cms.InputTag("caloStage2Digis:Jet"),
                  deltaRmax = cms.double(0.3),
                  )
        )
    ## for obj in ["Egm", "Jet"]:
    for obj in ["Egm"]:
        variables.extend(  ["leadL1%sMatch   := leadingPhoton.userInt('l1%sMatch')"                                                      % (obj,obj),                
                            "leadL1%sDr      := ?leadingPhoton.userInt('l1%sMatch')==1?leadingPhoton.userFloat('l1%sCandDR'):999."       % (obj,obj,obj),
                            "leadL1%sPt      := ?leadingPhoton.userInt('l1%sMatch')==1?leadingPhoton.userFloat('l1%sCandPt'):0."         % (obj,obj,obj),
                            "subleadL1%sMatch:= subLeadingPhoton.userInt('l1%sMatch')"                                                   % (obj,obj),                
                            "subleadL1%sDr   := ?subLeadingPhoton.userInt('l1%sMatch')==1?subLeadingPhoton.userFloat('l1%sCandDR'):999." % (obj,obj,obj),
                            "subleadL1%sPt   := ?subLeadingPhoton.userInt('l1%sMatch')==1?subLeadingPhoton.userFloat('l1%sCandPt'):0."   % (obj,obj,obj),
                            ] )

# electron matching
if invertEleVeto and customize.doeleId:
    from flashgg.MicroAOD.flashggLeptonSelectors_cff import flashggSelectedElectrons
    process.flashggIdentifiedElectrons = flashggSelectedElectrons.clone( 
        src=cms.InputTag("flashggSelectedElectrons"),
        cut=cms.string(customize.eleId)
        )
    # process.flashggSelectedElectrons.cut = customize.eleId
    extraSysModules.append(
        cms.PSet( PhotonMethodName = cms.string("FlashggPhotonEleMatch"),
                  MethodName = cms.string("FlashggDiPhotonFromPhoton"),
                  Label = cms.string("eleMatch"),
                  NSigmas = cms.vint32(),
                  ApplyCentralValue = cms.bool(True),
                  electronsSrc = cms.InputTag("flashggIdentifiedElectrons"),
                  )
        )
    variables.extend( ["leadEleMatch    := leadingPhoton.hasUserCand('eleMatch')",
                       "subleadEleMatch := subLeadingPhoton.hasUserCand('eleMatch')"
                       ] )
    # store cut-based IDs
    for eid in "Loose", "Medium", "Tight":
        variables.extend( [
                       "leadEleIs%s    := ?leadingPhoton.hasUserCand('eleMatch')?leadingPhoton.userCand('eleMatch').pass%sId:0"       % (eid,eid),
                       "subleadEleIs%s := ?subLeadingPhoton.hasUserCand('eleMatch')?subLeadingPhoton.userCand('eleMatch').pass%sId:0" % (eid,eid)
                       ])
        
# trigger filtering
from HLTrigger.HLTfilters.hltHighLevel_cfi import hltHighLevel
if customize.processType == "data" and not "electron" in customize.selection:
    if "Prompt" in customize.datasetName() or "04Dec" in customize.datasetName() or "16Dec2015" in customize.datasetName(): 
        filterProc = "RECO"
    else: 
        filterProc = "PAT"
    diphotonDumper.globalVariables.addTriggerBits = cms.PSet(
        tag=cms.InputTag("TriggerResults","",filterProc),bits=cms.vstring("eeBadScFilter","goodVertices")
        )
elif len(dumpBits) > 0:
    if doDoublePho:
        diphotonDumper.globalVariables.addTriggerBits = cms.PSet(
            tag=cms.InputTag("TriggerResults","","HLT"),bits=cms.vstring(dumpBits)
            )
    if doSinglePho:
        photonDumper.globalVariables.addTriggerBits = cms.PSet(
            tag=cms.InputTag("TriggerResults","","HLT"),bits=cms.vstring(dumpBits)
            )

# categories definition
if ":" in customize.massCut:
    massCutEB,massCutEE = map(float,customize.massCut.split(":"))
    massCut = min(massCutEB,massCutEE)
else:
    massCutEB,massCutEE = None,None
    massCut = float(customize.massCut)

if massCutEB or massCutEE:
    cfgTools.addCategory(diphotonDumper,"RejectLowMass",
                         "   (max(abs(leadingPhoton.superCluster.eta),abs(subLeadingPhoton.superCluster.eta))<1.4442 && mass <= %f)"
                         "|| (max(abs(leadingPhoton.superCluster.eta),abs(subLeadingPhoton.superCluster.eta))>1.566  && mass <= %f)" %
                                            (massCutEB,massCutEE),-1)
cfgTools.addCategories(diphotonDumper,
                       [## cuts are applied in cascade
                        ## ("all","1"),
                        ("EBHighR9","max(abs(leadingPhoton.superCluster.eta),abs(subLeadingPhoton.superCluster.eta))<1.4442"
                         "&& min(leadingPhoton.r9,subLeadingPhoton.r9)>0.94",0),
                        ("EBLowR9","max(abs(leadingPhoton.superCluster.eta),abs(subLeadingPhoton.superCluster.eta))<1.4442",0),
                        ("EEHighR9","min(leadingPhoton.r9,subLeadingPhoton.r9)>0.94",0),
                        ("EELowR9","1",0),
                        ],
                       variables=variables,
                       histograms=histograms
                       )

# single photon dumper
photonDumper.processId = "test"
photonDumper.dumpTrees = False
photonDumper.dumpWorkspace = False
photonDumper.quietRooFit = True
photonDumper.maxCandPerEvent=2
photonDumper.nameTemplate = "$PROCESS_$SQRTS_$LABEL_$SUBCAT"
cfgTools.addCategories(photonDumper,
                       [## cuts are applied in cascade
                        ("EBAnomalous","abs(superCluster.eta)<1.4442 && sqrt(sipip)<0.01 && full5x5_sigmaIetaIeta>0.0105",0),
                        ("EBHighR9","abs(superCluster.eta)<1.4442 && r9>0.94",0),
                        ("EBLowR9", "abs(superCluster.eta)<1.4442",0),
                        ("EEHighR9","r9>0.94",0),
                        ("EELowR9","1",0),
                        ],
                       variables=variablesSinglePho,
                       histograms=histogramsSinglePho,
                       )

# gen-level diphoton pairs dumper    
from flashgg.Taggers.genDiphotonDumper_cfi import genDiphotonDumper
from flashgg.Taggers.globalVariables_cff import globalVariables
genDiphotonDumper.dumpGlobalVariables = True
genDiphotonDumper.globalVariables = globalVariables
cfgTools.addCategories(genDiphotonDumper,
                       [("EB","max(abs(leadingPhoton.eta),abs(subLeadingPhoton.eta))<1.4442",0),
                        ("EE","1",0)
                        ],
                       variables=["genMass := mass","pt",
                                  "genLeadPt := leadingPhoton.pt",
                                  "genSubeadPt := subLeadingPhoton.pt",
                                  ],
                       histograms=["genMass>>genmass(1500,0,15000)",
                                   ]
                       )

# restricted set of variables to be dumped for ancillary event selections
minimalDumper = diphotonDumper.clone()
cfgTools.dumpOnly(minimalDumper,
                  ["mass","pt","genMass","satRegressedMass","regressedMass",
                   "leadEnergy","subLeadEnergy",
                   "leadSatRegressedEnergy","subLeadSatRegressedEnergy",
                   "leadRegressedEnergy","subLeadRegressedEnergy",
                   "leadIsSat","subLeadIsSat","leadIsWeird","subLeadIsWeird",
                   "leadPt","leadEta","leadScEta","leadPhi",
                   "subleadPt","subleadEta","subleadScEta","subleadPhi",
                   "leadBlockPhoIso","subleadBlockPhoIso",
                   "leadBlockChIso","subleadBlockChIso",
                   "leadRndConePhoIso","leadRndConeChIso",
                   "subleadRndConePhoIso","subleadRndConeChIso",
                   "leadRndConeChIso0","leadRndConeChIso1","leadRndConeChIso2","leadRndConeChIso3",
                   "leadRndConeChIso4","leadRndConeChIso5","leadRndConeChIso6","leadRndConeChIso7","leadRndConeChIso8",
                   "subleadRndConeChIso0","subleadRndConeChIso1","subleadRndConeChIso2","subleadRndConeChIso3",
                   "subleadRndConeChIso4","subleadRndConeChIso5","subleadRndConeChIso6","subleadRndConeChIso7","subleadRndConeChIso8",
                   "leadMatchType","leadGenIso",
                   "subleadMatchType","subleadGenIso",
                   "leadPhoIsoEA","subleadPhoIsoEA",
                   "leadPhoIso","subleadPhoIso",
                   "leadChIso","subleadChIso",
                   "leadSigmaIeIe","subleadSigmaIeIe",
                   "leadHoE","subleadHoE",
                   ])



# set up event selection(s)
from diphotons.Analysis.DiPhotonAnalysis import DiPhotonAnalysis
analysis = DiPhotonAnalysis(diphotonDumper,
                            massCut=massCut,ptLead=customize.ptLead,ptSublead=customize.ptSublead,scaling=customize.scaling, ## kinematic cuts
                            computeMVA=False,
                            genIsoDefinition=("genIso",10.),
                            dataTriggers=dataTriggers,
                            mcTriggers=mcTriggers,
                            askTriggerOnMc=askTriggerOnMc, ## if mcTriggers is not empty will still compute efficiencies
                            singlePhoDumperTemplate=photonDumper,
                            applyDiphotonCorrections=customize.applyDiphotonCorrections,
                            diphotonCorrectionsVersion=customize.diphotonCorrectionsVersion,
                            sourceDiphotons=sourceDiphotons,
                            extraSysModules=extraSysModules
                            )

dumpKinTree=False
if customize.datasetName():
    # drop samples overlap
    if "GJet-HT" in customize.datasetName() or "GJets_DR-0p4_HT" in customize.datasetName():
        analysis.keepPFOnly = True
    elif "QCD" in customize.datasetName():
        analysis.keepFFOnly = True
    elif "DiPhotonJetsBox_MGG-80toInf_13TeV-Sherpa" in customize.datasetName():
        analysis.vetoGenDiphotons = 200.
    
    # alyaws get full info for signal
    if "Grav" in customize.datasetName():
        dumpKinTree=True
        minimalDumper=diphotonDumper

dumpTrees=True
if customize.histosOnly:
    dumpKinTree=False
    dumpTrees=False

dumpNm1Trees=dumpTrees and not invertEleVeto
    
## kinematic selection
analysis.addKinematicSelection(process,dumpTrees=dumpKinTree,splitByIso=True
                               )

if not dumpKinTree: minimalDumper=diphotonDumper

## analysis selections
if customize.idversion != "":
    if customize.idversion == "V2":
        from diphotons.Analysis.highMassCiCDiPhotons_cfi import highMassCiCDiPhotonsV2   as highMassCiCDiPhotons
        from diphotons.Analysis.highMassCiCDiPhotons_cfi import highMassCiCDiPhotonsSBV2 as highMassCiCDiPhotonsSB
    else:
        print "Unknown ID version %s " % customize.idversion
        sys.exit(-1)
else:
    from diphotons.Analysis.highMassCiCDiPhotons_cfi import highMassCiCDiPhotons, highMassCiCDiPhotonsSB

if invertEleVeto:
    if doDoublePho0T:
        highMassCiCDiPhotons0T.variables[-1] = "? matchedGsfTrackInnerMissingHits==0 ? 2 : 0"
    else:
        highMassCiCDiPhotons.variables[-1] = "hasPixelSeed"
        highMassCiCDiPhotonsSB.variables[-1] = "hasPixelSeed"
        ## highMassCiCDiPhotons.variables[-1] = "-(passElectronVeto-1)"
        ## highMassCiCDiPhotonsSB.variables[-1] = "-(passElectronVeto-1)"

    if customize.doeleId:
        highMassCiCDiPhotons.cut = "( leadingPhoton.hasUserCand('eleMatch') || subLeadingPhoton.hasUserCand('eleMatch') ) && (%s)" % highMassCiCDiPhotons.cut.value()
    ###     ## highMassCiCDiPhotons.variables.append( "hasUserCand('matchedElectron')")
    ###     ## for cat in highMassCiCDiPhotons.categories:
    ###     ## cat.append( cms.PSet(min=cms.string("0.5"))  )        
            
# gen-only analysis
if( customize.processType!="data" ):
    analysis.addGenOnlySelection(process,genDiphotonDumper)


## Diphotons 0T
if doDoublePho0T:
    analysis.addAnalysisSelection(process, "cic",
                                  highMassCiCDiPhotons0T,
                                  dumpTrees=dumpTrees, dumpWorkspace=False, dumpHistos=True, splitByIso=True,
                                  dumperTemplate=diphotonDumper,
                                  nMinusOne=[(0,"NoSieie",        dumpNm1Trees, False, True), ## removeIndex(es), label, dumpTree, dumpWorkspace, dumpHistos
                                             (1,"NoSipip",        dumpNm1Trees, False, False),
                                             (2,"NoTrkIso",       dumpNm1Trees, False, False),
                                             (3,"NoPhoIso",       dumpNm1Trees, False, False),
                                             (4,"NoEleVeto",      dumpNm1Trees, False, False)
                                         ]
                              )    
    
elif doDoublePho:
    analysis.addAnalysisSelection(process,"cic",highMassCiCDiPhotons,dumpTrees=dumpTrees,dumpWorkspace=False,dumpHistos=True,splitByIso=True,
                                  dumperTemplate=minimalDumper,
                                  nMinusOne=[(0,"NoChIso",        dumpNm1Trees, False,True), ## removeIndex(es), label, dumpTree, dumpWorkspace, dumpHistos
                                             (1,"NoPhoIso",       False, False,True),
                                             (2,"NoNeuIso",       False,False,True),
                                             (3,"NoHoverE",       False,False,True),
                                             (4,"NoSigmaIetaIeta",False,False,True),
                                             (5,"NoEleVeto",      False,False,True),
                                             ]
                                  )
    
    ### analysis.addAnalysisSelection(process,"cicSB",highMassCiCDiPhotonsSB,dumpTrees=dumpTrees,dumpWorkspace=False,dumpHistos=True,splitByIso=True,
    ###                               dumperTemplate=minimalDumper,
    ###                               nMinusOne=[## Sidebands
    ###                                          ## removeIndex, (ignoreIndex(es),ingnoreNtimes), dumpTree, dumpWorkspace, dumpHistos, splitByIso
    ###                                          ((0),(4,1),"NoChIsoSingleSB",  True, False,True,False),
    ###                                          ((0),(4,2),"NoChIsoDoubleSB",  True, False,True,False)
    ###                                          ]
    ###                               )

# single photon selection
if customize.idversion != "":
    if customize.idversion == "V2":
        from diphotons.Analysis.highMassCiCPhotons_cfi import highMassCiCPhotonsV2 as highMassCiCPhotons
        from diphotons.Analysis.highMassCiCPhotons_cfi import highMassCiCPhotonsSBV2 as highMassCiCPhotonsSB
    else:
        print "Unknown ID version %s " % customize.idversion
        sys.exit(-1)
else:
    from diphotons.Analysis.highMassCiCPhotons_cfi import highMassCiCPhotons, highMassCiCPhotonsSB

if doSinglePho:

    if invertEleVeto:
        highMassCiCPhotons.variables[-1] = "hasPixelSeed"
        highMassCiCPhotonsSB.variables[-1] = "hasPixelSeed"
        ## highMassCiCPhotons.variables[-1] = "-(passElectronVeto-1)"
        ## highMassCiCPhotonsSB.variables[-1] = "-(passElectronVeto-1)"

    analysis.addPhotonAnalysisSelection(process,"cic",highMassCiCPhotons,dumpTrees=False,dumpWorkspace=False,dumpHistos=True,splitByIso=True,
                                        dumperTemplate=photonDumper,
                                        nMinusOne=[(0,"NoChIso",        True, False,True), ## removeIndex(es), label, dumpTree, dumpWorkspace, dumpHistos
                                                   (1,"NoPhoIso",       False, False,True),
                                                   (2,"NoNeuIso",       False,False,True),
                                                   (3,"NoHoverE",       False,False,True),
                                                   (4,"NoSigmaIetaIeta",False,False,True),
                                                   (5,"NoEleVeto",      False,False,True),
                                                   ]
                              )
    
    analysis.addPhotonAnalysisSelection(process,"cicSB",highMassCiCPhotonsSB,dumpTrees=False,dumpWorkspace=False,dumpHistos=True,splitByIso=True,
                                        dumperTemplate=photonDumper,
                                        nMinusOne=[## Sidebands
                                                   ## removeIndex, (ignoreIndex(es),ingnoreNtimes), dumpTree, dumpWorkspace, dumpHistos, splitByIso
                                                   ((0),(4,1),"NoChIsoSB",  True, False,True,False),
                                                   ]
                              )


if not customize.lastAttempt:
    # make sure process doesn't get stuck due to slow I/O
    process.watchDog = cms.EDAnalyzer("IdleWatchdog",
                                      minIdleFraction=cms.untracked.double(0.1),
                                      tolerance=cms.untracked.int32(10),
                                      checkEvery=cms.untracked.int32(100),
                                      )
    process.watch = cms.Path(
        process.watchDog
        )


# load appropriate scale and smearing bins here
# systematics customization scripts will take care of adjusting flashggDiPhotonSystematics
if "Run2015" in customize.datasetName() or "76X" in customize.datasetName():
    process.load('flashgg.Systematics.escales.escale76X_16DecRereco_2015')
    print "energy corrections file is escale76X_16DecRereco_2015"
else:
    ## process.load('flashgg.Systematics.escales.test_2016B_corr_DCSOnly')
    ## process.load('flashgg.Systematics.escales.Golden10June_plus_DCS')
    process.load('flashgg.Systematics.escales.Golden22June')
    print "energy corrections file is test_2016B_corr"


#
# input and output
#
process.source = cms.Source("PoolSource",
                            fileNames=cms.untracked.vstring(
        "file:diphotonsMicroAOD.root"
        )
)
process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("test.root")
)


# this will call customize(process), configure the analysis paths and make the process unscheduled
analysis.customize(process,customize)
