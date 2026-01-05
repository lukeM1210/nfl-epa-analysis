from pathlib import Path
import pandas as pd

OUTPUT_DIR = Path("output")
STATS_OUT_PATH = OUTPUT_DIR / "2025_epa_stats_analysis.csv"
STATS_OUT_PATH_WOD = OUTPUT_DIR / "2025_epa_stats_analysis_wod.csv"

df_offense_2025 = pd.read_csv(r"2025_EPA_Analysis/offensive_epa2025.csv")
df_defense_2025 = pd.read_csv(r"2025_EPA_Analysis/defensive_epa2025.csv")
df_qb_2025 = pd.read_csv(r"2025_EPA_Analysis/qb_epa2025.csv")

df_top_10_offense = df_offense_2025[df_offense_2025["Unnamed: 0"] <= 10]
df_top_8_defense = df_defense_2025[df_defense_2025["Unnamed: 0"] <= 8]
df_top_8_qb = df_qb_2025[df_qb_2025["Unnamed: 0"] <= 8]

common_teams = (
  set(df_top_10_offense["Abbr"]) & set(df_top_8_defense["Abbr"]) & set(df_top_8_qb["Team"])
)

common_teams_without_defense = (
  set(df_top_10_offense["Abbr"]) & set(df_top_8_qb["Team"])
)

df_out = df_top_10_offense[df_top_10_offense["Abbr"].isin(common_teams)].copy()
df_out_wod = df_top_10_offense[df_top_10_offense["Abbr"].isin(common_teams_without_defense)].copy()

# Write stats to CSV output file
OUTPUT_DIR.mkdir(exist_ok=True)
df_out.to_csv(STATS_OUT_PATH, index=False)
df_out_wod.to_csv(STATS_OUT_PATH_WOD, index=False)

print("Common teams:", sorted(common_teams_without_defense))
print(f"Saved results to {STATS_OUT_PATH_WOD}")

print("Common teams:", sorted(common_teams))
print(f"Saved results to {STATS_OUT_PATH}")
