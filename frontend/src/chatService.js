const connectWebSocket = (url) => {
    const socket = new WebSocket(url);

    socket.onopen = () => {
        console.log("Conexao WebSocket estabelecida");
    };

    socket.onmessage = (event) => {
        console.log("Mensagem recebida:", event.data);
    };

    socket.onclose = () => {
        console.log("conexao webscoket fechada");
    };

    socket.onerror = (error) => {
        console.error("Erro websocket:", error)
    };

    return socket
};

export default connectWebSocket;