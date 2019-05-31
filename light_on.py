import requests
import time

#электро станция
url_light_electro_1 = 'http://192.168.168.1:8000/cgi-bin/manager?CHANNEL=POWER_PLANT_BUILDING_RED&TASK=ON'
requests.get(url_light_electro_1)
time.sleep(1)
url_light_electro_2 = 'http://192.168.168.1:8000/cgi-bin/manager?CHANNEL=POWER_PLANT_LIGHTS&TASK=ON'
requests.get(url_light_electro_2)
time.sleep(1)
url_light_tes_1 = 'http://192.168.168.1:8000/cgi-bin/manager?CHANNEL=CHEMICAL_2_BUILDING&TASK=ON' 
requests.get(url_light_tes_1)
time.sleep(1)
url_light_tes_2 = 'http://192.168.168.1:8000/cgi-bin/manager?CHANNEL=CHEMICAL_2_FUNNELS&TASK=ON'
requests.get(url_light_tes_2)
time.sleep(1)
url_light_tes_3 = 'http://192.168.168.1:8000/cgi-bin/manager?CHANNEL=CHEMICAL_1_AND_2_LIGHTS&TASK=ON'
requests.get(url_light_tes_3)
time.sleep(1)

#Трансформатор
url_light_transf_1 = 'http://192.168.168.1:8000/cgi-bin/manager?CHANNEL=TRANS_1_RED&TASK=ON'
requests.get(url_light_transf_1)
time.sleep(1)
url_light_transf_2 = 'http://192.168.168.1:8000/cgi-bin/manager?CHANNEL=TRANS_2_RED&TASK=ON'
requests.get(url_light_transf_2)
time.sleep(1)

#подстанция
url_light_substa_1 = 'http://192.168.168.1:8000/cgi-bin/manager?CHANNEL=SUBSTATION_BUILDING&TASK=ON'
requests.get(url_light_substa_1)
time.sleep(1)
url_light_substa_2 = 'http://192.168.168.1:8000/cgi-bin/manager?CHANNEL=DEPOT_BUILDING&TASK=ON'
requests.get(url_light_substa_2)
time.sleep(1)
url_light_substa_3 = 'http://192.168.168.1:8000/cgi-bin/manager?CHANNEL=DEPOT_LIGHTS&TASK=ON'
requests.get(url_light_substa_3)
time.sleep(1)
url_light_substa_4 = 'http://192.168.168.1:8000/cgi-bin/manager?CHANNEL=POWER_TOWERS_1&TASK=ON'
requests.get(url_light_substa_4)
time.sleep(1)
url_light_substa_5 = 'http://192.168.168.1:8000/cgi-bin/manager?CHANNEL=POWER_TOWERS_2&TASK=ON'
requests.get(url_light_substa_5)
time.sleep(1)

#Химзавод
url_light_chem_fact_1 = 'http://192.168.168.1:8000/cgi-bin/manager?CHANNEL=CHEMICAL_1_BUILDING_RED&TASK=ON'
requests.get(url_light_chem_fact_1)
time.sleep(1)
url_light_chem_fact_2 = 'http://192.168.168.1:8000/cgi-bin/manager?CHANNEL=CHEMICAL_1_BUILDING_WHITE&TASK=ON'
requests.get(url_light_chem_fact_2)
time.sleep(1)
url_light_chem_fact_3 = 'http://192.168.168.1:8000/cgi-bin/manager?CHANNEL=CHEMICAL_1_SINK_PIPE_RED&TASK=ON'
requests.get(url_light_chem_fact_3)
time.sleep(1)
url_light_chem_riv = 'http://192.168.168.1:8000/cgi-bin/manager?CHANNEL=RIVER_RED&TASK=ON'
requests.get(url_light_chem_riv)
time.sleep(1)

#Город
url_light_city_1 = 'http://192.168.168.1:8000/cgi-bin/manager?CHANNEL=CITY_LIGHTS&TASK=ON'
requests.get(url_light_city_1)
time.sleep(1)
url_light_city_2 = 'http://192.168.168.1:8000/cgi-bin/manager?CHANNEL=CITY_BUILDINGS&TASK=ON'
requests.get(url_light_city_2)
time.sleep(1)
url_light_city_3 = 'http://192.168.168.1:8000/cgi-bin/manager?CHANNEL=TOWN_LIGHTS&TASK=ON'
requests.get(url_light_city_3)
time.sleep(1)
url_light_village = 'http://192.168.168.1:8000/cgi-bin/manager?CHANNEL=TOWN_BUILDINGS&TASK=ON'
requests.get(url_light_village)
time.sleep(1)