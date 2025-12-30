from pathlib import Path
import pandas as pd

OUTPUT_DIR = Path("output")
STATS_OUT_PATH = OUTPUT_DIR / "epa_stats.csv"
# Output rows
rows = []

sb_winner_2016 = "NE"
sb_winner_2017 = "PHI"
sb_winner_2018 = "NE"
sb_winner_2019 = "KC"
sb_winner_2020 = "TB"
sb_winner_2021 = "LA"
sb_winner_2022 = "KC"
sb_winner_2023 = "KC"
sb_winner_2024 = "PHI"

sb_winner_qb_2016 = "T.Brady"
sb_winner_qb_2017 = "C.Wentz"
sb_winner_qb_2018 = "T.Brady"
sb_winner_qb_2019 = "P.Mahomes"
sb_winner_qb_2020 = "T.Brady"
sb_winner_qb_2021 = "M.Stafford"
sb_winner_qb_2022 = "P.Mahomes"
sb_winner_qb_2023 = "P.Mahomes"
sb_winner_qb_2024 = "J.Hurts"

# ---------------------- 2016 ------------------------------
df_offense_2016 = pd.read_csv(r"EPA_data/offenseEPA2016.csv")
df_defense_2016 = pd.read_csv(r"EPA_data/defenseEPA2016.csv")
df_quarterback_2016 = pd.read_csv(r"EPA_data/quarterbackEPA2016.csv")

o_rank = df_offense_2016[df_offense_2016["Abbr"] == sb_winner_2016]
o_rank_val = o_rank["Unnamed: 0"].iloc[0]

d_rank = df_defense_2016[df_defense_2016["Abbr"] == sb_winner_2016]
d_rank_val = d_rank["Unnamed: 0"].iloc[0]

qb_rank = df_quarterback_2016[df_quarterback_2016["Player"] == sb_winner_qb_2016]
qb_rank_val = qb_rank["Unnamed: 0"].iloc[0]

rows.append({
  "Year": 2016,
  "Team": "NE Patriots",
  "Offensive EPA Rank": o_rank_val,
  "Defensive EPA Rank": d_rank_val,
  "Quarterback EPA Rank": qb_rank_val
})
# ----------------------------------------------------------

# ---------------------- 2017 ------------------------------
df_offense_2017 = pd.read_csv(r"EPA_data/offenseEPA2017.csv")
df_defense_2017 = pd.read_csv(r"EPA_data/defenseEPA2017.csv")
df_quarterback_2017 = pd.read_csv(r"EPA_data/quarterbackEPA2017.csv")

o_rank = df_offense_2017[df_offense_2017["Abbr"] == sb_winner_2017]
o_rank_val = o_rank["Unnamed: 0"].iloc[0]

d_rank = df_defense_2017[df_defense_2017["Abbr"] == sb_winner_2017]
d_rank_val = d_rank["Unnamed: 0"].iloc[0]

qb_rank = df_quarterback_2017[df_quarterback_2017["Player"] == sb_winner_qb_2017]
qb_rank_val = qb_rank["Unnamed: 0"].iloc[0]

rows.append({
  "Year": 2017,
  "Team": "PHI Eagles",
  "Offensive EPA Rank": o_rank_val,
  "Defensive EPA Rank": d_rank_val,
  "Quarterback EPA Rank": qb_rank_val
})
# ----------------------------------------------------------

# ---------------------- 2018 ------------------------------
df_offense_2018 = pd.read_csv(r"EPA_data/offenseEPA2018.csv")
df_defense_2018 = pd.read_csv(r"EPA_data/defenseEPA2018.csv")
df_quarterback_2018 = pd.read_csv(r"EPA_data/quarterbackEPA2018.csv")

o_rank = df_offense_2018[df_offense_2018["Abbr"] == sb_winner_2018]
o_rank_val = o_rank["Unnamed: 0"].iloc[0]

