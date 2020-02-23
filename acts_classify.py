#################################
#################################

# 1. Merge soc_wel8_3 and soc_wel9_1; leave all non-existant variables blank

# 2. Qualitatively code public servcies, social services, associational, and propaganda

# Dummy variables for the above


######################################
######################################

# qualitative coding


# read more the activities of party affiliated orgs
# find some standards and key words for propaganda

#####################################

# Step 1: merge soc_wel8_3_temp & soc_wel9_1_temp - append all other variables as empty

# soc_wel8_3_temp is longer

import csv
d = csv.DictReader(open('/Users/eunhousong/Home/AB/soc_wel8_3_temp.csv', 'rU'))

# list with dictionaries

soc = []
for row in d:
    soc.append(row)

len(soc)

# delete, list comprehension
# check type
type(soc[0]['is_shequ_act']) # if integer if string

soc = [x for x in soc if x['is_shequ_act'] == '1'] # subset

soc[0].keys()

len(soc) # around 800

# check length of keys:
soc_wel8 = soc[0].keys()
len(soc_wel8) # 29

soc_wel8.sort() # sort keys alphabetically

# Step 2: read soc_wel9_1, append the remaining variables, when organization name matches
# Append those without information as NA


import csv
d = csv.DictReader(open('/Users/eunhousong/Home/AB/soc_wel9_2_temp.csv', 'rU'))

soc2 = []
for row in d:
    soc2.append(row)

len(soc2)
soc2 = [x for x in soc2 if x['is_shequ_act'] == '1'] # subset
len(soc2) # 507

soc_wel8 = soc[0].keys()
len(soc_wel8) # 29

soc_wel9 = soc2[0].keys()
len(soc_wel9) # 48


# get the difference:
new_keys = list(set(soc_wel9) - set(soc_wel8))
len(new_keys) # the new variables, 19

# soc_wel8 elements are already in soc_wel9

# append the 80 elements to soc_wel9_1, leave rest of the 19 key values as 'NA'

# create the 19 new keys to soc, and then append the different org name elements to soc2

# use update:

for i in range(len(soc)):
    soc[i].update(dict.fromkeys(new_keys, 'NA')) # append all 'NA' to new keys

# check
len(soc[0].keys()) # should be 48, same as soc2

# subset soc, for those that name do not match with soc2
# the most recent organizations in the list

# list comprehension

org_names = []
for i in range(len(soc2)):
    org_names.append(soc2[i]['org_name'])

len(org_names) # around 507

# use list comprehension:

soc3 = [x for x in soc if x['org_name'] not in org_names]

# subset, get those that do not overlap, should be around 300

# add the soc3 to soc2:
len(soc3) # should be 304 - 224, 325 organizations

# soc3 is now a subset fromd the larger 4K data set, with those without reports as NA

soc4 = soc2 + soc3

len(soc4) # should be 832
soc4[0].keys()
len(soc4[0].keys())

