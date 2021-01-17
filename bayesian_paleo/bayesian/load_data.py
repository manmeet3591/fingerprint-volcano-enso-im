import numpy as np
dnino3_jjas = np.genfromtxt('tas_Amon_IPSL-CM5A-LR_past1000_r1i1p1_0865_1835_anom_nino3_jjas_ymean.csv', delimiter=",")
dnino3_djf = np.genfromtxt('tas_Amon_IPSL-CM5A-LR_past1000_r1i1p1_0865_1835_anom_nino3_djf_ymean.csv', delimiter=",")[:971]
dnino3 = np.genfromtxt('tas_Amon_IPSL-CM5A-LR_past1000_r1i1p1_0865_1835_anom_nino3_ymean.csv', delimiter=",")

im_jjas = np.genfromtxt('tas_Amon_IPSL-CM5A-LR_past1000_r1i1p1_0865_1835_anom_nino3_jjas_ymean.csv', delimiter=",")


dim_dandak_2010 = np.genfromtxt('ismr_dandak_2010_anom_yy.txt', delimiter=",")
im_dandak = dim_dandak_2010[:,2]
yy_dandak = dim_dandak_2010[:,0]

dim_jhumar_2011 = np.genfromtxt('ismr_jhumar_ann_yy.txt', delimiter=",")
im_jhumar = dim_jhumar_2011[:,2]
yy_jhumar = dim_jhumar_2011[:,0]

dim_cook_2010 = np.genfromtxt('ismr_cook_anom_yy.txt', delimiter=",")
im_cook = dim_cook_2010[:,2]
yy_cook = dim_cook_2010[:,0]

dim_sinha_2011 = np.genfromtxt('ismr_sinha_2011_anom_yy.txt', delimiter=",")
im_sinha_2011 = dim_sinha_2011[:,2]
yy_sinha_2011 = dim_sinha_2011[:,0]

dim_sinha_2015 = np.genfromtxt('ismr_sinha_2015_anom_yy.txt', delimiter=",")
im_sinha_2015 = dim_sinha_2015[:,2]
yy_sinha_2015 = dim_sinha_2015[:,0]

dim_shi_2018 = np.genfromtxt('indian_monsoon_shi_2018_tseries.txt', delimiter=",")
im_shi_2018 = dim_shi_2018[:]
yy_shi_2018 = np.arange(1470,2014)

dim_shi_2017 = np.genfromtxt('ismr_shi_2017_anom_yy.txt', delimiter=",")
im_shi_2017 = dim_shi_2017[:,1]
yy_shi_2017 = dim_shi_2017[:,0]

dim_shi_2014 = np.genfromtxt('ismr_shi_2014_anom_yy.txt', delimiter=",")
im_shi_2014 = dim_shi_2014[:,1]
yy_shi_2014 = dim_shi_2014[:,0]

dim_borgaonkar_2010 = np.genfromtxt('ktrc_data_borgaonkar.txt', delimiter=",")
im_borgaonkar_2010 = dim_borgaonkar_2010[:,1]
yy_borgaonkar_2010 = dim_borgaonkar_2010[:,0]

dim_yadava_2004 = np.genfromtxt('ismr_yadava_anom_yy.txt', delimiter=",")
im_yadava_2004 = dim_yadava_2004[:,1]
yy_yadava_2004 = dim_yadava_2004[:,0]


dim_sano_2017 = np.genfromtxt('ismr_sano_2017_anom_yy.txt', delimiter=",")
im_sano_2017 = dim_sano_2017[:,1]
yy_sano_2017 = dim_sano_2017[:,0]

dim_feng_2013 = np.genfromtxt('ismr_feng_2013_anom_yy.txt', delimiter=",")
im_feng_2013 = dim_feng_2013[:,1]
yy_feng_2013 = dim_feng_2013[:,0]


dnino3_li_2011 = np.genfromtxt('nino3_li_2011_anom_yy.txt', delimiter=",")
nino3_li_2011 = dnino3_li_2011[:,2]
yy_li_2011 = dnino3_li_2011[:,0]

dnino3_li_2013 = np.genfromtxt('nino3_li_2013_anom_yy.txt', delimiter=",")
nino3_li_2013 = dnino3_li_2013[:,2]
yy_li_2013 = dnino3_li_2013[:,0]

dnino3_mann_2009 = np.genfromtxt('nino3_mann_2009_anom_yy.txt', delimiter=",")
nino3_mann_2009 = dnino3_mann_2009[:,2]
yy_mann_2009 = dnino3_mann_2009[:,0]

