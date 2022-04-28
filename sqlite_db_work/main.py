import sqlite3
import pandas as pd


con = sqlite3.connect("chinook.db")
cur = con.cursor()

sql ="""SELECT DISTINCT City, a2.Name
        FROM customers INNER JOIN invoices i
            JOIN invoice_items ii on i.InvoiceId = ii.InvoiceId
            JOIN tracks t on t.TrackId = ii.TrackId
            JOIN albums a on a.AlbumId = t.AlbumId
            JOIN artists a2 on a2.ArtistId = a.ArtistId
        ORDER BY City
    """

df = pd.read_sql(sql, con)

new_frame = df.groupby(['City']).agg({"Name": ', '.join})
print(new_frame)

