# fingerprint-volcano-enso-im
Code for Fingerprint of Volcanic Forcing on the ENSO–Indian Monsoon Coupling

This repository contains the code to replicate the study "Fingerprint of Volcanic Forcing on the ENSO–Indian Monsoon Coupling"

The paper can be found at https://advances.sciencemag.org/content/6/38/eaba8164

Singh, M., Krishnan, R., Goswami, B., Choudhury, A.D., Swapna, P., Vellore, R., Prajeesh, A.G., Sandeep, N., Venkataraman, C., Donner, R.V. and Marwan, N., 2020. Fingerprint of volcanic forcing on the ENSO–Indian monsoon coupling. Science advances, 6(38), p.eaba8164.

Steps to reproduce the study

1. The phase coherence analysis by Maraun and Kurths 2005 (https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2005GL023225) is first reproduced. The period for phase-coherence analysis is chosen as 1871-2016

From the paper Maraun and Kurths 2005, to conduct phase coherence analysis:

Low‐pass filter the data in the spectral domain. A smooth function (arcus tangens) damping frequencies >0.7 year−1 is chosen.

Estimate derivatives by second order difference scheme and running mean with window width 2l + 1 = 13 months

Embed by Hilbert transformation with phase defined according to equation. We perform this using the hilbert function from scipy library (https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.hilbert.html)

Unwrap the phases (add 2π after each oscillation). This is performed using the unwrap function of numpy library (https://numpy.org/doc/stable/reference/generated/numpy.unwrap.html)

The analysis can be performed using the script phase_coh_1871_2016/codes/main.py

Source of data: Indian Monsoon (AIR: ftp://www.tropmet.res.in/pub/data/rain/iitm-regionrf.txt), ENSO (Nino3: https://psl.noaa.gov/gcos_wgsp/Timeseries/Data/nino3.long.anom.data)

2. The statistical significance testing of the phase coherence analysis from observational data is performed by generating 5000 twin surrogates of ENSO and
IM and performing the phase coherence analysis on all the pairs of ENSO and IM. The distribution of original relative phase difference is plotted with the 
distribution of 5000 surrogate relative phase difference. The code is present in the directory twin_surr_inst_data/

3. The number of surrogates required has been calculated using the methods named Holm's method Dunn-Sidak correction. The material on how to choose number of surrogates 
based on the alpha can be seen at the following links

https://www.statisticshowto.com/holm-bonferroni-method/

https://www.real-statistics.com/hypothesis-testing/familywise-error/bonferroni-and-dunn-sidak-tests/

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1380484/

4. Composite of Northern Hemispheric (NH) surface air temperature (SAT) anomalies based on LVEs during the last millennium.

Data source: https://www.ncdc.noaa.gov/paleo-search/study/19523

The codes can be found in northern_hemisphere_land_cooling/asia_1200_cook

5. hase coherence analysis of ENSO and IM using Institut Pierre Simon Laplace (IPSL) PMIP3 last-millennium simulations 

6. Bayesian analysis—probability of ENSO-IM phase coupling for year (0) conditioned on ENSO (0) (left) and ENSO (0) and Volcano (−1)

7. The restarts were identified using identifying_restarts_for_large_ensemble_simulation/pi_control_identify_restarts_final.ipynb

