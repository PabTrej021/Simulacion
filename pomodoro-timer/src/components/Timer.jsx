import React from 'react';

const Timer = ({ timeLeft }) => {
    const formatTime = (time) => {
        const minutes = Math.floor(time / 60);
        const seconds = time % 60;
        return `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    };

    const progress = (timeLeft / (25 * 60)) * 100; // Simplified progress for now, needs dynamic max based on mode

    return (
        <div className="timer-display">
            <div className="time-text">{formatTime(timeLeft)}</div>
        </div>
    );
};

export default Timer;
