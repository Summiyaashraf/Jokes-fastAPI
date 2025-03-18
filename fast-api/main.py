from fastapi import FastAPI
import random

app = FastAPI()

# Pakistani Jokes List
pakistani_jokes = [
    {"setup": "Ek Pathan ne fridge mein pahar ki tasveer kyun lagayi?", "punchline": "Taake thanda rahe! 😂"},
    {"setup": "Biwi: Tum mujhe kahin le kyun nahi jate?", "punchline": "Shauhar: Theek hai, chalo kitchen! 😆"},
    {"setup": "Teacher: 2 aur 2 kitne hote hain?", "punchline": "Student: Sir, jab mood acha ho toh 4, warna 22! 🤣"},
    {"setup": "Aik programmer ki shaadi ho gayi, aglay din kya huwa?", "punchline": "Usne commit kar diya! 😜"},
    {"setup": "Boy: Mujhe tumse ek baat kehni hai...", "punchline": "Girl: Pehlay batao, API secure hai ya nahi? 😆"},
    {"setup": "Ek Pakistani aur ek Amreeki lambi race lagate hain, kon jeeta?", "punchline": "Jo Metro pakar ke chala gaya! 🚇😂"},
    {"setup": "Aik bacha pizza shop gaya aur bola: Uncle ek pizza dedo.", "punchline": "Uncle: Beta kaat kar doon? Bacha: Nahi uncle, poora hi dedo! 😆"},
    {"setup": "Pathan barber shop gaya aur bola: Bhaiya, ganja kar do.", "punchline": "Barber: Thoda chhodoon? Pathan: Haan, jaan! 🤣"},
    {"setup": "Aik Pathan raat ko utha aur seedha fridge ki taraf chala gaya.", "punchline": "Fridge bola: Light band kar pehle! 😂"},
    {"setup": "Aik larka girlfriend se bola: Tum mujhse shadi karogi?", "punchline": "Girl: Pehle ghar walon se pooch lo! Larka: Wo toh mana kar rahe hain! 😆"},
    {"setup": "Aik doctor ne Pathan se poocha: Tum ne itne dinon se pills kyun nahi li?", "punchline": "Pathan: Doctor sahab, dabbi pe likha tha ‘Keep closed’! 🤣"},
    {"setup": "Ek larka apni maa se bola: Amma, main pilot ban gaya!", "punchline": "Ammi: Beta, Allah ka shukar hai. Larka: Lekin auto rickshaw ka! 😂"},
    {"setup": "Pathan ka mobile kharab ho gaya. Repair shop gaya aur bola:", "punchline": "Bhai isko theek kar do, isme sirf missed calls aati hain! 🤣"},
    {"setup": "Aik aadmi ka interview chal raha tha: Aapka experience kya hai?", "punchline": "Aadmi: Sir, main 5 saal se job dhoond raha hoon! 😆"},
    {"setup": "Biwi ne shauhar se kaha: Aaj se khana sirf pyaar se milega!", "punchline": "Shauhar: Phir mujhe MCDonald’s ka address de do! 🍔😂"},
    {"setup": "Aik Pathan kaak main se phone nikal raha tha.", "punchline": "Dost ne poocha: Kya kar raha hai? Pathan: Signal dhoond raha hoon! 🤣"},
    {"setup": "Aik Pathan ne naukri ke liye apply kiya.", "punchline": "Manager: Aapke paas experience hai? Pathan: Haan, bachpan se job dhund raha hoon! 😆"},
]

@app.get("/random_jokes")
def get_joke():
    return random.choice(pakistani_jokes)  # Ensure list is correct

