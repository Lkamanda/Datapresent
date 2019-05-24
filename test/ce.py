# import matplotlib.pyplot as plt
# x = [0,5,9,10,15]
# y = [0,1,2,3,4]
# plt.plot(x,y)
# plt.grid(True)
# plt.xticks(range(min(x),max(x)+1,3))
# plt.show()

# from pyecharts import Bar
# bar = Bar("数据分析")
#
# labels = data.columns.tolist()
# for la in labels:
#     # print("标签：",la,"时间：", hebing4[[la]].index,"数据：", hebing4[[la]].values)
#     bar.add(la, data[la].index, data[la].values, is_stack=True, mark_point=["max", "min"],
#     is_datazoom_show=True, # 默认为 X 轴，横向
#     datazoom_type="slider",
#     datazoom_range=[10, 25],
#     # 新增额外的 dataZoom 控制条，纵向
#     is_datazoom_extra_show=True,
#     datazoom_extra_type="slider",
#     datazoom_extra_range=[10, 25],
#     is_toolbox_show=False,)
# bar.render(r"/home/result/packetlen_avg.html")

#
# DateFormatter ('%H:%M:%S.%f')
# import matplotlib.pyplot as plt
# import matplotlib.dates as mdate
# import pandas as pd
# ##绘图代码省略，坐标轴设置如下
# ax = plt.gca()  # 表明设置图片的各个轴，plt.gcf()表示图片本身
# ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d'))  # 横坐标标签显示的日期格式
# plt.xticks(pd.date_range('2018-9-1', '2018-11-30', freq='10d'))  # 横坐标日期范围及间隔
# plt.yticks(range(20, 110, 10))  # 设置纵坐标，使用range()函数设置起始、结束范围及间隔步长


