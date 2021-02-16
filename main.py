from ucsmsdk.ucshandle import UcsHandle

ucsm_domain = '75.68.208.161'
user = 'ucspe'
password = 'password'

handle = UcsHandle(ucsm_domain, user, password)
handle.login()

lic_inventory = handle.query_classid('licenseInstance')

for lic in lic_inventory:
    print(lic)

handle.logout()

# license_inventory