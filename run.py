import gradio as gr
from sympy import symbols, integrate, sympify

def calculate_integral(expression_str, lower_limit, upper_limit):
    x = symbols('x')
    
    expr = sympify(expression_str)
    
    integral = integrate(expr, (x, lower_limit, upper_limit))
    
    return integral

def integral_calculator(expression_str, lower_limit, upper_limit):
    result = calculate_integral(expression_str, lower_limit, upper_limit)
    return str(result)

inputs = [
    "text",
    "text",
    "text",
]

output = "text"

gr.Interface(fn=integral_calculator, inputs=inputs, outputs=output, title="Integral Calculator").launch()
