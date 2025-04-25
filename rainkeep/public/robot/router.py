from agents import writer_mistral, coder_codex, phi_orchestrator

async def route_message(data):
    role = data.get("role", "assistant")
    prompt = data.get("message", "")

    if role == "writer":
        return {"response": writer_mistral.generate(prompt)}
    elif role == "coder":
        return {"response": coder_codex.generate_code(prompt)}
    else:
        return {"response": phi_orchestrator.reply(prompt)}