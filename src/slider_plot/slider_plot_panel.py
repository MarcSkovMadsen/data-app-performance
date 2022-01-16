import plotly.express as px


def plot(count):
    x = [str(i) for i in range(0, count)]
    y = list(range(0, count))
    return px.bar(x=x, y=y)


import panel as pn

pn.extension("plotly", sizing_mode="stretch_width", template="fast")

count = pn.widgets.IntSlider(name="Count", start=1, end=50, value=10).servable(area="sidebar")
pn.panel(pn.bind(plot, count)).servable(title="Slider Example")