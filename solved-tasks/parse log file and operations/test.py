import re

'''
To match and din url's we will use result = re.match(pattern, string)
'''

#cc_logs
with open('cc_logs') as f:
    cc_log_file = f.readlines()

reg_exp = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
main_url_list = []

#print(cc_log_file)
for line in cc_log_file:
    #print(line)
    main_url_list += reg_exp.findall(line)
    
#print(main_url_list)
print("Total number of url with duplicates:"+str(len(main_url_list)))

unique_list = []

[unique_list.append(raw_url) for raw_url in main_url_list if raw_url not in unique_list]
print("Total number of unique URL's:"+str(len(unique_list)))


index_dict = {}


for unique_url in unique_list:
    index_dict[unique_url] = 0
    for raw_url in main_url_list:
        if unique_url == raw_url:
            index_dict[unique_url] += 1
            

print(index_dict)
