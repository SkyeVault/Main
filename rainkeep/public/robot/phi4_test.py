from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

model_name = "microsoft/Phi-4-mini-instruct"

print("Loading model...")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)

print("Ready. Type a prompt:")

while True:
    prompt = input(">>> ")
    if prompt.lower() in ["exit", "quit"]: break
    output = pipe(prompt, max_new_tokens=150, 
do_sample=True)[0]["generated_text"]
    print("\n" + output + "\n")