dnino3_moy_2002 = np.genfromtxt('nino3_moy_2002_anom_yy.txt', delimiter=",")
nino3_moy_2002 = dnino3_moy_2002[:,2]
yy_moy_2002 = dnino3_moy_2002[:,0]

dnino3_arrigo_2005 = np.genfromtxt('nino3_recon_arrigo_cook_v1.txt', delimiter=",")
nino3_arrigo_2005 = dnino3_arrigo_2005[:,1]
yy_arrigo_2005 = dnino3_arrigo_2005[:,0]

dnino3_mcgregor_2010 = np.genfromtxt('mcgregor2010uep_v1.txt', delimiter=",")
nino3_mcgregor_2010 = dnino3_mcgregor_2010[:,1]
yy_mcgregor_2010 = dnino3_mcgregor_2010[:,0]

dnino3_stahle_1998 = np.genfromtxt('soi.recon_stahle_v1.txt', delimiter=",")
nino3_stahle_1998 = -dnino3_stahle_1998[:,1]
yy_stahle_1998 = dnino3_stahle_1998[:,0]

dnino3_emily_geay_2012 = np.genfromtxt('emile-geay2012_v1.txt', delimiter=",")
nino3_emily_geay_2012 = dnino3_emily_geay_2012[:,1]
yy_emily_geay_2012 = dnino3_emily_geay_2012[:,0]
nino3_emily_geay_2012 = nino3_emily_geay_2012[::-1]
yy_emily_geay_2012 = yy_emily_geay_2012[::-1]

dnino3_cook_2008 = np.genfromtxt('nino-cook2008_v1.txt', delimiter=",")
nino3_cook_2008 = dnino3_cook_2008[:,1]
yy_cook_2008 = dnino3_cook_2008[:,0]


dgergis_en = np.genfromtxt('gergis2009enso_en_v1_s.txt', delimiter=",")
dgergis_ln = np.genfromtxt('gergis2009enso_ln_v2_s.txt', delimiter=",")
yy_start_gergis = min(np.min(dgergis_en), np.min(dgergis_ln))
yy_end_gergis = max(np.max(dgergis_en), np.max(dgergis_ln))

yy_gergis_2009 = np.arange(yy_start_gergis,yy_end_gergis+1)
nino3_gergis_2009 = np.zeros((yy_gergis_2009.shape[0]))

for i in range(yy_gergis_2009.shape[0]):
    if yy_gergis_2009[i] in dgergis_en:
        nino3_gergis_2009[i] = 1.0
    if yy_gergis_2009[i] in dgergis_ln:
        nino3_gergis_2009[i] = -1.0


dnino3_yan_2011 = np.genfromtxt('yan2011soipr_v1.txt', delimiter=",")
nino3_yan_2011 = dnino3_yan_2011[:,1]
yy_yan_2011 = dnino3_yan_2011[:,0]

dnino3_datwyler_2019 = np.genfromtxt('datwyler2019_v1.txt', delimiter=";")
nino3_datwyler_2019 = dnino3_datwyler_2019[:,2]
yy_datwyler_2019 = dnino3_datwyler_2019[:,0]

dnino3_wilson_2010 = np.genfromtxt('enso-wilson2010_v1.txt', delimiter=",")
nino3_wilson_2010 = dnino3_wilson_2010[:,1]
yy_wilson_2010 = dnino3_wilson_2010[:,0]


dnino3_braganza_2009 = np.genfromtxt('braganza2009enso_v1.txt', delimiter=",")
nino3_braganza_2009 = -dnino3_braganza_2009[:,1]
yy_braganza_2009 = dnino3_braganza_2009[:,0]

dpdo_mann_2009 = np.genfromtxt('pdo_mann_2009_anom_yy.txt', delimiter=",")
pdo_mann_2009 = dpdo_mann_2009[:,1]
yy_mann_2009 = dpdo_mann_2009[:,0]

dpdo_macdonald_2005 = np.genfromtxt('pdo-macdonald2005_v1.txt', delimiter=",")
pdo_macdonald_2005 = dpdo_macdonald_2005[:,1]
yy_macdonald_2005 = dpdo_macdonald_2005[:,0]

dpdo_arrigo_2006 = np.genfromtxt('pdo-darrigo2006_v1.txt', delimiter=",")
pdo_arrigo_2006 = dpdo_arrigo_2006[:,1]
yy_arrigo_2006 = dpdo_arrigo_2006[:,0]


