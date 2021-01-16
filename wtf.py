# Return a list of Porn_hub Videos

Porn_Hub_Vids = ["youtube.com/phub"]


def Insert_Vids(table, url):

    table.insert(len(table) + 1, url)

    return table


Porn_Hub_Vids = Insert_Vids(Porn_Hub_Vids, "Porn.com")

print(Porn_Hub_Vids)
