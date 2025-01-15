import { useState } from 'react'
// import React from 'react';
import LoginForm from './components/LoginForm';
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import { BrowserRouter as Router, Route, Routes, useNavigate } from 'react-router-dom';
import './App.css'

const App: React.FC = () => {
  const navigate = useNavigate(); // 修正
  const handleLogin = (email: string, password: string) => {
    console.log('ログイン情報:', { email, password });
    // 本来はここでAPIリクエストなどを行います。
    alert(`メールアドレス：${email}\nパスワード：${password}`);
    navigate('/home'); // 修正
  };

  return (
    <>
    <div style={{ fontFamily: "'Arial', sans-serif", textAlign: 'center', marginTop: '50px' }}>
      <h1>React + TypeScript ログイン画面</h1>
      <LoginForm onLogin={handleLogin} />
    </div>
    <div>
      <a href="https://vite.dev" target="_blank">
        <img src={viteLogo} className="logo" alt="Vite logo" />
      </a>
      <a href="https://react.dev" target="_blank">
        <img src={reactLogo} className="logo react" alt="React logo" />
      </a>
    </div>
    </>
  );
};

export default App;



// function App() {
//   const [count, setCount] = useState(0)

//   return (
//     <>
//       <div>
//         <a href="https://vite.dev" target="_blank">
//           <img src={viteLogo} className="logo" alt="Vite logo" />
//         </a>
//         <a href="https://react.dev" target="_blank">
//           <img src={reactLogo} className="logo react" alt="React logo" />
//         </a>
//       </div>
//       <h1>Vite + React</h1>
//       <div className="card">
//         <button onClick={() => setCount((count) => count + 1)}>
//           count is {count}
//         </button>
//         <p>
//           Edit <code>src/App.tsx</code> and save to test HMR
//         </p>
//       </div>
//       <p className="read-the-docs">
//         Click on the Vite and React logos to learn more
//       </p>
//     </>
//   )
// }

// export default App
