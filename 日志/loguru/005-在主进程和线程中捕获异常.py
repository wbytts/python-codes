from loguru import logger

logger.add(sink='log.log', format="{time} - {level} - {message}", level="INFO")


@logger.catch
def my_function(x, y, z):
    return 1 / (x + y + z)


res = my_function(0, 1, -1)
print(res)
