from pathlib import Path
import pandas as pd

rookies_by_year = {
    2016: ["D.Prescott", "C.Wentz"],
    2017: ["D.Watson", "M.Trubisky", "D.Kizer"],
    2018: ["B.Mayfield", "L.Jackson", "S.Darnold", "J.Allen"],
    2019: ["K.Murray", "G.Minshew II", "D.Jones"],
    2020: ["J.Herbert", "T.Tagovailoa", "J.Burrow"],
    2021: ["M.Jones", "D.Mills", "J.Fields", "T.Lawrence", "Z.Wilson"],
    2022: ["K.Pickett"],
    2023: ["C.Stroud", "W.Levis", "B.Young"],
    2024: ["D.Maye", "B.Nix", "J.Daniels", "C.Williams"],
}

df_qb_epa_2016 = pd.read_csv(r"qb_EPA_data/quarterbackEPA2016.csv")
df_qb_epa_2017 = pd.read_csv(r"qb_EPA_data/quarterbackEPA2017.csv")
df_qb_epa_2018 = pd.read_csv(r"qb_EPA_data/quarterbackEPA2018.csv")
df_qb_epa_2019 = pd.read_csv(r"qb_EPA_data/quarterbackEPA2019.csv")
df_qb_epa_2020 = pd.read_csv(r"qb_EPA_data/quarterbackEPA2020.csv")
df_qb_epa_2021 = pd.read_csv(r"qb_EPA_data/quarterbackEPA2021.csv")
df_qb_epa_2022 = pd.read_csv(r"qb_EPA_data/quarterbackEPA2022.csv")
df_qb_epa_2023 = pd.read_csv(r"qb_EPA_data/quarterbackEPA2023.csv")
df_qb_epa_2024 = pd.read_csv(r"qb_EPA_data/quarterbackEPA2024.csv")

dfs_by_year = {
    2016: df_qb_epa_2016,
    2017: df_qb_epa_2017,
    2018: df_qb_epa_2018,
    2019: df_qb_epa_2019,
    2020: df_qb_epa_2020,
    2021: df_qb_epa_2021,
    2022: df_qb_epa_2022,
    2023: df_qb_epa_2023,
    2024: df_qb_epa_2024,
}

OUTPUT_DIR = Path("output")
STATS_OUT_PATH = OUTPUT_DIR / "qb_epa_stats.csv"
rows = []

for rookie_year, rookies in rookies_by_year.items():
    for qb in rookies:
        for season in range(rookie_year, 2025):
            df = dfs_by_year.get(season)
            if df is None:
                continue

            qb_row = df[df["Player"] == qb]

            if qb_row.empty:
                continue  # QB didn't play that season

            row = {
                "rank": qb_row.iloc[0]["Unnamed: 0"],
                "player": qb,
                "rookie_year": rookie_year,
                "season": season,
                "years_since_rookie": season - rookie_year,
                "epa_play": qb_row.iloc[0]["EPA/play"],
                "adj_epa_play": qb_row.iloc[0]["Adj. EPA/play"],
                "epa_cpoe": qb_row.iloc[0]["EPA+CPOE composite"],
            }

            rows.append(row)

OUTPUT_DIR.mkdir(exist_ok=True)

df_out = pd.DataFrame(rows)
df_out.to_csv(STATS_OUT_PATH, index=False)

print(f"Saved results to {STATS_OUT_PATH}")



