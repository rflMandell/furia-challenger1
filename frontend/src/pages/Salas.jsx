import { useLocation, useNavigate } from "react-router-dom";

function Salas(){
    const location = useLocation();
    const navigate = useNavigate();
    const { nickname } = location.state || {};

    const salas = [
        { id: 'cs', nome: 'Counter Strike'},
        { id: 'geral', nome: 'Chat Geral' },
        { id: 'lol', nome: 'League of Legends'},
        { id: 'valorant', nome: 'Valorant'},
        { id: 'kingsleague', nome: "King's League"},
    ];

    const handleSalaClick = (salaId) => {
        navigate(`/sala/${salaId}`, { state: { nickname } });
    };

    return(
        <div>
            <h1>Salas de Chat</h1>
            {nickname ? (
                <>
                    <p>Ola, {nickname}! Escolha uma sala para entrar:</p>
                    <ul>
                        {salas.map((sala) => (
                            <li key={sala.id}>
                                <button onClick={() => handleSalaClick(sala.id)}>
                                    {sala.nome}
                                </button>
                            </li>
                        ))}
                    </ul>
                </>
            ) : (
                <p>Nickname nao encontrado. Volte para a home e tente novamente</p>
            )}
        </div>
    );
}

export default Salas;