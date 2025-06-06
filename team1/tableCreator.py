def tableCreator(columnName, information):
    table = []

    for row in information:
        table.append(dict(zip(columnName, row)))


    print("hei")
    print(table)
    return table
