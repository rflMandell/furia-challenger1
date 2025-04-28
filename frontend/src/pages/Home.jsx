import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function Home() {
  const [nickname, setNickname] = useState('');
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    if (nickname.trim() !== '') {
      // futuramente validar se o nick já existe.
      navigate('/salas', { state: { nickname } });
    }
  };

  return (
    <div>
      <h1>Bem-vindo!</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Digite seu nickname"
          value={nickname}
          onChange={(e) => setNickname(e.target.value)}
        />
        <button type="submit">Entrar</button>
      </form>
    </div>
  );
}