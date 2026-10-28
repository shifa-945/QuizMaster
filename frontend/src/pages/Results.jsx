import { useLocation, useNavigate } from 'react-router-dom';
import { useEffect } from 'react';
import Navbar from '../components/Navbar';

function Results() {
  const location = useLocation();
  const navigate = useNavigate();
  const result = location.state;

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (!token) {
      navigate('/login');
    }
  }, [navigate]);

  if (!result) {
    return (
      <>
        <Navbar />
        <div style={{ minHeight: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center', background: '#ffffff' }}>
          <div style={{ background: 'white', padding: '2rem 3rem', border: '2px solid #556b2f', textAlign: 'center' }}>
            <h1 style={{ marginBottom: '1rem', color: '#556b2f' }}>No Result Found</h1>
            <button onClick={() => navigate('/rounds')}>Go to Rounds</button>
          </div>
        </div>
      </>
    );
  }

  return (
    <>
      <Navbar />
      <div style={{ minHeight: '100vh', background: '#ffffff', padding: '2rem 1rem', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        <div style={{ maxWidth: '450px', width: '100%' }}>
          <div style={{ background: '#ffffff', border: '2px solid #556b2f', padding: '2rem', textAlign: 'center' }}>
            <h1 style={{ fontSize: '1.75rem', fontWeight: '700', marginBottom: '0.5rem', color: '#556b2f' }}>Round {result.round_number} Completed</h1>

            {result.completed_all_rounds ? (
              <p style={{ color: '#6b8e23', fontWeight: '700', marginBottom: '1.5rem' }}>🎉 You completed all 10 rounds!</p>
            ) : (
              <p style={{ color: '#6b7280', marginBottom: '1.5rem' }}>Score 5/10 or higher to advance to the next round.</p>
            )}

            <div style={{ padding: '1.5rem', border: '2px solid #556b2f', background: '#f0f8e8', marginBottom: '1.5rem' }}>
              <div style={{ fontSize: '2.5rem', fontWeight: '700', color: '#556b2f', marginBottom: '0.25rem' }}>{result.score} / {result.total}</div>
              <div style={{ color: '#556b2f', fontWeight: '600' }}>Total Score</div>
            </div>

            <div style={{ display: 'flex', justifyContent: 'space-around', marginBottom: '1.5rem', padding: '1rem', border: '1px solid #556b2f' }}>
              <div>
                <div style={{ fontSize: '1.5rem', fontWeight: '700', color: '#556b2f' }}>{result.correct_answers}</div>
                <div style={{ color: '#556b2f', fontSize: '0.9rem' }}>Correct</div>
              </div>
              <div>
                <div style={{ fontSize: '1.5rem', fontWeight: '700', color: '#556b2f' }}>{result.incorrect_answers}</div>
                <div style={{ color: '#556b2f', fontSize: '0.9rem' }}>Incorrect</div>
              </div>
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
              {result.next_round && (
                <button onClick={() => navigate(`/round/${result.next_round}`)} style={{ width: '100%' }}>
                  Continue to Round {result.next_round} →
                </button>
              )}
              {!result.completed_all_rounds && (
                <button onClick={() => navigate(`/round/${result.round_number}`)} style={{ width: '100%' }}>
                  Try Round {result.round_number} Again
                </button>
              )}
              <button onClick={() => navigate('/rounds')} style={{ width: '100%' }}>All Rounds</button>
              <button onClick={() => navigate('/scores')} style={{ width: '100%' }}>View Previous Scores</button>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default Results;
