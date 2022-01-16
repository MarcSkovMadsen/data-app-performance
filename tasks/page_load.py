from invoke import task

PATH = ""

from .shared import run

@task()
def dash(context):
    run(context, PATH, "locust -f src/page_load/page_load_dash.py --host http://localhost:80 --users 10 & gunicorn src.slider_plot.slider_plot_dash:server -b :80")

@task()
def streamlit(context):
    run(context, PATH, "locust -f src/page_load/page_load_streamlit.py --host http://localhost:80 --users 10 & streamlit run src/slider_plot/slider_plot_streamlit.py --server.port 80 --server.address '0.0.0.0'")

@task()
def panel(context):
    run(context, PATH, "locust -f src/page_load/page_load_panel.py --host http://localhost:80 --users 10 & panel serve src/slider_plot/slider_plot_panel.py --port 80")