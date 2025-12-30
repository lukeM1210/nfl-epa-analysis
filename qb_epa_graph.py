import pandas as pd
import numpy as np
import plotly.express as px

df = pd.read_csv(r"./output/qb_epa_stats.csv")

fig = px.line(
  df,
  x="season",
  y="rank",
  color="player",
  markers=True,
  title="Rookie QB EPA Rank Trajectory 2016-2024",
  labels={
    "season":"season",
    "rank": "EPA Rank",
    "player": "Quarterback",
  },
)

# Invert Y-axis so rank 1 is at the top (better)
fig.update_yaxes(autorange="reversed")

fig.update_layout(
  template="plotly_dark",
  legend_title_text="QB",
  hovermode="x unified",
)

fig.show()