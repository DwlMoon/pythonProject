import datetime
import time
from dateutil import parser


import worklogfile.workLogging

class testlogger:

    logger=worklogfile.workLogging.Logger("testlogger").get_log()
    def test1(self):
        a="nihao"
        try:
            2/0
        except EOFError as e:
            testlogger.logger.info("错误信息为:")
            testlogger.logger.info(e)
        except Exception as e:
            testlogger.logger.info("异常信息为:")
            testlogger.logger.info(e)



if __name__=="__main__":
    a = "Oct 26 2020 13:00"
    # c = time.strptime(a, "%Y-%m-%d %H:%M:%S")
    # c = time.strptime(a, '%Y/%m/%d %H:%M:%S')
    # s = '25 April, 2020, 2:50, pm, IST'
    b=parser.parse(a)
    # datetime.timedelta()
    # print(c)
    c = b+datetime.timedelta(hours=15)
    d=time.strftime("%Y-%m-%d %H:%M:%S")
    print(d)