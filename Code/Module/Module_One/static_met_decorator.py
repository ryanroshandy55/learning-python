import time


# class Container:
#     def get_current_time():
#         return time.strftime("%H:%M:%S", time.localtime())

#     get_current_time = staticmethod(get_current_time)


# Container.get_current_time()


class Container:
    @staticmethod
    def get_current_time():
        return time.strftime("%H:%M:%S", time.localtime())


print(Container.get_current_time())
