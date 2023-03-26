import paho.mqtt.client as mqtt
import time
import json

def on_log(client, userdata, level, buf):
    print("log: ",+buf)
    
def on_message(client, userdata,msg):
     m_decode = str(msg.payload.decode("utf-8","ignore"))
     m_json = json.loads(m_decode)
     print(m_json)
    
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK rc = ",str(rc)," flags = ",str(flags))
        
    else:
        print("Bad connection returned code : ",rc)
        
def on_disconnect(client, userdata, flags, rc=0):
    print("disconnected result code:" +str(rc))
    

 
broker_address='192.168.0.10'
client = mqtt.Client('lkjui',transport='websockets') #create new instance
client.on_connect = on_connect
#client.on_disconnect = on_disconnect
client.on_log = on_log
client.on_message = on_message

print("connecting to broker ",broker_address)
client.username_pw_set("mna","mna0845")
client.connect(broker_address,1901,150)#connect to broker
client.loop_start()
client.subscribe("adduser",1,True)
time.sleep(0.1)
client.loop_stop()
client.disconnect()
