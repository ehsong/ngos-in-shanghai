
#################################################

# THIS SCRIPT INCLUDES PROCESS OF ATTACHING GOVERNMENT REPORT PARSED INFORMATION AS VARIABLES
# ORIGINAL FILE = SOC_WEL9
# USED TEXT FROM text_scraped0504.csv DONE BY LYU CHAO

# ORIGINAL NUMBER OF VARIABLES - 29
# ADDED NUMBER OF VARIABLES - 17

# SEE GOV_REPORTS_FIELD_CODED.TXT FOR FURTHER EXPLANATION


#########################################################

# Step 1: delete all organizations of which links did not work

# import the mega file
import csv
d = csv.DictReader(open('/Users/eunhousong/Home/AB/soc_wel8.csv', 'rU'))

soc = []
for row in d:
    soc.append(row)


soc[0].keys()
len(soc[0].keys())

# append the text scrapes:
# import the text file

import csv
d2 = csv.DictReader(open('/Users/eunhousong/Home/text_scraped0504.csv', 'rU'))

text = []
for row in d2:
    text.append(row)

text[0].keys() #['url', 'output', '\xef\xbb\xbforg_name', '']


for i in range(len(text)):
    for j in range(len(soc)):
        if (soc[j]['org_name'] == text[i]['\xef\xbb\xbforg_name']) is True:
            soc[j]['report_scraped'] = ''.join(text[i]['output'].split())
        else:
            pass

#
soc[0].keys()
len(soc[0].keys())

for i range(0,5):
    print soc[i]['report_scraped'] # success

# Step 2: extract information and append as text, if information does not exist they should be noted


# delete those, if report_scraped does not exist or is page Unavailable
# use list comprehension
new = [x for x in soc if x['report_scraped']!=''] # is a dictionary
new2 = [x for x in new if x['report_scraped']!='Page Unavailable']
new2 = [x for x in new2 if x['report_scraped']!='PageUnavailable']

len(new2) # 3023 with new key 'report_scraped'


# Step 3: ADD WANTED VARIABLES AS A DICTIONARY

# first variable: origins of funding when first established
# 'funding_start'

import re

for i in range(len(new2)):
    text = new2[i]['report_scraped']
    m = re.search('开办资金来源：(.+?)行', text)
    if m:
        new2[i]['funding_start'] = m.group(1) # the text between the two
    else:
        new2[i]['funding_start'] = found = 'NA' # leave blank



# number of members

import re

for i in range(len(new2)):
    text = new2[i]['report_scraped']
    m = re.search('单位会员数：(.+?)个', text)
    if m:
        new2[i]['members_no'] = m.group(1) # the text between the two
    else:
        new2[i]['members_no'] = 'NA' # leave blank


# party building

import re

pb_form = []
for i in range(len(new2)):
    text = new2[i]['report_scraped']
    m = re.search('党建形式：(.+?)2', text)
    if m:
        pb_form.append(m.group(1)) # the text between the two
    else:
        pb_form.append('NA') # leave blank

# append party building as dummy variable:

for i in range(len(new2)):
    if (pb_form[i]!='无') is True:
        new2[i]['pb_dum'] = 1
    else:
        new2[i]['pb_dum'] = pb_form[i]

# finances

# search list:
sl = ['本年度收入合计：(.+?)元',
'政府购买服务收入：(.+?)元',
'接受社会捐赠：(.+?)元',
'政府补助（资助）收入：(.+?)元',
'来自市级有关部门：(.+?)元',
'来自区县级有关部门：(.+?)元',
'来自街镇级有关部门：(.+?)元',
'会费收入：(.+?)元',
'政府补助（资助）项目：(.+?)个'
]

# income
import re
for i in range(len(new2)):
    text = new2[i]['report_scraped']
    m = re.search(sl[0], text)
    if m:
        new2[i]['fi_income'] = m.group(1) # the text between the two
    else:
        new2[i]['fi_income'] = 'NA' # leave blank

# procurement
import re
for i in range(len(new2)):
    text = new2[i]['report_scraped']
    m = re.search(sl[1], text)
    if m:
        new2[i]['fi_pro_income'] = m.group(1) # the text between the two
    else:
        new2[i]['fi_pro_income'] = 'NA' # leave blank

# donations
import re
for i in range(len(new2)):
    text = new2[i]['report_scraped']
    m = re.search(sl[2], text)
    if m:
        new2[i]['fi_do'] = m.group(1) # the text between the two
    else:
        new2[i]['fi_do'] = 'NA' # leave blank

# gov subsidy
import re
for i in range(len(new2)):
    text = new2[i]['report_scraped']
    m = re.search(sl[3], text)
    if m:
        new2[i]['fi_sub'] = m.group(1) # the text between the two
    else:
        new2[i]['fi_sub'] = 'NA' # leave blank


# gov subsidy - bureau
import re
for i in range(len(new2)):
    text = new2[i]['report_scraped']
    m = re.search(sl[4], text)
    if m:
        new2[i]['fi_sub_bur'] = m.group(1) # the text between the two
    else:
        new2[i]['fi_sub_bur'] = 'NA' # leave blank


