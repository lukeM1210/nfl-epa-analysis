import pandas as pd

sb_2016 = ["T.Brady", "M.Ryan"]
sb_2017 = ["N.Foles", "T.Brady"]
sb_2018 = ["T.Brady", "J.Goff"]
sb_2019 = ["P.Mahomes", "J.Garoppolo"]
sb_2020 = ["T.Brady", "P.Mahomes"]
sb_2021 = ["M.Stafford", "J.Burrow"]
sb_2022 = ["P.Mahomes", "J.Hurts"]
sb_2023 = ["P.Mahomes", "B.Purdy"]
sb_2024 = ["P.Mahomes", "J.Hurts"]

qbs_2016 = pd.read_csv("qb_EPA_data/quarterbackEPA2016.csv")
qbs_2017 = pd.read_csv("qb_EPA_data/quarterbackEPA2017.csv")
qbs_2018 = pd.read_csv("qb_EPA_data/quarterbackEPA2018.csv")
qbs_2019 = pd.read_csv("qb_EPA_data/quarterbackEPA2019.csv")
qbs_2020 = pd.read_csv("qb_EPA_data/quarterbackEPA2020.csv")
qbs_2021 = pd.read_csv("qb_EPA_data/quarterbackEPA2021.csv")
qbs_2022 = pd.read_csv("qb_EPA_data/quarterbackEPA2022.csv")
qbs_2023 = pd.read_csv("qb_EPA_data/quarterbackEPA2023.csv")
qbs_2024 = pd.read_csv("qb_EPA_data/quarterbackEPA2024.csv")

df = qbs_2016[qbs_2016["Player"].isin(sb_2016)]

print(df)

df.to_csv(
    "sb_qbs.csv",
    mode="a",          # append
    header=False,      # don't duplicate header
    index=False
)



# if df.empty:
#   print("F")
# else:
#   print("T")