import pandas as pd

chunk_size = 10000

chunk_count = 0

for chunk in pd.read_csv("Crime_Data_from_2020_to_Present.csv",chunksize=chunk_size):

    filtered_chunk = chunk[chunk["Crm Cd Desc"] == "VEHICLE - STOLEN"]

    filtered_chunk.to_csv("stolen_vehicles.csv", mode="a", index=False, header=False)

    chunk_count += 1

    print(f"{chunk} processed")

print(f"All data processed through {chunk_count} chunks")
