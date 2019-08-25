import schedule
import time
import sqlite3
from datetime import datetime

 
conn =sqlite3.connect('D:\sqllite_database\prac2.db')

def update():  
    today = datetime.today()
    cursor = conn.execute("Select * from bk_tbl")
    for row in cursor:
        startdate= datetime.strptime(row[5],'%Y-%m-%d %H:%M:%S')
        diff=abs(today-startdate).total_seconds()
        vsr=str(row[0])
        if diff/3600.0>12:
            statement= """
                update bk_tbl set status='Error' where fileid='%s'
            """ %vsr
            conn.execute(statement)
            conn.commit()
            print("Updated")
        print(vsr)

schedule.every(10).seconds.do(update)

# loops so that the scheduling task keeps on running
while True:
    #Checks whether a scheduled task is pending to run or not
    schedule.run_pending()
    time.sleep(1)