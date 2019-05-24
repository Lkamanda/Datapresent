# import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# def draw_picture(date_x1, date_y1):
date_x1 = ['201601010601','201601010702','201601010803','201601010904','201601011005','201601011106', '201601011207','201601011308',
         '201601011409','201601011510','201601011611','201601011712','201601011813', '201601011914']
print("总共有%s条数据" % len(date_x1))
#把string格式的日期转换成datetime格式

xs = [datetime.strptime(d, '%Y%m%d%H%M') for d in date_x1]
ys = [i for i in range(1,15)]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
#指定X轴的以日期格式（带小时）显示
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y%m%d%H%M'))
#X轴的间隔为小时
# ax.xaxis.set_major_locator(mdates.SecondLocator)
ax.xaxis.set_major_locator(mdates.HourLocator())
plt.plot(xs, ys)
plt.gcf().autofmt_xdate()
font1 = FontProperties(fname=r"c:\windows\fonts\simsun.ttc",size=20)
plt.title(u"标题",fontproperties=font1)
plt.xlabel(u"x轴",fontproperties=font1)
plt.ylabel(u"Y轴",fontproperties=font1)
plt.show()


