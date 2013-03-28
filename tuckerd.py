#!/usr/bin/env python

import SocketServer

class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        print "Prey at %s" % self.client_address[0]

        self.insults = []
        self.insults.append("")
        self.insults.append("\nfucking wrong shitehead, try again.\n")
        self.insults.append("\nstill fucking wrong shitehead, try again.\n")
        self.insults.append("\nFUCK ME. Wrong again, I am so fucking surprised, try again.\n")

        self.request.sendall("Come the fuck in, or fuck the fuck off.\n")

        self.request.sendall("fucking username: ")
        prey_username = self.request.recv(1024).strip()
        print "victim supplied: %s as username." % prey_username

        for i in range(4):
            if self.insults[i]:
                self.request.sendall(self.insults[i])
            self.request.sendall("fucking password: ")
            prey_password = self.preypassword1 = self.request.recv(1024).strip()
            print "victim supplied: %s as password." % prey_password

        # nope.jpg
        print "Administering a bollocking to %s" % self.client_address[0]
        self.request.sendall("\nYou have proven yourself to be as useful as a marzipan dildo.\nYou connect here again, you mincing fucking CUNT, and I will tear your fucking skin off, I will wear it to your mother's birthday party, and rub your nuts up and down her leg whilst whistling Bohemian fucking Rhapsody, right?\n\nNow get out of my fucking sight.\n")
        print


if __name__ == "__main__":
    HOST = raw_input("IP for Malcolm to listen on, use 0.0.0.0 for open access: ")
    PORT = 9999

    SocketServer.TCPServer.allow_reuse_address = True
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    print "Malcolm awaits his prey on %s:%s" % (HOST, PORT)

    # Keep running until we're killed with Ctrl-C
    server.serve_forever()
