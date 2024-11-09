import React, { useState } from "react";
import axios from "axios";
import GeneticForm from "../components/GeneticForm";
import SolutionDisplay from "../components/SolutionDisplay";

const Home = () => {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleFormSubmit = async (params) => {
    setLoading(true);
    setError(null);
    try {
      const response = await axios.post("http://localhost:8000/run-genetic-algorithm/", params);
      setResult(response.data);
    } catch (err) {
      setError("An error occurred while running the algorithm.");
    }
    setLoading(false);
  };

  return (
    <div>
      <h1>Magic Cube Genetic Algorithm</h1>
      <GeneticForm onSubmit={handleFormSubmit} />
      {loading && <p>Loading...</p>}
      {error && <p style={{ color: "red" }}>{error}</p>}
      {result && (
        <SolutionDisplay
          fitnessHistory={result.fitness_history}
          bestFitness={result.best_fitness}
          solution={result.solution}
        />
      )}
    </div>
  );
};

export default Home;
