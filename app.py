import streamlit as st

# 1. Page Configuration (SEO Optimized for Budgeting & Personal Finance)
st.set_page_config(
    page_title="Subscription Burn Rate | Stop the Budget Leakage",
    page_icon="💸",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "Professional utility to calculate the true annual impact of monthly recurring subscriptions."
    }
)

# 2. CUSTOM CSS (Urgent & Modern Facelift)
st.markdown("""
    <style>
    .main { background-color: #fcfcfc; }
    .stNumberInput div div input { border-radius: 10px; border: 2px solid #d32f2f; }
    .stButton button { 
        width: 100%; 
        border-radius: 25px; 
        background-color: #d32f2f; 
        color: white; 
        font-weight: bold; 
        height: 3.5em;
        transition: 0.3s;
    }
    .stButton button:hover { background-color: #b71c1c; border: none; }
    .burn-box { 
        padding: 30px; 
        border-radius: 15px; 
        background-color: #fff5f5; 
        border: 2px solid #d32f2f; 
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
        text-align: center;
    }
    .metric-card {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #e0e0e0;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar (Factory Network Block)
with st.sidebar:
    st.image("https://img.icons8.com/clouds/200/fire-alarm.png", width=120)
    st.markdown("### THE NICHE DECODER")
    st.caption("A Stealth Factory Production")
    st.divider()
    st.link_button("☕ Support the Decoder", "https://buymeacoffee.com/the_niche_decoder")
    st.divider()
    st.markdown("**Other Reality Checks:**")
    with st.expander("⚖️ Decision Tools"):
        st.page_link("https://worth-the-buy-calc.streamlit.app", label="Should I Buy This?", icon="🛒")
        st.page_link("https://take-home-pay-calc.streamlit.app", label="Tax Reality Check", icon="🏦")
    with st.expander("💸 Side Hustle Tools"):
        st.page_link("https://hustle-check-calc.streamlit.app", label="Hustle Reality Check", icon="💸")
    st.divider()
    st.caption("v1.0 - Budget Series")

# 4. Main Interface
st.title("💸 Subscription Burn Rate")
st.markdown("### Small monthly leaks sink big financial ships.")

# Input Section
st.write("Enter your monthly 'Autopay' amounts:")
col1, col2 = st.columns(2)

with col1:
    streaming = st.number_input("Streaming (Netflix, Hulu, etc.)", min_value=0.0, value=15.0)
    software = st.number_input("Software (iCloud, Adobe, AI)", min_value=0.0, value=20.0)
    fitness = st.number_input("Fitness (Gym, Apps)", min_value=0.0, value=30.0)

with col2:
    delivery = st.number_input("Delivery (Prime, DoorDash)", min_value=0.0, value=15.0)
    entertainment = st.number_input("Gaming & Fun (Xbox, Spotify)", min_value=0.0, value=10.0)
    other = st.number_input("Misc. (News, Patreons, etc.)", min_value=0.0, value=5.0)

# 5. Calculation Logic
monthly_burn = streaming + software + fitness + delivery + entertainment + other
annual_burn = monthly_burn * 12
ten_year_cost = annual_burn * 10 # Ignoring interest for raw impact

# 6. Results
if st.button("🔥 CALCULATE THE LEAKAGE"):
    st.divider()
    
    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Monthly Burn", f"${monthly_burn:,.2f}")
        st.markdown('</div>', unsafe_allow_html=True)
    with m2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Annual Burn", f"${annual_burn:,.2f}")
        st.markdown('</div>', unsafe_allow_html=True)
    with m3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("10-Year Cost", f"${ten_year_cost:,.0f}")
        st.markdown('</div>', unsafe_allow_html=True)

    st.write("")
    
    # Verdicts based on annual impact
    if annual_burn < 500:
        verdict = "✅ LEAN & MEAN"
        color = "#2e7d32"
        advice = "You have tight control over your recurring costs. You're effectively avoiding 'subscription creep.'"
    elif annual_burn < 2000:
        verdict = "⚠️ STEALTH DRAIN"
        color = "#d32f2f"
        advice = f"You are spending ${annual_burn:,.2f} a year on things you might not even use daily. Time for a 'Cancelation Spree'?"
    else:
        verdict = "🚨 TOTAL MELTDOWN"
        color = "#b71c1c"
        advice = f"Your subscriptions are costing you ${ten_year_cost:,.0f} every decade. That is a down payment on a house or a massive head start on retirement."

    st.markdown(f"""
    <div class="burn-box">
        <h2 style="color: {color};">{verdict}</h2>
        <p style="font-size: 18px; color: #555;">{advice}</p>
    </div>
    """, unsafe_allow_html=True)

# 7. Final Attribution
st.divider()
st.caption("Developed by The Niche Decoder Factory. Anonymous & Professional.")
