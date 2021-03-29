import time


def get_timestamp():
    """
    获取毫秒级
    :return:
    """
    return str(int(time.time() * 1000))[-8:]


# def test():
#     return time.time()


if __name__ == "__main__":
    pass
    # print(get_timestamp())
    # print(test())
