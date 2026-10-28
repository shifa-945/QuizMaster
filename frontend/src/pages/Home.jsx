import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import api from '../services/api';

function Home() {
  const [quizzes, setQuizzes] = useState([]);

  useEffect(() => {
    api.get('quizzes/').then(res => setQuizzes(res.data)).catch(console.error);
  }, []);

  return (
    <div style={{ padding: '2rem' }}>
      <h1>Quiz Master</h1>
      <Link to="/create">Create Quiz</Link>
      <h2>Available Quizzes</h2>
      <ul>
        {quizzes.map(q => (
          <li key={q.id}>
            <Link to={`/quiz/${q.id}`}>{q.title}</Link> - {q.question_count} questions
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Home;
