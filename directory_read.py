import os
#directories =["L:\\mxd_versioned\\01_GEN","L:\\mxd_versioned\\02_ENR","L:\\mxd_versioned\\03_AD\MGGT","L:\\mxd_versioned\\03_AD\MGMM","L:\\mxd_versioned\\03_AD\MHLC","L:\\mxd_versioned\\03_AD\MHLM","L:\\mxd_versioned\\03_AD\MHRO","L:\\mxd_versioned\\03_AD\MHTG","L:\\mxd_versioned\\03_AD\MNMG","L:\\mxd_versioned\\03_AD\MRLB","L:\\mxd_versioned\\03_AD\MRLM","L:\\mxd_versioned\\03_AD\MROC","L:\\mxd_versioned\\03_AD\MRPV","L:\\mxd_versioned\\03_AD\MSLP","L:\\mxd_versioned\\03_AD\MSSS","L:\\mxd_versioned\\03_AD\MZBZ","L:\\mxd_versioned\\03_AD"]
#directories =["L:\\mxd_versioned\\03_AD\MHLM"]
directories =["L:\\MXD_AIP_HONDURAS\\02_ENR"]

for n in directories:
    for s in os.listdir(n):
        print os.path.splitext(s)[0]