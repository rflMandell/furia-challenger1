import { useEffect, useState } from 'react';
import { io } from 'socket.io-client';

function Home() {
  const [nickname, setNickname] = useState('');
  const [inputValue, setInputValue] = useState('');
  const [socket, setSocket] = useState(null);
  const [messages, setMessages] = useState([]);
  const [messageInput, setMessageInput] = useState('');

  const handleSubmitNickname = (e) => {
    e.preventDefault();
    if (inputValue.trim() !== '') {
      setNickname(inputValue.trim());
    }
  };

  const handleSendMessage = (e) => {
    e.preventDefault();
    if (messageInput.trim() !== '') {
      socket.emit('send_message', { message: messageInput }); // envia a mensagem pelo socket
      setMessageInput(''); // limpa o input depois de enviar
    }
  };

  useEffect(() => {
    if (nickname) {
      const newSocket = io('http://localhost:8000', {
        query: { nickname: nickname },
      });
      setSocket(newSocket);

      newSocket.on('receive_message', (data) => {
        setMessages((prevMessages) => [...prevMessages, data]);
      });

      return () => newSocket.close();
    }
  }, [nickname]);

  if (!nickname) {
    return (
      <div className="flex items-center justify-center min-h-screen bg-gray-100">
        <form onSubmit={handleSubmitNickname} className="bg-white p-6 rounded shadow-md">
          <h1 className="text-2xl font-bold mb-4">Escolha seu Nickname:</h1>
          <input
            type="text"
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            placeholder="Digite seu nome..."
            className="border border-gray-300 p-2 w-full mb-4 rounded"
          />
          <button
            type="submit"
            className="bg-blue-500 text-white p-2 w-full rounded hover:bg-blue-600"
          >
            Entrar no Chat
          </button>
        </form>
      </div>
    );
  }

  return (
    <div className="flex flex-col h-screen bg-gray-100">
      <div className="flex-1 overflow-y-auto p-4">
        {messages.map((msg, index) => (
          <div key={index} className="mb-2">
            <strong>{msg.sender}:</strong> {msg.message}
          </div>
        ))}
      </div>
      <form onSubmit={handleSendMessage} className="p-4 bg-white flex">
        <input
          type="text"
          value={messageInput}
          onChange={(e) => setMessageInput(e.target.value)}
          placeholder="Digite sua mensagem..."
          className="border border-gray-300 p-2 flex-1 mr-2 rounded"
        />
        <button
          type="submit"
          className="bg-blue-500 text-white p-2 rounded hover:bg-blue-600"
        >
          Enviar
        </button>
      </form>
    </div>
  );
}

export default Home;
