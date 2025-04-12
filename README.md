        instalation:
        clone this repo 
        dowload your model here ==> https://alphacephei.com/vosk/models  
        install python lib via pip:
            - vosk
            - souddevice
            - paho-mqtt
        put your downloaded model in the folder 'model' without subfolder

    usage:
     first run:
        run run.py
        speak your desired wakeword multiple time to see how it's interpreted (check python output) and take note of the output.
            exemple: when i say "eve" sometime the prog understand "euh" or "aise" so i need to add this 3 word as wakeword in myinterpreter.py

        edit myinterpreter.py with your wakeword 
        count the number of letter for each one, the prog will send to ha only the message after wakeword
            exemple:             

                """
                if data.find('eve') == 0 or data.find('euh') == 0 or data.find('aise') == 0:
            
                    if data.find('eve') == 0:               
                        data2 = data[3:]
                    elif data.find('aise') == 0:
                        data2 = data[4:]
                    elif data.find('euh') == 0:
                        data2 = data[3:]
                """
        edit myinterpreter.py to reflect your install ( mqtt broker ip,wakeword, mqtt topic ...)
        

        home assitant part:
            use an automation tha will redirect the question (mqtt) to assist with ollama ==>  "mqtttoollama.yaml"
            use an automation tha will redirect the question (mqtt) to assist without ollama ==>  "mqtttoassist.yaml"
            with this ypu don't need to expose entity to ollama.
            use an automation that will redirect the response to your media_player_entity_id ==>  "ollamaspeak.yaml"
            (don't forget to change the  media_player_entity_id)
            

           