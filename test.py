import json
import datetime

test={'salutations': ['hello', 'hi'], 'names': ['world', 'john']}
#test={}
str_dict='|'.join([f"{key}:{(',').join(value)}" for key, value in test.items()])
print(str_dict)
result = {}
if str_dict.strip() != '':
    for report_type_lists in str_dict.split('|'):
        if report_type_lists.strip() != '':
            report_type = report_type_lists.split(':')
            result[report_type[0]] = [x for x in report_type[1].split(',')]
        
print(result)

p1='test'
p2=datetime.date.today()
subidx_reports='"report_name": "{0}","date": "{1}"'
subidx_reports = "{" + subidx_reports.format(p1, p2) + "}"
# subidx_reports = subidx_reports.format(p1, p2)
print(subidx_reports)
ret_val = json.loads(subidx_reports)
print(str(ret_val))