dpdo_biondi_2001 = np.genfromtxt('pdo_biondi_2001_v1.txt', delimiter=",")
pdo_biondi_2001 = dpdo_biondi_2001[:,1]
yy_biondi_2001 = dpdo_biondi_2001[:,0]

dpdo_shen_2006 = np.genfromtxt('pdo-shen2006_v1.txt', delimiter=",")
pdo_shen_2006 = dpdo_shen_2006[:,1]
yy_shen_2006 = dpdo_shen_2006[:,0]


damo_mann_2009 = np.genfromtxt('amo_mann_2009_v1.txt', delimiter=",")
amo_mann_2009 = damo_mann_2009[:,1]
yy_mann_2009 = damo_mann_2009[:,0]


yy_model = np.arange(865,1836)
#dstrong1 = np.genfromtxt('strong0.25.txt', delimiter=",")
dstrong1 = np.genfromtxt('strong1.txt', delimiter=",")

volc_model = np.zeros((yy_model.shape[0]))
for i in range(yy_model.shape[0]):
    if yy_model[i] in dstrong1:
        volc_model[i] = 1.0

volc_dandak = np.zeros((yy_dandak.shape[0]))
for i in range(yy_dandak.shape[0]):
    if yy_dandak[i] in dstrong1:
        volc_dandak[i] = 1.0

volc_jhumar = np.zeros((yy_jhumar.shape[0]))
for i in range(yy_jhumar.shape[0]):
    if yy_jhumar[i] in dstrong1:
        volc_jhumar[i] = 1.0

volc_cook = np.zeros((yy_cook.shape[0]))
for i in range(yy_cook.shape[0]):
    if yy_cook[i] in dstrong1:
        volc_cook[i] = 1.0

volc_sinha_2011 = np.zeros((yy_sinha_2011.shape[0]))
for i in range(yy_sinha_2011.shape[0]):
    if yy_sinha_2011[i] in dstrong1:
        volc_sinha_2011[i] = 1.0

volc_sinha_2015 = np.zeros((yy_sinha_2015.shape[0]))
for i in range(yy_sinha_2015.shape[0]):
    if yy_sinha_2015[i] in dstrong1:
        volc_sinha_2015[i] = 1.0

volc_shi_2018 = np.zeros((yy_shi_2018.shape[0]))
for i in range(yy_shi_2018.shape[0]):
    if yy_shi_2018[i] in dstrong1:
        volc_shi_2018[i] = 1.0


volc_shi_2017 = np.zeros((yy_shi_2017.shape[0]))
for i in range(yy_shi_2017.shape[0]):
    if yy_shi_2017[i] in dstrong1:
        volc_shi_2017[i] = 1.0

volc_shi_2014 = np.zeros((yy_shi_2014.shape[0]))
for i in range(yy_shi_2014.shape[0]):
    if yy_shi_2014[i] in dstrong1:
        volc_shi_2014[i] = 1.0

volc_sano_2017 = np.zeros((yy_sano_2017.shape[0]))
for i in range(yy_sano_2017.shape[0]):
    if yy_sano_2017[i] in dstrong1:
        volc_sano_2017[i] = 1.0

volc_borgaonkar_2010 = np.zeros((yy_borgaonkar_2010.shape[0]))
for i in range(yy_borgaonkar_2010.shape[0]):
    if yy_borgaonkar_2010[i] in dstrong1:
        volc_borgaonkar_2010[i] = 1.0

volc_yadava_2004 = np.zeros((yy_yadava_2004.shape[0]))
for i in range(yy_yadava_2004.shape[0]):
    if yy_yadava_2004[i] in dstrong1:
        volc_yadava_2004[i] = 1.0

volc_feng_2013 = np.zeros((yy_feng_2013.shape[0]))
for i in range(yy_feng_2013.shape[0]):
    if yy_feng_2013[i] in dstrong1:
        volc_feng_2013[i] = 1.0

volc_li_2011 = np.zeros((yy_li_2011.shape[0]))
for i in range(yy_li_2011.shape[0]):
    if yy_li_2011[i] in dstrong1:
        volc_li_2011[i] = 1.0

volc_li_2013 = np.zeros((yy_li_2013.shape[0]))
for i in range(yy_li_2013.shape[0]):
    if yy_li_2013[i] in dstrong1:
        volc_li_2013[i] = 1.0

