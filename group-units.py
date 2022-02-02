# import the required libraries
import os
import json
import csv
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
csv_save_path = 'H:/WORK/Upwork/Project 7 - Python School Data Analysis/Countries Admin Levels/GADM-Countries/Extracted/'
completeName = os.path.join(csv_save_path, 'admin_level_order_structures.csv')
# we can now create a csv file to save each of our data once we iterate through it
with open(completeName,'w',newline='') as csvfile:
    # field names that will be the title of our columns
    fieldnames = ['Country Name', 'Lowest Admin Level', 'AdminLevel0Units', 'AdminLevel0Names', 'AdminLevel1Units', 'AdminLevel1Names', 'AdminLevel2Units', 'AdminLevel2Names', 
                  'AdminLevel3Units', 'AdminLevel3Names', 'AdminLevel4Units', 'AdminLevel4Names', 'AdminLevel5Units', 'AdminLevel5Names'] 
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    # writer.writerows(data)

    for file in os.listdir():
        admin_level1_names, admin_level2_names, admin_level3_names, admin_level4_names,admin_level5_names = '', '', '', '', ''
        # create a sub-folder for geojson files
        sub_path = os.path.join(save_path, file)
        sub_path = sub_path + '/'
        for items in os.listdir(sub_path):
            subb_path, sub_dirs, sub_files = next(os.walk(sub_path))
            admin_level1_units = ''
            admin_level2_units = ''
            admin_level3_units = ''
            admin_level4_units = ''
            admin_level5_units = ''
            
            # when the number of files present in the file path is 3
            if len(sub_files) == 3:
                province_sub_1 = sub_files[1]
                district_sub_2 = sub_files[2]
                province_path = os.path.join(sub_path, province_sub_1)
                path_to_geojson = os.path.join(sub_path, district_sub_2)
                with open(province_path) as f:
                    data = json.load(f)
                type_adm_1_list = []
                for m in data['features']:
                    type_adm_1 = m['properties']['ENGTYPE_1']
                    if type_adm_1 not in type_adm_1_list:
                        type_adm_1_list.append(type_adm_1)
                break
            
            # when the number of files present in the file path is 4
            elif len(sub_files) == 4:
                province_sub_1 = sub_files[1]
                district_sub_2 = sub_files[2]
                sub_county_3 = sub_files[3]
                province_path = os.path.join(sub_path, province_sub_1)
                district_path = os.path.join(sub_path, district_sub_2)
                path_to_geojson = os.path.join(sub_path, sub_county_3)
                temp_list = [province_path, district_path]
                type_adm_1_list = []
                type_adm_2_list = []
                for i in temp_list:
                    with open(i) as f:
                        data = json.load(f)  
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
                break
                                
            # when the number of files present in the file path is 5
            elif len(sub_files) == 5:
                province_sub_1 = sub_files[1]
                district_sub_2 = sub_files[2]
                sub_county_3 = sub_files[3]
                sub_ward_4 = sub_files[4]
                province_path = os.path.join(sub_path, province_sub_1)
                district_path = os.path.join(sub_path, district_sub_2)
                sub_county_path = os.path.join(sub_path,sub_county_3)
                path_to_geojson = os.path.join(sub_path, sub_ward_4)
                temp_list = [province_path, district_path, sub_county_path]
                type_adm_1_list = []
                type_adm_2_list = []
                type_adm_3_list = []
                for i in temp_list:
                    with open(i) as f:
                        data = json.load(f)
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
                break
                    
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
                path_to_geojson = os.path.join(sub_path, location_sub_5)
                temp_list = [province_path, district_path, sub_county_path, location_sub_path]
                type_adm_1_list = []
                type_adm_2_list = []
                type_adm_3_list = []
                type_adm_4_list = []
                for i in temp_list:
                    with open(i) as f:
                        data = json.load(f)
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
                break
            
            elif len(sub_files) == 2:
                province_sub_1 = sub_files[1]
                path_to_geojson = os.path.join(sub_path, province_sub_1)
                break
            
            else:
                path_to_geojson = os.path.join(sub_path, items)
                break
            
            # we can use here to parse previous files to get type of admin level
            
        path, dirs, files = next(os.walk(sub_path))
        file_count = len(files)
        # this is where the reading happens:
        # load the json file
        with open(path_to_geojson) as f:
            data = json.load(f)
            
        n = ''
        # global information
        if len(sub_files) == 3 or len(sub_files) == 4 or len(sub_files) == 5 or len(sub_files) == 6:
            # admin level 1
            new_names_adm1 = ''
            if len(type_adm_1_list) > 5: 
                for i in type_adm_1_list:
                    if i == 'District' or i =='County' or i == 'Metropolitan Borough' or i == 'District Council' or i == 'Borough' or i == 'Shire' or i == 'Municipality' or i == 'Region' or i == 'Territory' or i == 'Districts|Municipals' or i == 'Sector' or i == 'Subregion':
                        if not new_names_adm1:
                            new_names_adm1 = i
                        else:
                            new_names_adm1 = new_names_adm1 + '/' + i
            elif type(type_adm_1_list) == list and len(type_adm_1_list) <= 5:
                if len(type_adm_1_list) == 1:
                    new_names_adm1 = type_adm_1_list[0]
                else:
                    for i in type_adm_1_list:
                        if not new_names_adm1:
                            new_names_adm1 = i
                        else:
                            new_names_adm1 = new_names_adm1 + '/' + i
        if len(sub_files) == 4 or len(sub_files) == 5 or len(sub_files) == 6:
        # admin level 2
            new_names_adm2 = ''
            if len(type_adm_2_list) > 5: 
                for i in type_adm_2_list:
                    if i == 'District' or i =='County' or i == 'Metropolitan Borough' or i == 'District Council' or i == 'Borough' or i == 'Shire' or i == 'Municipality' or i == 'Region' or i == 'Territory' or i == 'Districts|Municipals' or i == 'Sector' or i == 'Subregion':
                        if not new_names_adm2:
                            new_names_adm2 = i
                        else:
                            new_names_adm2 = new_names_adm2 + '/' + i
            elif type(type_adm_2_list) == list and len(type_adm_2_list) <= 5:
                if len(type_adm_2_list) == 1:
                    new_names_adm2 = type_adm_2_list[0]
                else:
                    for i in type_adm_2_list:
                        if not new_names_adm2:
                            new_names_adm2 = i
                        else:
                            new_names_adm2 = new_names_adm2 + '/' + i
        if len(sub_files) == 5 or len(sub_files) == 6:                
            # admin level 3
            new_names_adm3 = ''
            if len(type_adm_3_list) > 5: 
                for i in type_adm_3_list:
                    if i == 'Municipality' or i =='Region' or i == 'Unitary' or i == 'Unitary district' or i == 'Metropolitan Borough' or i == 'Unitary District' or i == 'Sub County' or i =='Commune' or i == 'Division' or i == 'Municipality (urban)' or i == 'Municipality (rural)' or i == 'City County' or i == 'Administrative District' or i == 'Town' or i == 'Village' or i == 'Census Division' or i == 'District Municipality':
                        if not new_names_adm3:
                            new_names_adm3 = i
                        else:
                            new_names_adm3 = new_names_adm3 + '/' + i
            elif type(type_adm_3_list) == list and len(type_adm_3_list) <= 5:
                if len(type_adm_3_list) == 1:
                    new_names_adm3 = type_adm_3_list[0]
                else:
                    for i in type_adm_3_list:
                        if not new_names_adm3:
                            new_names_adm3 = i
                        else:
                            new_names_adm3 = new_names_adm3 + '/' + i
        
        if len(sub_files) == 6: 
            # admin level 4
            new_names_adm4 = ''
            if len(type_adm_4_list) > 5: 
                for i in type_adm_4_list:
                    if i == 'Commune' or i =='Municipality' or i == 'Town' or i == 'Sovereign territories' or i == 'Sovereign territory':
                        if not new_names_adm4:
                            new_names_adm4 = i
                        else:
                            new_names_adm4 = new_names_adm4 + '/' + i
            elif type(type_adm_4_list) == list and len(type_adm_4_list) <= 5:
                if len(type_adm_4_list) == 1:
                    new_names_adm4 = type_adm_4_list[0]
                else:
                    for i in type_adm_4_list:
                        if not new_names_adm4:
                            new_names_adm4 = i
                        else:
                            new_names_adm4 = new_names_adm4 + '/' + i
        
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
            country_name = file
            lowest_admin_level = file_count - 1
            admin_level0_unit = 1
                    
        elif file_count == 2:
            print(file, '2 files were found')
            admin_level_type = []
            for item in data['features']:
                if n:
                    b = item['properties']['NAME_1']
                    # c = item['properties']['NAME_2']
                    # d = item['properties']['NAME_3']
                    country_group[n][b].append({'Adm_1': b})
                    #country_group[n][b].append({'Adm_2':c,'Adm_3':d})
                    type_admin_level = item['properties']['ENGTYPE_1']
                    if type_admin_level not in admin_level_type:
                        admin_level_type.append(type_admin_level)
                else:
                    n = item['properties']['NAME_0']
                    country_group[n] = defaultdict(list)
                    b = item['properties']['NAME_1']
                    # c = item['properties']['NAME_2']
                    # d = item['properties']['NAME_3']
                    country_group[n][b].append({'Adm_1': b})
                    #country_group[n][b].append({'Adm_2':c,'Adm_3':d})
                    type_admin_level = item['properties']['ENGTYPE_1']
                    if type_admin_level not in admin_level_type:
                        admin_level_type.append(type_admin_level)
            
            new_names = ''
            if len(admin_level_type) > 5: 
                for i in admin_level_type:
                    if i == 'Kingdom' or i =='Province' or i == 'Principality' or i == 'State' or i == 'Territory':
                        if not new_names:
                            new_names = i
                        else:
                            new_names = new_names + '/' + i
            elif type(admin_level_type) == list and len(admin_level_type) <= 5:
                if len(admin_level_type) == 1:
                    new_names = admin_level_type[0]
                else:
                    for i in admin_level_type:
                        if not new_names:
                            new_names = i
                        else:
                            new_names = new_names + '/' + i
            
            country_name = file
            lowest_admin_level = file_count - 1
            admin_level0_unit = 1
            admin_level1_units = len(country_group[n].keys())
            admin_level1_names = new_names
             
        elif file_count == 3:
            print(file, '3 files were found')
            admin_level_type = []
            for item in data['features']:
                if n:
                    b = item['properties']['NAME_1']
                    c = item['properties']['NAME_2']
                    #d = item['properties']['NAME_3']
                    #country_group[n][b].append(c)
                    country_group[n][b].append({'Adm_2':c})
                    type_admin_level = item['properties']['ENGTYPE_2']
                    if type_admin_level not in admin_level_type:
                        admin_level_type.append(type_admin_level)
                else:
                    n = item['properties']['NAME_0']
                    country_group[n] = defaultdict(list)
                    b = item['properties']['NAME_1']
                    c = item['properties']['NAME_2']
                    #d = item['properties']['NAME_3']
                    #country_group[n][b].append(c)
                    country_group[n][b].append({'Adm_2':c})
                    type_admin_level = item['properties']['ENGTYPE_2']
                    if type_admin_level not in admin_level_type:
                        admin_level_type.append(type_admin_level)
            z_adm = country_group[file].keys()
            adm_2_list = []
            z = 0
            for i in z_adm:
                for p in country_group[file][i]:
                    if p['Adm_2'] not in adm_2_list:
                        adm_2_list.append(p['Adm_2'])
                        z += 1
            
            new_names = ''
            if len(admin_level_type) > 5: 
                for i in admin_level_type:
                    if i == 'District' or i =='County' or i == 'Metropolitan Borough' or i == 'District Council' or i == 'Borough' or i == 'Shire' or i == 'Municipality' or i == 'Region' or i == 'Territory' or i == 'Districts|Municipals' or i == 'Sector' or i == 'Subregion':
                        if not new_names:
                            new_names = i
                        else:
                            new_names = new_names + '/' + i
            elif type(admin_level_type) == list and len(admin_level_type) <= 5:
                if len(admin_level_type) == 1:
                    new_names = admin_level_type[0]
                else:
                    for i in admin_level_type:
                        if not new_names:
                            new_names = i
                        else:
                            new_names = new_names + '/' + i
            
            country_name = file
            lowest_admin_level = file_count - 1
            admin_level0_unit = 1
            admin_level1_units = len(country_group[n].keys())
            admin_level1_names = new_names_adm1
            admin_level2_units = len(adm_2_list)
            admin_level2_names = new_names
                    
        elif file_count == 4:
            print(file, '4 files were found')
            admin_level_type = []
            for item in data['features']:
                if n:
                    b = item['properties']['NAME_1']
                    c = item['properties']['NAME_2']
                    d = item['properties']['NAME_3']
                    type_admin_level = item['properties']['ENGTYPE_3']
                    if type_admin_level not in admin_level_type:
                        admin_level_type.append(type_admin_level)
                    country_group[n][b].append({'Adm_2':c,'Adm_3':d})
                else:
                    n = item['properties']['NAME_0']
                    country_group[n] = defaultdict(list)
                    b = item['properties']['NAME_1']
                    c = item['properties']['NAME_2']
                    d = item['properties']['NAME_3']
                    type_admin_level = item['properties']['ENGTYPE_3']
                    if type_admin_level not in admin_level_type:
                        admin_level_type.append(type_admin_level)
                    #country_group[n][b].append(c)
                    country_group[n][b].append({'Adm_2':c,'Adm_3':d})
                    
            z_adm = country_group[file].keys()
            adm_2_list = []
            adm_3_list = []
            z = 0
            for i in z_adm:
                for p in country_group[file][i]:
                    if p['Adm_2'] not in adm_2_list:
                        adm_2_list.append(p['Adm_2'])
                        z += 1
                    if p['Adm_3'] not in adm_3_list:
                        adm_3_list.append(p['Adm_3'])
                        z += 1
            
            new_names = ''
            if len(admin_level_type) > 5: 
                for i in admin_level_type:
                    if i == 'Municipality' or i =='Region' or i == 'Unitary' or i == 'Unitary district' or i == 'Metropolitan Borough' or i == 'Unitary District' or i == 'Sub County' or i =='Commune' or i == 'Division' or i == 'Municipality (urban)' or i == 'Municipality (rural)' or i == 'City County' or i == 'Administrative District' or i == 'Town' or i == 'Village' or i == 'Census Division' or i == 'District Municipality':
                        if not new_names:
                            new_names = i
                        else:
                            new_names = new_names + '/' + i
            elif type(admin_level_type) == list and len(admin_level_type) <= 5:
                if len(admin_level_type) == 1:
                    new_names = admin_level_type[0]
                else:
                    for i in admin_level_type:
                        if not new_names:
                            new_names = i
                        else:
                            new_names = new_names + '/' + i
            
            country_name = file
            lowest_admin_level = file_count - 1
            admin_level0_unit = 1
            admin_level1_units = len(country_group[n].keys())
            admin_level1_names = new_names_adm1
            admin_level2_units = len(adm_2_list)
            admin_level2_names = new_names_adm2
            admin_level3_units = len(adm_3_list)
            admin_level3_names = new_names
            
        elif file_count == 5:
            print(file, '5 files were found')
            admin_level_type = []
            for item in data['features']:
                if n:
                    b = item['properties']['NAME_1']
                    c = item['properties']['NAME_2']
                    d = item['properties']['NAME_3']
                    e = item['properties']['NAME_4']
                    #country_group[n][b].append(c)
                    country_group[n][b].append({'Adm_2':c,'Adm_3':d, 'Adm_4':e})
                    type_admin_level = item['properties']['ENGTYPE_4']
                    if type_admin_level not in admin_level_type:
                        admin_level_type.append(type_admin_level)
                else:
                    n = item['properties']['NAME_0']
                    country_group[n] = defaultdict(list)
                    b = item['properties']['NAME_1']
                    c = item['properties']['NAME_2']
                    d = item['properties']['NAME_3']
                    e = item['properties']['NAME_4']
                    #country_group[n][b].append(c)
                    country_group[n][b].append({'Adm_2':c,'Adm_3':d, 'Adm_4':e})
                    type_admin_level = item['properties']['ENGTYPE_4']
                    if type_admin_level not in admin_level_type:
                        admin_level_type.append(type_admin_level)
            y_adm = country_group[file].keys()
            adm_2_list = []
            adm_3_list = []
            adm_4_list = []
            z = 0
            for i in y_adm:
                for p in country_group[file][i]:
                    if p['Adm_2'] not in adm_2_list:
                        adm_2_list.append(p['Adm_2'])
                        z += 1
                    if p['Adm_3'] not in adm_3_list:
                        adm_3_list.append(p['Adm_3'])
                        z += 1
                    if p['Adm_4'] not in adm_4_list:
                        adm_4_list.append(p['Adm_4'])
                        z += 1
            
            new_names = ''
            if len(admin_level_type) > 5: 
                for i in admin_level_type:
                    if i == 'Commune' or i =='Municipality' or i == 'Town' or i == 'Sovereign territories' or i == 'Sovereign territory':
                        if not new_names:
                            new_names = i
                        else:
                            new_names = new_names + '/' + i
            elif type(admin_level_type) == list and len(admin_level_type) <= 5:
                if len(admin_level_type) == 1:
                    new_names = admin_level_type[0]
                else:
                    for i in admin_level_type:
                        if not new_names:
                            new_names = i
                        else:
                            new_names = new_names + '/' + i
            
            country_name = file
            lowest_admin_level = file_count - 1
            admin_level0_unit = 1
            admin_level1_units = len(country_group[n].keys())
            admin_level1_names = new_names_adm1
            admin_level2_units = len(adm_2_list)
            admin_level2_names = new_names_adm2
            admin_level3_units = len(adm_3_list)
            admin_level3_names = new_names_adm3
            admin_level4_units = len(adm_4_list)
            admin_level4_names = new_names
            
        elif file_count == 6:
            print(file, '6 files were found')
            admin_level_type = []
            for item in data['features']:
                if n:
                    b = item['properties']['NAME_1']
                    c = item['properties']['NAME_2']
                    d = item['properties']['NAME_3']
                    e = item['properties']['NAME_4']
                    f = item['properties']['NAME_5']
                    #country_group[n][b].append(c)
                    country_group[n][b].append({'Adm_2':c,'Adm_3':d, 'Adm_4':e, 'Adm_5':f})
                    type_admin_level = item['properties']['ENGTYPE_5']
                    if type_admin_level not in admin_level_type:
                        admin_level_type.append(type_admin_level)
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
                    type_admin_level = item['properties']['ENGTYPE_5']
                    if type_admin_level not in admin_level_type:
                        admin_level_type.append(type_admin_level)
            x_adm = country_group[file].keys()
            adm_2_list = []
            adm_3_list = []
            adm_4_list = []
            adm_5_list = []
            z = 0
            for i in x_adm:
                for p in country_group[file][i]:
                    if p['Adm_2'] not in adm_2_list:
                        adm_2_list.append(p['Adm_2'])
                        z += 1
                    if p['Adm_3'] not in adm_3_list:
                        adm_3_list.append(p['Adm_3'])
                        z += 1
                    if p['Adm_4'] not in adm_4_list:
                        adm_4_list.append(p['Adm_4'])
                        z += 1
                    if p['Adm_5'] not in adm_5_list:
                        adm_5_list.append(p['Adm_5'])
                        z += 1
            
            new_names = ''
            if len(admin_level_type) > 5: 
                for i in admin_level_type:
                    if i == 'Commune' or i =='Waterbody':
                        if not new_names:
                            new_names = i
                        else:
                            new_names = new_names + '/' + i
            elif type(admin_level_type) == list and len(admin_level_type) <= 5:
                if len(admin_level_type) == 1:
                    new_names = admin_level_type[0]
                else:
                    for i in admin_level_type:
                        if not new_names:
                            new_names = i
                        else:
                            new_names = new_names + '/' + i
            
            country_name = file
            lowest_admin_level = file_count - 1
            admin_level0_unit = 1
            admin_level1_units = len(country_group[n].keys())
            admin_level1_names = new_names_adm1
            admin_level2_units = len(adm_2_list)
            admin_level2_names = new_names_adm2
            admin_level3_units = len(adm_3_list)
            admin_level3_names = new_names_adm3
            admin_level4_units = len(adm_4_list)
            admin_level4_names = new_names_adm4
            admin_level5_units = len(adm_5_list)
            admin_level5_names = new_names
            
        print('\n')
        print(file)
        print(admin_level1_names)
        print(admin_level2_names)
        print(admin_level3_names)
        print(admin_level4_names)
        print(admin_level5_names)
        
        
        # saving the data we obtaned as a dictionary. Keys must be similar to fieldnames
        data = [{'Country Name': country_name, 'Lowest Admin Level': lowest_admin_level, 'AdminLevel0Units': admin_level0_unit, 'AdminLevel0Names': country_name, 
                  'AdminLevel1Units': admin_level1_units, 'AdminLevel1Names': admin_level1_names, 'AdminLevel2Units': admin_level2_units, 'AdminLevel2Names': admin_level2_names, 
                  'AdminLevel3Units': admin_level3_units, 'AdminLevel3Names': admin_level3_names, 'AdminLevel4Units': admin_level4_units, 'AdminLevel4Names': admin_level4_names, 
                  'AdminLevel5Units': admin_level5_units, 'AdminLevel5Names': admin_level5_names}]
        writer.writerows(data) # this will write the rows to the file csv created above
