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

and run interactively with

```bash
docker run --rm -it  -p 80:80 dataappperformance:latest
```

You can list all tests with

```bash
$ docker run --rm -it -p 80:80 dataappperformance:latest -c 'invoke --list'
Available tasks:

  page-load.dash
  page-load.panel
  page-load.streamlit
  slider-plot.dash
  slider-plot.panel
  slider-plot.streamlit
```

So to run for example the Panel slider-plot app you would run

```bash
docker run --rm -it -p 80:80 dataappperformance:latest -c 'invoke slider-plot.panel'
```

To run the page load test you would have to add port 8089 to the mix like

```bash
docker run --rm -it -p 80:80 -p 8089:8089 dataappperformance:latest -c 'invoke page-load.panel'
```

## Test Results

Click the images to dive into the test and its results

### Drag Slider with Plot Updating Performance Test

Only works for Panel

[![Slider with Plot Test](https://user-images.githubusercontent.com/42288570/149649081-f4bc0c64-1a9f-466c-95f5-3cbbafe273cb.gif)](https://github.com/MarcSkovMadsen/data-app-performance/issues/1).

### Page Load and Refresh

Dash clear winner. Panel server shows blocking behaviour. Streamlit is consistently slow.

[![Page Load and Refresh Test](https://user-images.githubusercontent.com/42288570/149675838-62a2075d-36c8-44c6-b5ea-61f75446ea49.gif)](https://github.com/MarcSkovMadsen/data-app-performance/issues/2).
