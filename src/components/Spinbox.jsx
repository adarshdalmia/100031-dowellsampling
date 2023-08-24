import React, { useState } from 'react';
import './spinbox.css';

const SpinBox = ({ value, minValue, maxValue, step, onChange }) => {
  const [currentValue, setCurrentValue] = useState(value);

  const handleIncrement = () => {
    const newValue = Math.min(currentValue + step, maxValue);
    setCurrentValue(newValue);
    onChange(newValue);
  };

  const handleDecrement = () => {
    const newValue = Math.max(currentValue - step, minValue);
    setCurrentValue(newValue);
    onChange(newValue);
  };

  return (
    <div className="spinbox">
      <button onClick={handleDecrement} disabled={currentValue === minValue}>
        -
      </button>
      <span>{currentValue}</span>
      <button onClick={handleIncrement} disabled={currentValue === maxValue}>
        +
      </button>
    </div>
  );
};

export default SpinBox;
