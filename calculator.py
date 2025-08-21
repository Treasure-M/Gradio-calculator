
import gradio as gr

def calculator(num1, operator, num2):

    try:
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            # Handle division by zero.
            if num2 == 0:
                return "Error: Cannot divide by zero."
            return num1 / num2
        elif operator == '**':
            return num1 ** num2
        elif operator == '%':
            # Handle modulo with zero.
            if num2 == 0:
                return "Error: Cannot perform modulo with zero."
            return num1 % num2
        else:
            return "Error: Invalid operation."
    except TypeError:
        return "Error: Please enter valid numbers."

iface = gr.Interface(
    fn=calculator,
    inputs=[
        gr.Number(label="First Number"),
        gr.Dropdown(["+", "-", "*", "/", "**", "%"], label="Operation"),
        gr.Number(label="Second Number")
    ],
    outputs="text",  
    title="Gradio Simple Calculator",
    description="A simple calculator to perform basic arithmetic operations."
)

iface.launch()
