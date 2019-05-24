from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

dates = ['2016010106','2016010107','2016010108','2016010109','2016010110','2016010111','2016010112','2016010113',
         '2016010114','2016010115','2016010116','2016010117','2016010118']
#把string格式的日期转换成datetime格式
xs = [datetime.strptime(d, '%Y%m%d%H') for d in dates]
ys = ['36','29','26','22','29','38','48','55','56','60','55','48','51']

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
#指定X轴的以日期格式（带小时）显示
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S.%f'))
#X轴的间隔为小时


ax.xaxis.set_major_locator(mdates.HourLocator())
plt.plot(xs, ys)
plt.gcf().autofmt_xdate()
plt.show()
