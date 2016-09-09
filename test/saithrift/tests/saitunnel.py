<<<<<<< HEAD
# (C) Copyright @ 2016 Broadcom.  All Rights Reserved.  The term Broadcom refers to Broadcom Limited and/or its subsidiaries.
=======
# (C) Copyright © 2016 Broadcom.  All Rights Reserved.  The term “Broadcom” refers to Broadcom Limited and/or its subsidiaries.
>>>>>>> 1709aebeca3f62978b0928e4833baa576e2f3d40
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Thrift SAI interface Tunnel tests
"""
import socket

from switch import *

import sai_base_test

<<<<<<< HEAD
@group("tunnel")
@disabled
class TunnelEncapsulation(sai_base_test.ThriftInterfaceDataPlane):
=======

@group("group_1")
@disabled
class encapsulation(sai_base_test.ThriftInterfaceDataPlane):
>>>>>>> 1709aebeca3f62978b0928e4833baa576e2f3d40
    '''
    performs the encapsulation 
    we send normal ip packet on port2 and we expected to receive encapsulated packet on port 1
    Tunnel source is 2.2.2.2
    Tunnel Dest is 10.10.1.1
    -----------------------------------------------------------------
    Ingress side[port2]           |          Egress side[port1]
    ------------------------------------------------------------------
    ip's falls in 20.20.1.0       |        ip's falls in 10.10.1.0
    ------------------------------------------------------------------
    '''
    def runTest(self):
        print
        switch_init(self.client)
        time.sleep(10)
<<<<<<< HEAD
        port1=port_list[0] #From where we expect encapsulated packet 
        port2=port_list[1] #From where we send normal ip packet
=======
        port1=port_list[11] #From where we expect encapsulated packet 
        port2=port_list[13] #From where we send normal ip packet
>>>>>>> 1709aebeca3f62978b0928e4833baa576e2f3d40
        mac1 = '00:05:06:00:00:00' # port1 l2 entry
        mac2 = '00:05:06:00:00:02' 
        vr_mac='00:00:08:08:08:08'
        mac_action=1                
        vlan_id=0            #expecting to use unused vlans
        addr_family=0 #1 for v6
        tunnel_src_ip_addr='2.2.2.2' #src for outer ip
        encap_ip_addr='10.10.1.1'    #egress enighbhor
        ingress_ip_addr='20.20.1.1'  #ingress neighbor 
        tunnel_ip_addr='1.1.1.0'     #to reach tunnel nhop
        tunnel_ip_mask='255.255.255.0'
        ingress_nhop_ip_addr='20.20.1.1'
        egress_nhop_ip_addr='10.10.1.1'
        nhop_ip_addr_ingress='20.20.1.0'
        nhop_ip_mask_ingress='255.255.255.0'
        nhop_ip_addr_encap='10.10.1.0'
        nhop_ip_mask_encap='255.255.255.0'
        initiator_ip_addr='10.10.1.1'  #tunnel dest ip(outer header)
        neighbor_mac_ingress='00:05:06:00:00:02'
        neighbor_mac_encap='00:05:06:00:00:00' #egress side
        ip_addr_decap_src='10.10.1.1'
        ip_addr_decap_dst='2.2.2.2'
        
        ########################################################################
        # FDB Operations
        #########################################################################
        sai_thrift_create_fdb(self.client, vlan_id, mac1, port1, mac_action)
        sai_thrift_create_fdb(self.client, vlan_id, mac2, port2, mac_action)
        
<<<<<<< HEAD
               
        ########################################################################
        #Virtual router created with Mac = 00:00:08:08:08:08
        #######################################################################
        vr_id=sai_thrift_create_virtual_router(self.client,1,1,vr_mac)
            
=======
		
        ########################################################################
        #  Virtual router created with Mac = 00:00:08:08:08:08
        #######################################################################
        vr_id=sai_thrift_create_virtual_router(self.client,vr_mac,1,1)
		
>>>>>>> 1709aebeca3f62978b0928e4833baa576e2f3d40
        #creating a underlay interface in loopback
        underlay_if = sai_thrift_create_router_interface(self.client,is_port=1,port_id=0,vr_id=vr_id,vlan_id=vlan_id,v4_enabled=1,v6_enabled=1,is_lb=1, mac='')
        #creating an overlay interface in loopback
        overlay_if = sai_thrift_create_router_interface(self.client,is_port=1,port_id=0,vr_id=vr_id,vlan_id=vlan_id,v4_enabled=1,v6_enabled=1,is_lb=1,mac='')
        #creating a tunnel
        tunnel_id=sai_thrift_create_tunnel(self.client,addr_family=addr_family,ip_addr=tunnel_src_ip_addr,underlay_if=underlay_if,overlay_if=overlay_if)
<<<<<<< HEAD
      
=======
	   
>>>>>>> 1709aebeca3f62978b0928e4833baa576e2f3d40
        ##############################################################################
        #  Egress configurations
        #  create router interface,
        #  create neighbor
        #  create nhop
        #  create route
        #   
        ##############################################################################
<<<<<<< HEAD
       
=======
	   
>>>>>>> 1709aebeca3f62978b0928e4833baa576e2f3d40
        #encap router interface
        encap_if_id=sai_thrift_create_router_interface(self.client,vr_id=vr_id,is_port=1,port_id=port1,vlan_id=vlan_id,v4_enabled = 1,v6_enabled = 1,is_lb=0,mac='')
        #egress(encap side) neighbor (ip=10.10.1.1 , mac=00:05:06:00:00:00 )
        sai_thrift_create_neighbor(self.client,addr_family=addr_family,rif_id=encap_if_id,ip_addr=encap_ip_addr,dmac=neighbor_mac_encap)
        #egress(encap) nhop and route create
        egress_nhop=sai_thrift_create_nhop(self.client,addr_family=addr_family,is_tunnel=0,ip_addr=egress_nhop_ip_addr,rif_id=encap_if_id)
        sai_thrift_create_route(self.client,vr_id=vr_id,addr_family=addr_family,ip_addr=nhop_ip_addr_encap,ip_mask=nhop_ip_mask_encap,nhop=egress_nhop)
<<<<<<< HEAD
        
=======
		
>>>>>>> 1709aebeca3f62978b0928e4833baa576e2f3d40
        ###############################################################################
        #  Ingress configurations
        #  create router interface,
        #  create neighbor
        #  create nhop
        #  create route
        #   
        ##############################################################################
<<<<<<< HEAD
         
=======
		
>>>>>>> 1709aebeca3f62978b0928e4833baa576e2f3d40
        #ingress router interface
        ingress_if_id=sai_thrift_create_router_interface(self.client,vr_id=vr_id,is_port=1,port_id=port2,vlan_id=vlan_id,v4_enabled=1,v6_enabled = 1,is_lb=0,mac='')
        #ingress neighbor neighbor (ip=20.20.1.1 , mac = 00:05:06:00:00:02)
        sai_thrift_create_neighbor(self.client,addr_family=addr_family,rif_id=ingress_if_id,ip_addr=ingress_ip_addr,dmac=neighbor_mac_ingress)
        #ingress nhop and route create
        ingress_nhop=sai_thrift_create_nhop(self.client,addr_family=addr_family,is_tunnel=0,ip_addr=ingress_nhop_ip_addr,rif_id=ingress_if_id)
        sai_thrift_create_route(self.client,vr_id=vr_id,addr_family=addr_family,ip_addr=nhop_ip_addr_ingress,ip_mask=nhop_ip_mask_ingress,nhop=ingress_nhop)

        
        #adding tunnel and route
        initiator_id=sai_thrift_create_nhop(self.client,addr_family=addr_family,is_tunnel=1,ip_addr=initiator_ip_addr,rif_id=tunnel_id)
        sai_thrift_create_route(self.client,vr_id=vr_id,addr_family=addr_family,ip_addr=tunnel_ip_addr,ip_mask=tunnel_ip_mask,nhop=initiator_id)
        

<<<<<<< HEAD
=======


>>>>>>> 1709aebeca3f62978b0928e4833baa576e2f3d40
        pkt = simple_tcp_packet(eth_dst='00:00:08:08:08:08',
                                eth_src='00:00:00:00:00:01',
                                ip_src='20.20.1.2',
                                ip_dst='1.1.1.1',
                                ip_id=1,
                                ip_ttl=64)

        inner_hdr = simple_tcp_packet(eth_dst='00:00:08:08:08:08',
<<<<<<< HEAD
                                eth_src='00:00:00:00:00:01',
=======
                                eth_src='00:00:00:00:00:11',
>>>>>>> 1709aebeca3f62978b0928e4833baa576e2f3d40
                                ip_src='20.20.1.2',
                                ip_dst='1.1.1.1',
                                ip_id=1,
                                ip_ttl=63)
        exp_pkt = simple_ipv4ip_packet(eth_dst='00:05:06:00:00:00',
                                eth_src='00:00:08:08:08:08',
                                ip_dst='10.10.1.1',
                                ip_src='2.2.2.2',
<<<<<<< HEAD
                                ip_id=0,#mask the indentifier during check because it differs evry time.better chech with wireshark
=======
                                ip_id=0,#mask the indentifier during check
>>>>>>> 1709aebeca3f62978b0928e4833baa576e2f3d40
                                ip_ttl=64,
                                inner_frame=inner_hdr['IP']
                                )
        
        m=Mask(exp_pkt)
        m.set_do_not_care_scapy(IP , 'id')
<<<<<<< HEAD
        
        try:
            # in tuple: 0 is device number, 2 is port number
            # this tuple uniquely identifies a port
            send_packet(self, 2, pkt)
            #verify_packets(self,exp_pkt,ports=[1])
            verify_packets(self,str(m),[1])

        
=======
        try:
            # in tuple: 0 is device number, 2 is port number
            # this tuple uniquely identifies a port
            send_packet(self, 1, pkt)
            #verify_packets(self,exp_pkt,ports=[1])
            verify_packets(self,str(m),[2])


>>>>>>> 1709aebeca3f62978b0928e4833baa576e2f3d40
        finally:
            sai_thrift_remove_route(self.client,vr_id,addr_family,tunnel_ip_addr,tunnel_ip_mask,initiator_id) 
            self.client.sai_thrift_remove_next_hop(initiator_id)

            sai_thrift_remove_route(self.client,vr_id,addr_family,nhop_ip_addr_encap,nhop_ip_mask_encap,egress_nhop) 
            self.client.sai_thrift_remove_next_hop(egress_nhop)

            sai_thrift_remove_route(self.client,vr_id,addr_family,nhop_ip_addr_ingress,nhop_ip_mask_ingress,ingress_nhop) 
            self.client.sai_thrift_remove_next_hop(ingress_nhop)

            sai_thrift_remove_neighbor(self.client,addr_family,rif_id=ingress_if_id,ip_addr=ingress_ip_addr,dmac=neighbor_mac_ingress)
            
            sai_thrift_remove_neighbor(self.client,addr_family,rif_id=encap_if_id,ip_addr=encap_ip_addr,dmac=neighbor_mac_encap)
            self.client.sai_thrift_remove_router_interface(ingress_if_id)

            self.client.sai_thrift_remove_router_interface(encap_if_id)

            self.client.sai_thrift_remove_tunnel(tunnel_id)


<<<<<<< HEAD
@group("tunnel")
=======
@group("group_2")
@disabled
>>>>>>> 1709aebeca3f62978b0928e4833baa576e2f3d40
class decapsulation(sai_base_test.ThriftInterfaceDataPlane):
    '''
    performs the decapsulation 
    Tunnel table source is 10.10.1.1
    Tunnel table Dest is 2.2.2.2
<<<<<<< HEAD
    
=======
	
>>>>>>> 1709aebeca3f62978b0928e4833baa576e2f3d40
    We will send encapsulated packet from port1 and expects a decapsulated packet on port2
    -----------------------------------------------------------------
    Egress side[port2]           |          ingress side[port1]
    ------------------------------------------------------------------
    ip's falls in 20.20.1.0       |        ip's falls in 10.10.1.0
    ------------------------------------------------------------------
    '''
    def runTest(self):
        print
<<<<<<< HEAD
        switch_init(self.client)
        time.sleep(10)
        port1=port_list[0] #From where we send encapsulated packet 
        port2=port_list[1] #From where we see normal ip packet
        mac1 = '00:05:06:00:00:00' # port1 l2 entry
        mac2 = '00:05:06:00:00:02' 
=======
        global value_oid;
        switch_init(self.client)
        time.sleep(10)
        port1=port_list[11] #From where we send encapsulated packet 
        port2=port_list[13] #From where we see normal ip packet
        mac1 = '00:05:06:00:00:00' # port1 l2 entry
        mac2 = '00:05:06:00:00:02' 
	    
>>>>>>> 1709aebeca3f62978b0928e4833baa576e2f3d40
        mac_action=1                
        vlan_id=0            #expecting to use unused vlans
        addr_family=0 #1 for v6
        tunnel_src_ip_addr='2.2.2.2'   #src for outer ip for encapsulation
        ingress_ip_addr='10.10.1.1'    #ingress enighbhor
        egress_ip_addr='20.20.1.1'     #egress neighbor 
        tunnel_ip_addr='1.1.1.0'       #to reach tunnel nhop
        tunnel_ip_mask='255.255.255.0'
        egress_nhop_ip_addr='20.20.1.1'
        ingress_nhop_ip_addr='10.10.1.1'
        nhop_ip_addr_egress='20.20.1.0' #for route
        nhop_ip_mask_egress='255.255.255.0'
        nhop_ip_addr_ingress='10.10.1.0' #for route
        nhop_ip_mask_ingress='255.255.255.0'
        initiator_ip_addr='10.10.1.1'  #tunnel dest ip(outer header)
        neighbor_mac_egress='00:05:06:00:00:02'
        neighbor_mac_ingress='00:05:06:00:00:00' #egress side
        ip_addr_decap_src='10.10.1.1' #tunnel table decap src to macth
        ip_addr_decap_dst='2.2.2.2'   #tunnel table decap dest to match
         
        ######################################################################################
        #Create FDBs
        ######################################################################################  		
  
        sai_thrift_create_fdb(self.client, vlan_id, mac1, port1, mac_action)
        sai_thrift_create_fdb(self.client, vlan_id, mac2, port2, mac_action)
        vr_id=0 #using default vr id
<<<<<<< HEAD
                
=======
	    
>>>>>>> 1709aebeca3f62978b0928e4833baa576e2f3d40
        #creating a underlay interface in loopback
        underlay_if = sai_thrift_create_router_interface(self.client,is_port=1,port_id=0,vr_id=vr_id,vlan_id=vlan_id,v4_enabled=1,v6_enabled=1,is_lb=1, mac='')
        
        #creating an overlay interface in loopback
        overlay_if = sai_thrift_create_router_interface(self.client,is_port=1,port_id=0,vr_id=vr_id,vlan_id=vlan_id,v4_enabled=1,v6_enabled=1,is_lb=1,mac='')
<<<<<<< HEAD
        
        #creating a tunnel
        tunnel_id=sai_thrift_create_tunnel(self.client,addr_family=addr_family,ip_addr=tunnel_src_ip_addr,underlay_if=underlay_if,overlay_if=overlay_if)
            
=======
     	
        #creating a tunnel
        tunnel_id=sai_thrift_create_tunnel(self.client,addr_family=addr_family,ip_addr=tunnel_src_ip_addr,underlay_if=underlay_if,overlay_if=overlay_if)
	     
>>>>>>> 1709aebeca3f62978b0928e4833baa576e2f3d40
        ###############################################################################
        #  Ingress configurations
        #  create router interface,
        #  create neighbor
        #  create nhop
        #  create route
        #   
        ############################################################################## 
<<<<<<< HEAD

=======
		
>>>>>>> 1709aebeca3f62978b0928e4833baa576e2f3d40
        #ingress router interface
        ingress_if_id=sai_thrift_create_router_interface(self.client,vr_id=vr_id,is_port=1,port_id=port1,vlan_id=vlan_id,v4_enabled = 1,v6_enabled = 1,is_lb=0,mac='')
        #ingress neighbor (ip=10.10.1.1 , mac=00:05:06:00:00:00 )
        sai_thrift_create_neighbor(self.client,addr_family=addr_family,rif_id=ingress_if_id,ip_addr=ingress_ip_addr,dmac=neighbor_mac_ingress)
        #ingress(encap) nhop and route create
        ingress_nhop=sai_thrift_create_nhop(self.client,addr_family=addr_family,is_tunnel=0,ip_addr=ingress_nhop_ip_addr,rif_id=ingress_if_id)
        sai_thrift_create_route(self.client,vr_id=vr_id,addr_family=addr_family,ip_addr=nhop_ip_addr_ingress,ip_mask=nhop_ip_mask_ingress,nhop=ingress_nhop)
<<<<<<< HEAD
        
=======
	   
>>>>>>> 1709aebeca3f62978b0928e4833baa576e2f3d40
        ###############################################################################
        #  Ingress configurations
        #  create router interface,
        #  create neighbor
        #  create nhop
        #  create route
        #   
        ############################################################################## 
<<<<<<< HEAD
            
=======
        	
>>>>>>> 1709aebeca3f62978b0928e4833baa576e2f3d40
        #egress router interface
        egress_if_id=sai_thrift_create_router_interface(self.client,vr_id=vr_id,is_port=1,port_id=port2,vlan_id=vlan_id,v4_enabled=1,v6_enabled = 1,is_lb=0,mac='')
        #egress neighbor (ip=20.20.1.1 , mac = 00:05:06:00:00:02)
        sai_thrift_create_neighbor(self.client,addr_family=addr_family,rif_id=egress_if_id,ip_addr=egress_ip_addr,dmac=neighbor_mac_egress)
        #egress nhop and route create
        egress_nhop=sai_thrift_create_nhop(self.client,addr_family=addr_family,is_tunnel=0,ip_addr=egress_nhop_ip_addr,rif_id=egress_if_id)
        sai_thrift_create_route(self.client,vr_id=vr_id,addr_family=addr_family,ip_addr=nhop_ip_addr_egress,ip_mask=nhop_ip_mask_egress,nhop=egress_nhop)
        #adding tunnel and route
        initiator_id=sai_thrift_create_nhop(self.client,addr_family=addr_family,is_tunnel=1,ip_addr=initiator_ip_addr,rif_id=tunnel_id)
        sai_thrift_create_route(self.client,vr_id=vr_id,addr_family=addr_family,ip_addr=tunnel_ip_addr,ip_mask=tunnel_ip_mask,nhop=initiator_id)
<<<<<<< HEAD
            
=======
        
        
		
>>>>>>> 1709aebeca3f62978b0928e4833baa576e2f3d40
        ###################################################################################
        #Creating a Tunnel Table entry with
        #Source match 10.10.1.10
        #Dest match 2.2.2.2
        #
        #####################################################################################
        
        #create tunnel table entry for incoming match 		
<<<<<<< HEAD
        tunnel_entry_id=sai_thrift_create_tunnel_term_table(self.client,addr_family=addr_family,vr_id=vr_id,ip_addr_dst=ip_addr_decap_dst,ip_addr_src=ip_addr_decap_src,tunnel_oid=tunnel_id)
        
            
        exp_pkt = simple_tcp_packet(eth_src='00:77:66:55:44:00',
=======
        tunnel_entry_id=sai_thrift_create_tunnel_table(self.client,addr_family=addr_family,vr_id=vr_id,ip_addr_dst=ip_addr_decap_dst,ip_addr_src=ip_addr_decap_src,tunnel_oid=tunnel_id)
        
		
        exp_pkt = simple_tcp_packet(eth_src='00:77:66:55:44:33',
>>>>>>> 1709aebeca3f62978b0928e4833baa576e2f3d40
                                eth_dst='00:05:06:00:00:02',
                                ip_dst='20.20.1.2',
                                ip_src='1.1.1.1',
                                ip_id=108,
                                ip_ttl=63)

        inner_hdr = simple_tcp_packet(eth_dst='00:00:08:08:08:08',
                                eth_src='00:00:00:00:00:11',
                                ip_dst='20.20.1.2',
                                ip_src='1.1.1.1',
                                ip_id=108,
                                ip_ttl=63)
<<<<<<< HEAD
        pkt = simple_ipv4ip_packet(eth_dst='00:77:66:55:44:00',
=======
        pkt = simple_ipv4ip_packet(eth_dst='00:77:66:55:44:33',
>>>>>>> 1709aebeca3f62978b0928e4833baa576e2f3d40
                                eth_src='00:00:08:08:08:08',
                                ip_src='10.10.1.1',
                                ip_dst='2.2.2.2',
                                ip_id=50,
                                ip_ttl=64,
                                inner_frame=inner_hdr['IP'])
        
        #send_packet(self, 2, pkt)
        try:
            # in tuple: 0 is device number, 2 is port number
            # this tuple uniquely identifies a port
<<<<<<< HEAD
            send_packet(self, 1, pkt)
            #verify_packets(self,exp_pkt,ports=[1])
            verify_packets(self,exp_pkt,[2])


        finally:
            self.client.sai_thrift_remove_tunnel_term_table_entry(tunnel_entry_id)
=======
            send_packet(self, 2, pkt)
            #verify_packets(self,exp_pkt,ports=[1])
            verify_packets(self,exp_pkt,[1])


        finally:
            self.client.sai_thrift_remove_tunnel_table_entry(tunnel_entry_id)
>>>>>>> 1709aebeca3f62978b0928e4833baa576e2f3d40
            sai_thrift_remove_route(self.client,vr_id,addr_family,tunnel_ip_addr,tunnel_ip_mask,initiator_id) 
            self.client.sai_thrift_remove_next_hop(initiator_id)

            sai_thrift_remove_route(self.client,vr_id,addr_family,nhop_ip_addr_ingress,nhop_ip_mask_ingress,ingress_nhop) 
            self.client.sai_thrift_remove_next_hop(ingress_nhop)

            sai_thrift_remove_route(self.client,vr_id,addr_family,nhop_ip_addr_egress,nhop_ip_mask_egress,egress_nhop) 
            self.client.sai_thrift_remove_next_hop(egress_nhop)

            sai_thrift_remove_neighbor(self.client,addr_family,rif_id=egress_if_id,ip_addr=egress_ip_addr,dmac=neighbor_mac_egress)
            
            sai_thrift_remove_neighbor(self.client,addr_family,rif_id=ingress_if_id,ip_addr=ingress_ip_addr,dmac=neighbor_mac_ingress)
            self.client.sai_thrift_remove_router_interface(egress_if_id)

            self.client.sai_thrift_remove_router_interface(ingress_if_id)

            self.client.sai_thrift_remove_tunnel(tunnel_id)