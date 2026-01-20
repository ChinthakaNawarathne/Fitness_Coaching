import streamlit as st
from core.config import GROQ_API_KEY  # just to ensure it's loaded

from agents.dietary_planner import generate_meal_plan
from agents.fitness_trainer import generate_fitness_plan
from agents.team_lead import generate_full_plan

st.set_page_config(
    page_title="AI Health & Fitness Coach",
    page_icon="🏋️‍♂️🍎",
    layout="wide"
)

# ── Custom CSS (same as yours, slightly cleaned) ──
st.markdown("""
    <style>
        .title { text-align: center; font-size: 3.2rem; font-weight: bold; color: #FF6347; }
        .subtitle { text-align: center; font-size: 1.4rem; color: #4CAF50; margin-bottom: 2rem; }
        .profile { background: #E8F5E9; padding: 1.5rem; border-radius: 10px; margin: 1rem 0; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="title">🏋️‍♂️ AI Health & Fitness Coach</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Your personal AI-powered diet + workout strategist</p>', unsafe_allow_html=True)

# ── Sidebar Inputs ──
with st.sidebar:
    st.header("⚙️ Your Profile")
    name = st.text_input("Your name", "Alex")
    age = st.number_input("Age", 10, 100, 28)
    weight = st.number_input("Weight (kg)", 30.0, 200.0, 72.0)
    height = st.number_input("Height (cm)", 100, 250, 172)
    activity_level = st.selectbox("Activity Level", ["Low", "Moderate", "High"])
    dietary_preference = st.selectbox("Diet Preference", ["Keto", "Vegetarian", "Low Carb", "Balanced"])
    fitness_goal = st.selectbox("Main Goal", ["Weight Loss", "Muscle Gain", "Endurance", "Flexibility"])

    generate_button = st.button("💪 Generate My Plan", type="primary", use_container_width=True)

# ── Main Content ──
if generate_button:
    if not all([age, weight, height, name.strip()]):
        st.warning("Please complete all fields.")
    else:
        with st.spinner("🤖 Agents are collaborating on your plan..."):
            user_info = f"{age} years old, {weight} kg, {height} cm, activity: {activity_level}"

            meal = generate_meal_plan(age, weight, height, activity_level, dietary_preference, fitness_goal)
            workout = generate_fitness_plan(age, weight, height, activity_level, fitness_goal)

            full_plan = generate_full_plan(name, meal, workout, user_info, fitness_goal)

        st.subheader(f"🌟 Your Personalized Plan, {name}!")
        st.markdown(full_plan)

        st.success("Plan ready! Consistency is your superpower 💥")

        st.info("This plan was created by three specialized AI agents working together.")