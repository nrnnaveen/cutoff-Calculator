import streamlit as st

st.title("WELCOME TO CUTOFF CALCULATOR 2026")

st.write("""
Which cutoff do you want to calculate?
""")

option = st.selectbox(
    "Select your cutoff type",
    (
        "TNEA (ENGINEERING)",
        "TNAU (AGRICULTURE)",
        "TNDALU (LAW)",
        "TNGASA (ARTS & SCIENCE)",
        "TNMEDICAL SELECTION (PARAMEDICAL)",
        "TANUVAS (VETERINARY)"
    )
)

if option == "TNEA (ENGINEERING)":
    st.subheader("TNEA 2026 CUTOFF CALCULATOR")

    phy = st.number_input("Enter Physics Score /100",0,100)
    che = st.number_input("Enter Chemistry Score /100",0,100)
    math = st.number_input("Enter Maths Score /100",0,100)

    if st.button("Calculate"):
        phy_che = (phy/2)+(che/2)
        cutoff = phy_che + math
        st.success(f"Your Engineering Cutoff is: {cutoff}")

elif option == "TNAU (AGRICULTURE)":
    st.subheader("TNAU 2026 CUTOFF CALCULATOR")

    phy = st.number_input("Enter Physics Score /100",0,100)
    che = st.number_input("Enter Chemistry Score /100",0,100)
    math = st.number_input("Enter Maths Score /100",0,100)
    bio = st.number_input("Enter Biology Score /100",0,100)

    if st.button("Calculate"):
        cutoff = (phy/2)+(che/2)+(math/2)+(bio/2)
        st.success(f"Your Agriculture Cutoff is: {cutoff}")

elif option == "TNDALU (LAW)":
    st.subheader("TNDALU 2026 CUTOFF CALCULATOR")

    s1 = st.number_input("Enter Main Subject 1 /100",0,100)
    s2 = st.number_input("Enter Main Subject 2 /100",0,100)
    s3 = st.number_input("Enter Main Subject 3 /100",0,100)
    s4 = st.number_input("Enter Main Subject 4 /100",0,100)

    if st.button("Calculate"):
        cutoff = (s1/2)+(s2/2)+(s3/2)+(s4/2)
        st.success(f"Your Law Cutoff is: {cutoff}")

elif option == "TNGASA (ARTS & SCIENCE)":
    st.subheader("TNGASA 2026 CUTOFF CALCULATOR")

    s1 = st.number_input("Enter Main Subject 1 /100",0,100)
    s2 = st.number_input("Enter Main Subject 2 /100",0,100)
    s3 = st.number_input("Enter Main Subject 3 /100",0,100)
    s4 = st.number_input("Enter Main Subject 4 /100",0,100)

    if st.button("Calculate"):
        cutoff = (s1/2)+(s2/2)+(s3/2)+(s4/2)
        st.success(f"Your Arts & Science Cutoff is: {cutoff}")

elif option == "TNMEDICAL SELECTION (PARAMEDICAL)":
    st.subheader("TN MEDICAL (PARAMEDICAL) CUTOFF CALCULATOR")

    s1 = st.number_input("Enter Main Subject 1 /100",0,100)
    s2 = st.number_input("Enter Main Subject 2 /100",0,100)
    s3 = st.number_input("Enter Main Subject 3 /100",0,100)
    s4 = st.number_input("Enter Main Subject 4 /100",0,100)

    if st.button("Calculate"):
        cutoff = (s1/2)+(s2/2)+(s3/2)+(s4/2)
        st.success(f"Your Paramedical Cutoff is: {cutoff}")

elif option == "TANUVAS (VETERINARY)":
    st.subheader("TANUVAS 2026 CUTOFF CALCULATOR")

    phy = st.number_input("Enter Physics Score /100",0,100)
    che = st.number_input("Enter Chemistry Score /100",0,100)
    bio = st.number_input("Enter Biology Score /100",0,100)

    if st.button("Calculate"):
        cutoff = (phy/2)+(che/2)+bio
        st.success(f"Your Veterinary Cutoff is: {cutoff}")

st.markdown("---")
st.caption("Developed by Naveen")
