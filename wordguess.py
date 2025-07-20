import random 

def choose_word():
    words = words = ["کتاب", "خانه", "مدرسه", "بايثون", "برمجة", "كمبيوتر", "كورسات", "تعليم", "تكنولوجيا"]

    return random.choice(words)

def word_status(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def word_guessing_game():
    secret_word = choose_word()
    guessed_letters = []
    attempts = 6

    print("لعبة تخمين الكلمة")
    print("لديك 6 محاولات لتخمين الكلمة.")
    print("الكلمة:", word_status(secret_word, guessed_letters))
    print("ابدأ التخمين")

    while attempts > 0:

        guess = input("أدخل حرفًا: ").strip()

        if len(guess) != 1 or not guess.isalpha():
            print("الرجاء إدخال حرف واحد فقط")
            continue
        if guess in guessed_letters:
            print("لقد خمنت هذا الحرف بالفعل")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            attempts-= 1
            print(f"خطأ! لديك {attempts} محاولات متبقية.")
        else:
            occurrences = secret_word.count(guess)
            print(f"صحيح! الحرف '{guess}' موجود {occurrences} مرة في الكلمة")

        current_status = word_status(secret_word, guessed_letters)
        print("الكلمة:", current_status)

        if "_" not in current_status:
            print("تهانينا! لقد خمّنت الكلمة بنجاح:", secret_word)
            break
    if "_" in current_status:
        print("للأسف، لقد نفدت محاولاتك. الكلمة الصحيحة كانت:", secret_word)

word_guessing_game()