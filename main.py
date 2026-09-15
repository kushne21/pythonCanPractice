import can

def main():
    '''
    CAN bus simulation project — 
    Using python-can (or a cheap CAN shield with a Raspberry Pi/Arduino
      if you want hardware), simulate a simple ECU sending messages, 
      then write automated tests that validate message timing/content
        against expected behavior. This is the single highest-leverage 
        project for an automotive-specific SQE role since it touches 
        "hardware and software in-the-loop simulators" and CAN — most CS-only 
        candidates won't have this.
    '''

    #ECU send message
    #ECU: electronic control unit, communicate
    #CAN/LIN : serial communication protocols
    #CAN: Controller area network
        #high speed, robust, critical communication (1Mbit/s)
        #originally for automotive applications
        #several nodes can listen to a single bus
        #no central controller
    #LIN: local interconnect network
        #low speed (15 kbit/s)
        #for UI or comfort features
        #master / slave arrangement : 1 master per 15 slaves nodes
    with can.interface.Bus('test', interface='virtual') as bus:
        bus2 = can.interface.Bus('test', interface='virtual')
        #uses virtual CAN bus
        #bus1 = can.interface.Bus('test', interface='virtual')
        #can create a can message
        #arbitration id: unique message identifier for priority
            #  and simultaneous transmissions
        a_text = can.Message(arbitration_id=0xC0FFEE,is_extended_id=True,data="hey".encode('utf-8'))
        try:
            bus.send(a_text)
            print(f"message sent on {bus.channel_info}")
            
            #channel info
            msg2 = bus2.recv()
            #CAN COMMUNICATE WITH EACH OTHER BECAUSE THEY SHARE THE CHANNEL 'TEST'
            assert a_text.data == msg2.data
        except can.CanError:
            print("message not sent")
    #automate test to validate message timing / content 
    #see if it is expected behavior
    return

#can use a data lake to store a bunch of data
main()