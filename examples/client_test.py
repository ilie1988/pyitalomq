import pyitalomq

def do_connected(lmq, conn):
    print("connected via", conn)
    return lmq.request(conn, "llarp.auth", "dq3j4dj99w6wi4t4yjnya8sxtqr1rojt8jgnn6467o6aoenm3o3o.italo")

def do_request(lmq):
    print('connect')
    conn = lmq.connect_remote("ipc:///tmp/lmq.sock")
    if conn:
        return do_connected(lmq, conn)

def main():
    lmq = pyitalomq.ItaloMQ()
    print("start")
    lmq.start()
    print(do_request(lmq))
    print("done")

if __name__ == '__main__':
    main()
