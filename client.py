import threading
import store

class Thread(threading.Thread):

    def __init__(self, connection, client_addr):
        threading.Thread.__init__(self)
        self.connection = connection
        (self.ip, self.port) = client_addr
        print(" -> new thread for %s %s" % (self.ip, self.port))

    def run(self): 
        print(" -> connection from %s %s" % (self.ip, self.port))
        while True:
            data = self.connection.recv(2048).rstrip()
            if data:
                args = data.split(' ')
                print ' -> execute: [%s]' % (', '.join(args))
                cmd = args[0].lower()
                if cmd == 'get':
                    res = store.Store.get(args[1])
                elif cmd == 'set':
                    res = store.Store.set(args[1], args[2])
                elif cmd == 'del':
                    res = store.Store.delete(args[1])
                elif cmd == 'lpush':
                    res = store.Store.lpush(args[1], args[2])
                elif cmd == 'rpush':
                    res = store.Store.rpush(args[1], args[2])
                elif cmd == 'lpop':
                    res = store.Store.lpop(args[1])
                elif cmd == 'rpop':
                    res = store.Store.rpop(args[1])
                elif cmd == 'llen':
                    res = store.Store.llen(args[1])
                elif cmd == 'exit':
                    res = "BYE"
                else:
                    print ' -> error: unknown command "%s"' % cmd
                    res = "ERROR"
                
                self.connection.sendall(res + "\n")
                
                if cmd == 'exit':
                    self.connection.close()
                    break
            else:
                print(" -> Do data received. Exiting...")
                self.connection.close()
                break
