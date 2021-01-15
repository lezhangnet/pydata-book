# dealing with the bitly JSON data with pandas

import json
path = 'usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)] # list comprehension
print("records count: " + str(len(records))) # 3560
# above is the same as vanilla.py

from pandas import DataFrame, Series
import pandas as pd

frame = DataFrame(records)
print(frame)
#                                                       a   c   nk  ...                        ll _heartbeat_   kw
# 0     Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKi...  US  1.0  ...   [42.576698, -70.954903]         NaN  NaN
# 1                                GoogleMaps/RochesterNY  US  0.0  ...  [40.218102, -111.613297]         NaN  NaN
# 2     Mozilla/4.0 (compatible; MSIE 8.0; Windows NT ...  US  1.0  ...     [38.9007, -77.043098]         NaN  NaN
# 3     Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8)...  BR  0.0  ...  [-23.549999, -46.616699]         NaN  NaN
# 4     Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKi...  US  0.0  ...   [42.286499, -71.714699]         NaN  NaN
# ...                                                 ...  ..  ...  ...                       ...         ...  ...
# 3555  Mozilla/4.0 (compatible; MSIE 9.0; Windows NT ...  US  1.0  ...         [40.9445, -74.07]         NaN  NaN
# 3556  Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1...  US  0.0  ...     [35.4715, -97.518997]         NaN  NaN
# 3557                             GoogleMaps/RochesterNY  US  0.0  ...  [40.218102, -111.613297]         NaN  NaN
# 3558                                     GoogleProducer  US  0.0  ...  [37.419201, -122.057404]         NaN  NaN
# 3559  Mozilla/4.0 (compatible; MSIE 8.0; Windows NT ...  US  0.0  ...   [38.935799, -77.162102]         NaN  NaN
# [3560 rows x 18 columns]

print(frame['tz'][:10])
# 0     America/New_York
# 1       America/Denver
# 2     America/New_York
# 3    America/Sao_Paulo
# 4     America/New_York
# 5     America/New_York
# 6        Europe/Warsaw
# 7
# 8
# 9
# Name: tz, dtype: object

