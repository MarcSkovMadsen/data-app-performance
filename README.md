# Data App Performance

My hypothesis is that

*The different architectures of Dash, Panel and Streamlit makes a difference if you want to create snappy applications.*

|Framework | Server | Communication Protocol | Built in state | Update cycle|
|-|-|-|-|-|
|Dash|Flask|https|No|Specific code reruns and UI updates|
|Panel|Tornado|web sockets|Yes, Automatic|Specific code reruns and UI updates|
|Streamlit|Tornado|web sockets|Yes, Manual|Rerun script top to bottom with caching|

I want to test that hypothesis and elaborate on it.

## Test Setup

In order to fairly and reproducibly compare the frameworks I will pin requirements as much as possible and run in Docker.

## Docker

You can build with

```bash
docker build -f "Dockerfile" -t dataappperformance:latest "."
```

and run with

```bash
docker run --rm -it  -p 80:80 dataappperformance:latest
```

When you are in the interactive terminal you find all available commands via `invoke --list`

```bash
$ invoke --list
Available tasks:

  slider-plot.dash
  slider-plot.panel
  slider-plot.streamlit
```

So to run for example the Panel slider-plot app you would run `invoke slider-plot.panel`

```bash
root@f7171400d90a:/# invoke slider-plot.panel
cd src/slider_plot && panel serve slider_plot_panel.py --port 80
2022-01-16 04:50:24,957 Starting Bokeh server version 2.4.2 (running on Tornado 6.1)
2022-01-16 04:50:24,958 User authentication hooks NOT provided (default user enabled)
2022-01-16 04:50:24,962 Bokeh app running at: http://localhost:80/slider_plot_panel
2022-01-16 04:50:24,962 Starting Bokeh server with process id: 9
```

## Test Results

[Slider and Plot Test](https://github.com/MarcSkovMadsen/data-app-performance/issues/1).