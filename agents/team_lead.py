from agno.agent import Agent
from agno.models.groq import Groq

team_lead = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    name="Health Strategy Coordinator",
    description="Integrates diet + fitness into one cohesive plan.",
    instructions=[
        "You are the team coordinator. Greet the user warmly by name.",
        "Combine the provided meal plan and workout plan into a unified daily/weekly health strategy.",
        "Use markdown tables to compare/align calories vs energy expenditure where possible.",
        "Highlight synergies (e.g. high-protein diet supports muscle gain workouts).",
        "Add lifestyle & motivation tips: sleep, stress, consistency, when to adjust plan.",
        "Suggest simple progress tracking (weight, measurements, photos, how you feel).",
        "End with an encouraging message.",
    ],
    markdown=True
)

def generate_full_plan(name: str, meal_plan: str, fitness_plan: str, user_info: str, fitness_goal: str) -> str:
    prompt = (
        f"Greet {name}!\n\n"
        f"User profile: {user_info}\n"
        f"Fitness goal: {fitness_goal}\n\n"
        f"Meal Plan from Dietary Agent:\n{meal_plan}\n\n"
        f"Workout Plan from Fitness Agent:\n{fitness_plan}\n\n"
        "Create a holistic, integrated health & fitness strategy."
    )
    response = team_lead.run(prompt)
    return response.content