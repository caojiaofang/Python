import schedule
import time
import datetime


def job():
    times = datetime.datetime.now()
    print("I'm working...,time : %s" % times)


# 每10秒执行一次
# schedule.every(10).seconds.do(job)
#
# # 每10分钟执行一次
# schedule.every(10).minutes.do(job)
#
# # 每小时执行一次
# schedule.every().hour.do(job)
#
# # 每天十点半执行
# schedule.every().day.at("10:30").do(job)
#
# 每隔2到4分钟之内执行一次任务
schedule.every(2).to(4).minutes.do(job)
#
# # 每周一执行
# schedule.every().monday.do(job)
#
# # 每周三13点15执行
# schedule.every().wednesday.at("13:15").do(job)

# 每分钟第二十五秒的时候执行
# schedule.every().minute.at(":25").do(job)


while True:
    # 运行所有可运行的任务
    schedule.run_pending()
    time.sleep(1)
