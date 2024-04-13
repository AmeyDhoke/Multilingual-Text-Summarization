from typing import Union, Optional 
from fastapi import FastAPI, Path
import torch
from transformers import pipeline
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    'http://localhost:5173',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)

@app.get("/")
def read_root():
    return {"hello": "world"}

students = {
    1: {
        "name": "john",
        "age": 17,
        "year": "year 12"
    }
}


class Student(BaseModel):
    name: str
    age: int
    year: str



@app.get("/text/summarize")
def getsummarize(text_to_summarize: str):
    print("I got the request")
    summarizer = pipeline("summarization", "pszemraj/long-t5-tglobal-base-16384-book-summary")
    result = summarizer(text_to_summarize)
    return {"result": result[0]['summary_text']}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.get('/student/{id}')
def getidinfo(id: int):
    return students[id]


@app.get("/get-by-name")
def get_student(name: str):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"data": "not found"}


@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "This student already exsists"}
    students[student_id] = student
    return students[student_id]


@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: Student):
    if student_id not in students:
        return {"Error": "This student does not exists in the data"}
    students[student_id] = student
    return students[student_id]



'''A young girl named Alice sits bored by a riverbank, where she suddenly spots a White Rabbit with a pocket watch and waistcoat lamenting that he is late. The surprised Alice follows him down a rabbit hole, which sends her down a lengthy plummet but to a safe landing. Inside a room with a table, she finds a key to a tiny door, beyond which is a beautiful garden. As she ponders how to fit through the door, she discovers a bottle reading "Drink me". Alice hesitantly drinks a portion of the bottle's contents, and to her astonishment, she shrinks small enough to enter the door. However, she had left the key upon the table and is unable to reach it. Alice then discovers and eats a cake, which causes her to grow to a tremendous size. As the unhappy Alice bursts into tears, the passing White Rabbit flees in a panic, dropping a fan and pair of gloves. Alice uses the fan for herself, which causes her to shrink once more and leaves her swimming in a pool of her own tears. Within the pool, Alice meets a variety of animals and birds, who convene on a bank and engage in a "Caucus Race" to dry themselves. Following the end of the race, Alice inadvertently frightens the animals away by discussing her cat.


The Cheshire Cat
The White Rabbit appears in search of the gloves and fan. Mistaking Alice for his maidservant, the White Rabbit orders Alice to go into his house and retrieve them. Alice finds another bottle and drinks from it, which causes her to grow to such an extent that she gets stuck within the house. The White Rabbit and his neighbors attempt several methods to extract her, eventually taking to hurling pebbles that turn into small cakes. Alice eats one and shrinks herself, allowing her to flee into the forest. She meets a Caterpillar seated on a mushroom and smoking a hookah. Amidst the Caterpillar's questioning, Alice begins to admit to her current identity crisis, compounded by her inability to remember a poem. Before crawling away, the Caterpillar tells her that a bite of one side of the mushroom will make her larger, while a bite from the other side will make her smaller. During a period of trial and error, Alice's neck extends between the treetops, frightening a pigeon who mistakes her for a serpent. After shrinking to an appropriate height, Alice arrives at the home of a Duchess, who owns a perpetually grinning Cheshire Cat. The Duchess's baby, whom she hands to Alice, transforms into a piglet, which Alice releases into the woods. The Cheshire Cat appears to Alice and directs her toward the Hatter and March Hare before disappearing, leaving his grin behind. Alice finds the Hatter, March Hare, and a sleepy Dormouse in the midst of an absurd tea party. The Hatter explains that it is always 6 pm (tea time), claiming that time is standing still as punishment for the Hatter trying to "kill it". A strange conversation ensues around the table, and the riddle "Why is a raven like a writing desk?" is brought forward. Eventually, Alice impatiently decides to leave, dismissing the affair as "the stupidest tea party that [she has] ever been to".


Alice trying to play croquet with a Flamingo
Noticing a door on one of the trees, Alice passes through and finds herself back in the room from the beginning of her journey. She is able to take the key and use it to open the door to the garden, which turns out to be the croquet court of the Queen of Hearts, whose guard consists of living playing cards. Alice participates in a croquet game, in which hedgehogs are used as balls, flamingos are used as mallets, and soldiers act as gates. The Queen proves to be short-tempered, and she constantly orders beheadings. When the Cheshire Cat appears as only a head, the Queen orders his beheading, only to be told that such an act is impossible. Because the cat belongs to the Duchess, Alice prompts the Queen to release the Duchess from prison to resolve the matter. When the Duchess ruminates on finding morals in everything around her, the Queen dismisses her on the threat of execution. Alice then meets a Gryphon and a weeping Mock Turtle, who dance to the Lobster Quadrille while Alice recites (rather incorrectly) "'Tis the Voice of the Lobster". The Mock Turtle sings them "Beautiful Soup" during which the Gryphon drags Alice away for an impending trial, in which the Knave of Hearts stands accused of stealing the Queen's tarts. The trial is ridiculously conducted by the King of Hearts, and the jury is composed of various animals that Alice had previously met. Alice gradually grows in size and confidence, allowing herself increasingly frequent remarks on the irrationality of the proceedings. The Queen finally commands Alice's beheading, but Alice scoffs that the Queen's guard is only a pack of cards. Although Alice holds her own for a time, the card guards soon gang up and start to swarm all over her. Alice's sister wakes her up from a dream, brushing what turns out to be some leaves from Alice's face. Alice leaves her sister on the bank to imagine all the curious happenings for herself.'''