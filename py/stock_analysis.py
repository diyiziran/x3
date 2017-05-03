#!/usr/bin/env python
# -*- coding: utf-8 -*-



import pandas as pd
import pandas_datareader.data as web

import datetime

start=datetime.datetime(2010,1,1)
end=datetime.date.today()

maotai=web.DataReader("600519.SS","yahoo",start,end)

type(maotai)




