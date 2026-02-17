import React from 'react';

const Controls = ({ isActive, onToggle, onReset }) => {
    return (
        <div className="controls">
            <button className="btn-primary" onClick={onToggle}>
                {isActive ? 'Pause' : 'Start'}
            </button>
            <button className="btn-secondary" onClick={onReset}>
                Reset
            </button>
        </div>
    );
};

export default Controls;
