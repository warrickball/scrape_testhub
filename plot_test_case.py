#!/usr/bin/env python

import json
import numpy as np
from matplotlib import pyplot as pl
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('test_case', type=str,
                    help="name of test_case")
parser.add_argument('filenames', type=str, nargs='+',
                    help="filenames containing JSON data")
parser.add_argument('-x', type=str, default='version',
                    help="key for x axis (default='version')")
parser.add_argument('-y', type=str, default='runtime',
                    help="key for y axis (default='runtime')")
parser.add_argument('-o', '--output', type=str, default=None,
                    help="save plot to this filename instead of plotting")
parser.add_argument('-s', '--style', type=str, default='o',
                    help="point style (default='o')")
args = parser.parse_args()

for filename in args.filenames:
    with open(filename, 'r') as f:
        data = json.loads(f.read())

    x, y, passed = [np.array([row[k] for row in data
                              if row['test_case'] == args.test_case])
                    for k in [args.x, args.y, 'passed']]
    
    pl.plot(x[passed], y[passed], args.style, label=filename)

pl.title(args.test_case)
pl.xlabel(args.x)
pl.ylabel(args.y)
pl.legend()

if args.output is None:
    pl.show()
else:
    pl.savefig(args.output)
