import { Link, NavLink, useNavigate } from 'react-router-dom';

function Navbar() {
  const navigate = useNavigate();
  const token = localStorage.getItem('token');

  let user = null;
  try {
    user = JSON.parse(localStorage.getItem('user'));
  } catch {
    user = null;
  }

  if (!token) return null;

  const logout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    navigate('/login');
  };

  const linkClass = ({ isActive }) => `qm-nav-link${isActive ? ' active' : ''}`;

  return (
    <nav className="qm-nav">
      <div className="qm-nav-inner">
        <Link to="/rounds" className="qm-nav-brand">
          <span>🎯</span>
          <span>QuizMaster</span>
        </Link>

        <div className="qm-nav-links">
          <NavLink to="/rounds" className={linkClass}>Rounds</NavLink>
          <NavLink to="/scores" className={linkClass}>My Scores</NavLink>
          {user && <span className="qm-nav-user">Hi, {user.username}</span>}
          <button type="button" onClick={logout} className="qm-nav-logout">
            Logout
          </button>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
