import streamlit as st

# Set up the page configuration
st.set_page_config(
    page_title="Emotion Echo - Depression Assessment",
    page_icon="🌅",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Style customizations using HTML and CSS
st.markdown(
    """
    <style>
    body {
        background-color: #1a1a1a;
        color: white;
        font-family: "Arial", sans-serif;
    }
    .title-text {
        font-size: 3em;
        color: #ff9900;
        font-weight: bold;
    }
    .subtitle-text {
        font-size: 1.2em;
        color: #d9d9d9;
        margin-top: -10px;
    }
    .question {
        font-size: 1.2em;
        font-weight: bold;
        margin: 10px 0;
    }
    .footer {
        font-size: 0.9em;
        color: #b3b3b3;
        margin-top: 50px;
    }
    .btn-primary {
        background-color: #ff9900;
        color: white;
        font-size: 1.1em;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Display the logo and title
st.markdown(
    """
    <div style="text-align: center;">
        <h1 class="title-text">Emotion Echo</h1>
        <p class="subtitle-text">"Helping you understand and manage your emotions."</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Questions and options for the assessment
questions = [
    {"question": "Mood", "options": [
        ("I do not feel sad.", 0),
        ("I feel blue or sad.", 1),
        ("I am blue or sad all the time and I can't snap out of it.", 2),
        ("I am so sad or unhappy that it is very painful.", 2),
        ("I am so sad or unhappy that I can't stand it.", 3),
    ]},
    {"question": "Pessimism", "options": [
        ("I am not particularly pessimistic or discouraged about the future.", 0),
        ("I feel discouraged about the future.", 1),
        ("I feel I have nothing to look forward to.", 2),
        ("I feel that I won't ever get over my troubles.", 2),
        ("I feel that the future is hopeless and that things cannot improve.", 3),
    ]},
    {"question": "Sense of Failure", "options": [
        ("I do not feel like a failure.", 0),
        ("I feel I have failed more than the average person.", 1),
        ("I feel I have accomplished very little that is worthwhile or that means anything.", 2),
        ("As I look back on my life all I can see is a lot of failures.", 2),
        ("I feel I am a complete failure as a person.", 3),
    ]},
    {"question": "Lack of Satisfaction", "options": [
        ("I am not particularly dissatisfied.", 0),
        ("I feel bored most of the time.", 1),
        ("I don't enjoy things the way I used to.", 1),
        ("I don't get satisfaction out of anything any more.", 2),
        ("I am dissatisfied with everything.", 3),
    ]},
    {"question": "Guilty Feelings", "options": [
        ("I don't feel particularly guilty.", 0),
        ("I feel bad or unworthy a good part of the time.", 1),
        ("I feel quite guilty.", 2),
        ("I feel bad or unworthy practically all the time now.", 2),
        ("I feel as though I am very bad or worthless.", 3),
    ]},
    {"question": "Sense of Punishment", "options": [
        ("I don't feel I am being punished.", 0),
        ("I have a feeling that something bad may happen to me.", 1),
        ("I feel I am being punished or will be punished.", 2),
        ("I feel I deserve to be punished.", 3),
        ("I want to be punished.", 3),
    ]},
    {"question": "Self-Hate", "options": [
        ("I don't feel disappointed in myself.", 0),
        ("I am disappointed in myself.", 1),
        ("I don't like myself.", 1),
        ("I am disgusted with myself.", 2),
        ("I hate myself.", 3),
    ]},
    {"question": "Self-Accusations", "options": [
        ("I don't feel I am any worse than anybody else.", 0),
        ("I am very critical of myself for my weaknesses or mistakes.", 1),
        ("I blame myself for everything that goes wrong.", 2),
        ("I feel I have many bad faults.", 2),
    ]},
    {"question": "Self-Punitive Wishes", "options": [
        ("I don't have any thoughts of harming myself.", 0),
        ("I have thoughts of harming myself but I wouldn't carry them out.", 1),
        ("I feel I would be better off dead.", 2),
        ("I have definite plans about committing suicide.", 2),
        ("I feel my family would be better off if I were dead.", 2),
        ("I would kill myself if I could.", 3),
    ]},
    {"question": "Crying Spells", "options": [
        ("I don't cry any more than usual.", 0),
        ("I cry more now than I used to.", 1),
        ("I cry all the time now. I can't stop it.", 2),
        ("I used to be able to cry but now I can't cry at all even though I want to.", 3),
    ]},
    {"question": "Irritability", "options": [
        ("I am no more irritated now than I ever am.", 0),
        ("I get annoyed or irritated more easily than I used to.", 1),
        ("I feel irritated all the time.", 2),
        ("I don't get irritated at all at the things that used to irritate me.", 3),
    ]},
    {"question": "Social Withdrawal", "options": [
        ("I have not lost interest in other people.", 0),
        ("I am less interested in other people now than I used to be.", 1),
        ("I have lost most of my interest in other people and have little feeling for them.", 2),
        ("I have lost all of my interest in other people and don't care about them at all.", 3),
    ]},
    {"question": "Indecisiveness", "options": [
        ("I make decisions about as well as ever.", 0),
        ("I am less sure of myself now and try to put off making decisions.", 1),
        ("I can't make decisions any more without help.", 2),
        ("I can't make any decisions at all any more.", 3),
    ]},
    {"question": "Body Image", "options": [
        ("I don't feel I look any worse than I used to.", 0),
        ("I am worried that I am looking old or unattractive.", 1),
        ("I feel that there are permanent changes in my appearance and they make me look unattractive.", 2),
        ("I feel that I am ugly or repulsive looking.", 3),
    ]},
    {"question": "Work Inhibition", "options": [
        ("I can work about as well as before.", 0),
        ("It takes extra effort to get started at doing something.", 1),
        ("I don't work as well as I used to.", 1),
        ("I have to push myself very hard to do anything.", 2),
        ("I can't do any work at all.", 3),
    ]},
    {"question": "Sleep Disturbance", "options": [
        ("I can sleep as well as usual.", 0),
        ("I wake up more tired in the morning than I used to.", 1),
        ("I wake up 1-2 hours earlier than usual and find it hard to get back to sleep.", 2),
        ("I wake up early every day and can't get more than 5 hours of sleep.", 3),
    ]},
    {"question": "Fatigability", "options": [
        ("I don't get any more tired than usual.", 0),
        ("I get tired more easily than I used to.", 1),
        ("I get tired from doing anything.", 2),
        ("I get too tired to do anything.", 3),
    ]},
    {"question": "Loss of Appetite", "options": [
        ("My appetite is no worse than usual.", 0),
        ("My appetite is not as good as it used to be.", 1),
        ("My appetite is much worse now.", 2),
        ("I have no appetite at all any more.", 3),
    ]},
    {"question": "Weight Loss", "options": [
        ("I haven't lost much weight, if any, lately.", 0),
        ("I have lost more than 5 pounds.", 1),
        ("I have lost more than 10 pounds.", 2),
        ("I have lost more than 15 pounds.", 3),
    ]},
    {"question": "Somatic Preoccupations", "options": [
        ("I am no more concerned about my health than usual.", 0),
        ("I am concerned about aches and pains or other unpleasant feelings in my body.", 1),
        ("I am so concerned with how I feel that it's hard to think of much else.", 2),
        ("I am completely absorbed in what I feel.", 3),
    ]},
    {"question": "Loss of Libido", "options": [
        ("I have not noticed any recent change in my interest in sex.", 0),
        ("I am less interested in sex than I used to be.", 1),
        ("I am much less interested in sex now.", 2),
        ("I have lost interest in sex completely.", 3),
    ]},
    # Add remaining questions here in a similar format
]

# Function to determine depression level
def assess_depression(total_score):
    if total_score <= 9:
        return "Minimal Depression"
    elif 10 <= total_score <= 18:
        return "Mild Depression"
    elif 19 <= total_score <= 29:
        return "Moderate Depression"
    else:
        return "Severe Depression"

# Display the form for assessment
total_score = 0
with st.form("depression_assessment_form"):
    for i, q in enumerate(questions, 1):
        st.markdown(f"<p class='question'>Q{i}. {q['question']}</p>", unsafe_allow_html=True)
        options = [opt[0] for opt in q["options"]]
        scores = [opt[1] for opt in q["options"]]
        user_response = st.radio("", options, key=f"q{i}")
        total_score += scores[options.index(user_response)]

    # Submit button
    submitted = st.form_submit_button("Submit")

# Display the result
if submitted:
    depression_level = assess_depression(total_score)
    st.markdown(
        f"""
        <div style="text-align: center; margin-top: 20px;">
            <h2 style="color: #ff9900;">Assessment Result</h2>
            <p><strong>Total Inventory Score:</strong> {total_score}</p>
            <p><strong>Depression Level:</strong> {depression_level}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Footer
st.markdown(
    """
    <div class="footer" style="text-align: center;">
        Emotion Echo | Bringing positivity to your life 🌅
    </div>
    """,
    unsafe_allow_html=True,
)