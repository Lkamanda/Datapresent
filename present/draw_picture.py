# import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


def draw_picture(date_x1, date_y1, date_y2, title):
    """
    :param date_x1: 当前时间 list  x 轴
    :param date_y1: 使用时间 list  y 轴         ms 毫秒
    :param date_y2: 处理文件大小 list  y 轴
    :param title: 本张图片的名字
    """
    print(date_x1)
    print(date_y1)
    print(date_y2)
    print("总共有%s条数据" % len(date_x1))
    # 把string格式的日期转换成datetime格式

    xs = [datetime.strptime(d, '%Y%m%d%H%M%S%f') for d in date_x1]
    # ys = [i for i in range(1,15)]

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    # 指定X轴的以日期格式（带小时）显示
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y%m%d%H%M%S%f'))
    # X轴的间隔为小时
    # ax.xaxis.set_major_locator(mdates.SecondLocator)
    ax.xaxis.set_major_locator(mdates.HourLocator())

    plt.plot(xs, date_y1, label="消耗时间", color="#F08080")
    plt.plot(xs, date_y2, label="处理文件大小", linestyle="--")
    # plt.legend(handles=[ln2, ln1], labels=['Android基础', 'Java基础'],
    #            loc='lower right')
    # 设置旋转日期
    plt.gcf().autofmt_xdate()

    # 设置标题和x轴y轴大小
    font1 = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=20)
    plt.title(u"%s" % title, fontproperties=font1)
    plt.xlabel(u"Local time", fontproperties=font1)
    plt.ylabel(u"消耗时间/处理文件的大小", fontproperties=font1)

    # 绘制网格
    plt.grid(alpha=0.4, linestyle=':')

    # 添加图例，prop指定图例的字体, loc参数可以查看源码
    plt.legend(prop=font1, loc="upper right")

    plt.show()


# if __name__ == '__main__':
#     # date_x1 = ['2016 01 01 06 01', '201601010702', '201601010803', '201601010904', '201601011005', '201601011106',
#     #            '201601011207', '201601011308',
#     #            '201601011409', '201601011510', '201601011611', '201601011712', '201601011813', '201601011914']
#     # date_x1 = ["20190522104245462000","20190522104245462000","20190522104245462000"]
#     # date_x1 = ["20190522109245462000","20190522104245462000","20190522108245462000"]
#     date_x1 = ['2019052224245462000', '20190522094245462000', '20190522204245462000']
#     y1 = ['399', '599', '999']
#     y2 = ['10311', '10312', '10318']
#     # y1 = [i for i in range(1,4)]
#     # y2 = [i for i in range(1,4)]
#     title = "stallite tag"
#     draw_picture(date_x1=date_x1, date_y1=y1, date_y2=y2, title=title)
#     # "20190522104245462000"
