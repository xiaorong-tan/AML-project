import pandas as pd
import matplotlib.pyplot as plt
hpgres = pd.read_csv('hpg_reserve.csv')
import csv
import numpy as np
hpg_id = hpgres.hpg_store_id;
hpg_date = hpgres.visit_datetime;
list_id = []
list_date = [] # 
list_res_date = [] # 
# get date
for i in range(0,len(hpg_date)):
    string_date = hpg_date[i];
    split_date = string_date.split(' ');
    list_res_date.append(split_date[0]);
    if(split_date[0] not in list_date):
        list_date.append(split_date[0]);

for i in range(0,len(hpg_id)):
    if(hpg_id[i] not in list_id):
        list_id.append(hpg_id[i]);

import time
start = time.clock();
day_vis = np.zeros((len(list_id),len(list_date)))
for k in range(0, len(hpg_id)):
  timeConsumed = (time.clock() - start);
    print("calculating restaurant",k,"daily visitors, time consumed", timeConsumed, "second");
    i = 0;
    j = 0;
    while (hpg_id[k] != list_id[i]) :
        i = i + 1;
        # throw exception
        if (i > len(list_id)):
            print("error i");
    while (list_res_date[k] != list_date[j]):
        j = j + 1;
        # throw exception
        if (j > len(list_date)):
            print("error j");
    day_vis[i,j] = hpgres.reserve_visitors[k] + day_vis[i,j];
 
np.savetxt('hpg_id_visitor_FromReserveInformation.csv', day_vis, delimiter = ',')   