# electricity-consumption-for-my-home
Scripts to produce reports on my electricity use, and its cost.
Used under Ubuntu linux. Should work under other OS:s as well, if they have python, egrep, sed, sh.

I download data about my electricity use from my electric grid operator (SEOM). I store this as CSV files.
I copy data from a web page, to get todays electric current prices (per hour). I store this as CSV files.

Currently it does not seem to be possible to get historic electric current prices, per hour, in Sweden,
only for the current day. I suspect that this is due to business license agreements.

I use script collect_förbrukning.sh to copy downloaded SEOM CSV files to file "förbrukning.dump",
and sanitize that file.

I use script "pris/collect_el_pris.sh" to copy CSV files with daily current prices to "pris/el-pris_dump.csv",
and sanitize that file.

I then run python script "kostnad_timme.py" (in english: cost_hour) to produce a report with costs per hour.
I run the script as follows:

  ./kostnad_timme.py 2022-09-18 2022-09-26

This produces a per hour report for the days from 2022-09-18 inclusive, to 2022-09-26 exclusive.
Missing data is handled.

I run script "kostnad_dag.py" (in english: cost_day) to produce a report with costs per day.
I run the script as follows:

  ./kostnad_dag.py 2022-09-18 2022-09-26

This produces a per day report for the days from 2022-09-18 inclusive, to 2022-09-26 exclusive.
Missing data is handled.  
