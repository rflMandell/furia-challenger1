import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Salas from './pages/Salas';
import Sala from './pages/Sala';
import Chat from './Chat';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/salas" element={<Salas />} />
        <Route path="/salas/:salaId" element={<Sala />} />
        <div>
          <Chat />
        </div>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
