import React, { useState, useEffect} from "react";
import connectWebSocket from "./chatService";

const Chat = () => {
    const [message, setMessage] = useState('');
    const [messages, setMessages] = useState([]);
    const [socket, setSocket] = useState(null);

    useEffect(() => {
        //conectando o websocket
        const ws = connectWebSocket('ws://localhost:8000/ws/chat/');
        setSocket(ws);

        //limpeza da conexao
        return () => {
            if (ws) {
                ws.close();
            }
        };
    }, []);

    const sendMessage = () => {
        if (socket && message){
            socket.send(message);
            setMessage('');
        }
    };

    return(
        <div>
            <div>
                <h2>Chat</h2>
                <div>
                    {messages.map((msg, index) => (
                        <p key={index}>{msg}</p>
                    ))}
                </div>
            </div>
            <input
                type="text"
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                placeholder="Digite sua mensagem..."
            />
            <button onClick={sendMessage}>Enviar</button>
        </div>
    );
};

export default Chat;