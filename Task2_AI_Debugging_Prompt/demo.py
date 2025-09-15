from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load StarCoder
model_name = "bigcode/starcoder"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")

# Example student code with a misconception
student_code = """
def factorial(n):
    if n == 0:
        return 0   # mistake: should return 1
    else:
        return n * factorial(n-1)
"""

# Ask the model to generate a reflective question
prompt = f"""
Analyze the following Python code and generate a conceptual question 
to help the student reflect on their understanding (without giving the solution):

{student_code}
"""

inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=100)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))