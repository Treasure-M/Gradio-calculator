A simple web calculator 

This is a straightforward online calculator created with the Gradio package and Python. It offers an intuitive user interface for carrying out standard mathematical calculations.

Features

* User-Friendly Interface: A straightforward web user interface with dropdown menus and numerical inputs.
* Basic Arithmetic: Supports addition (+), subtraction (-), multiplication (*), and division (/).
* Advanced Operations: Includes exponentiation (**) and modulo (%).
* Error Handling: Divides by zero and displays unambiguous error messages for incorrect inputs.

Installation

1. Clone the repository:

git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name

1. Replace your-username/your-repository-name with the actual path to your repository.
2. Install Gradio:
3. This project requires the Gradio library. You can install it using pip:

pip install gradio



Usage

To run the application, execute the Python script from your terminal:
python gradio_calculator.py
After running the command, a local server will start, and a link will be provided in your terminal (usually http://127.0.0.1:7860). Open this link in your web browser to use the calculator.



Flagging Data

The "Flag" button in this program lets users save a calculation's inputs and outputs. Debugging and gathering a dataset of interactions are two uses for this capability. 
The data is saved in a CSV file under a new folder called flagged in the same directory as the application when you click the flag button.

