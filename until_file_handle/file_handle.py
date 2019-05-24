import os
import re
import until_file_handle.config

date = until_file_handle.config.MyConfig().get_date()


# "2019 05 22 10 45 06
def read_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        print(lines)


def get_data_path():
    """获取数据存放目录"""
    return os.path.dirname(os.getcwd()) + r'\data'


def file_name():
    """获取文件下所有非目录文件"""
    file_dir = get_data_path()
    for root, dirs, files in os.walk(file_dir):
        # print('root_dir:', root)  # 当前目录路径
        # print('sub_dirs:', dirs)  # 当前路径下所有子目录
        # print('files:', files)  # 当前路径下所有非目录子文件
        return files


def search_date_file():
    """
    根据日期搜索指定目录下所有文件
    :param: data 指定的日期 月份下的所有文件  正则匹配的条件
    :return: 将要执行读取操作的文件列表
    """
    files = file_name()
    new_file = []
    for file in files:
        if re.match('%s.*' % date, file) is not None:
            new_file.append(file)
    return new_file


def join_together_file_name():
    new_file = search_date_file()
    all_new_files = []
    for file in new_file:
        all_new_file = get_data_path() + "\\" + file
        # print(all_new_file)
        all_new_files.append(all_new_file)
    return all_new_files


def filtrate_text():
    """遍历所有文件获取指定日期的所有数据"""
    all_data_list = []
    all_new_file = join_together_file_name()
    for file in all_new_file:
        # read_file(filename=file)
        with open(file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if re.match('.*%s.*' % date, line) is not None:
                    all_data_list.append(line)
    # print(all_data_list)
    return all_data_list


def choice_method(method):
    """根据method对数据进行分离"""
    method_list = []
    all_data_list = filtrate_text()
    for all_data in all_data_list:
        if re.match('.*%s.*' % method, all_data) is not None:
            method_list.append(all_data)
    # print(method_list)
    return method_list


# ="stallitetag"
def generate_draw_list(method):
    """根据分离完的数据生成画图需要的list"""
    title = method
    date_x1 = []
    date_y1 = []
    date_y2 = []
    method_list = choice_method(method)
    for i in method_list:
        z = i.split(',')
        date_x1.append(z[1])
        date_y1.append(z[2])
        date_y2.append(z[3])
    new_date_x1 = []
    for y in date_x1:
        new_y = y + "000"
        print(type(new_y))
        # new_y = int(new_y)
        new_date_x1.append(new_y)
    date_x1 = new_date_x1
    new_date_y2 = []
    # 去掉"data_y2"中的"\n"
    for z in date_y2:
        new_z = z.strip()
        new_date_y2.append(new_z)
    date_y2 = new_date_y2

    return date_x1, date_y1, date_y2, title
