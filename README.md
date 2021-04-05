# fingerprint-volcano-enso-im
Code for Fingerprint of Volcanic Forcing on the ENSO–Indian Monsoon Coupling

This repository contains the code for the the study "Fingerprint of Volcanic Forcing on the ENSO–Indian Monsoon Coupling"

To cite 

Singh, M., Krishnan, R., Goswami, B., Choudhury, A.D., Swapna, P., Vellore, R., Prajeesh, A.G., Sandeep, N., Venkataraman, C., Donner, R.V. and Marwan, N., 2020. Fingerprint of volcanic forcing on the ENSO–Indian monsoon coupling. Science advances, 6(38), p.eaba8164.

    @article{singh2020fingerprint,
      title={Fingerprint of volcanic forcing on the ENSO--Indian monsoon coupling},
      author={Singh, Manmeet and Krishnan, Raghavan and Goswami, Bedartha and Choudhury, Ayantika Dey and Swapna, P and Vellore, Ramesh and Prajeesh, AG and Sandeep, N and Venkataraman, Chandra and Donner, Reik V and others},
      journal={Science advances},
      volume={6},
      number={38},
      pages={eaba8164},
      year={2020},
      publisher={American Association for the Advancement of Science}
    }


![alt text](https://github.com/manmeet3591/fingerprint-volcano-enso-im/blob/master/figures/fig1/output/fig6_review.png?raw=true)

The paper can be found at https://advances.sciencemag.org/content/6/38/eaba8164

Singh, M., Krishnan, R., Goswami, B., Choudhury, A.D., Swapna, P., Vellore, R., Prajeesh, A.G., Sandeep, N., Venkataraman, C., Donner, R.V. and Marwan, N., 2020. Fingerprint of volcanic forcing on the ENSO–Indian monsoon coupling. Science advances, 6(38), p.eaba8164.

# Steps to reproduce the study

# 1. Phase coherence analysis for the instrumental period (1871-2016)

The phase coherence analysis by Maraun and Kurths 2005 (https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2005GL023225) is first reproduced. The period for phase-coherence analysis is chosen as 1871-2016

From the paper Maraun and Kurths 2005, to conduct phase coherence analysis:

Low‐pass filter the data in the spectral domain. A smooth function (arcus tangens) damping frequencies >0.7 year−1 is chosen.

Estimate derivatives by second order difference scheme and running mean with window width 2l + 1 = 13 months

Embed by Hilbert transformation with phase defined according to equation. We perform this using the hilbert function from scipy library (https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.hilbert.html)

Unwrap the phases (add 2π after each oscillation). This is performed using the unwrap function of numpy library (https://numpy.org/doc/stable/reference/generated/numpy.unwrap.html)

The analysis can be performed using the script phase_coh_1871_2016/codes/main.py

Source of data: Indian Monsoon (AIR: ftp://www.tropmet.res.in/pub/data/rain/iitm-regionrf.txt), ENSO (Nino3: https://psl.noaa.gov/gcos_wgsp/Timeseries/Data/nino3.long.anom.data)

# 2. Statistical significance of phase coherence analysis

The statistical significance testing of the phase coherence analysis from observational data is performed by generating 5000 twin surrogates of ENSO and
IM and performing the phase coherence analysis on all the pairs of ENSO and IM. The distribution of original relative phase difference is plotted with the 
distribution of 5000 surrogate relative phase difference. The code is present in the directory twin_surr_inst_data/

# 3. Choosing the number of surrogates

The number of surrogates required has been calculated using the methods named Holm's method Dunn-Sidak correction. The material on how to choose number of surrogates 
based on the alpha can be seen at the following links

https://www.statisticshowto.com/holm-bonferroni-method/

https://www.real-statistics.com/hypothesis-testing/familywise-error/bonferroni-and-dunn-sidak-tests/

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1380484/

# 4. Phase coherence analysis of ENSO and IM using Institut Pierre Simon Laplace (IPSL) PMIP3 last-millennium simulations 

The phase coherence analysis for the last millenium is performed using the data from IPSL PMIP3 simulations. The data can be found at https://esgf-node.llnl.gov/search/cmip5/

The extracted data for the core monsoon zone (Goswami et al 2006) has been kept in https://github.com/manmeet3591/fingerprint-volcano-enso-im/blob/master/pmip3_data/pr_Amon_IPSL-CM5A-LR_past1000_r1i1p1_0850_1850_goswami_india_tseries.csv and https://github.com/manmeet3591/fingerprint-volcano-enso-im/blob/master/pmip3_data/tas_Amon_IPSL-CM5A-LR_past1000_r1i1p1_0850_1850_nino3_tseries.csv The data is in monthly temporal resolution from Jan 850 to Dec 1850

The code for conducting phase coherence analysis of the PMIP3 IPSL simulation is kept at https://github.com/manmeet3591/fingerprint-volcano-enso-im/blob/master/figures/fig1/codes/main.py The filtering parameters for the data can be found from the codes at https://github.com/manmeet3591/fingerprint-volcano-enso-im/tree/master/choosing_filtering_parameters/filtering_ipsl For the purposes of statistical significance, the code can be found at https://github.com/manmeet3591/fingerprint-volcano-enso-im/tree/master/twin_surr_pmip_ipsl_last_millenium

# 5. Composite of Northern Hemispheric (NH) surface air temperature (SAT) anomalies based on LVEs during the last millennium.

Data source: https://www.ncdc.noaa.gov/paleo-search/study/19523

The codes can be found in northern_hemisphere_land_cooling/asia_1200_cook

The data is first transformed to a netcdf form using the code https://github.com/manmeet3591/fingerprint-volcano-enso-im/blob/master/northern_hemisphere_land_cooling/asia_1200_cook/txt2nc.py This is followed by selecting the top 25 volcanic eruptions https://github.com/manmeet3591/fingerprint-volcano-enso-im/blob/master/northern_hemisphere_land_cooling/asia_1200_cook/volc_eruptions_sigl.txt Now if the eruption happened in the year 0, the years from -5 to +1 are selected for each of these eruptions.The final figure is generated using the data and codes at https://github.com/manmeet3591/fingerprint-volcano-enso-im/tree/master/northern_hemisphere_land_cooling/asia_1200_cook/timmean/analysis_1

# 6. Bayesian analysis—probability of ENSO-IM phase coupling for year (0) conditioned on ENSO (0) (left) and ENSO (0) and Volcano (−1)

The datasets are first downloaded from the following sources 

the dataset used for IM proxies were mostly open-source and were accessed from https://www.ncdc.noaa.gov/data-access/paleoclimatology-data/datasets for the 8 IM proxies

1. A. Sinha, K. G. Cannariato, L. D. Stott, H. Cheng, R. L. Edwards, M. G. Yadava, R. Ramesh, I. B. Singh. A 900-year (600 to 1500 A.D.) record of the Indian summer monsoon precipitation from the core monsoon zone of India. Geophys. Res. Lett. 34, L16707 (2007). https://www.ncei.noaa.gov/pub/data/paleo/speleothem/asia/india/dandak2010.txt

2. A. Sinha, M. Berkelhammer, L. Stott, M. Mudelsee, H. Cheng, J. Biswas, The leading mode of Indian Summer Monsoon precipitation variability during the last millennium. Geophys. Res. Lett.
38, L15703 (2011). https://www.ncei.noaa.gov/pub/data/paleo/speleothem/asia/india/jhumar-wah-shikar2011.txt

3. E. R. Cook, K. J. Anchukaitis, B. M. Buckley, R. D’Arrigo, G. C. Jacoby, W. E. Wright, Asian monsoon failure and megadrought during the last millennium. Science 328, 486–489 (2010). http://drought.memphis.edu/MADA/

4. A. Sinha, G. Kathayat, H. Cheng, S. F. Breitenbach, M. Berkelhammer, M. Mudelsee, J. Biswas, R. L. Edwards, Trends and oscillations in the Indian summer monsoon rainfall over the last two millennia. Nat. Commun. 6, 6309 (2015) Data given as supplementary 2 in https://www.nature.com/articles/ncomms7309 https://static-content.springer.com/esm/art%3A10.1038%2Fncomms7309/MediaObjects/41467_2015_BFncomms7309_MOESM878_ESM.xlsx

5. H. Shi, B. Wang, E. R. Cook, J. Liu, F. Liu, Asian summer precipitation over the past 544 years reconstructed by merging tree rings and historical documentary records. J. Climate 31, 7845–7861 (2018). https://www.ncdc.noaa.gov/paleo-search/study/24391

6. F. Shi, K. Fang, C. Xu, Z. Guo, H. P. Borgaonkar, Interannual to centennial variability of the South Asian summer monsoon over the past millennium. Climate Dynam. 49, 2803–2814 (2017). https://www.ncdc.noaa.gov/paleo-search/study/22730

7. F. Shi, J. Li, R. J. Wilson, A tree-ring reconstruction of the South Asian summer monsoon index over the past millennium. Sci. Rep. 4, 6739 (2014).https://www.ncdc.noaa.gov/paleo-search/study/17369

8. M. Sano, A. P. Dimri, R. Ramesh, C. Xu, Z. Li, T. Nakatsuka, Moisture source signals preserved in a 242-year tree-ring δ18O chronology in the western Himalaya. Glob. Planet. Change 157, 73–82
(2017) https://www.ncdc.noaa.gov/paleo-search/study/22549

There are three datasets which are not open source and I had obtained from the authors of the following 3 studies:

1. M. G. Yadava, R. Ramesh, G. B. Pant, Past monsoon rainfall variations in peninsular India recorded in a 331-year-old speleothem. Holocene 14, 517–524 (2004).

2. H. P. Borgaonkar, A. B. Sikder, S. Ram, G. B. Pant, El Niño and related monsoon drought signals in 523-year-long ring width records of teak (Tectona grandis L.F.) trees from south India. Palaeogeogr. Palaeoclimatol. Palaeoecol. 285, 74–84 (2010).
 
3. S. Feng, Q. Hu, Q. Wu, M. E. Mann, A gridded reconstruction of warm season precipitation for Asia spanning the past half millennium. J. Climate 26, 2192–2204 (2013).

The datasets are mostly in a raw form and first they were filtered or processed to replicate the time series plots as shown in the respective papers. The codes for this preprocessing are in the folders https://github.com/manmeet3591/fingerprint-volcano-enso-im/tree/master/bayesian_paleo/ismr_proxies https://github.com/manmeet3591/fingerprint-volcano-enso-im/tree/master/bayesian_paleo/nino3_proxies The codes for Bayesian probability estimation are available in the folder https://github.com/manmeet3591/fingerprint-volcano-enso-im/tree/master/bayesian_paleo/bayesian 

# 7. IITM-ESM sensitivity experiments 

The restarts were identified using identifying_restarts_for_large_ensemble_simulation/pi_control_identify_restarts_final.ipynb

The experiments are performed following the flowchart in the Fig. S7. The schematic in Fig. S7 has been prepared using draw.io and can be found at https://tinyurl.com/37m8rvs8

# 8. Jupyter notebooks to reproduce all the figures (main+supplementary) in the paper

https://github.com/manmeet3591/fingerprint-volcano-enso-im/blob/master/figures/fig1/output/figures_final_main.ipynb

https://github.com/manmeet3591/fingerprint-volcano-enso-im/blob/master/figures/fig1/output/re_review_pi_control_reference_final_minor.ipynb

https://github.com/manmeet3591/fingerprint-volcano-enso-im/blob/master/figures/fig1/output/supplementary_figures_final.ipynb


