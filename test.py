import pymysql  

def dbconnect():
  conn = pymysql.connect (host='127.0.0.1', user = 'root', password= '12345678',db='test',charset='utf8')
  return conn


def search_data(conn):
  cur = conn.cursor()
  sql = 'SELECT * FROM test'
  cur.execute(sql)
  results = cur.fetchall()
  print(results)

def main():
    conn = dbconnect()
    print('연결완료')
    search_data(conn)
    conn.close()
    print('연결해제')


if __name__=="__main__":
  main()

