from django.shortcuts import render
from .utils import run_experiment
import plotly.graph_objects as go
import json


def plot_results(execution_times):
    threads = [key[0] for key in execution_times.keys()]
    times = list(execution_times.values())

    fig = go.Figure(data=go.Scatter(
        x=threads,
        y=times,
        mode='lines+markers',
        marker=dict(color='blue'),
        line=dict(width=2)
    ))

    fig.update_layout(
        title="Performance by Threads",
        xaxis_title="Number of Threads",
        yaxis_title="Time (seconds)"
    )

    graph_html = fig.to_html(full_html=False)

    return graph_html


def performance_view(request):
    execution_times = {}
    for threads in range(1, 6):
        for batch_size in [10, 20, 30]:
            execution_times[(threads, batch_size)] = run_experiment(threads, batch_size)

    graph_html = plot_results(execution_times)

    return render(request, 'performance/performance_dashboard.html', {'graph_html': graph_html})
