from cutecharts.charts import Bar
from cutecharts.faker import Faker  # Faker 在这里主要用来生成随机数


def bar_base() -> Bar:
    chart = Bar("Bar-基本示例")
    chart.set_options(labels=Faker.choose(),
                      x_label="This is x label",
                      y_label="This is y label",
                      colors=Faker.colors  # 调整颜色
                      )
    chart.add_series("series-A", Faker.values())
    return chart


bar_base().render()
