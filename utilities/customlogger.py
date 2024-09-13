import logging

class LogGen:
    @staticmethod
    def loggen():
        # Simplified logging configuration
        logging.basicConfig(
            format='%(asctime)s:%(levelname)s:%(message)s',
            datefmt='%m %d %Y %I:%M:%S %p',
            level=logging.INFO  # Set the logging level
        )

        # Get the logger
        logger = logging.getLogger()

        # Add a handler to write logs to a file
        file_handler = logging.FileHandler("C:\\Users\Ansar\\PycharmProjects\\pythonProject1\\nopcommerceApp\\Logs\\automation.log")
        file_handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s', datefmt='%m %d %Y %I:%M:%S %p')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)








        # Optionally, add a console handler to see logs in the terminal
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # Print out handlers to confirm they are attached
        print(f"Attached Handlers: {logger.handlers}")

        return logger

