import { useParams, useLocation } from 'react-router-dom';
import { useState } from 'react';

function Sala() {
  const { salaId } = useParams();
  const location = useLocation();
  const { nickname } = location.state || {};

  const [mensagens, setMensagens] = useState([]);
  const [novaMensagem, setNovaMensagem] = useState('');

  const handleEnviarMensagem = (e) => {
    e.preventDefault();
    if (novaMensagem.trim() !== '') {
      // Temporariamente, só adiciona a mensagem localmente
      const mensagem = {
        id: Date.now(),
        texto: novaMensagem,
        autor: nickname,
      };
      setMensagens([...mensagens, mensagem]);
      setNovaMensagem('');
    }
  };

  if (!nickname) {
    return <p>Nickname não encontrado. Volte para a Home.</p>;
  }

  return (
    <div style={{ padding: '20px' }}>
      <h1>Chat da sala: {salaId}</h1>
      <p>Usuário: {nickname}</p>

      <div
        style={{
          border: '1px solid #ccc',
          padding: '10px',
          height: '400px',
          overflowY: 'scroll',
          marginTop: '20px',
          marginBottom: '20px'
        }}
      >
        {/* Área de mensagens */}
        {mensagens.map((msg) => (
          <div key={msg.id}>
            <strong>{msg.autor}: </strong>{msg.texto}
          </div>
        ))}
      </div>

      {/* form para envio de mensagem */}
      <form onSubmit={handleEnviarMensagem}>
        <input
          type="text"
          placeholder="Digite sua mensagem..."
          value={novaMensagem}
          onChange={(e) => setNovaMensagem(e.target.value)}
          style={{ width: '70%', padding: '10px', marginRight: '10px' }}
        />
        <button type="submit" style={{ padding: '10px 20px' }}>
          Enviar
        </button>
      </form>
    </div>
  );
}

export default Sala;