# gov subsidy - dis
import re
for i in range(len(new2)):
    text = new2[i]['report_scraped']
    m = re.search(sl[5], text)
    if m:
        new2[i]['fi_sub_dis'] = m.group(1) # the text between the two
    else:
        new2[i]['fi_sub_dis'] = 'NA' # leave blank


# gov subsidy - neigh
import re
for i in range(len(new2)):
    text = new2[i]['report_scraped']
    m = re.search(sl[6], text)
    if m:
        new2[i]['fi_sub_nb'] = m.group(1) # the text between the two
    else:
        new2[i]['fi_sub_nb'] = 'NA' # leave blank


# membership fee

import re
for i in range(len(new2)):
    text = new2[i]['report_scraped']
    m = re.search(sl[7], text)
    if m:
        new2[i]['fi_mf'] = m.group(1) # the text between the two
    else:
        new2[i]['fi_mf'] = 'NA' # leave blank


# gov project
import re
for i in range(len(new2)):
    text = new2[i]['report_scraped']
    m = re.search(sl[8], text)
    if m:
        new2[i]['gpro_no'] = m.group(1) # the text between the two
    else:
        new2[i]['gpro_no'] = 'NA' # leave blank


############################################################

# parse board of directors information

import re

bdinfo = []
for i in range(len(new2)):
    text = new2[i]['report_scraped']
    m = re.search('其他工作单位及职务(.+?)（', text)
    if m:
        bdinfo.append(m.group(1)) # the text between the two
    else:
        bdinfo.append('NA') # leave blank

len(new2)
len(bdinfo)

# save the positions where information exists

index = []
for i in range(len(bdinfo)):
    if (bdinfo[i]!='NA') is True:
        index.append(i) # the rows that has this information, total #1845, same order as new2
    else:
        pass

len(index)

# work with bdinfo_ex, a list with all the texts:

bdinfo_ex = []
for i in index:
    bdinfo_ex.append(bdinfo[i])


# list of positions:

# 理事长
# 副理事长
# 理事
# 理事
# 理事
# 理事会成员、法定代表人
# 董事长

# check if all the elements have the word 'director'

# use regualr expression, matching

pattern = re.compile(u'副理')

index = []

for i in range(len(bdinfo_ex)):
    match = pattern.search(unicode(bdinfo_ex[i],'utf8'))
    if match:
        index.append(i)
    else:
        pass

len(index)

# how many 'head of bd' 1419

# how many 'vice hed of bd' 881

# how many 'directors' # 1493


####### Just work with head of board of directors ########


# structure of the text I want to extract:

# 1祁军男1970-03-23理事长2015-11-2010.00上海创叶广告设计有限公司策划2

# specific condition:
# position name + 2015-1
# find the start of the text I want to scrape

s = bdinfo_ex[4] # this is a string
uni_s = unicode(s,'utf8')

print uni_s[0] # works

start = uni_s.find(u'理事长') # this is not an accurate way to find where things start
# re-configure so that I find this word, between some numbers, two numbers to be exact

print uni_s[start+18]

subset = uni_s[start+18:(len(uni_s)-1)]
end = subset.find('2')
print subset[0:end] # the work place of the director

# creat a forloop for this:

directors = []

for i in range(len(bdinfo_ex)):
    uni_s = unicode(bdinfo_ex[i],'utf8')
    start = uni_s.find(u'理事长')
    subset = uni_s[start+18:(len(uni_s)-1)]
    end = subset.find('2') # 2 is for sub-directors
    directors.append(subset[0:end])

len(directors)
len(bdinfo_ex)

for i in range(0,10):
    print directors[i]


#######################

# write multiple patterns, append to the board of directors info
pattern = re.compile(u'理事长')

import re
match = []
directors = [] # save as a separate list for convenient indexing

for i in range(len(bdinfo)):
    match = pattern.search(unicode(bdinfo[i],'utf8'))
    if match:
        uni_s = unicode(bdinfo[i],'utf8')
        start = uni_s.find(u'理事长')
        if start < 32: # only if this word is in the first row, on average the first rows are around 32
            subset = uni_s[start+18:(len(uni_s)-1)]
            end = subset.find('2') # 2 is for sub-directors
            directors.append([i,subset[0:end]])
        else:
            directors.append([i,'没有信息'])
    else:
        directors.append([i,'没有信息'])

len(new2)
len(bdinfo)
len(directors)

# count those that are not 'no info'
index3 = []

for i in range(len(directors)):
    if (directors[i][1] != '没有信息') is True:
        index3.append(i)
    else:
        pass

len(index3) # 1385 has information on board of directors

# save as a separate index
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import pickle
with open("directors.txt", "wb") as f:
    for i in range(len(directors)):
        pickle.dump(print directors[i][1], f) # saved

# append as a value

for i in range(len(new2)):
    new2[i]['bdinfo'] = directors[i][1]

