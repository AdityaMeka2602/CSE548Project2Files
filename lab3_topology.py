from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink

setLogLevel('info')

net = Mininet(topo=None,build=False,ipBase='10.0.2.0/8',autoSetMacs=True)

info('***Adding two controllers namely {c1 and c2}:\n')
c1=net.addController('c1',controller=RemoteController,ip='127.0.0.1',protocol='tcp',port=6633)
c2=net.addController('c2',controller=RemoteController,ip='127.0.0.1',protocol='tcp',port=6655)

info('***Adding two switches s1 and s2:\n')
s1 = net.addSwitch('s1',cls=OVSKernelSwitch)
s2 = net.addSwitch('s2',cls=OVSKernelSwitch)

info('***Adding Hosts{h1,h2,h3,h4}:\n')
h1=net.addHost('h1',ip='10.0.2.10',mac='00:00:00:00:00:01',dimage="ubuntu:trusty")
h2=net.addHost('h2',ip='10.0.2.20',mac='00:00:00:00:00:02',dimage="ubuntu:trusty")
h3=net.addHost('h3',ip='192.168.2.30',mac='00:00:00:00:00:03',dimage="ubuntu:trusty")
h4=net.addHost('h4',ip='192.168.2.40',mac='00:00:00:00:00:04',dimage="ubuntu:trusty")

info('***creating Links\n')
net.addLink(h1,s1)
net.addLink(h1,s2,params1={'ip':'192.168.2.10/8'})
net.addLink(h2,s1)
net.addLink(h3,s2)
net.addLink(h4,s2)

info('***Starting network\n')
net.build()

info('***Starting Controller\n')
c1.start()
c2.start()

info('***Starting Switches\n')
s1.start([c1])
s2.start([c2])

info('***Running CLI\n')
CLI(net)

info('***Stopping network')
net.stop()