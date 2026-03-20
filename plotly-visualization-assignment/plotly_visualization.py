import pandas as pd
import plotly.express as px

data = {
    "Epoch": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Training Loss": [0.95, 0.88, 0.82, 0.76, 0.70, 0.65, 0.61, 0.59, 0.58, 0.57]
}

df = pd.DataFrame(data)

fig = px.line(
    df,
    x="Epoch",
    y="Training Loss",
    title="Training Loss Over Epochs",
    markers=True
)

fig.update_layout(
    xaxis_title="Epoch",
    yaxis_title="Training Loss"
)

fig.update_traces(line_shape="spline")

fig.show()