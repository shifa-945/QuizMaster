import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Login from './pages/Login';
import Register from './pages/Register';
import Rounds from './pages/Rounds';
import TakeRound from './pages/TakeRound';
import Results from './pages/Results';
import PreviousScores from './pages/PreviousScores';
import './App.css';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Navigate to="/rounds" replace />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/rounds" element={<Rounds />} />
        <Route path="/round/:id" element={<TakeRound />} />
        <Route path="/results" element={<Results />} />
        <Route path="/scores" element={<PreviousScores />} />
      </Routes>
    </Router>
  );
}

export default App;


