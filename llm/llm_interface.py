import abc


class LLMInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def chat(self, prompt):
        """
        Sends a chat prompt to an agent, print the result, and returns the full response.

        Parameters:
        - prompt (str): The message or question to send to the agent.

        Returns:
        - str: The full response from the agent.
        """
        pass

    @abc.abstractmethod
    def chat_iter(self, prompt):
        """
        Sends a chat prompt to an agent and return an iterator to the response.

        Parameters:
        - prompt (str): The message or question to send to the agent.

        Returns:
        - Iterator[str]: An iterator to the response from the agent.
        """
        pass

    @abc.abstractmethod
    def chat_stream_audio(
        self, prompt, generate_audio_file=None, stream_audio_file=None
    ):
        """
        Call the llm with text, print the result, and stream the audio to the frontend if the generate_audio_file and stream_audio_file functions are provided.
        prompt: str
            the text to send to the llm
        generate_audio_file: function
            the function to generate audio file from text. The function should take the text as input and return the path to the generated audio file. Defaults to None.
        stream_audio_file: function
            the function to stream the audio file to the frontend. The function should take the path to the audio file as input. Defaults to None.

        Returns:
        str: the full response from the llm
        """
        pass

    @staticmethod
    def is_complete_sentence(self, text:str):
        """
        Check if the text is a complete sentence.
        text: str
            the text to check
        """

        white_list = ["...", "Dr.", "Mr.", "Ms.", "Mrs.", "Jr.", "Sr.", "St.", "Ave.", "Rd.", "Blvd.", "Dept.", "Univ.", "Prof.", "Ph.D.", "M.D.", "U.S.", "U.K.", "U.N.", "E.U.", "U.S.A.", "U.K.", "U.S.S.R.", "U.A.E."]

        for item in white_list:
            if text.strip().endswith(item):
                return False

        punctuation_blacklist = [".", "?", "!", "。", "；", "？", "！", "…", "〰", "〜", "～", "！", ]
        return any(text.strip().endswith(punct) for punct in punctuation_blacklist)
