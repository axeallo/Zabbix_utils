# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 22:13:56 2020

@author: axeallo
"""

import requests, urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def auth(user, pwd, adr):
    '''
    To authenticate put on first place login, next password, then link.
    Link is usually looks like 'https://zabbixserver/zabbix/api_jsonrpc.php'
    Returns authentication token
    '''
    res={"jsonrpc": "2.0","method": "user.login","params": {"user": user,"password":pwd},"id": 1,}
    tkn = requests.get(adr, json=res, verify = False)
    return tkn.json()['result']