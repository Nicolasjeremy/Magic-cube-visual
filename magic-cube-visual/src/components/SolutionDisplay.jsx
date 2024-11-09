import React from "react";

const SolutionDisplay = ({ fitnessHistory, bestFitness, solution }) => {
  return (
    <div>
      <h2>Solution</h2>
      <p>Best Fitness: {bestFitness}</p>
      <h3>Fitness History</h3>
      <ul>
        {fitnessHistory.map((fitness, index) => (
          <li key={index}>
            Generation {index + 1}: {fitness}
          </li>
        ))}
      </ul>
      <h3>Best Cube</h3>
      {solution.map((level, index) => (
        <div key={index}>
          <h4>Level {index + 1}</h4>
          <pre>{JSON.stringify(level, null, 2)}</pre>
        </div>
      ))}
    </div>
  );
};

export default SolutionDisplay;
