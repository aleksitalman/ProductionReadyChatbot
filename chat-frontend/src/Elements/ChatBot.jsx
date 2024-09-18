import React, { useState, useEffect, useRef } from "react";
import axios from "axios";
import "./ChatBot.css";


const Chat = () => {
    const [userInput, setUserInput] = useState("");
    const [chatLog, setChatLog] = useState([]);
    const [isChatting, setIsChatting] = useState(true);
    const chatboxRef = useRef(null);

    const handleInputChange = (e) => {
        setUserInput(e.target.value);
    };

    const send = async () => {
        if (userInput.trim() === "") return;

        if (userInput.toLowerCase() === "exit" || userInput.toLowerCase() === "quit") {
          setIsChatting(false);
          return;
        }
    
        const url = "http://127.0.0.1:8000/chat"; 
        const payload = { input: userInput };

        //save user input log
        setChatLog((prevLog) => [...prevLog, { type: "user", message: userInput }]);
    
        try {
            //send the request to server
            const response = await axios.post(url, payload);
        
            const endTime = performance.now();
            const timeTaken = response.data.time_taken;
        
            //fetch message from response
            const answer = response.data.response || "No response";
        
            //save chat bot asnwer log
            setChatLog((prevLog) => [
                ...prevLog,
                { type: "bot", message: answer, timeTaken },
              ]);
        
            setUserInput(""); //empty input field

            } catch (error) {
            console.error("Error sending request:", error);
            setChatLog((prevLog) => [
                ...prevLog,
                { type: "system", message: "Error: Failed to communicate with server" },
              ]);
      };
    };

    useEffect(() => {
        if (chatboxRef.current) {
          chatboxRef.current.scrollTop = chatboxRef.current.scrollHeight;
        }
      }, [chatLog]);  

      return (
        <div className="chat-container">
          <div className="chatbox" ref={chatboxRef}>
            <div className="message-container">
              {chatLog.map((chat, index) => (
                <div
                  key={index}
                  className={chat.type === "user" ? "user-message" : "bot-message"}
                >
                  {chat.message}
                  {chat.type === "bot" && chat.timeTaken && (
                    <p className="time-taken">Time taken: {chat.timeTaken} seconds</p>
                  )}
                </div>
              ))}
            </div>
          </div>
          {isChatting ? (
            <div className="input-container">
              <input
                type="text"
                value={userInput}
                onChange={handleInputChange}
                onKeyPress={(e) => {
                  if (e.key === "Enter") send();
                }}
                placeholder="Type your message..."
              />
              <button onClick={send}>Send</button>
            </div>
          ) : (
            <p>Goodbye!</p>
          )}
        </div>
    );  
}

export default Chat;