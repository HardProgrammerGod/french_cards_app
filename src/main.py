from db_manager import DBManager

def start_flashcards():
    db = DBManager()
    
    while True:
        word = db.get_random_word()
        if not word:
            print("Всі слова вивчені! 🎉")
            break
        
        french, ukrainian = word
        print(f"Перекладіть слово: {french}")
        user_input = input("Ваш варіант: ").strip().lower()
        
        if user_input == ukrainian.lower():
            print("✅ Правильно!")
            db.mark_as_learned(french)
        else:
            print(f"❌ Неправильно. Вірна відповідь: {ukrainian}")
        
        if input("Продовжити? (так/ні): ").strip().lower() != "так":
            break

if __name__ == "__main__":
    start_flashcards()

