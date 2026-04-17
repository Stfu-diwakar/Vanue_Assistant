# Smart Venue Assistant  
### AI-Powered Real-Time Crowd Intelligence for Large-Scale Sporting Events  

**Live Application:**  
https://vanueassistant.streamlit.app/

---

## Overview

Smart Venue Assistant is an intelligent system designed to enhance the physical experience of attendees in large-scale sporting venues.  

It combines real-time insights, predictive modeling, and AI-driven assistance to help users navigate complex environments efficiently, reduce waiting times, and make informed decisions during live events.

---

## Problem

Large venues often struggle with:

- Unstructured crowd movement leading to congestion  
- Long queues at food stalls and facilities  
- Lack of real-time visibility into crowd conditions  
- Inefficient navigation inside complex layouts  

These issues reduce both user satisfaction and operational efficiency.

---

## Solution

Smart Venue Assistant introduces a dynamic, context-aware system that:

- Monitors and represents crowd distribution  
- Predicts waiting times at key locations  
- Suggests optimal routes within the venue  
- Provides real-time assistance through an AI-powered interface  

---

## Key Features

### Real-Time Dashboard  
Provides a live overview of venue activity through structured visualizations, enabling users to understand crowd density and trends instantly.

### Intelligent Navigation  
Implements graph-based routing to guide users through the venue while avoiding congested areas.

### Queue Prediction  
Estimates waiting times dynamically, allowing users to plan movements more effectively.

### Crowd Visualization  
Displays spatial distribution of crowd density using an interactive map interface.

### AI Assistant  
A context-aware assistant powered by Google Gemini that delivers concise, relevant, and actionable guidance based on current conditions.

---

## System Design
User Interface (Streamlit)
↓
Application Logic (Python Modules)
↓
AI Processing (Google Gemini API)
↓
Data Layer (Simulated, Extendable to Real-Time Sources)

---

---

## Technology Stack

- Frontend: Streamlit  
- Backend: Python  
- AI Integration: Google Gemini API  
- Data Visualization: Plotly  
- Mapping: Folium  
- Data Handling: Pandas  

---

## Security and Best Practices

- Sensitive credentials are managed using Streamlit Secrets  
- No API keys are exposed in the codebase  
- Modular architecture ensures maintainability and scalability  
- Lightweight repository compliant with submission constraints  

---

## Project Structure

    smart-venue-assistant/
    ├── streamlit_app.py
    ├── config.py
    ├── requirements.txt
    ├── README.md
    ├── utils/
    ├── ai/
    ├── services/
    ├── assets/
    ├── data/
    └── tests/

---
## Execution

To run the project locally:


git clone https://github.com/your-username/smart-venue-assistant.git

cd smart-venue-assistant

pip install -r requirements.txt
streamlit run streamlit_app.py


---

## Assumptions

- Crowd data is simulated and can be replaced with real-time sources  
- Venue layout is simplified for demonstration purposes  
- Indoor positioning is abstracted  

---

## Future Scope

- Integration with real-time data sources such as Firebase or IoT sensors  
- Indoor positioning using Bluetooth or WiFi-based systems  
- Personalized recommendations based on user behavior  
- Voice-enabled interaction for accessibility  
- Multi-user coordination features  

---

## Impact

This system improves:

- Crowd safety and flow management  
- Time efficiency for attendees  
- Overall event experience  
- Data-driven decision-making for venue operators  

---

## Conclusion
Smart Venue Assistant transforms complex and crowded environments into structured, navigable, and intelligent spaces. By combining AI with real-time analytics, it bridges the gap between physical infrastructure and digital intelligence in modern event venues.
