import pandas as pd
from pathlib import Path

OUTPUT_DIR = Path("output")
STATS_OUT_PATH = OUTPUT_DIR / "analysis.csv"

# Write stats to CSV output file
OUTPUT_DIR.mkdir(exist_ok=True)

# df_out = pd.DataFrame(df_games_since_2018)
# df_out_1 = pd.DataFrame(df_game_weather_since_2018)
# df_out_1.to_csv(STATS_OUT_PATH, index=False)
# print(f"Saved results to {STATS_OUT_PATH}")
# Join games_weather_since_2018.csv and games_since_2018.csv
# games_weather = pd.read_csv("datasets/game_weather_since_2018.csv")
# games = pd.read_csv("datasets/games_since_2018.csv")
# df = pd.merge(games_weather,games,on="game_id",how="inner")
# df_out = df.to_csv(STATS_OUT_PATH, index=False)
# print(f"Saved csv to {STATS_OUT_PATH}")

df1 = pd.read_csv("datasets/merged_weather_and_game.csv")
df2 = pd.read_csv("datasets/nfl_mahomes_era_games.csv")

print(len(df1) / len(df2))
