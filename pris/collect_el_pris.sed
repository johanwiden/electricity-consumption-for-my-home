# sed script to change el-pris_dump.csv into a csv file
s/[.]json:.*Kl[.] /;/
s/ - [0-2][0-9].*: "/;/
s/ öre.*//
s/,/./
s/;/,/g
s/^\(2[0-9]\)\([0-1][0-9]\)\([0-3][0-9]\)/20\1-\2-\3/