d_rank = df_defense_2018[df_defense_2018["Abbr"] == sb_winner_2018]
d_rank_val = d_rank["Unnamed: 0"].iloc[0]

qb_rank = df_quarterback_2018[df_quarterback_2018["Player"] == sb_winner_qb_2018]
qb_rank_val = qb_rank["Unnamed: 0"].iloc[0]

rows.append({
  "Year": 2018,
  "Team": "NE Patriots",
  "Offensive EPA Rank": o_rank_val,
  "Defensive EPA Rank": d_rank_val,
  "Quarterback EPA Rank": qb_rank_val
})
# ----------------------------------------------------------

# ---------------------- 2019 ------------------------------
df_offense_2019 = pd.read_csv(r"EPA_data/offenseEPA2019.csv")
df_defense_2019 = pd.read_csv(r"EPA_data/defenseEPA2019.csv")
df_quarterback_2019 = pd.read_csv(r"EPA_data/quarterbackEPA2019.csv")

o_rank = df_offense_2019[df_offense_2019["Abbr"] == sb_winner_2019]
o_rank_val = o_rank["Unnamed: 0"].iloc[0]

d_rank = df_defense_2019[df_defense_2019["Abbr"] == sb_winner_2019]
d_rank_val = d_rank["Unnamed: 0"].iloc[0]

qb_rank = df_quarterback_2019[df_quarterback_2019["Player"] == sb_winner_qb_2019]
qb_rank_val = qb_rank["Unnamed: 0"].iloc[0]

rows.append({
  "Year": 2019,
  "Team": "KC Chiefs",
  "Offensive EPA Rank": o_rank_val,
  "Defensive EPA Rank": d_rank_val,
  "Quarterback EPA Rank": qb_rank_val
})
# ----------------------------------------------------------

# ---------------------- 2020 ------------------------------
df_offense_2020 = pd.read_csv(r"EPA_data/offenseEPA2020.csv")
df_defense_2020 = pd.read_csv(r"EPA_data/defenseEPA2020.csv")
df_quarterback_2020 = pd.read_csv(r"EPA_data/quarterbackEPA2020.csv")

o_rank = df_offense_2020[df_offense_2020["Abbr"] == sb_winner_2020]
o_rank_val = o_rank["Unnamed: 0"].iloc[0]

d_rank = df_defense_2020[df_defense_2020["Abbr"] == sb_winner_2020]
d_rank_val = d_rank["Unnamed: 0"].iloc[0]

qb_rank = df_quarterback_2020[df_quarterback_2020["Player"] == sb_winner_qb_2020]
qb_rank_val = qb_rank["Unnamed: 0"].iloc[0]

rows.append({
  "Year": 2020,
  "Team": "TB Buccaneers",
  "Offensive EPA Rank": o_rank_val,
  "Defensive EPA Rank": d_rank_val,
  "Quarterback EPA Rank": qb_rank_val
})
# ----------------------------------------------------------

# ----------------------- 2021 ------------------------------
df_offense_2021 = pd.read_csv(r"EPA_data/offenseEPA2021.csv")
df_defense_2021 = pd.read_csv(r"EPA_data/defenseEPA2021.csv")
df_quarterback_2021 = pd.read_csv(r"EPA_data/quarterbackEPA2021.csv")

o_rank = df_offense_2021[df_offense_2021["Abbr"] == sb_winner_2021]
o_rank_val = o_rank["Unnamed: 0"].iloc[0]

d_rank = df_defense_2021[df_defense_2021["Abbr"] == sb_winner_2021]
d_rank_val = d_rank["Unnamed: 0"].iloc[0]

qb_rank = df_quarterback_2021[df_quarterback_2021["Player"] == sb_winner_qb_2021]
qb_rank_val = qb_rank["Unnamed: 0"].iloc[0]

