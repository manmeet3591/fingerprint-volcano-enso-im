Global 1500 Year Spatial Temperature Reconstructions
-----------------------------------------------------------------------
               World Data Center for Paleoclimatology, Boulder
                                  and
                     NOAA Paleoclimatology Program
-----------------------------------------------------------------------
NOTE: PLEASE CITE ORIGINAL REFERENCE WHEN USING THIS DATA!!!!!


NAME OF DATA SET: Global 1500 Year Spatial Temperature Reconstructions
LAST UPDATE: 4/2010 (Original receipt by WDC Paleo) 
CONTRIBUTORS: Mann, M.E., Z. Zhang, S. Rutherford, R.S. Bradley, 
M.K. Hughes, D. Shindell, C. Ammann, G. Faluvegi, and F. Ni.

IGBP PAGES/WDCA CONTRIBUTION SERIES NUMBER: 2010-023  

WDC PALEO CONTRIBUTION SERIES CITATION: 
Mann, M.E., et al. 2010. 
Global 1500 Year Spatial Temperature Reconstructions. 
IGBP PAGES/World Data Center for Paleoclimatology 
Data Contribution Series # 2010-023. 
NOAA/NCDC Paleoclimatology Program, Boulder CO, USA. 


ORIGINAL REFERENCE: 
Mann, M.E., Z. Zhang, S. Rutherford, R.S. Bradley, M.K. Hughes, 
D. Shindell, C. Ammann, G. Faluvegi, and F. Ni. 2009.
Global Signatures and Dynamical Origins of the Little Ice Age 
and Medieval Climate Anomaly.
Science, Vol. 326, pp. 1256-1260, 27 November 2009. 
DOI: 10.1126/science.1177303

ABSTRACT: 
Global temperatures are known to have varied over the past 1500 years, 
but the spatial patterns have remained poorly defined. We used a global 
climate proxy network to reconstruct surface temperature patterns over 
this interval. The Medieval period is found to display warmth that
matches or exceeds that of the past decade in some regions, but which 
falls well below recent levels globally. This period is marked by a 
tendency for La Niña-like conditions in the tropical Pacific.
The coldest temperatures of the Little Ice Age are observed over 
the interval 1400 to 1700 C.E., with greatest cooling over the 
extratropical Northern Hemisphere continents. The patterns of
temperature change imply dynamical responses of climate to natural 
radiative forcing changes involving El Niño and the North Atlantic 
Oscillation-Arctic Oscillation.


GEOGRAPHIC REGION: Global
PERIOD OF RECORD: 500 - 2006 AD
  
FUNDING SOURCES:
US National Science Foundation ATM program (grant ATM-0542356, 
M.E.M. and Z.Z.), U.S. Department of Energy (grant DE-FG02-98ER62604, 
R.S.B.), Office of Science (BER, R.S.B.),  US National Oceanic 
and Atmospheric Administration (grant NA16GP2914 from CCDD, 
M.K.H. and F.B.N.), US NASA's Atmospheric Chemistry, Modeling, 
and Analysis Program (D.T.S. and G.F.). 



DESCRIPTION: 
Supplemental information for:
Mann et al. Science, 326:1256-1260.

The data series shown in Figure 1
Each of the following files corresponds to a panel in Figure 1. 
Files have 4 columns, year, reconstruction, -2sigma and +2sigma. 
File name ending in "all" are from the "allproxy" or full network 
reconstruction and file names ending in "scr" are from the "screened" 
proxy reconstruction. For each series, the years 1850-2006 are the 
PC-filtered instrumental data. That is, the instrumental data but 
retaining the first 7 PCs, the number that were retained in the 
1800-1849 reconstruction step. 

AMO Full - file amoall.txt 
AMO screened - file amoscr.txt 
Northern Hemisphere full - file nhall.txt 
Northern Hemisphere screened - file nhscr.txt 
NINO3 full - file nino3all.txt 
NINO3 screened - file nino3scr.txt 
PDO full - file pdoall.txt 
PDO screened - file pdoscr.txt 
Global SST full - file sstall.txt 
Global SST screened - file sstscr.txt 



The Spatial Reconstruction 
The Spatial Reconstruction is a large file and has been gzipped. 
Column 1 is year, columns 2-2593 are gridboxes. 
Years 1850-2006 are the PC-filtered instrumental data (retaining 7 PCs). 
The RegEM infilled instrumental data can be found in the "allproxy" tarball 
listed below.  File allproxyfieldrecon.gz

The longitudes and latitudes for each gridbox are listed in file longlat.txt



Code and Data
The "allproxy" code and data are in a gzipped tarball, file name 
allproxy.tar.gz. After unpacking the tarball, you will have to change 
the paths in the code to run on your machine. See the "README.txt" 
in the tarball for more information. The RegEM code is included but 
is from Tapio Schneider's Web Site:
http://www.gps.caltech.edu/~tapio/ 

Metadata for the proxies used here and in Mann et al., 2008 
are in an Excel file, filename 1209proxynames.xls

All the proxy series are in the directory for Mann et al. 2008:
ftp://ftp.ncdc.noaa.gov/pub/data/paleo/contributions_by_author/mann2008/
and information about the proxies can be found there. 

Verification data are in the matlab file named verificationpost.mat,
and the code is in the matlab file indexverifypost.m. 
Included are the gridbox verification scores, the monte carlo, 
red-noise significant levels and the code to calculate the 
spatial series RE/CE values.  