volc_mann_2009 = np.zeros((yy_mann_2009.shape[0]))
for i in range(yy_mann_2009.shape[0]):
    if yy_mann_2009[i] in dstrong1:
        volc_mann_2009[i] = 1.0

volc_moy_2002 = np.zeros((yy_moy_2002.shape[0]))
for i in range(yy_moy_2002.shape[0]):
    if yy_moy_2002[i] in dstrong1:
        volc_moy_2002[i] = 1.0

volc_arrigo_2005 = np.zeros((yy_arrigo_2005.shape[0]))
for i in range(yy_arrigo_2005.shape[0]):
    if yy_arrigo_2005[i] in dstrong1:
        volc_arrigo_2005[i] = 1.0

volc_mcgregor_2010 = np.zeros((yy_mcgregor_2010.shape[0]))
for i in range(yy_mcgregor_2010.shape[0]):
    if yy_mcgregor_2010[i] in dstrong1:
        volc_mcgregor_2010[i] = 1.0

volc_stahle_1998 = np.zeros((yy_stahle_1998.shape[0]))
for i in range(yy_stahle_1998.shape[0]):
    if yy_stahle_1998[i] in dstrong1:
        volc_stahle_1998[i] = 1.0

volc_emily_geay_2012 = np.zeros((yy_emily_geay_2012.shape[0]))
for i in range(yy_emily_geay_2012.shape[0]):
    if yy_emily_geay_2012[i] in dstrong1:
        volc_emily_geay_2012[i] = 1.0

volc_cook_2008 = np.zeros((yy_cook_2008.shape[0]))
for i in range(yy_cook_2008.shape[0]):
    if yy_cook_2008[i] in dstrong1:
        volc_cook_2008[i] = 1.0

volc_gergis_2009 = np.zeros((yy_gergis_2009.shape[0]))
for i in range(yy_gergis_2009.shape[0]):
    if yy_gergis_2009[i] in dstrong1:
        volc_gergis_2009[i] = 1.0

volc_yan_2011 = np.zeros((yy_yan_2011.shape[0]))
for i in range(yy_yan_2011.shape[0]):
    if yy_yan_2011[i] in dstrong1:
        volc_yan_2011[i] = 1.0

volc_datwyler_2019 = np.zeros((yy_datwyler_2019.shape[0]))
for i in range(yy_datwyler_2019.shape[0]):
    if yy_datwyler_2019[i] in dstrong1:
        volc_datwyler_2019[i] = 1.0

volc_wilson_2010 = np.zeros((yy_wilson_2010.shape[0]))
for i in range(yy_wilson_2010.shape[0]):
    if yy_wilson_2010[i] in dstrong1:
        volc_wilson_2010[i] = 1.0

volc_braganza_2009 = np.zeros((yy_braganza_2009.shape[0]))
for i in range(yy_braganza_2009.shape[0]):
    if yy_braganza_2009[i] in dstrong1:
        volc_braganza_2009[i] = 1.0

volc_mann_2009 = np.zeros((yy_mann_2009.shape[0]))
for i in range(yy_mann_2009.shape[0]):
    if yy_mann_2009[i] in dstrong1:
        volc_mann_2009[i] = 1.0

volc_macdonald_2005 = np.zeros((yy_macdonald_2005.shape[0]))
for i in range(yy_macdonald_2005.shape[0]):
    if yy_macdonald_2005[i] in dstrong1:
        volc_macdonald_2005[i] = 1.0

volc_arrigo_2006 = np.zeros((yy_arrigo_2006.shape[0]))
for i in range(yy_arrigo_2006.shape[0]):
    if yy_arrigo_2006[i] in dstrong1:
        volc_arrigo_2006[i] = 1.0

volc_biondi_2001 = np.zeros((yy_biondi_2001.shape[0]))
for i in range(yy_biondi_2001.shape[0]):
    if yy_biondi_2001[i] in dstrong1:
        volc_biondi_2001[i] = 1.0

volc_shen_2006 = np.zeros((yy_shen_2006.shape[0]))
for i in range(yy_shen_2006.shape[0]):
    if yy_shen_2006[i] in dstrong1:
        volc_shen_2006[i] = 1.0

volc_mann_2009 = np.zeros((yy_mann_2009.shape[0]))
for i in range(yy_mann_2009.shape[0]):
    if yy_mann_2009[i] in dstrong1:
        volc_mann_2009[i] = 1.0



pr_dr = 0.0
prob_dr_en = 0.0
prob_dr_en_volc = 0.0

