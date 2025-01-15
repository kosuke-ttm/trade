import React from 'react';
import { useNavigate, useLocation } from 'react-router-dom';

const Login: React.FC = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const from = location.state?.from?.pathname || '/'; // リダイレクト先

  const handleLogin = () => {
    // ログイン処理（例: トークンを保存）
    localStorage.setItem('token', 'sample-token');

    // 元のページまたはデフォルトページへ遷移
    navigate(from, { replace: true });
  };

  return (
    <div>
      <h1>ログイン</h1>
      <button onClick={handleLogin}>ログインする</button>
    </div>
  );
};

export default Login;
