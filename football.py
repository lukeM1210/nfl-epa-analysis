import pandas as pd

df = pd.read_csv(r"data/yearly_team_stats_offense.csv")
df_reg = df[(df["season_type"] == "REG") & (df["season"] == 2023)]


avg_total_off_yards = df_reg["total_off_yards"].mean()
avg_wins = df_reg["win"].mean()
avg_yac = df_reg["yards_after_catch"].mean()

avg_fourth_down_conversions = df_reg["fourth_down_converted"].mean()

df_reg_find_best = df_reg[(df_reg["total_off_yards"] > avg_total_off_yards) & (df_reg["win"] > avg_wins) & (df_reg["yards_after_catch"] > avg_yac) & (df_reg["fourth_down_converted"] > avg_fourth_down_conversions)]

print(df_reg_find_best)