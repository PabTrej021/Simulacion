import { useState, useEffect } from 'react';
import Timer from './components/Timer';
import Controls from './components/Controls';
import Settings from './components/Settings';
import TaskManager from './components/TaskManager';
import './index.css';

function App() {
  const [timeLeft, setTimeLeft] = useState(25 * 60);
  const [isActive, setIsActive] = useState(false);
  const [mode, setMode] = useState('work'); // 'work', 'short', 'long'

  // Timer Logic
  useEffect(() => {
    let interval = null;
    if (isActive && timeLeft > 0) {
      interval = setInterval(() => {
        setTimeLeft((timeLeft) => timeLeft - 1);
      }, 1000);
    } else if (timeLeft === 0) {
      setIsActive(false);
      // Optional: Play sound here
    }
    return () => clearInterval(interval);
  }, [isActive, timeLeft]);

  const toggleTimer = () => setIsActive(!isActive);
  const resetTimer = () => {
    setIsActive(false);
    if (mode === 'work') setTimeLeft(25 * 60);
    if (mode === 'short') setTimeLeft(5 * 60);
    if (mode === 'long') setTimeLeft(15 * 60);
  };

  const handleModeChange = (newMode) => {
    setMode(newMode);
    setIsActive(false);
    if (newMode === 'work') setTimeLeft(25 * 60);
    if (newMode === 'short') setTimeLeft(5 * 60);
    if (newMode === 'long') setTimeLeft(15 * 60);
  };

  return (
    <div className="app-container">
      <header>
        <h1>Pomodoro</h1>
      </header>
      <main>
        <div className="timer-card">
          <div className="mode-selector">
            <button
              className={mode === 'work' ? 'active' : ''}
              onClick={() => handleModeChange('work')}
            >Work</button>
            <button
              className={mode === 'short' ? 'active' : ''}
              onClick={() => handleModeChange('short')}
            >Short Break</button>
            <button
              className={mode === 'long' ? 'active' : ''}
              onClick={() => handleModeChange('long')}
            >Long Break</button>
          </div>

          <Timer timeLeft={timeLeft} />
          <Controls isActive={isActive} onToggle={toggleTimer} onReset={resetTimer} />
        </div>
        <TaskManager />
      </main>
    </div>
  );
}

export default App;
