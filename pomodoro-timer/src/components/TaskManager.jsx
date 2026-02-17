import React, { useState } from 'react';

const TaskManager = () => {
    const [tasks, setTasks] = useState([]);
    const [newTask, setNewTask] = useState('');

    const addTask = (e) => {
        e.preventDefault();
        if (!newTask.trim()) return;
        setTasks([...tasks, { id: Date.now(), text: newTask, completed: false }]);
        setNewTask('');
    };

    const toggleTask = (id) => {
        setTasks(tasks.map(task =>
            task.id === id ? { ...task, completed: !task.completed } : task
        ));
    };

    const deleteTask = (id) => {
        setTasks(tasks.filter(task => task.id !== id));
    };

    return (
        <div className="task-manager">
            <h2>Tasks</h2>
            <form onSubmit={addTask} className="task-input-form">
                <input
                    type="text"
                    value={newTask}
                    onChange={(e) => setNewTask(e.target.value)}
                    placeholder="What are you working on?"
                />
                <button type="submit" className="btn-add">+</button>
            </form>
            <ul className="task-list">
                {tasks.map(task => (
                    <li key={task.id} className={task.completed ? 'completed' : ''}>
                        <span onClick={() => toggleTask(task.id)}>{task.text}</span>
                        <button className="btn-delete" onClick={() => deleteTask(task.id)}>×</button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default TaskManager;
