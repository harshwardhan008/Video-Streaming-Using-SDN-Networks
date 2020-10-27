#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    c0=net.addController(name='c0',
                      controller=Controller,
                      protocol='tcp',
                      port=6633)

    info( '*** Add switches\n')
    jaipur = net.addSwitch('jaipur', cls=OVSKernelSwitch, dpid='5')
    delhi = net.addSwitch('delhi', cls=OVSKernelSwitch, dpid='1')
    pune = net.addSwitch('pune', cls=OVSKernelSwitch, dpid='8')
    gorakhpur = net.addSwitch('gorakhpur', cls=OVSKernelSwitch, dpid='3')
    allahabad = net.addSwitch('allahabad', cls=OVSKernelSwitch, dpid='4')
    hyderabad = net.addSwitch('hyderabad', cls=OVSKernelSwitch, dpid='12')
    bengaluru = net.addSwitch('bengaluru', cls=OVSKernelSwitch, dpid='10')
    guwhati = net.addSwitch('guwhati', cls=OVSKernelSwitch, dpid='15')
    ahmedabad = net.addSwitch('ahmedabad', cls=OVSKernelSwitch, dpid='6')
    kolkata = net.addSwitch('kolkata', cls=OVSKernelSwitch, dpid='14')
    kanpur = net.addSwitch('kanpur', cls=OVSKernelSwitch, dpid='2')
    chennai = net.addSwitch('chennai', cls=OVSKernelSwitch, dpid='11')
    indore = net.addSwitch('indore', cls=OVSKernelSwitch, dpid='16')
    trivandrum = net.addSwitch('trivandrum', cls=OVSKernelSwitch, dpid='9')
    mumbai = net.addSwitch('mumbai', cls=OVSKernelSwitch, dpid='7')
    bhuv = net.addSwitch('bhuv', cls=OVSKernelSwitch, dpid='13')

    info( '*** Add hosts\n')
    h14 = net.addHost('h14', cls=Host, ip='10.0.0.14', defaultRoute=None)
    h10 = net.addHost('h10', cls=Host, ip='10.0.0.10', defaultRoute=None)
    h11 = net.addHost('h11', cls=Host, ip='10.0.0.11', defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='10.0.0.6', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='10.0.0.5', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h7 = net.addHost('h7', cls=Host, ip='10.0.0.7', defaultRoute=None)
    h15 = net.addHost('h15', cls=Host, ip='10.0.0.15', defaultRoute=None)
    h12 = net.addHost('h12', cls=Host, ip='10.0.0.12', defaultRoute=None)
    h9 = net.addHost('h9', cls=Host, ip='10.0.0.9', defaultRoute=None)
    h13 = net.addHost('h13', cls=Host, ip='10.0.0.13', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)
    h16 = net.addHost('h16', cls=Host, ip='10.0.0.16', defaultRoute=None)
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    h8 = net.addHost('h8', cls=Host, ip='10.0.0.8', defaultRoute=None)

    info( '*** Add links\n')
    net.addLink(delhi, kanpur)
    net.addLink(kanpur, gorakhpur)
    net.addLink(gorakhpur, allahabad)
    net.addLink(jaipur, kanpur)
    net.addLink(ahmedabad, jaipur)
    net.addLink(kanpur, bengaluru)
    net.addLink(mumbai, pune)
    net.addLink(pune, bengaluru)
    net.addLink(chennai, bengaluru)
    net.addLink(hyderabad, bengaluru)
    net.addLink(hyderabad, chennai)
    net.addLink(trivandrum, bengaluru)
    net.addLink(kolkata, guwhati)
    net.addLink(bhuv, kolkata)
    net.addLink(indore, mumbai)
    net.addLink(kanpur, mumbai)
    net.addLink(hyderabad, kolkata)
    net.addLink(delhi, h1)
    net.addLink(kanpur, h2)
    net.addLink(gorakhpur, h3)
    net.addLink(allahabad, h4)
    net.addLink(jaipur, h5)
    net.addLink(ahmedabad, h6)
    net.addLink(mumbai, h7)
    net.addLink(pune, h8)
    net.addLink(trivandrum, h9)
    net.addLink(bengaluru, h10)
    net.addLink(chennai, h11)
    net.addLink(hyderabad, h12)
    net.addLink(h13, bhuv)
    net.addLink(kolkata, h14)
    net.addLink(guwhati, h15)
    net.addLink(indore, h16)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('jaipur').start([c0])
    net.get('delhi').start([c0])
    net.get('pune').start([c0])
    net.get('gorakhpur').start([c0])
    net.get('allahabad').start([c0])
    net.get('hyderabad').start([c0])
    net.get('bengaluru').start([c0])
    net.get('guwhati').start([c0])
    net.get('ahmedabad').start([c0])
    net.get('kolkata').start([c0])
    net.get('kanpur').start([c0])
    net.get('chennai').start([c0])
    net.get('indore').start([c0])
    net.get('trivandrum').start([c0])
    net.get('mumbai').start([c0])
    net.get('bhuv').start([c0])

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

