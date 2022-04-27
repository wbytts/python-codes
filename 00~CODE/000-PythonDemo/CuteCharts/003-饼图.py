from cutecharts.charts import Pie
from cutecharts.components import Page
from cutecharts.faker import Faker


def pie_base() -> Pie:
    chart = Pie("Pie-基本示例")
    chart.set_options(
        labels=Faker.choose(),
        legend_pos="upRight",  # 图例的位置
        inner_radius=0,  # 饼图内圈的半径
    )
    chart.add_series(Faker.values())
    return chart


pie_base().render()
