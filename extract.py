import pandas as pd

print("Extract Data From Mysql")

data = {
    "id":[1,2,3],
    "name":["A","B","C"],
    "age":[10,20,30]
}

df = pd.DataFrame(data)
print(df)   