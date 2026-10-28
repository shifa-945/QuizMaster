import { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import api from '../services/api';

function TakeQuiz() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [quiz, setQuiz] = useState(null);
  const [answers, setAnswers] = useState({});

  useEffect(() => {
    api.get(`quizzes/${id}/`).then(res => setQuiz(res.data)).catch(console.error);
  }, [id]);

  const handleChange = (questionId, choiceId) => {
    setAnswers({ ...answers, [questionId]: choiceId });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await api.post(`quizzes/${id}/submit/`, { answers });
      alert(`Score: ${res.data.score} / ${res.data.total}`);
      navigate('/');
    } catch (err) {
      console.error(err);
    }
  };

  if (!quiz) return <div>Loading...</div>;

  return (
    <div style={{ padding: '2rem' }}>
      <h1>{quiz.title}</h1>
      <p>{quiz.description}</p>
      <form onSubmit={handleSubmit}>
        {quiz.questions.map((q, idx) => (
          <div key={q.id} style={{ marginBottom: '1rem' }}>
            <p>{idx + 1}. {q.text}</p>
            {q.choices.map(c => (
              <label key={c.id} style={{ display: 'block' }}>
                <input
                  type="radio"
                  name={`q${q.id}`}
                  value={c.id}
                  onChange={() => handleChange(q.id, c.id)}
                />
                {c.text}
              </label>
            ))}
          </div>
        ))}
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default TakeQuiz;
