import pandas as pd
import numpy as np
import plotly.express as px

df = pd.read_csv(r"./output/qb_epa_stats.csv")

num_players = df["player"].nunique()

fig = px.line(
  df,
  x="season",
  y="rank",
  markers=True,
  facet_row="player",
  title="Rookie QB EPA Rank Trajectory (2016-2024)",
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
    hovermode="x unified",
    height=300 * num_players,    # KEY: makes each chart big
)

# Clean up facet labels
fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[1]))

fig.show()