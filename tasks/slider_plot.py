from invoke import task

PATH = "src/slider_plot"

from .shared import run

@task()
def dash(context):
    run(context, PATH, "gunicorn slider_plot_dash:server -b :80")

@task()
def streamlit(context):
    run(context, PATH, "streamlit run slider_plot_streamlit.py --server.port 80 --server.address '0.0.0.0'")

@task()
def panel(context):
    run(context, PATH, "panel serve slider_plot_panel.py --port 80")