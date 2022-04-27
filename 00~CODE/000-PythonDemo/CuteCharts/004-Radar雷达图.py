from cutecharts.charts import Radar
from cutecharts.components import Page
from cutecharts.faker import Faker


def radar_base() -> Radar:
    chart = Radar("Radar-基本示例")
    chart.set_options(
        labels=Faker.choose(),
        colors=Faker.colors,
        legend_pos="upRight",
    )
    chart.add_series("series-A", Faker.values())
    chart.add_series("series-B", Faker.values())
    return chart


radar_base().render()
