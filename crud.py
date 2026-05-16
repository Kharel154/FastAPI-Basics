from fastapi import FastAPI, HTTPException, status



Books = [
    {
        "id": 1,
        "title": "The Great Gatsby", 
        "author": "F. Scott Fitzgerald"
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee"
    },
    {
        "id": 3,
        "title": "1984",
        "author": "George Orwell"
    },
    {
        "id": 4,
        "title": "Pride and Prejudice",
        "author": "Jane Austen"
    },
    {
        "id": 5,
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger"
    }
]

app = FastAPI()

@app.get("/books")
def get_books():
    return Books

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in Books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")