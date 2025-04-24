import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api/';
export const getChats = () => {
    return axios.get(`${API_URL}chat/`);
};

export const sendMessage = (chatId, content) => {
    return axios.post(`${API_URL}message/`, {
        chat: chatId,
        content: content,
    });
};