rows.append({
  "Year": 2021,
  "Team": "LA Rams",
  "Offensive EPA Rank": o_rank_val,
  "Defensive EPA Rank": d_rank_val,
  "Quarterback EPA Rank": qb_rank_val
})
# ------------------------------------------------------------


# ------------------------ 2022 ------------------------------
df_offense_2022 = pd.read_csv(r"EPA_data/offenseEPA2022.csv")
df_defense_2022 = pd.read_csv(r"EPA_data/defenseEPA2022.csv")
df_quarterback_2022 = pd.read_csv(r"EPA_data/quarterbackEPA2022.csv")

o_rank = df_offense_2022[df_offense_2022["Abbr"] == sb_winner_2022]
o_rank_val = o_rank["Unnamed: 0"].iloc[0]

d_rank = df_defense_2022[df_defense_2022["Abbr"] == sb_winner_2022]
d_rank_val = d_rank["Unnamed: 0"].iloc[0]

qb_rank = df_quarterback_2022[df_quarterback_2022["Player"] == sb_winner_qb_2022]
qb_rank_val = qb_rank["Unnamed: 0"].iloc[0]

rows.append({
  "Year": 2022,
  "Team": "KC Chiefs",
  "Offensive EPA Rank": o_rank_val,
  "Defensive EPA Rank": d_rank_val,
  "Quarterback EPA Rank": qb_rank_val
})
# -------------------------------------------------------------

# ------------------------ 2023 -------------------------------
df_offense_2023 = pd.read_csv(r"EPA_data/offenseEPA2023.csv")
df_defense_2023 = pd.read_csv(r"EPA_data/defenseEPA2023.csv")
df_quarterback_2023 = pd.read_csv(r"EPA_data/quarterbackEPA2023.csv")

o_rank = df_offense_2023[df_offense_2023["Abbr"] == sb_winner_2023]
o_rank_val = o_rank["Unnamed: 0"].iloc[0]

d_rank = df_defense_2023[df_defense_2023["Abbr"] == sb_winner_2023]
d_rank_val = d_rank["Unnamed: 0"].iloc[0]

qb_rank = df_quarterback_2023[df_quarterback_2023["Player"] == sb_winner_qb_2023]
qb_rank_val = qb_rank["Unnamed: 0"].iloc[0]

rows.append({
  "Year": 2023,
  "Team": "KC Chiefs",
  "Offensive EPA Rank": o_rank_val,
  "Defensive EPA Rank": d_rank_val,
  "Quarterback EPA Rank": qb_rank_val
})
# -------------------------------------------------------------

# -------------------------- 2024 ------------------------------
df_offense_2024 = pd.read_csv(r"EPA_data/offenseEPA2024.csv")
df_defense_2024 = pd.read_csv(r"EPA_data/defenseEPA2024.csv")
df_quarterback_2024 = pd.read_csv(r"EPA_data/quarterbackEPA2024.csv")

o_rank = df_offense_2024[df_offense_2024["Abbr"] == sb_winner_2024]
o_rank_val = o_rank["Unnamed: 0"].iloc[0]

d_rank = df_defense_2024[df_defense_2024["Abbr"] == sb_winner_2024]
d_rank_val = d_rank["Unnamed: 0"].iloc[0]

qb_rank = df_quarterback_2024[df_quarterback_2024["Player"] == sb_winner_qb_2024]
qb_rank_val = qb_rank["Unnamed: 0"].iloc[0]

rows.append({
  "Year": 2024,
  "Team": "PHI Eagles",
  "Offensive EPA Rank": o_rank_val,
  "Defensive EPA Rank": d_rank_val,
  "Quarterback EPA Rank": qb_rank_val
})
# --------------------------------------------------------------

# Write stats to CSV output file
OUTPUT_DIR.mkdir(exist_ok=True)

df_out = pd.DataFrame(rows)
df_out.to_csv(STATS_OUT_PATH, index=False)

print(f"Saved results to {STATS_OUT_PATH}")