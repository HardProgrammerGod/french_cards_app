import json
from db_manager import DBManager

def load_words(json_path="data/words.json"):
    """Загрузка слова з JSON у бд"""
    db = DBManager()
    
    with open(json_path, "r", encoding="utf-8") as file:
        words = json.load(file)
    
    for word in words:
        db.add_word(word["french"], word["ukrainian"])
    
    print("Слова завантажено!")

if __name__ == "__main__":
    load_words()

