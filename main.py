from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
from backend import *

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, change to specific origin(s) for security
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all HTTP headers
)

class GeneticRequest(BaseModel):
    population_size: int
    generation_rate: int
    mutation_rate: float
    elitism_size: int

@app.post("/run-genetic-algorithm/")
def run_genetic_algorithm(request: dict):
    # Ensure correct data types
    population_size = int(request.get("populationSize"))
    generation_rate = int(request.get("generationRate"))
    mutation_rate = float(request.get("mutationRate"))
    elitism_size = int(request.get("elitismSize"))
    
    problem_cube = Tensor(5, 5, 5)
    cube = problem_cube.initial_state()
    algo = GeneticAlgoNJ(
        cube,
        population_size=population_size,
        generation_rate=generation_rate,
        mutation_rate=mutation_rate,
        elitism_size=elitism_size,
    )
    algo.evolve()
    best_cube, best_fitness = algo.get_best_solution()
    return {
        "best_fitness": best_fitness,
        "fitness_history": algo.fitness_history,
        "solution": best_cube.array.tolist(),
    }

