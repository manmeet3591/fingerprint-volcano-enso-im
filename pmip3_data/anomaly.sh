#!/bin/bash
var=$1
file="${var}_Amon_IPSL-CM5A-LR_past1000_r1i1p1_0850-1850.nc"
for yyyy in {865..1835}
do
cdo selyear,$yyyy $file ${var}_Amon_IPSL-CM5A-LR_past1000_r1i1p1_${yyyy}.nc
cdo selyear,$((yyyy - 15))/$((yyyy + 15)) $file ${var}_Amon_IPSL-CM5A-LR_past1000_r1i1p1_${yyyy}_$((yyyy + 30)).nc
cdo ymonmean ${var}_Amon_IPSL-CM5A-LR_past1000_r1i1p1_${yyyy}_$((yyyy + 30)).nc ${var}_Amon_IPSL-CM5A-LR_past1000_r1i1p1_${yyyy}_clim.nc
cdo ymonsub ${var}_Amon_IPSL-CM5A-LR_past1000_r1i1p1_${yyyy}.nc ${var}_Amon_IPSL-CM5A-LR_past1000_r1i1p1_${yyyy}_clim.nc ${var}_Amon_IPSL-CM5A-LR_past1000_r1i1p1_${yyyy}_anom.nc
rm -rf ${var}_Amon_IPSL-CM5A-LR_past1000_r1i1p1_${yyyy}.nc ${var}_Amon_IPSL-CM5A-LR_past1000_r1i1p1_${yyyy}_$((yyyy + 30)).nc ${var}_Amon_IPSL-CM5A-LR_past1000_r1i1p1_${yyyy}_clim.nc

echo "$((yyyy -15)),$((yyyy + 15))"
done
ncrcat ${var}_Amon_IPSL-CM5A-LR_past1000_r1i1p1_???_anom.nc ${var}_Amon_IPSL-CM5A-LR_past1000_r1i1p1_????_anom.nc ${var}_Amon_IPSL-CM5A-LR_past1000_r1i1p1_0865_1835_anom.nc
rm -rf ${var}_Amon_IPSL-CM5A-LR_past1000_r1i1p1_???_anom.nc ${var}_Amon_IPSL-CM5A-LR_past1000_r1i1p1_????_anom.nc
