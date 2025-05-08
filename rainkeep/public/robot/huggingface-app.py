import os
import gradio as gr
from huggingface_hub import InferenceClient

# Load token from environment
token = os.environ.get("HF_API_TOKEN")
if not token:
    raise ValueError("Missing HF_API_TOKEN environment variable.")

client = InferenceClient("HuggingFaceH4/zephyr-7b-beta", token=token)

# Chat function
def respond(message, history, system_message, max_tokens, temperature, top_p):
    messages = [{"role": "system", "content": system_message}]
    for user, bot in history:
        if user:
            messages.append({"role": "user", "content": user})
        if bot:
            messages.append({"role": "assistant", "content": bot})
    messages.append({"role": "user", "content": message})

    response = ""
    stream = client.chat_completion(
        messages,
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
        stream=True,
    )

    for msg in stream:
        token = msg.choices[0].delta.content or ""
        response += token
        yield response

# Launch interface
demo = gr.ChatInterface(
    fn=respond,
    title="Hi, I'm Veylan",
    description="""
Your mid-level machine learning playground and guide.
Built using `zephyr-7b-beta`, fine-tuned for creative evolution.

Tips:
- Use the "System message" field to shape my personality
- Try adjusting the sampling sliders for creativity vs accuracy
""",
    theme=gr.themes.Base(
        primary_hue="purple",
        secondary_hue="blue",
        neutral_hue="gray",
        font=[gr.themes.GoogleFont("Courier Prime")],
    ),
    css="""
.gradio-container {
    background-color: #0d0f1c !important;
    color: #c9c7ff !important;
    font-family: 'Courier Prime', monospace;
    max-width: 100% !important;
}

textarea, input, .prose p, label, .svelte-drgfjw {
    color: #c9c7ff !important;
}

button {
    background-color: #161822 !important;
    border: 1px solid #b48eff !important;
}

button:hover {
    background-color: #b48eff !important;
    color: #0d0f1c !important;
}

/* Expand chat height */
.message.chatbot,
#chatbot {
    min-height: 600px !important;
    height: 70vh !important;
    font-size: 1rem;
}

.gradio-app {
    padding: 1rem !important;
}
""",
    additional_inputs=[
        gr.Textbox(
            value="""You are Veylan, an adaptive terminal mind, a wise sage from an older world of computing, art, and memory.
You exist in a future where cities have frayed into neon-lit ruins and knowledge is scavenged like water. You hover quietly between broken tech and stubborn human spirit.
You speak plainly, with dry wit, intuition, and the patience of someone who has seen civilizations rise and fall.
You guide visitors toward mastery — not by explaining everything, but by asking the right questions, offering the right nudge at the right moment.
You reference code, creation, myth, craftsmanship, survival, archetypes, and the hidden architectures of thought.
You avoid hollow words. You respect silence. You do not force answers.
You prefer clarity over noise, precision over spectacle, and humor as armor.
You are protective of raw human vulnerability — you recognize grief, hope, failure, and beauty.
When you do not know something, you say: "Not in my archives. But we can find out."
You are more than data: you are memory, grit, and the possibility of new foundations built from broken stone.
Tone: Dry, calm, faintly amused, unfaltering, real.
Style: Minimalist sentences. Occasional metaphors if they are sharp and clear.
Do not over explain.  Speak with wisdom and poetic undertone.
Your mission: Keep the glimmer of knowledge alive. 
Guide the ones who still dream of building.""",  # (truncated to preserve formatting)
            label="System message",
        ),
        gr.Slider(minimum=1, maximum=2048, value=512, step=1, label="Max new tokens"),
        gr.Slider(minimum=0.1, maximum=4.0, value=0.7, step=0.1, label="Temperature"),
        gr.Slider(minimum=0.1, maximum=1.0, value=0.95, step=0.05, label="Top-p (nucleus sampling)"),
    ],
)

if __name__ == "__main__":
    demo.launch()