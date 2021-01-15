# coding=utf-8
import xlrd
import xlwt
from xlutils.copy import copy


class ReadExcel:

    # 读数据
    def read_xlrd(excelFile):
        data = xlrd.open_workbook('E:\\pythonProject\\mytest\\longTest.xls')

        print("工作表为：" + str(data.sheet_names()))

        table = data.sheet_by_name('My Worksheet')

        print("总行数：" + str(table.nrows))
        print("总列数：" + str(table.ncols))
        line = int(table.nrows)
        column = int(table.ncols)

        if column==2:
            for l in range(1, line):
                account = str(table.cell(l, 0).value)
                password = str(table.cell(l, 1).value)
                print("第%s行第一列的值为: %s" % (l, account))
                print("第%s行第二列的值为: %s" % (l, password))


    # 写入数据
    def write_excel(self,livingRoomId,excel):
        try:
            data = xlrd.open_workbook('E:\\pythonProject\\mytest\\longTest.xls')

            print("工作表为：" + str(data.sheet_names()))

            table = data.sheet_by_name('My Worksheet')

            print("总行数：" + str(table.nrows))
            print("总列数：" + str(table.ncols))
            line = int(table.nrows)
            column = int(table.ncols)
            if line>0 and column>0:
                ReadExcel.followWrite(None,livingRoomId,excel)
        except FileNotFoundError:
            print("文件不存在,创建文件中")

            # 创建excel
            workbook = xlwt.Workbook(encoding='utf-8')
            # 创建一个worksheet
            worksheet = workbook.add_sheet('My Worksheet')
            worksheet.write(0, 0, label=livingRoomId)

            workbook.save('E:\\pythonProject\\mytest\\longTest.xls')
            print("excel保存成功")

        except EOFError as e:
            print("错误信息：%s :"%e)
        except Exception as exc:
            print("异常信息 %s : "%exc)


    # 追加数据
    def followWrite(self,livingRoomId,excel_line):
        data = xlrd.open_workbook('E:\\pythonProject\\mytest\\longTest.xls', formatting_info=True)
        excel = copy(wb=data)  # 完成xlrd对象向xlwt对象转换
        excel_table = excel.get_sheet(0)
        table = data.sheets()[0]
        nrows = table.nrows  # 获得行数
        ncols = table.ncols  # 获得列数
        excel_table.write(nrows, int(excel_line), livingRoomId)  # 因为单元格从0开始算
            # nrows = nrows + 1
        excel.save('E:\\pythonProject\\mytest\\longTest.xls')
        print("excel数据追加保存成功")


if __name__ == '__main__':
    for i in range(1,6):
        ReadExcel.write_excel(None,'haliluya')