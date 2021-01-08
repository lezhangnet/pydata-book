# dealing with the bitly JSON data with vanilla python

import json
path = 'usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)] # list comprehension
print("records count: " + str(len(records))) # 3560
print(records[0]) # each record is a dictionary
# {'a': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.78 Safari/535.11', 'c': 'US', 'nk': 1, 'tz': 'America/New_York', 'gr': 'MA', 'g': 'A6qOVH', 'h': 'wfLQtf', 'l': 'orofrog', 'al': 'en-US,en;q=0.8', 'hh': '1.usa.gov', 'r': 'http://www.facebook.com/l/7AQEFzjSi/1.usa.gov/wfLQtf', 'u': 'http://www.ncbi.nlm.nih.gov/pubmed/22415991', 't': 1331923247, 'hc': 1331822918, 'cy': 'Danvers', 'll': [42.576698, -70.954903]}
print(records[0]['tz']) # time zone

time_zones = [rec['tz'] for rec in records if 'tz' in rec]
print("time zones count: " + str(len(time_zones))) # 3440
print(time_zones[:10]) # first 10
# ['America/New_York', 'America/Denver', 'America/New_York', 'America/Sao_Paulo', 'America/New_York', 'America/New_York', 'Europe/Warsaw', '', '', '']

def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts

tz_counts = get_counts(time_zones) # this needs to be below the method definition
print("time zones count dict: " + str(tz_counts))
# {'America/New_York': 1251, 'America/Denver': 191, ...}

from collections import defaultdict
def get_counts2(sequence):
    counts = defaultdict(int) # values will initialize to 0
    for x in sequence:
        counts[x] += 1
    return counts

tz_counts2 = get_counts2(time_zones) # this needs to be below the method definition
print("time zones count dict 2: " + str(tz_counts2))
# defaultdict(<class 'int'>, {'America/New_York': 1251, 'America/Denver': 191, ...})

def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort() # sort by 1st element?
    return value_key_pairs[-n:]

print("top time zones: " + str(top_counts(tz_counts)))
# [(33, 'America/Sao_Paulo'), (35, 'Europe/Madrid'), (36, 'Pacific/Honolulu'), (37, 'Asia/Tokyo'), (74, 'Europe/London'), (191, 'America/Denver'), (382, 'America/Los_Angeles'), (400, 'America/Chicago'), (521, ''), (1251, 'America/New_York')]

from collections import Counter
counts = Counter(time_zones)
print("counts.most_common(): " + str(counts.most_common(10)))
# [('America/New_York', 1251), ('', 521), ('America/Chicago', 400), ('America/Los_Angeles', 382), ('America/Denver', 191), ('Europe/London', 74), ('Asia/Tokyo', 37), ('Pacific/Honolulu', 36), ('Europe/Madrid', 35), ('America/Sao_Paulo', 33)]
