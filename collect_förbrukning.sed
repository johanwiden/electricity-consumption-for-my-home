# sed script to clean förbrukning_dump.csv
s/",/";/g
s/,"/;"/g
s/,/./g
s/ /;/
s/"//g
s/;[^;]*$//
s/;/,/g
s/:00//
