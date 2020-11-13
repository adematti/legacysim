#!/bin/bash

#BLOB_MASK_DIR=/global/cfs/cdirs/cosmo/work/legacysurvey/dr9/south

#export LEGACY_SURVEY_DIR=/global/cfs/cdirs/cosmo/work/legacysurvey/dr9m/
export LEGACY_SURVEY_DIR=/global/cscratch1/sd/adematti/Obiwan/dr9m/obiwan_data/
export DUST_DIR=/global/cfs/cdirs/cosmo/data/dust/v0_1
export UNWISE_COADDS_DIR=/global/cfs/cdirs/cosmo/work/wise/outputs/merge/neo6/fulldepth:/global/cfs/cdirs/cosmo/data/unwise/allwise/unwise-coadds/fulldepth
export UNWISE_COADDS_TIMERESOLVED_DIR=/global/cfs/cdirs/cosmo/work/wise/outputs/merge/neo6
export UNWISE_MODEL_SKY_DIR=/global/cfs/cdirs/cosmo/work/wise/unwise_catalog/dr3/mod
export GAIA_CAT_DIR=/global/cfs/cdirs/cosmo/work/gaia/chunks-gaia-dr2-astrom-2
export GAIA_CAT_VER=2
export TYCHO2_KD_DIR=/global/cfs/cdirs/cosmo/staging/tycho2
export LARGEGALAXIES_CAT=/global/cfs/cdirs/cosmo/staging/largegalaxies/v3.0/LSLGA-ellipse-v3.0.kd.fits
export PS1CAT_DIR=/global/cfs/cdirs/cosmo/work/ps1/cats/chunks-qz-star-v3
export SKY_TEMPLATE_DIR=/global/cfs/cdirs/cosmo/work/legacysurvey/dr9m/calib/sky_pattern

# PYTHONPATH is set in the container.
#export PYTHONPATH=/usr/local/lib/python:/usr/local/lib/python3.6/dist-packages:/src/unwise_psf/py:.

export OUTPUT_DIR=${CSCRATCH}/Obiwan/test/
export RANDOMS_FN=${OUTPUT_DIR}/randoms/randoms.fits

mkdir -p "${OUTPUT_DIR}"
mkdir -p "${RANDOMS_FN%/*}"
