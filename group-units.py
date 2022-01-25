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
        subb_path, sub_dirs, sub_files = next(os.walk(sub_path))
        
        # when the number of files present in the file path is 3
        if len(sub_files) == 3:
            province_sub_1 = sub_files[1]
            district_sub_2 = sub_files[2]
            province_path = os.path.join(sub_path, province_sub_1)
            with open(province_path) as f:
                data = json.load(f)
            type_adm_1_list = []
            for m in data['features']:
                type_adm_1 = m['properties']['ENGTYPE_1']
                if type_adm_1 not in type_adm_1_list:
                    type_adm_1_list.append(type_adm_1)
        
        # when the number of files present in the file path is 4
        elif len(sub_files) == 4:
            province_sub_1 = sub_files[1]
            district_sub_2 = sub_files[2]
            sub_county_3 = sub_files[3]
            province_path = os.path.join(sub_path, province_sub_1)
            district_path = os.path.join(sub_path, district_sub_2)
            temp_list = [province_path, district_path]
            for i in temp_list:
                with open(i) as f:
                    data = json.load(f)
                type_adm_1_list = []
                type_adm_2_list = []
                if i == province_path:
                    for m in data['features']:
                        type_adm_1 = m['properties']['ENGTYPE_1']
                        if type_adm_1 not in type_adm_1_list:
                            type_adm_1_list.append(type_adm_1)
                elif i == district_path:
                    for m in data['features']:
                        type_adm_2 = m['properties']['ENGTYPE_2']
                        if type_adm_2 not in type_adm_2_list:
                            type_adm_2_list.append(type_adm_2) 
                            
        # when the number of files present in the file path is 5
        elif len(sub_files) == 5:
            province_sub_1 = sub_files[1]
            district_sub_2 = sub_files[2]
            sub_county_3 = sub_files[3]
            sub_ward_4 = sub_files[4]
            province_path = os.path.join(sub_path, province_sub_1)
            district_path = os.path.join(sub_path, district_sub_2)
            sub_county_path = os.path.join(sub_path,sub_county_3)
            temp_list = [province_path, district_path, sub_county_path]
            for i in temp_list:
                with open(i) as f:
                    data = json.load(f)
                type_adm_1_list = []
                type_adm_2_list = []
                type_adm_3_list = []
                if i == province_path:
                    for m in data['features']:
                        type_adm_1 = m['properties']['ENGTYPE_1']
                        if type_adm_1 not in type_adm_1_list:
                            type_adm_1_list.append(type_adm_1)
                elif i == district_path:
                    for m in data['features']:
                        type_adm_2 = m['properties']['ENGTYPE_2']
                        if type_adm_2 not in type_adm_2_list:
                            type_adm_2_list.append(type_adm_2) 
                elif i == sub_county_path:
                    for m in data['features']:
                        type_adm_3 = m['properties']['ENGTYPE_3']
                        if type_adm_3 not in type_adm_3_list:
                            type_adm_3_list.append(type_adm_3) 
                            
        # when the number of files present in the file path is 6
        elif len(sub_files) == 6:
            province_sub_1 = sub_files[1]
            district_sub_2 = sub_files[2]
            sub_county_3 = sub_files[3]
            sub_ward_4 = sub_files[4]
            location_sub_5 = sub_files[5]
            province_path = os.path.join(sub_path, province_sub_1)
            district_path = os.path.join(sub_path, district_sub_2)
            sub_county_path = os.path.join(sub_path,sub_county_3)
            location_sub_path = os.path.join(sub_path, sub_ward_4)
            temp_list = [province_path, district_path, sub_county_path, location_sub_path]
            for i in temp_list:
                with open(i) as f:
                    data = json.load(f)
                type_adm_1_list = []
                type_adm_2_list = []
                type_adm_3_list = []
                type_adm_4_list = []
                if i == province_path:
                    for m in data['features']:
                        type_adm_1 = m['properties']['ENGTYPE_1']
                        if type_adm_1 not in type_adm_1_list:
                            type_adm_1_list.append(type_adm_1)
                elif i == district_path:
                    for m in data['features']:
                        type_adm_2 = m['properties']['ENGTYPE_2']
                        if type_adm_2 not in type_adm_2_list:
                            type_adm_2_list.append(type_adm_2)   
                elif i == sub_county_path:
                    for m in data['features']:
                        type_adm_3 = m['properties']['ENGTYPE_3']
                        if type_adm_3 not in type_adm_3_list:
                            type_adm_3_list.append(type_adm_3) 
                elif i == location_sub_path:
                    for m in data['features']:
                        type_adm_4 = m['properties']['ENGTYPE_4']
                        if type_adm_4 not in type_adm_4_list:
                            type_adm_4_list.append(type_adm_4) 
        path_to_geojson = os.path.join(sub_path, items)
        # we can use here to parse previous files to get type of admin level
        
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
        admin_level1_units = len(country_group[n].keys())
        admin_level1_names = item['properties']['ENGTYPE_1']
        country_name = file
        lowest_admin_level = file_count - 1
        
    
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
        admin_level1_units = len(country_group[n].keys())
        #admin_level1_names = item['properties']['ENGTYPE_1']
        country_name = file
        lowest_admin_level = file_count - 1
        # admin_level2_units 
        admin_level2_names = item['properties']['ENGTYPE_2']
                
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


# adm_2_list = []
# z = 0
# for i in country_group['United Kingdom']['England']:
#     if i['Adm_2'] not in adm_2_list:
#         adm_2_list.append(i['Adm_2'])
#         z += 1

# if len(sub_files) == 4:
#     province_sub_1 = sub_files[1]
#     district_sub_2 = sub_files[2]
#     sub_county_3 = sub_files[3]
#     province_path = os.path.join(sub_path, province_sub_1)
#     district_path = os.path.join(sub_path, district_sub_2)
#     temp_list = [province_path, district_path]
#     for i in temp_list:
#         with open(i) as f:
#             data = json.load(f)
#         type_adm_1_list = []
#         type_adm_2_list = []
#         if i == province_path:
#             for m in data['features']:
#                 type_adm_1 = m['properties']['ENGTYPE_1']
#                 if type_adm_1 not in type_adm_1_list:
#                     type_adm_1_list.append(type_adm_1)
#         elif i == district_path:
#             for m in data['features']:
#                 type_adm_2 = m['properties']['ENGTYPE_2']
#                 if type_adm_2 not in type_adm_2_list:
#                     type_adm_2_list.append(type_adm_2)  