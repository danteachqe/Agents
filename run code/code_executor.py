class PythonCodeExecutor:
    """
    A simple Python code executor for evaluating and running Python code.
    """

    def execute(self, code: str) -> str:
        """
        Executes the provided Python code and returns the result or error.
        
        Args:
            code (str): The Python code to execute.
        
        Returns:
            str: The output of the code execution or an error message.
        """
        try:
            # Capture the output using StringIO
            from io import StringIO
            import sys

            output_capture = StringIO()
            sys.stdout = output_capture  # Redirect standard output

            # Execute the code
            exec(code, {})  # Run the code in an isolated environment

            # Reset stdout
            sys.stdout = sys.__stdout__

            # Get the captured output
            output = output_capture.getvalue()
            return output.strip() if output.strip() else "Execution completed successfully but produced no output."
        except Exception as e:
            return f"Execution Error: {e}"
        finally:
            sys.stdout = sys.__stdout__  # Ensure stdout is always reset
