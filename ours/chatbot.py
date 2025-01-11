import json
from difflib import get_close_matches

def load_knowledge_base(file_path: str) -> dict:
    # Membuka file menggunakan `with` agar otomatis ditutup setelah selesai
    with open(file_path, 'r') as file:
        # Membaca isi file JSON dan mengonversinya menjadi dictionary
        data: dict = json.load(file)
    return data

# def load_knowledge_base(file_path: str) -> dict:
    # file = open(file_path, 'r')
    # data: dict = json.load(file)
    # file.close()  # Harus manual menutup file
    # return data

def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6) #Threshold kesamaan minimal (0.6 atau 60% mirip)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]

def load_pc_recommendations(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data
    
# Fungsi untuk mendapatkan rekomendasi PC
def get_pc_recommendation():
    file_path = 'ours/pc_recommendations.json'
    data = load_pc_recommendations(file_path)
    return data  # Data berisi semua rekomendasi PC dari file JSON

def get_bot_response(user_input: str) -> str:
    knowledge_base: dict = load_knowledge_base('ours/knowledge_base.json')
    # Mencari Pertanyaan yang Cocok
    #ist comprehension untuk mengambil semua pertanyaan dari knowledge base
    best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])
    
    if best_match:
        answer: str = get_answer_for_question(best_match, knowledge_base)
        return answer
    else:
        return "I'm sry for being too stupid to understand are you saying."