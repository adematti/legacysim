import os
import logging

import numpy as np
import galsim

from legacysim import setup_logging
from legacysim.survey import (find_file, find_legacypipe_file, find_legacysim_file, get_git_version, get_version, get_sim_id,
                            get_survey, DecamSim, NinetyPrimeMosaicSim, CosmosSim, LegacySurveySim)
from legacysim.image import GSImage


setup_logging(logging.DEBUG)


def test_paths():

    fn = find_legacypipe_file('tests','bricks',brickname='2599p187',fileid=0,rowstart=0,skipid=0)
    assert os.path.normpath(fn) == os.path.normpath('tests/survey-bricks.fits.gz')
    fn2 = find_file('tests','bricks',brickname='2599p187',source='legacypipe',fileid=0,rowstart=0,skipid=0)
    assert fn2 == fn
    fn = find_legacypipe_file('','tractor',brickname='2599p187',fileid=0,rowstart=0,skipid=0)
    fn2 = find_legacysim_file('tests','tractor',brickname='2599p187',fileid=1,rowstart=2,skipid=3)
    assert fn2 == os.path.join('tests','file1_rs2_skip3',fn)
    fn = find_legacysim_file('tests','injected',brickname='2599p187',fileid=1,rowstart=2,skipid=3)
    assert os.path.normpath(fn) == os.path.normpath('tests/file1_rs2_skip3/sim/259/injected-2599p187.fits')
    fn2 = find_file(base_dir='tests',filetype='injected',brickname='2599p187',source='legacysim',fileid=1,rowstart=2,skipid=3)
    assert fn2 == fn
    fn = find_file(base_dir='tests',filetype='pickle',brickname='2599p187',source='legacysim',fileid=1,rowstart=2,skipid=3,stage='fitblobs')
    assert os.path.normpath(fn) == os.path.normpath('tests/file1_rs2_skip3/pickles/259/runbrick-2599p187-fitblobs.pickle')
    fn = find_file(base_dir='.',filetype='checkpoint',brickname='2599p187',source='legacysim',fileid=1,rowstart=2,skipid=3)
    assert os.path.normpath(fn) == os.path.normpath('file1_rs2_skip3/checkpoints/259/checkpoint-2599p187.pickle')
    fn = find_file(base_dir='.',filetype='log',brickname='2599p187',source='legacysim',fileid=1,rowstart=2,skipid=3)
    assert os.path.normpath(fn) == os.path.normpath('file1_rs2_skip3/logs/259/log-2599p187.log')
    fn = find_file(base_dir='.',filetype='ps',brickname='2599p187',source='legacysim',fileid=1,rowstart=2,skipid=3)
    assert os.path.normpath(fn) == os.path.normpath('file1_rs2_skip3/metrics/259/ps-2599p187.fits')


def test_versions():

    get_git_version()
    assert len(get_version())


def test_sim_id():

    assert len(get_sim_id.keys()) == len(get_sim_id.default())
    assert get_sim_id() == get_sim_id.template() % tuple(get_sim_id.default())
    assert get_sim_id.match_template() == get_sim_id.template() % tuple(get_sim_id.as_list(**get_sim_id.kwargs_match_template()))
    kwargs = {get_sim_id.keys()[0]:3}
    simid = get_sim_id(**kwargs)
    okwargs = get_sim_id.match(simid)
    assert okwargs == get_sim_id.as_dict(**kwargs)


def test_get_survey():

    kwargs = {}
    fns = ['test-decam','test-90prime','test-mosaic']
    for run in ['decam','south']:
        tmp = get_survey(run,**kwargs)
        assert isinstance(tmp,DecamSim)
        assert tmp.filter_ccd_kd_files(fns) == [fns[0]]
    for run in ['90prime-mosaic','north']:
        tmp = get_survey(run,**kwargs)
        assert isinstance(tmp,NinetyPrimeMosaicSim)
        assert tmp.filter_ccd_kd_files(fns) == fns[1:]
    for run in ['cosmos']:
        tmp = get_survey(run,**kwargs)
        assert isinstance(tmp,CosmosSim)
        assert tmp.filter_ccd_kd_files(fns) == fns
        assert hasattr(tmp,'subset')
    for run in [None]:
        tmp = get_survey(run,**kwargs)
        assert isinstance(tmp,LegacySurveySim)
        assert tmp.filter_ccd_kd_files(fns) == fns


def test_gsimage():

    array = np.zeros((3,3))
    im = GSImage(array,xmin=1,ymin=1)
    im.array[...] = np.arange(9).reshape((3,3))
    mask = im.array < 3
    im2 = im.copy()
    assert isinstance(im2,GSImage)
    im[mask] = 0
    assert np.all(im.array[0,np.arange(3)] == 0)
    im[galsim.BoundsI(1,3,1,1)] = np.ones((1,3))
    assert np.all(im.array[0,:3] == 1)
    im3 = GSImage(array,xmin=1,ymin=1)
    im3[mask] = im2.array[mask]
    assert im3 == im2


if __name__ == '__main__':

    test_paths()
    test_versions()
    test_sim_id()
    test_get_survey()
    test_gsimage()
