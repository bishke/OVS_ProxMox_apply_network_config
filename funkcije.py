############### Funkcije ########################
import requests
from datetime import datetime

def headcoockie():
    connection = requests.Session()
    login_data = {
        'username': 'root@pam',
        'password':'Kr4guj034'
            }
    proxmox = connection.post('https://147.91.209.5:8006/api2/json/access/ticket', data=login_data, verify=False)
    data = proxmox.json()
    CSRFPreventionToken = data['data']['CSRFPreventionToken']
    ticket = data['data']['ticket']
    cookies = {
        'PVEAuthCookie': ticket
            }
    headers = {
        'CSRFPreventionToken': CSRFPreventionToken
            }
    return cookies,headers

def prijava_na_klaster(username, password):
    connection = requests.Session()
    login_data = {
        'username': username+'@pam',
        'password': password
            }
    proxmox = connection.post('https://147.91.209.5:8006/api2/json/access/ticket', data=login_data, verify=False)
    data = proxmox.json()
    CSRFPreventionToken = data['data']['CSRFPreventionToken']
    ticket = data['data']['ticket']
    cookies = {
        'PVEAuthCookie': ticket
            }
    headers = {
        'CSRFPreventionToken': CSRFPreventionToken
            }
    if CSRFPreventionToken and ticket:
        status_code = 'OK!'
    else:
        status_code = 'Error!'

    return status_code, cookies,headers
