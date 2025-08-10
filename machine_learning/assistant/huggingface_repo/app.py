import gradio as gr
#import warnings
from openai import OpenAI

def hello(name, age, gender, season, phys, skill, experience, future,  api_key):
    #warnings.filterWarnings("ignore, category=DeprecationWarning)
    client = OpenAI(api_key=api_key)

    open_file = open("dataset.json", "rb")
    data_file = client.files.create(file=open_file, purpose='assistants')

    sports = {
        'fall': [
            'cross country',
            'field hockey',
            'football'
        ],
        'winter': [
            'basketball',
            'ice hockey',
            'squash'
        ],
        'spring': [
            'baseball',
            'crew',
            'golf'
        ]
    }

    sports_string = "Choose a sport in the correct season"
    for season in sports.keys():
        season_sports = ",".join(sports[season])
        sports_string += f"The {season} sports are {season_sports}"

    instructions = """The 'sport advisor' is an AI assistant that specializes in recommending sports for highschool students.
       The assistant takes into account the user’s age, gender, season of sport, skill level, amount of experience, wanting to play in college, and physical attributes.
        Along with advising for sports, recommend equipment needed for each sport. Finally, depending on what the user is asking for, provide information on the ratings, price range, and sub-city area."""
    instructions += sports_string

    ai_assistant = client.beta.assistants.create(
        name='Sports Advisor',
        instructions=instructions,
        model="gpt-4.1-mini",
        tools=[{"type": "file_search"}]
    )

    prompt = (f"What sport should I choose? My age is {age}, gender {gender}, my sport of season is {season}, skill level {skill}," +
              f" I have played for {experience} years, I want to play this sport after highschool {future}, my physical attributes are {phys}")

    thread = client.beta.threads.create(messages = [
        {
            "role" : "user",
            "content" : prompt,
            "attachments": [
                {"file_id": data_file.id, "tools": [{"type": "file_search"}]}
            ]
        }
    ])
    
    return_text = "Thread id: " + thread.id + "\n"
    return_text = return_text + "Assistant id: " + ai_assistant.id + "\n"
    
    run = client.beta.threads.runs.create_and_poll(thread_id = thread.id, assistant_id=ai_assistant.id)
    if run.status == 'completed':
        messages = client.beta.threads.messages.list(thread_id=thread.id)
        return_text = return_text + "Run id: " + run.id
        return_text = return_text + "User: " + messages.data[1].content[0].text.value + "\n"
        return_text = return_text + "Assistant: " + messages.data[0].content[0].text.value + "\n"
    else:
        return_text = return_text + "Error, status: " + run.status

    return return_text

input_name = gr.Textbox(label="What is your name?")
input_age = gr.Textbox(label="How old are you?")
input_gender = gr.Textbox(label="What is your gender?")
input_season = gr.Textbox(label="What season(s) do you play your sport?")
input_skill = gr.Textbox(label="Please describe your skill level")
input_experience = gr.Textbox(label="How much experience do you have in this sport?")
input_future = gr.Textbox(label="Would you want to play this sport in college?")
input_phys = gr.Textbox(label="What are your physical attributes?")

input_api_key = gr.Textbox(label="API key")

label = gr.Label(label="Assistant Response")
demo = gr.Interface(fn=hello, inputs=[input_name, input_age, input_gender, input_season, input_phys, input_skill, input_experience, input_future,  input_api_key], outputs=label)

demo.launch()
