# import the required libraries
import os
import json
from collections import defaultdict

# parsing through the root folder
#path to the directory that has our zipped files
path = 'H:/WORK/Upwork/Project 7 - Python School Data Analysis/Countries Admin Levels/GADM-Countries/Extracted/Admin Data GeoJSON/'

# Change directory
os.chdir(path)
z = 1
# Iterating through all the files in our folder
# create the major folder here
save_path = 'H:/WORK/Upwork/Project 7 - Python School Data Analysis/Countries Admin Levels/GADM-Countries/Extracted/Admin Data GeoJSON/'
country_group = {}
for file in os.listdir():
    # create a sub-folder for geojson files
    sub_path = os.path.join(save_path, file)
    sub_path = sub_path + '/'
    for items in os.listdir(sub_path):
        path_to_geojson = os.path.join(sub_path, items)
    path, dirs, files = next(os.walk(sub_path))
    file_count = len(files)
    # this is where the reading happens:
    # load the json file
    with open(path_to_geojson) as f:
        data = json.load(f)
        
    n = ''
    
    
    # filter
    if file_count == 1:
        print(file, '1 file was found')
        for item in data['features']:
            if n:
                continue
                # b = item['properties']['NAME_1']
                # c = item['properties']['NAME_2']
                # d = item['properties']['NAME_3']
                # country_group[n][b].append(c)
                # country_group[n][b].append({'Adm_2':c,'Adm_3':d})
            else:
                n = item['properties']['NAME_0']
                country_group[n] = defaultdict(list)
                # b = item['properties']['NAME_1']
                # c = item['properties']['NAME_2']
                # d = item['properties']['NAME_3']
                country_group[n]['Adm_0'].append(n)
                # country_group[n][b].append({'Adm_2':c,'Adm_3':d})
                
    elif file_count == 2:
        print(file, '2 files were found')
        for item in data['features']:
            if n:
                b = item['properties']['NAME_1']
                # c = item['properties']['NAME_2']
                # d = item['properties']['NAME_3']
                country_group[n][b].append({'Adm_1': b})
                #country_group[n][b].append({'Adm_2':c,'Adm_3':d})
            else:
                n = item['properties']['NAME_0']
                country_group[n] = defaultdict(list)
                b = item['properties']['NAME_1']
                # c = item['properties']['NAME_2']
                # d = item['properties']['NAME_3']
                country_group[n][b].append({'Adm_1': b})
                #country_group[n][b].append({'Adm_2':c,'Adm_3':d})
    
    elif file_count == 3:
        print(file, '3 files were found')
        for item in data['features']:
            if n:
                b = item['properties']['NAME_1']
                c = item['properties']['NAME_2']
                #d = item['properties']['NAME_3']
                #country_group[n][b].append(c)
                country_group[n][b].append({'Adm_2':c})
            else:
                n = item['properties']['NAME_0']
                country_group[n] = defaultdict(list)
                b = item['properties']['NAME_1']
                c = item['properties']['NAME_2']
                #d = item['properties']['NAME_3']
                #country_group[n][b].append(c)
                country_group[n][b].append({'Adm_2':c})
                
    elif file_count == 4:
        print(file, '4 files were found')
        for item in data['features']:
            if n:
                b = item['properties']['NAME_1']
                c = item['properties']['NAME_2']
                d = item['properties']['NAME_3']
                #country_group[n][b].append(c)
                country_group[n][b].append({'Adm_2':c,'Adm_3':d})
            else:
                n = item['properties']['NAME_0']
                country_group[n] = defaultdict(list)
                b = item['properties']['NAME_1']
                c = item['properties']['NAME_2']
                d = item['properties']['NAME_3']
                #country_group[n][b].append(c)
                country_group[n][b].append({'Adm_2':c,'Adm_3':d})
                
    elif file_count == 5:
        print(file, '5 files were found')
        for item in data['features']:
            if n:
                b = item['properties']['NAME_1']
                c = item['properties']['NAME_2']
                d = item['properties']['NAME_3']
                e = item['properties']['NAME_4']
                #country_group[n][b].append(c)
                country_group[n][b].append({'Adm_2':c,'Adm_3':d, 'Adm_4':e})
            else:
                n = item['properties']['NAME_0']
                country_group[n] = defaultdict(list)
                b = item['properties']['NAME_1']
                c = item['properties']['NAME_2']
                d = item['properties']['NAME_3']
                e = item['properties']['NAME_4']
                #country_group[n][b].append(c)
                country_group[n][b].append({'Adm_2':c,'Adm_3':d, 'Adm_4':e})
                
    elif file_count == 6:
        print(file, '6 files were found')
        for item in data['features']:
            if n:
                b = item['properties']['NAME_1']
                c = item['properties']['NAME_2']
                d = item['properties']['NAME_3']
                e = item['properties']['NAME_4']
                f = item['properties']['NAME_5']
                #country_group[n][b].append(c)
                country_group[n][b].append({'Adm_2':c,'Adm_3':d, 'Adm_4':e, 'Adm_5':f})
            else:
                n = item['properties']['NAME_0']
                country_group[n] = defaultdict(list)
                b = item['properties']['NAME_1']
                c = item['properties']['NAME_2']
                d = item['properties']['NAME_3']
                e = item['properties']['NAME_4']
                f = item['properties']['NAME_5']
                #country_group[n][b].append(c)
                country_group[n][b].append({'Adm_2':c,'Adm_3':d, 'Adm_4':e, 'Adm_5':f})


# Reference Code
# n = ''
# country_group = {}
# for item in data['features']:
#     if n:
#         b = item['properties']['NAME_1']
#         c = item['properties']['NAME_2']
#         d = item['properties']['NAME_3']
#         country_group[n][b].append({'Adm_2':c,'Adm_3':d})
#         #country_group[n]['Adm_3'].append(d)
#     else:
#         n = item['properties']['NAME_0']
#         country_group[n] = defaultdict(list)
#         b = item['properties']['NAME_1']
#         c = item['properties']['NAME_2']
#         d = item['properties']['NAME_3']
#         #country_group[n][b].append(c)
#         country_group[n][b].append({'Adm_2':c,'Adm_3':d})
#         #country_group[n]['Adm_3'].append(d)