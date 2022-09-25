#!/usr/bin/env python3

# List cost,used-kwh,avg-price,avg-temp,date per day
# When there is a lack of data, nothing is listed.
# The indata is taken from files förbrukning_dump.csv and pris/el-pris_dump.csv
# Usage:
#   $0 from-date to-date

import sys
import numpy as np
import pandas as pd
import datetime

if len(sys.argv) < 3:
    sys.exit("Usage: kostnad_timme.py from-date to-date")

fromDate = sys.argv[1]
toDate = sys.argv[2]

förbrukningCsv = pd.read_csv(
    "förbrukning_dump.csv", header=None, names=["date", "hr", "kwh", "temp"]
)
elPrisCsv = pd.read_csv(
    "pris/el-pris_dump.csv", header=None, names=["date", "hr", "price"]
)

# print(förbrukningCsv[förbrukningCsv["temp"].isnull()])
förbrukningCsv.dropna(inplace=True)

# print(förbrukningCsv.loc[[3, 5]])
# print(elPrisCsv.loc[[3, 5]])
# print(förbrukningCsv.head())
# print(elPrisCsv.head())
# print(förbrukningCsv.info())
# print(elPrisCsv.info())
# print(förbrukningCsv[förbrukningCsv["date"] == fromDate])
# print(elPrisCsv[elPrisCsv["date"] == "2022-09-18"])

datetimeFrom = datetime.date.fromisoformat(fromDate)
datetimeTo = datetime.date.fromisoformat(toDate)

timedeltaDay = datetime.timedelta(days=1)

datetimeCur = datetimeFrom

while datetimeCur < datetimeTo:
    curFörbrukningCsv = förbrukningCsv[
        förbrukningCsv["date"] == datetimeCur.strftime("%Y-%m-%d")
    ]
    curPrisCsv = elPrisCsv[elPrisCsv["date"] == datetimeCur.strftime("%Y-%m-%d")]
    hrFörbrukningNp = curFörbrukningCsv.loc[:, "hr"].to_numpy(dtype="int8")
    kwhNp = curFörbrukningCsv.loc[:, "kwh"].to_numpy(dtype="float32")
    tempNp = curFörbrukningCsv.loc[:, "temp"].to_numpy(dtype="float32")
    hrPrisNp = curPrisCsv.loc[:, "hr"].to_numpy(dtype="int8")
    priceNp = curPrisCsv.loc[:, "price"].to_numpy(dtype="float32")
    # print(hrFörbrukningNp)
    # print(kwhNp)
    # print(tempNp)
    # print(hrPrisNp)
    # print(priceNp)
    lenFörbrukning = len(hrFörbrukningNp)
    lenPris = len(hrPrisNp)
    if lenFörbrukning == 0 or lenPris == 0:
        datetimeCur = datetimeCur + timedeltaDay
        continue
    costSum = 0.0
    kwhSum = 0.0
    priceSum = 0.0
    temperatureSum = 0.0
    numCosts = 0
    ixFörbrukning = 0
    ixPris = 0
    while ixFörbrukning < lenFörbrukning and ixPris < lenPris:
        if hrFörbrukningNp[ixFörbrukning] < hrPrisNp[ixPris]:
            kwhSum += kwhNp[ixFörbrukning]
            temperatureSum += tempNp[ixFörbrukning]
            ixFörbrukning += 1
            continue
        if hrFörbrukningNp[ixFörbrukning] > hrPrisNp[ixPris]:
            priceSum += priceNp[ixPris]
            ixPris += 1
            continue
        numCosts += 1
        costSum += kwhNp[ixFörbrukning] * priceNp[ixPris]
        kwhSum += kwhNp[ixFörbrukning]
        priceSum += priceNp[ixPris]
        temperatureSum += tempNp[ixFörbrukning]
        ixFörbrukning += 1
        ixPris += 1

    print(
        "{:04.0f},{:03.1f},{:03.0f},{:02.0f},{}".format(
            costSum,
            kwhSum,
            priceSum / ixPris,
            temperatureSum / ixFörbrukning,
            datetimeCur,
        )
    )

    datetimeCur = datetimeCur + timedeltaDay
