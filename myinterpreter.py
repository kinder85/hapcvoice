import paho.mqtt.client as mqtt




clientm = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
clientm.username_pw_set(username="test", password="test")
clientm.connect("HAIP",1883,60)



  


class Myinterpreter():
    
    def __init__(self):
        super().__init__()
        
        self.status = 1
    
    
    

   def interpret(self, data):
        
        
        clientm.loop_start()
        if data.find('eve') == 0 or data.find('euh') == 0 or data.find('aise') == 0:
            
            if data.find('eve') == 0:
                data2 = data[3:]
            elif data.find('aise') == 0:
                data2 = data[4:]
            elif data.find('euh') == 0:
                data2 = data[3:]
            #uncomment this if you want only 1 assistant
            
            #clientm.publish("haassist", data2)   

            # and delete or comment this part 
            if data2.find('allume') >= 0 or data2.find('démarre') >= 0 or data2.find('éteins') >= 0 or data2.find('arrête') >= 0 :
                clientm.publish("haassist", data2)
            else:
                clientm.publish("ollamaassist", data2)
                
                
        
