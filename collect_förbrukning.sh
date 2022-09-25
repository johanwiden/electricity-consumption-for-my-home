#!/usr/bin/env sh

# Dumpa förbrukningsrader till förbrukning_dump.csv.
# förbrukning_dump.csv hyfsas så den följer csv format.
#   datum,timme,förbrukning,temperatur
# Usage:
#   $0 csv-fil...
dumpfile="förbrukning_dump.csv"

egrep --no-filename '^.20' $* >"${dumpfile}"
sed -i -f collect_förbrukning.sed "${dumpfile}"
