#!/usr/bin/env sh

# Dumpa prisrader, med datum tillagt, till el_pris_dump.csv
# Hyfsa el_pris_dump.csv så den följer csv format.
#   datum,timme,pris
# Usage:
#   $0 el-pris-fil...
dumpfile=el-pris_dump.csv

fgrep --with-filename 'Kl. ' $* >"${dumpfile}"
sed -i -f collect_el_pris.sed "${dumpfile}"
