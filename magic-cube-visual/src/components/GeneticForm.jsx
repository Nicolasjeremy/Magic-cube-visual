import React, { useState } from "react";

const GeneticForm = ({ onSubmit }) => {
  const [populationSize, setPopulationSize] = useState(10);
  const [generationRate, setGenerationRate] = useState(5);
  const [mutationRate, setMutationRate] = useState(0.1);
  const [elitismSize, setElitismSize] = useState(2);

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({ populationSize, generationRate, mutationRate, elitismSize });
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Population Size:</label>
        <input
          type="number"
          value={populationSize}
          onChange={(e) => setPopulationSize(e.target.value)}
          min="1"
          required
        />
      </div>
      <div>
        <label>Generation Rate:</label>
        <input
          type="number"
          value={generationRate}
          onChange={(e) => setGenerationRate(e.target.value)}
          min="1"
          required
        />
      </div>
      <div>
        <label>Mutation Rate:</label>
        <input
          type="number"
          step="0.01"
          value={mutationRate}
          onChange={(e) => setMutationRate(e.target.value)}
          min="0"
          max="1"
          required
        />
      </div>
      <div>
        <label>Elitism Size:</label>
        <input
          type="number"
          value={elitismSize}
          onChange={(e) => setElitismSize(e.target.value)}
          min="0"
          required
        />
      </div>
      <button type="submit">Run Genetic Algorithm</button>
    </form>
  );
};

export default GeneticForm;