# save as csv
import csv
keys = soc4[0].keys()
with open('soc_wel9_comm.csv', 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(soc4)


##############################

import csv
d = csv.DictReader(open('/Users/eunhousong/Home/AB/soc_wel9_comm.csv', 'rU'))

soc = []
for row in d:
    soc.append(row)

len(soc)


# qualitative coding on the soc_wel9 data:


# 1) Public Service, Community Self-Governance, Volunteer and Social Work

# PUBLIC SERVICE

# use simple in and then index

# overwrite ps:

for i in range(len(soc)):
    soc[i]['pbs'] = 0

pbs = ['社区管里',
'治安',
'综合治理',
'人口管理',
'外来人口登记管理',
'外来人口管理',
'公共管理',
'卫生管理',
'环境管理',
'登记管理',
'社会组织',
'民间组织',
'群众组织',
'消防',
'社会管理',
'社会组织',
'人民调解',
'矛盾调处',
'综合帮扶',
'综合协管服务',
'党建',
'社区事务',
'公共文化',
'公共文化服务',
'体育设施',
'社区环境',
'综合协管',
'社区矛盾调解',
'社会组织孵化',
'民生服务',
'民生类服务',
'社区民生服务',
'便民',
'便民服务',
'社区服务',
'社区居民服务',
'互助',
'公益类服务',
'公益性服务',
'市民综合帮扶',
'社区事务',
'综合服务',
'社会便民服务']


index0 = []

for i in range(len(soc)):
    for word in pbs:
        if word in soc[i]['act']:
            index0.append(i)
        else:
            pass


index0_true = list(set(index0)) # remove duplicates

len(index0)
len(index0_true)

# for the index, create dummies:
for i in range(len(soc)):
    soc[i]['pbs'] = 0

# overwrite

for index in index0_true:
    soc[index]['pbs'] = 1




# COMMUNITY SELF GOVERNANCE

# find comm_self

comms = ['社区治理活动', '社区治理','自治','社区自治','共治']

index = []

for i in range(len(soc)):
    for word in comms:
        if word in soc[i]['act']:
            index.append(i)
        else:
            pass

index_true = list(set(index)) # remove duplicates

# for the index, create dummies:
for i in range(len(soc)):
    soc[i]['comm_self'] = 0

# overwrite

for index in index_true:
    soc[index]['comm_self'] = 1

# SOCIAL WORKER
# find volunteer and social work:

shegong = ['社区工作者','社工','社区志愿者','社会工作','志愿','志愿者']

index2 = []

for i in range(len(soc)):
    for word in shegong:
        if word in soc[i]['act']:
            index2.append(i)
        else:
            pass

index2_true = list(set(index2)) # remove duplicates

for i in range(len(soc)):
    soc[i]['swo'] = 0

# overwrite

for index in index2_true:
    soc[index]['swo'] = 1

# SOCIAL SERVICES
# code the rest of pb as social services:

for i in range(len(soc)):
    if soc[i]['pbs'] == 0:
        soc[i]['ss'] = 1
    else:
        soc[i]['ss'] = 0

# 2) Propaganda vs. Associational

# create propaganda dummy variable

propa = ['思想道德',
'优生优育知识的宣传',
'人口计划生育',
'人口与计生',
'人口计生',
'政策宣传',
'精神文明建设',
'文明',
'宣传党的政策方针',
'宣传党的']


index3 = []

for i in range(len(soc)):
    for word in propa:
        if word in soc[i]['act']:
            index3.append(i)
        else:
            pass

index3_true = list(set(index3)) # remove duplicates

for i in range(len(soc)):
    soc[i]['prop'] = 0

# overwrite

for index in index3_true:
    soc[index]['prop'] = 1

# create associational activity dummy variable

# ASSOCIATIONAL

asso = ['文化活动',
'体育',
'文体',
'交流活动',
'青年活动',
'竞赛',
'音乐']


index4 = []

for i in range(len(soc)):
    for word in asso:
        if word in soc[i]['act']:
            index4.append(i)
        else:
            pass

index4_true = list(set(index4)) # remove duplicates

for i in range(len(soc)):
    soc[i]['asso'] = 0

# overwrite

for index in index4_true:
    soc[index]['asso'] = 1

# PUBLIC INTEREST ACTIVITIES
# 3) pi_act

pi = ['公益活动','公益性活动','公益类活动','公益项目']



index5 = []

for i in range(len(soc)):
    for word in pi:
        if word in soc[i]['act']:
            index5.append(i)
        else:
            pass

index5_true = list(set(index5)) # remove duplicates

for i in range(len(soc)):
    soc[i]['pi_act'] = 0

# overwrite

for index in index5_true:
    soc[index]['pi_act'] = 1


# rep_is_rc:


# created 7 new variables, now keys should be 48+7 = 56

len(soc[0].keys())


# save

import csv
keys = soc[0].keys()
with open('soc_wel9_qualc.csv', 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(soc)



########### Go back to ArcGIS ###########







###### Write Out What I Need to Know Further Before Survey #####


# get more clear on the qualitative evidence of party affiliation

# get more clear on how to approach migrant organizations

# get more clear on how to approach community self reliance

# I also want to know what are the affiliations of the propaganda organizations - bdinfo & sup_org

# I want to know how social work is organized
