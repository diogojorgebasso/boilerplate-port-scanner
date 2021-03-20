import socket
from common_ports import ports_and_services
print(ports_and_services)
def fancyList(arrayInput):
  for x in arrayInput:
    print(x,end=".")
def findService(port):
  for x in ports_and_services:
    if port ==x:
      return ports_and_services[x]
def get_open_ports(target, port_range, verbose=False):
  open_ports=[]
  if verbose:
    print(f"Open ports for {target} ({fancyList(open_ports)})")
    print("PORT     SERVICE")
  for i in range(port_range[0], port_range[1]):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    if s.connect_ex((target,i)) ==0:
      print(f'{i}    {findService(i)}')
      open_ports.append(i)
    s.close()
  return(open_ports)
