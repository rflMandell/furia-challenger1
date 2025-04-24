import React, { useState, useEffect } from 'react';
import { getChats, sendMessage } from './api';

const ChatList = () => {
    const [chats, setChats] = useState([]);
    const [message, setMessage] = useState('');
    const [selectedChat, setSelectedChat] = useState(null);

    useEffect(() => {
        getChats().then((response) => {
            setChats(response.data);
        });
    }, []);

    const handleSendMessage = () => {
        if (message && selectedChat) {
            sendMessage(selectedChat, message).then(() => {
                setMessage('');
                // atualiza a lista de msg ou renderiza o chat apos enviar a msg
            });
        }
    };

    return (
        <div>
            <h2>Chats</h2>
            <div>
                {chats.map((chat) => (
                    <button key={chat.id} onClick={() => setSelectedChat(chat.id)}>
                        {chat.name}
                    </button>
                ))}
            </div>

            {selectedChat && (
                <div>
                    <h3>Chat {selectedChat}</h3>
                    <textarea
                        value={message}
                        onChange={(e) => setMessage(e.target.value)}
                        placeholder='Digite sua mensagem'
                    />
                    <button onClick={handleSendMessage}>enviar</button>
                </div>
            )}
        </div>
    );
};

export default ChatList;