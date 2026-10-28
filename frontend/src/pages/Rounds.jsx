import { useEffect, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import Navbar from '../components/Navbar';
import api from '../services/api';

function Rounds() {
  const [rounds, setRounds] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (!token) {
      navigate('/login');
      return;
    }
    api.get('rounds/').then(res => setRounds(res.data)).catch(console.error);
  }, [navigate]);

  return (
    <>
      <Navbar />
      <div style={{ minHeight: '100vh', padding: '2rem 1rem' }}>
        <div style={{ maxWidth: '1100px', margin: '0 auto' }}>
          <div style={{ background: 'white', borderRadius: '12px', boxShadow: '0 1px 3px rgba(0,0,0,0.1)', padding: '1.5rem 2rem', marginBottom: '2rem', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '1rem' }}>
            <div>
              <h1 style={{ fontSize: '1.875rem', fontWeight: '700', marginBottom: '0.25rem' }}>🎯 QuizMaster</h1>
              <p style={{ color: '#6b7280', fontSize: '0.9rem', margin: 0 }}>General Knowledge Quiz Platform</p>
            </div>
            <span style={{ padding: '0.4rem 0.85rem', background: '#f0f8e8', color: '#556b2f', borderRadius: '999px', fontSize: '0.85rem', fontWeight: '700' }}>
              10 Rounds • 10 Questions Each
            </span>
          </div>

          <div style={{ background: 'white', borderRadius: '12px', boxShadow: '0 1px 3px rgba(0,0,0,0.1)', padding: '1.5rem 2rem', marginBottom: '2rem' }}>
            <h2 style={{ fontSize: '1.5rem', fontWeight: '600', marginBottom: '0.5rem' }}>Available Rounds</h2>
            <p style={{ color: '#6b7280', margin: 0 }}>Select a round to start your quiz • Score 5/10 or higher to advance to the next round</p>
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(320px, 1fr))', gap: '1.5rem' }}>
            {rounds.map(r => (
              <div key={r.id} style={{ background: 'white', borderRadius: '12px', boxShadow: '0 1px 3px rgba(0,0,0,0.1)', overflow: 'hidden', transition: 'transform 0.2s, box-shadow 0.2s', border: '1px solid #e5e7eb' }}
                   onMouseEnter={(e) => { e.currentTarget.style.transform = 'translateY(-2px)'; e.currentTarget.style.boxShadow = '0 10px 15px -3px rgba(0,0,0,0.1), 0 4px 6px -4px rgba(0,0,0,0.1)'; }}
                   onMouseLeave={(e) => { e.currentTarget.style.transform = 'translateY(0)'; e.currentTarget.style.boxShadow = '0 1px 3px rgba(0,0,0,0.1)'; }}>
                <div style={{ padding: '1.5rem' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'start', marginBottom: '0.75rem' }}>
                    <h3 style={{ fontSize: '1.25rem', fontWeight: '600', color: '#111827' }}>Round {r.round_number}</h3>
                    <span style={{ padding: '0.25rem 0.75rem', background: '#eff6ff', color: '#2563eb', borderRadius: '6px', fontSize: '0.8rem', fontWeight: '600' }}>{r.question_count} Questions</span>
                  </div>
                  <h4 style={{ fontSize: '1.1rem', fontWeight: '600', color: '#1f2937', marginBottom: '0.5rem' }}>{r.title}</h4>
                  <p style={{ color: '#6b7280', fontSize: '0.9rem', marginBottom: '1rem', lineHeight: '1.5' }}>{r.description}</p>

                  {r.attempted ? (
                    <div style={{ paddingTop: '1rem', borderTop: '1px solid #f3f4f6' }}>
                      <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.75rem', padding: '0.75rem', background: '#f0fdf4', borderRadius: '8px' }}>
                        <span style={{ fontSize: '1.25rem' }}>✓</span>
                        <span style={{ color: '#059669', fontWeight: '600' }}>Completed • Score: {r.score}/10</span>
                      </div>
                      <Link to={`/round/${r.id}`} style={{ display: 'block' }}><button style={{ width: '100%' }}>Review / Retake Round</button></Link>
                    </div>
                  ) : (
                    <Link to={`/round/${r.id}`} style={{ display: 'block' }}><button style={{ width: '100%', padding: '0.75rem' }}>Start Round →</button></Link>
                  )}
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </>
  );
}

export default Rounds;
