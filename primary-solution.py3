import socket

def get_open_ports(target, port_range):
  open_ports=[]
  for i in range(port_range[0], port_range[1]):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    if s.connect_ex((target,i)) ==0:
      print(f'port {i} is opened')
      open_ports.append(i)
    s.close()
  return open_ports
get_open_ports("www.freecodecamp.org", [75,85])
