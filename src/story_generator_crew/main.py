import os
from dotenv import load_dotenv
load_dotenv()

from story_generator_crew.crew import StoryGeneratorCrew

def run():
    inputs = {
        "theme": "Fantasy",
        "main_character": {
            "name": "Leo",
            "age": 12,
            "gender": "Male",
            "personality_traits": ["Brave", "Curious", "Kind"],
            "appearance": "A boy with black hair and green eyes, wearing a red cape"
        },
        "supporting_characters": [
            {
            "name": "Aria",
            "role": "Friend",
            "personality_traits": ["Intelligent", "Loyal"],
            "appearance": "A girl with long blonde hair and blue eyes"
            },
            {
            "name": "Nimbus",
            "role": "Talking animal",
            "personality_traits": ["Wise", "Witty"],
            "appearance": "A talking owl with golden feathers"
            }
        ],
        "setting": "Enchanted forest",
        "time_period": "Medieval",
        "plot_points": [
            "Leo discovers a hidden magical portal",
            "Leo and Aria embark on a quest to find a legendary treasure",
            "They encounter Nimbus, who helps them solve ancient riddles",
            "They must overcome a wicked sorcerer guarding the treasure"
        ],
        "mood": "Exciting and adventurous",
        "narrative_style": "Third-person",
        "language_complexity": "Suitable for children"
        }


    StoryGeneratorCrew().crew().kickoff(inputs=inputs)

if __name__ == '__main__':
    run()