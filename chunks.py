import pandas as pd

chunk_size = 10_000

for chunk in pd.read_csv("Crime_Data_from_2020_to_Present.csv",chunksize=chunk_size):

    filtered_chunk = chunk[chunk["Crm Cd Desc"] == "VEHICLE - STOLEN"]

    filtered_chunk.to_csv("stolen_vehicles.csv", mode="a", index=False, header=False)
    
    print(f"{chunk} processed")

print("All data processed")