# check
print new2[500]['bdinfo']
print new2[500]['report_url']
print bdinfo[500] # all matched



##################################
###### create dummy variable from the directors info #######

# directors list; includes extracted text, includes wrong extractions
# for instance those wrong are mostly '无'
# could also code as 'NA'

# Step 1: Identify Party and Gov Affiliations + Append As Values of New2

# party --> party organizations ['残联','妇联','青团','工会','党']
# district --> names of each district， district_list.csv
# nb ---> ‘街道’

# simple finding & append

for i in range(len(directors)):
    if '党' in directors[i][1]:
        index.append(i)
    else:
        index.append()

len(index) # about 49



### other options ###
# use regular expression, party affiliation

party_org = ['残联','妇联','青团','工会','党']

# most are, party cells within different organizations
# such as universities, nb gov party secretaries, etc.

pattern = re.compile(u'残联|妇联|青团|工会|党')

import re
match = []
index = []

for i in range(len(directors)):
    match = pattern.search(directors[i][1])
    if match:
        index.append(i)
    else:
        pass

len(index)

# append
pattern = re.compile(u'残联|妇联|青团|工会|党')

import re
match = []
index = []

# find way to include
for i in range(len(directors)):
    match = pattern.search(directors[i][1])
    if match:
        new2[i]['rep_is_party'] = 1
    else:
        new2[i]['rep_is_party'] = 0

# overwrite NA
for i in range(len(directors)):
    if 'NA' in directors[i][1]:
        new2[i]['rep_is_party'] = directors[i][1]
    else:
        pass

# check
type(new2[0]['rep_is_party']) # is str

check = []
for i in range(len(new2)):
    if (new2[i]['rep_is_party'] == 1) is True:
        check.append(i)
    else:
        pass

len(check)



# the same:
index = []
for i in range(len(directors)):
    for j in range(len(party_org)):
        if party_org[j] in directors[i][1]:
            index.append(i)
        else:
            pass

len(index)

## District Level information

# for instance, if db is district affiliated

import pandas
data = pandas.read_csv('/Users/eunhousong/Home/district_list.csv',header=None)

dis=list(data[0])

u_dis = []
for district in dis:
    u_dis.append(unicode(district,'utf-8'))


u_dis

index = []
for i in range(len(directors)):
    for j in range(len(u_dis)):
        if u_dis[j] in directors[i][1]:
            index.append(i)
        else:
            pass

len(index) # 70

for i in index:
    print directors[i][1]


# append

# first code all as 0

for i in range(len(new2)):
    new2[i]['report_is_dis'] = 0

# overwrite NA
for i in range(len(directors)):
    if 'NA' in directors[i][1]:
        new2[i]['report_is_dis'] = directors[i][1]
    else:
        pass

for i in index:
    new2[i]['report_is_dis'] = 1

# overwrite NA


# check
type(new2[0]['report_is_dis']) # is str

check = []
for i in range(len(new2)):
    if (new2[i]['report_is_dis'] == 1) is True:
        check.append(i)
    else:
        pass

len(check)
# Neighborhood Afffiliation Information

index = []
for i in range(len(directors)):
    if '街道' in directors[i][1]:
        index.append(i)
    else:
        pass

len(index)

for i in index:
    print directors[i][1]

# append
for i in range(len(directors)):
    for j in range(len(dis)):
        if '街道' in directors[i][1]: # change condition -- should include 街道 but not 党
            new2[i]['report_is_nb'] = 1
        else:
            new2[i]['report_is_nb'] = 0

# overwrite NA

for i in range(len(directors)):
    if 'NA' in directors[i][1]:
        new2[i]['report_is_nb'] = directors[i][1]
    else:
        pass

# check
type(new2[0]['report_is_nb']) # is str

check = []
for i in range(len(new2)):
    if (new2[i]['report_is_nb'] == 1) is True:
        check.append(i)
    else:
        pass

len(check)



#########################

# just check:

# Neighborhood AND Party Affiliations

# Start from Party Affilated
# No need to create some variable, this is accessible with R

pattern = re.compile(u'残联|妇联|青团|工会|党')

import re
match = []
index = []

for i in range(len(directors)):
    match = pattern.search(directors[i][1])
    if match:
        index.append(i)
    else:
        pass

len(index)

for i in index:
    if '街道' in directors[i][1]:
        print directors[i][1]
    else:
        pass


#########################


# final check:

# original file soc_wel8 has 29 keys
# this script is adding 15 more keys

len(new2[0].keys()) # should be 44

new2[0].keys()
soc[0].keys()

# check if worked, random:

for i in range(0,3):
    print new2[i]['members_no']
    print new2[i]['fi_income']
    print new2[i]['fi_pro_income']
    print new2[i]['fi_do']
    print new2[i]['fi_sub_bur']
    print new2[i]['fi_sub_nb']
    print new2[i]['fi_mf']
    print new2[i]['gpro_no']


# save as soc_wel9
import csv
keys = new2[0].keys()
with open('soc_wel9.csv', 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(new2)
