# CASA 6.5.6
# Developed by J.Sai
# Jan 7, 2024


### Modules
import glob
import sys, os
import numpy as np
from dataclasses import dataclass, replace


@dataclass #(slots=True)
class MS:

    msname: 'none'
    fields: [] # field names
    spws: []   # science spws
    restfreqs: {} # Rest frequencies
    nspws: 0 # number of spws
    lines: []



class MSSet(object):
    """docstring for MSSet"""
    def __init__(self, arg):
        super(MSSet, self).__init__()


    def get_vises(self, key='*.split.cal', lines=[]):
        self.mslist = glob.glob(key)
        self.msdict = {'%i'%i: i for i in range(len(mslist))}

        for i, vis in enumerate(self.mslist):
            msmd.open(vis)
            fieldnames = msmd.fieldnames()
            #fieldids = msmd.fieldsforname
            spws = msmd.spwsforintent('*TARGET*')
            nspws = len(spws)
            trg_fields = msmd.fieldsforintent('*TARGET*')
            trg_srcids = [msmd.sourceidforfield(k) for k in trg_fields]
            restfreqs = {'%i'%spw:
            msmd.restfreqs(trg_srcids[0], spw)['0']['m0'] for spw in spws
            }

            _ms = MS(vis, fieldnames, spws, restfreqs, nspws, lines)
            self.msdict[i] = _ms
            print(_ms)


    def add_lines(self, lines):
        if type(lines[0]) == 'str':
            for i in self.msdict.keys():
                ms = self.msdict[i]
                setattr(_ms, 'lines', lines)


    def summary(self):
        for i in self.msdict.keys():
            ms = self.msdict[i]
            print(ms)


    def splitout(self, field = None, line = None):
        vises = self.mslist
        outvises = []
        for i in self.msdict.keys():
            vis = self.msdict[i]['msname']
            spws = self.msdict[i]['spws']
            lines = self.msdict[i]['lines']
            spw = np.array(spws)[np.array(lines) == line]

            outputvis = '.'.join([vis, field, line])
            split(vis, outputvis = '.'.join([vis, field, line]),
                field=field, spw = spw)
            outvises.append(outputvis)

        concat(vis = outvises, concatvis = '_'.join(field, line) + '.ms')
        for vis in outvises:
            os.system('rm -r ' + vis)