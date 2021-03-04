import datetime


def get_pass_date(interval_day):
    """
    获取未来的日期
    :param interval_day: 间隔的天数
    :return:
    """
    today_date = datetime.date.today()
    future_date = today_date + datetime.timedelta(days=-interval_day)
    return future_date


if __name__ == "__main__":
    print(get_pass_date(10))
