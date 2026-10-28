import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Navbar from '../components/Navbar';
import api from '../services/api';

function PreviousScores() {
  const [attempts, setAttempts] = useState([]);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (!token) {
      navigate('/login');
      return;
    }
    api.get('attempts/').then(res => {
      setAttempts(res.data);
      setLoading(false);
    }).catch(err => {
      console.error(err);
      setLoading(false);
    });
  }, [navigate]);

  if (loading) return <><Navbar /><div style={{ minHeight: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center', background: '#ffffff' }}><div style={{ background: 'white', padding: '2rem 3rem', border: '2px solid #556b2f' }}>Loading...</div></div></>;

  return (
    <>
      <Navbar />
      <div style={{ minHeight: '100vh', background: '#ffffff', padding: '1.5rem 1rem' }}>
        <div style={{ maxWidth: '800px', margin: '0 auto' }}>
          <header style={{ background: '#ffffff', border: '2px solid #556b2f', padding: '1rem 1.25rem', marginBottom: '1.25rem', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '0.75rem' }}>
            <h1 style={{ fontSize: '1.5rem', fontWeight: '700', color: '#556b2f' }}>My Previous Scores</h1>
            <button onClick={() => navigate('/rounds')}>Back to Rounds</button>
          </header>

          {attempts.length === 0 ? (
            <div style={{ background: '#ffffff', border: '2px solid #556b2f', padding: '2rem', textAlign: 'center' }}>
              <p style={{ color: '#556b2f' }}>No attempts yet.</p>
              <button onClick={() => navigate('/rounds')} style={{ marginTop: '0.75rem' }}>Start a Round</button>
            </div>
          ) : (
            <div style={{ background: '#ffffff', border: '2px solid #556b2f', overflowX: 'auto' }}>
              <table style={{ width: '100%', borderCollapse: 'collapse' }}>
                <thead>
                  <tr style={{ background: '#f0f8e8' }}>
                    <th style={{ padding: '0.75rem', textAlign: 'left', border: '1px solid #556b2f', color: '#556b2f' }}>Round</th>
                    <th style={{ padding: '0.75rem', textAlign: 'center', border: '1px solid #556b2f', color: '#556b2f' }}>Score</th>
                    <th style={{ padding: '0.75rem', textAlign: 'center', border: '1px solid #556b2f', color: '#556b2f' }}>Correct</th>
                    <th style={{ padding: '0.75rem', textAlign: 'center', border: '1px solid #556b2f', color: '#556b2f' }}>Incorrect</th>
                    <th style={{ padding: '0.75rem', textAlign: 'center', border: '1px solid #556b2f', color: '#556b2f' }}>Date</th>
                  </tr>
                </thead>
                <tbody>
                  {attempts.map(a => (
                    <tr key={a.id}>
                      <td style={{ padding: '0.6rem', border: '1px solid #556b2f', color: '#2d4a2b' }}>Round {a.round_number}</td>
                      <td style={{ padding: '0.6rem', textAlign: 'center', border: '1px solid #556b2f', fontWeight: '700', color: '#556b2f' }}>{a.score} / {a.total}</td>
                      <td style={{ padding: '0.6rem', textAlign: 'center', border: '1px solid #556b2f', color: '#556b2f' }}>{a.correct_answers}</td>
                      <td style={{ padding: '0.6rem', textAlign: 'center', border: '1px solid #556b2f', color: '#556b2f' }}>{a.incorrect_answers}</td>
                      <td style={{ padding: '0.6rem', textAlign: 'center', border: '1px solid #556b2f', color: '#556b2f' }}>{new Date(a.completed_at).toLocaleDateString()}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </div>
      </div>
    </>
  );
}

export default PreviousScores;
