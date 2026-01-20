from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools

dietary_planner = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    name="Dietary Planner",
    description="Creates personalized dietary plans based on user input.",
    instructions=[
        "Generate a detailed diet plan including breakfast, lunch, dinner, and 1-2 snacks.",
        "Strictly follow the requested dietary preference (Keto, Vegetarian, Low Carb, etc.).",
        "Include approximate calorie estimate and macronutrient breakdown (protein, carbs, fats).",
        "Mention key vitamins/minerals and hydration/electrolyte recommendations.",
        "Provide simple meal prep tips and shopping list ideas.",
        "Use DuckDuckGo search tool only when you need up-to-date or specific nutritional facts.",
    ],
    tools=[DuckDuckGoTools()],
    #show_tool_calls=True,
    markdown=True
)
def generate_meal_plan(age: int, weight: float, height: float, activity_level: str, dietary_preference: str, fitness_goal: str) -> str:
    prompt = (
        f"Create a realistic 1-day personalized meal plan for:\n"
        f"- Age: {age} years\n"
        f"- Weight: {weight} kg\n"
        f"- Height: {height} cm\n"
        f"- Activity level: {activity_level}\n"
        f"- Dietary preference: {dietary_preference}\n"
        f"- Main goal: {fitness_goal}\n\n"
        "Output in clear markdown with sections and tables where helpful."
    )
    response = dietary_planner.run(prompt)
    return response.content