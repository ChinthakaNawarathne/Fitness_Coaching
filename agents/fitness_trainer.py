from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools

fitness_trainer = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    name="Fitness Trainer",
    description="Generates safe, customized workout routines.",
    instructions=[
        # ... (same instructions as before)
    ],
    tools=[DuckDuckGoTools()],
    #show_tool_calls=True,
    markdown=True
)

def generate_fitness_plan(age: int, weight: float, height: float, activity_level: str, fitness_goal: str) -> str:
    prompt = (
        f"Create a personalized workout plan for:\n"
        f"- Age: {age} years\n"
        f"- Weight: {weight} kg\n"
        f"- Height: {height} cm\n"
        f"- Activity level: {activity_level}\n"
        f"- Goal: {fitness_goal}\n\n"
        "Include warm-up (5-10 min), main exercises with sets/reps, cool-down, "
        "and progression advice. Use tables for clarity."
    )
    response = fitness_trainer.run(prompt)
    return response.content