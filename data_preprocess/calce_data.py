
from tqdm.notebook import tqdm
import os
import glob
import pandas as pd
from pathlib import Path

filenames = []
outdir = Path("data_v0")
Path.mkdir(outdir, exist_ok=True)
for folder in tqdm(os.listdir("calce")):
    if "type" in folder:
        print(folder)
        data = []
        typedir = Path(outdir/folder)
        Path.mkdir(typedir, exist_ok=True)
        print(sorted(os.listdir("calce/"+folder)))
        for subfolder in tqdm(os.listdir("calce/"+folder)):
            #print(filenames)
            if "CS" in subfolder:
                print(subfolder)
                cell_name = subfolder
                filenames = glob.glob(f"calce/{folder}/{subfolder}/"+"*.xlsx")
                for file in tqdm(filenames):
                    df = pd.read_excel(file,sheet_name=1)
                    df["cell_type"] = cell_name

                    df = df.drop(columns=["Data_Point", "Test_Time(s)", "Step_Time(s)", "Step_Index",
                    "Is_FC_Data", "Internal_Resistance(Ohm)", "dV/dt(V/s)", "AC_Impedance(Ohm)"])
                    df.index = pd.to_datetime(df["Date_Time"])
                    df = df.drop(columns=["Date_Time"])
                    data.append(df)
        data_df = pd.concat(data)
        data_df.to_csv(Path(typedir/"data.csv"))
#data_df.describe()