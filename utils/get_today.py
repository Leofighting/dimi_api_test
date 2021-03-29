import datetime


def get_today_date():
    """
    获取今天的日期
    :return:
    """
    today_date = datetime.date.today()
    return today_date


if __name__ == "__main__":
    print(get_today_date(), type(get_today_date()))
