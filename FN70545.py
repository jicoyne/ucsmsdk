from ucsmsdk.ucshandle import UcsHandle

handle = UcsHandle('10.201.27.108', 'jicoyne', 'password?')

handle.login()

storage_resources = handle.query_classid('storageLocalDisk')

for item in storage_resources:
    if item.device_version == 'C401' or item.device_version == 'C402' or item.device_version == 'C403':
        print(item.dn, item.device_version + ' Matches FN70545! ')
    else:
        print(item.dn, item.device_version)

handle.logout()

#https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70545.html

#https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvt55829/?rfs=iqvred