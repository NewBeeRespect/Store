import xlrd

wb = xlrd.open_workbook(filename=r"D:\0Sx\sql\day9\任务\2020年每个月的销售情况.xlsx",encoding_override=True)
# 全年的销售总额
sum = 0
data = 0
for i in range(0, 12):
    st = wb.sheet_by_index(i)
    rows = st.nrows
    cols = st.ncols
    for j in range(1, rows):
        data = data+st.row_values(j)[2]*st.row_values(j)[4]
print('全年的销售总额为:', data)


list=['羽绒服','牛仔裤','铅笔裤','皮草','衬衫','卫衣','T恤','风衣','马甲','小西装','休闲裤','棉衣','皮衣']
for k in range(len(list)):
    sum = 0
    data = 0
    for i in range(0,12):
        st=wb.sheet_by_index(i)
        rows=st.nrows
        cols=st.ncols
        for j in range(1,rows):
            sum=sum+st.row_values(j)[4]
            if st.row_values(j)[1]==list[k]:
                data=data+st.row_values(j)[4]
    print(list[k],'的销售占比为：','{:.2%}'.format(data/sum))


#每件衣服的销售占比
for i in range(0, 12):
    st = wb.sheet_by_index(i)
    rows = st.nrows
    cols = st.ncols
    for k in range(len(list)):
        sum = 0
        data = 0
        for j in range(1,rows):
            sum = sum+st.row_values(j)[4]
            if st.row_values(j)[1]==list[k]:
                data = data+st.row_values(j)[4]
        print(list[k], i+1, '月的销售占比为：', '{:.2%}'.format(data/sum))


#每件衣服的月销售占比
for k in range(len(list)):
    sum = 0
    data = 0
    for i in range(0,12):
        st = wb.sheet_by_index(i)
        rows = st.nrows
        cols = st.ncols
        for j in range(1,rows):
            sum = sum+st.row_values(j)[4]*st.row_values(j)[2]
            if st.row_values(j)[1] == list[k]:
                data=data+st.row_values(j)[4]*st.row_values(j)[2]
    print(list[k], '的销售额占比为：', '{:.2%}'.format(data/sum))

#每件衣服的销售额占比
sum = 0
a = 0
for k in range(len(list)):
    data = 0
    sum1 = 0
    for i in range(0,12):
        st = wb.sheet_by_index(i)
        rows = st.nrows
        cols = st.ncols
        for j in range(1, rows):
            sum1 += st.row_values(j)[4]
            if st.row_values(j)[1] == list[k]:
                data = data+st.row_values(j)[4]
    if data > sum:
        sum = data
        a = k
print('最畅销的衣服是', list[a], '{:.2%}'.format(sum/sum1))

#最畅销衣服
sum = 0
a = 0
for k in range(len(list)):
    data = 0
    sum1 = 0
    for i in range(0, 12):
        st = wb.sheet_by_index(i)
        rows = st.nrows
        cols = st.ncols
        for j in range(1, rows):
            sum1 += st.row_values(j)[4]
            if st.row_values(j)[1] == list[k]:
                data = data+st.row_values(j)[4]
    if sum == 0:
        sum = data
    if sum > data:
        sum = data
        a = k
print('最不畅销的衣服是', list[a], '{:.2%}'.format(sum/sum1))


#每个季度畅销衣服
sum = 0
a = 0
b = 0
c = 0
d = 0
sum1 = 0
sum2 = 0
sum3 = 0
for k in range(len(list)):
    data = 0
    data1=0
    data2=0
    data3=0
    for i in range(12):
        st = wb.sheet_by_index(i)
        rows = st.nrows
        cols = st.ncols
        if i >= 3 and i <= 5:
            for j in range(1, rows):
                sum1 += st.row_values(j)[4]
                if st.row_values(j)[1] == list[k]:
                    data = data+st.row_values(j)[4]
            if data > sum:
                sum = data
                a = k
        elif i >= 6 and i <= 8:
            for j in range(1, rows):
                if st.row_values(j)[1] == list[k]:
                    data1 = data1 + st.row_values(j)[4]
            if data1 > sum1:
                sum1 = data1
                b = k
        elif i >= 9 and i <= 11:
            for j in range(1, rows):
                if st.row_values(j)[1] == list[k]:
                    data2 = data2 + st.row_values(j)[4]
            if data2 > sum2:
                sum2 = data2
                c = k
        else:
            for j in range(1, rows):
                if st.row_values(j)[1] == list[k]:
                    data3 = data3 + st.row_values(j)[4]
            if data3 > sum3:
                sum3 = data3
                d = k
print('第一个季度最畅销的衣服',list[a])
print('第二个季度最畅销的衣服',list[b])
print('第三个季度最畅销的衣服',list[c])
print('第四个季度最畅销的衣服',list[d])





















