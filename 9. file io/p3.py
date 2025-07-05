def generateTables(n):
    table = "none"
    for i in range(1,11):
        table += f"{n} X {i} = {n*i}\n"


for i in range(2,11):
    with open(f"tables/table_of_{i}.txt", "w") as f:
        f.write(str(generateTables(i)))