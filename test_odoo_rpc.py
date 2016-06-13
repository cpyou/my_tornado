# -*- coding: utf-8 -*-
import requests
import datetime


post_url = 'http://127.0.0.1:33806/'
data = {
    'total_num': 100,
}
cycle_start_time = datetime.datetime.now()
for i in range(20):
    read_start_time = datetime.datetime.now()
    print '次数:%s, 时间:%s' % (i, read_start_time)
    r = requests.post(post_url, data=data, timeout=15)
    read_end_time = datetime.datetime.now()
    print '次数:%s, 时间:%s' % (i, read_end_time)
    print '读取%s条，总用时：%s，平均用时：%s\n' % (
        data['total_num'], read_end_time - read_start_time, str((read_end_time - read_start_time) / data['total_num']))
cycle_end_time = datetime.datetime.now()
print "完成时间:%s, 用时:%s" % (cycle_end_time, cycle_end_time - cycle_start_time)
