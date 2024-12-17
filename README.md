# ProductionReadyChatbot
For Software Project Group




# Instructions

To run the LLM, navigate to *./ProductionReadyChatbot* and run ```python llm.py``` in your terminal


To run the ChatBot Frontend, navigate to *./ProductionReadyChatbot/chat-frontend* and run ```npm start``` in your terminal. If the app doesn't open in browser immediately, navigate to *[http://localhost:3000/](http://localhost:3000/)*. If Axios is missing, navigate to *./ProductionReadyChatbot/chat-frontend* and run ```npm install axios``` 


To run the Terminal ChatBot, navigate to *./ProductionReadyChatbot* and run ```python ChatBot.py``` in your terminal


Of course due to the repo being public we cannot include the certification and key's used. They need to be created by the user.


Use command:


```openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes``` 


to create a key and certificate to use them with the HTTPS server.


Save the cert.pem and key.pem in *./chat-frontend* directory
