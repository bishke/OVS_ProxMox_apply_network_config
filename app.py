import requests

from funkcije import prijava_na_klaster, headcoockie
#disable warnings
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#

host='https://147.91.209.5:8006/api2/json/nodes/pve-ovs-01/network'
connection = requests.Session()
status = headcoockie()


###### izlistaj sve sviceve ################
#proxmox = connection.get(host, cookies=status[0], verify=False)
#print('-----------------')
#data = proxmox.json()
#for i in range(len(data['data'])):
#    if data['data'][i]['type'] =='OVSBridge':
#        print(data['data'][i]['iface'])

##################vmid & name############################
host='https://147.91.209.5:8006/api2/json/nodes/pve-ovs-01/lxc'
proxmox = connection.get(host, cookies=status[0], verify=False)
data = proxmox.json()
net_interfaces=[]
#prodji kroz sve vmid iz lxc skupa
for i in range(len(data['data'])):
    vmid = data['data'][i]['vmid']
    print('Radim: '+str(vmid))
    host1=host+'/'+str(vmid)+'/config/'
    proxmox = connection.get(host1, cookies=status[0], verify=False)
    data2 = proxmox.json()
    net_interfaces=[]
    #za svaki vmid, izvuci sve sto pocinje sa 'netX' (jedan vmid moze imati net0,net1,net2...)
    # i dodaj pronadjeni net u listu net_interfaces - dakle, jedan vmid u listi net_interfaces[]
    # moze da ima jedan clan, ili vise clanova liste
    # print(data2) za detalje
    for j in data2['data'].keys():      
        if j.startswith('net'):
            net_interfaces.append(j)
    #
    for j in net_interfaces:
        bridge = data2['data'][j].split(',')
        name = ''
        br=''
       
        for k in bridge:
            if k.startswith("name="):
                name = k

            if k.startswith('bridge='):
                br = k
             
       
        dataX = {
            str(j):''+str(name)+','+str(br)+''
        }
        print('Radim: '+str(name)+','+str(br)+'')
        #print(dataX)
        proxmox = connection.put('https://147.91.209.5:8006/api2/json/nodes/pve-ovs-01/lxc/100/config', data=dataX, headers=status[1],cookies=status[0], verify=False)
        




###################azuriranje networking kod vm##################
#print('######-----------------------------')
#data = {
#    'net0':'name=eth0,bridge=vmbr1'
#}
#t=proxmox = connection.put('https://147.91.209.5:8006/api2/json/nodes/pve-ovs-01/lxc/100/config', data=data, headers=status[1],cookies=status[0], verify=False)
#print(t)