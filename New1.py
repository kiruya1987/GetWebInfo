import MySQLdb

conn= MySQLdb.connect(
        host='42.159.249.108',
        port = 53306,
        user='root',
        passwd='root',
        db ='BigDataSample',
        )
cur = conn.cursor()

sqli = "INSERT INTO TyreData VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
cur.execute(sqli, ('a','b',1.1, 10,70,15,'aaa','bbb',0))
cur.close()

conn.commit()
conn.close()