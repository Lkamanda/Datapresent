from present.draw_picture import draw_picture
from until_file_handle.file_handle import generate_draw_list

method_list = ["stallitetag"]

for i in method_list:
    date_x1, date_y1, date_y2, title = generate_draw_list(method=i)
    print(date_x1)
    print(date_y1)
    print(date_y2)
    draw_picture(date_x1, date_y1, date_y2, title)