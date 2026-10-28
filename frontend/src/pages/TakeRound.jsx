import { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import Navbar from '../components/Navbar';
import Dialog from '../components/Dialog';
import api from '../services/api';

function TakeRound() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [round, setRound] = useState(null);
  const [answers, setAnswers] = useState({});
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [loading, setLoading] = useState(true);
  const [dialog, setDialog] = useState(null);

  const closeDialog = () => {
    const action = dialog?.onConfirm;
    setDialog(null);
    if (action) action();
  };

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (!token) {
      navigate('/login');
      return;
    }
    api.get(`rounds/${id}/`).then(res => {
      setRound(res.data);
      setCurrentQuestion(0);
      setAnswers({});
      setLoading(false);
    }).catch(err => {
      console.error(err);
      setLoading(false);
    });
  }, [id, navigate]);

  const handleSelect = (questionId, choiceId) => {
    if (!round) return;
    setAnswers({ ...answers, [questionId]: choiceId });
  };

  const handlePrev = () => {
    if (currentQuestion > 0) {
      setCurrentQuestion(currentQuestion - 1);
    }
  };

  const handleMarkAndNext = () => {
    if (!round) return;
    const q = round.questions[currentQuestion];
    if (!answers[q.id]) {
      setDialog({
        variant: 'warning',
        title: 'Select an Answer',
        message: 'Please choose one of the options before continuing.',
      });
      return;
    }
    if (currentQuestion < round.questions.length - 1) {
      setCurrentQuestion(currentQuestion + 1);
    } else {
      handleSubmit();
    }
  };

  const handleSubmit = async () => {
    if (!round) return;
    if (Object.keys(answers).length < round.questions.length) {
      setDialog({
        variant: 'warning',
        title: 'Incomplete Quiz',
        message: 'Please answer all questions before submitting the round.',
      });
      return;
    }
    try {
      const res = await api.post(`rounds/${id}/submit/`, { answers });
      const score = res.data.score;
      const total = res.data.total;
      const currentRound = res.data.round_number;
      const passed = score >= 5;
      const nextRound = currentRound + 1;
      const completedAllRounds = passed && currentRound === 10;

      if (passed && currentRound < 10) {
        setDialog({
          variant: 'success',
          title: `Round ${currentRound} Cleared!`,
          message: `Congrats! You scored ${score}/${total}. You are selected for Round ${nextRound}.`,
          confirmLabel: `Continue to Round ${nextRound}`,
          onConfirm: () => navigate(`/round/${nextRound}`),
        });
        return;
      }

      const resultState = {
        score: res.data.score,
        total: res.data.total,
        correct_answers: res.data.correct_answers,
        incorrect_answers: res.data.incorrect_answers,
        round_number: res.data.round_number,
        completed_all_rounds: completedAllRounds,
        next_round: null,
      };

      if (completedAllRounds) {
        setDialog({
          variant: 'success',
          title: 'All 10 Rounds Completed!',
          message: 'Congratulations! You cleared the final round and completed the entire quiz.',
          confirmLabel: 'See Final Results',
          onConfirm: () => navigate('/results', { state: resultState }),
        });
        return;
      }

      setDialog({
        variant: 'warning',
        title: 'Round Not Cleared',
        message: `You scored ${score}/${total}. You need at least 5 correct answers to advance to the next round.`,
        confirmLabel: 'See Results',
        onConfirm: () => navigate('/results', { state: resultState }),
      });
    } catch (err) {
      console.error(err);
      setDialog({
        variant: 'danger',
        title: 'Submission Failed',
        message: 'We could not submit your quiz. Please check your connection and try again.',
        confirmLabel: 'Try Again',
      });
    }
  };

  if (loading) return <><Navbar /><div style={{ minHeight: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center', background: '#ffffff' }}><div style={{ background: 'white', padding: '2rem 3rem', border: '2px solid #556b2f' }}>Loading...</div></div></>;
  if (!round) return <><Navbar /><div style={{ minHeight: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center', flexDirection: 'column', gap: '1rem', background: '#ffffff' }}><h2 style={{ color: '#556b2f' }}>Round not found</h2><button onClick={() => navigate('/rounds')}>Go to Rounds</button></div></>;

  const question = round.questions[currentQuestion];
  const totalQuestions = round.questions.length;
  const progress = ((currentQuestion + 1) / totalQuestions) * 100;

  return (
    <>
      <Navbar />
      <div style={{ minHeight: '100vh', background: '#ffffff', padding: '1rem' }}>
      <div style={{ maxWidth: '800px', margin: '0 auto' }}>
        <header style={{ background: '#ffffff', border: '2px solid #556b2f', padding: '1rem 1.25rem', marginBottom: '1rem' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '0.75rem', marginBottom: '0.75rem' }}>
            <div>
              <h1 style={{ fontSize: '1.4rem', fontWeight: '700', color: '#556b2f' }}>Round {round.round_number} of 10</h1>
              <p style={{ color: '#556b2f', fontSize: '0.9rem', margin: 0 }}>{round.title} • Question {currentQuestion + 1} of {totalQuestions}</p>
            </div>
            <span style={{ padding: '0.3rem 0.75rem', background: '#f0f8e8', color: '#556b2f', borderRadius: '999px', fontSize: '0.8rem', fontWeight: '700' }}>
              Score 5/10 to advance
            </span>
          </div>
          <div style={{ height: '8px', background: '#e5ebd8', borderRadius: '999px', overflow: 'hidden' }}>
            <div style={{ height: '100%', width: `${progress}%`, background: '#6b8e23', transition: 'width 0.25s ease' }} />
          </div>
        </header>

        <div style={{ background: '#ffffff', border: '2px solid #556b2f', padding: '1.25rem', marginBottom: '1rem' }}>
          <div style={{ display: 'flex', alignItems: 'start', gap: '0.75rem', marginBottom: '1rem' }}>
            <div style={{ minWidth: '32px', height: '32px', background: '#6b8e23', color: 'white', display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: '700' }}>{currentQuestion + 1}</div>
            <h2 style={{ fontSize: '1.05rem', fontWeight: '600', lineHeight: '1.6', color: '#556b2f', flex: 1 }}>{question.text}</h2>
          </div>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
            {question.choices.map((choice, idx) => {
              const isSelected = answers[question.id] === choice.id;
              const label = choice.option_label || String.fromCharCode(65 + idx);
              return (
                <div
                  key={choice.id}
                  onClick={() => handleSelect(question.id, choice.id)}
                  style={{
                    padding: '0.7rem 1rem',
                    border: isSelected ? '2px solid #556b2f' : '1.5px solid #556b2f',
                    background: isSelected ? '#f0f8e8' : '#ffffff',
                    cursor: 'pointer',
                    display: 'flex',
                    alignItems: 'center',
                    gap: '0.75rem'
                  }}
                >
                  <span style={{ fontWeight: '700', color: '#556b2f', minWidth: '20px' }}>{label}.</span>
                  <span style={{ color: '#2d4a2b', fontSize: '0.95rem' }}>{choice.text}</span>
                </div>
              );
            })}
          </div>
        </div>

        <div style={{ background: '#ffffff', border: '2px solid #556b2f', padding: '0.75rem 1rem', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '0.5rem' }}>
          <button onClick={handlePrev} disabled={currentQuestion === 0}>Previous</button>
          <div style={{ color: '#556b2f', fontWeight: '600' }}>
            {currentQuestion + 1} / {totalQuestions}
          </div>
          <button onClick={handleMarkAndNext} disabled={!answers[question.id]}>
            {currentQuestion === totalQuestions - 1 ? 'Submit Round' : 'Next'}
          </button>
        </div>
      </div>
      </div>

      <Dialog
        open={Boolean(dialog)}
        variant={dialog?.variant}
        title={dialog?.title}
        message={dialog?.message}
        confirmLabel={dialog?.confirmLabel}
        onConfirm={closeDialog}
      />
    </>
  );
}

export default TakeRound;

