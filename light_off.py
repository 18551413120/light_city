import requests
import time

#электро станция
OFF = 'http://192.168.168.1:8000/cgi-bin/manager?CHANNEL=ALL_OFF_ONLY&TASK=OFF'
requests.get(OFF)