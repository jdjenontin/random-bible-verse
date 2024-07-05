from sqlmodel import Session, select

from random_bible_verse.models import Version, Book, Chapter, Verse, VerseDetails
from random_bible_verse.db import engine
import random

def get_versions():
    """Get all versions"""
    with Session(engine) as session:
        statement = select(Version)
        versions = session.exec(statement).all()
        return versions

def get_version(version_name : str):
    with Session(engine) as session:
        statement = select(Version).where(Version.name == version_name)
        version = session.exec(statement).first()
        return version
    

def get_books(version_name : str):
    version = get_version(version_name)
    if not version:
        raise ValueError(f"Version {version_name} not found")
    
    with Session(engine) as session:
        statement = select(Book).where(Book.version_id == version.id)
        books = session.exec(statement).all()
        return books
    
def get_book(version_name : str, book_name : str):
    version = get_version(version_name)
    if not version:
        raise ValueError(f"Version {version_name} not found")
    
    with Session(engine) as session:
        statement = select(Book).where(Book.version_id == version.id).where(Book.name == book_name)
        book = session.exec(statement).first()
        return book

def get_chapters(version_name : str, book_name : str):
    book = get_book(version_name, book_name)
    if not book:
        raise ValueError(f"Book {book_name} not found in version {version_name}")
    
    with Session(engine) as session:
        statement = select(Chapter).where(Chapter.book_id == book.id)
        chapters = session.exec(statement).all()
        return chapters

def get_chapter(version_name : str, book_name : str, chapter_number : int):
    book = get_book(version_name, book_name)
    if not book:
        raise ValueError(f"Book {book_name} not found in version {version_name}")
    
    with Session(engine) as session:
        statement = select(Chapter).where(Chapter.book_id == book.id).where(Chapter.number == chapter_number)
        chapter = session.exec(statement).first()
        return chapter
    
def get_verses(version_name : str, book_name : str, chapter_number : int):
    chapter = get_chapter(version_name, book_name, chapter_number)
    if not chapter:
        raise ValueError(f"Chapter {chapter_number} not found in book {book_name} in version {version_name}")
    
    with Session(engine) as session:
        statement = select(Verse).where(Verse.chapter_id == chapter.id)
        verses = session.exec(statement).all()

        verses = [VerseDetails(
            version_name=version_name,
            book_name=book_name,
            chapter_number=chapter_number,
            verse_number=verse.number,
            verse_text=verse.text
        ) for verse in verses]
        
        return verses
    
def get_verse(version_name : str, book_name : str, chapter_number : int, verse_number : int):
    chapter = get_chapter(version_name, book_name, chapter_number)
    if not chapter:
        raise ValueError(f"Chapter {chapter_number} not found in book {book_name} in version {version_name}")
    
    with Session(engine) as session:
        statement = select(Verse).where(Verse.chapter_id == chapter.id).where(Verse.number == verse_number)
        verse = session.exec(statement).first()
        return VerseDetails(
            version_name=version_name,
            book_name=book_name,
            chapter_number=chapter_number,
            verse_number=verse_number,
            verse_text=verse.text
        
        )
    

def get_random_book(version_name : str):
    books = get_books(version_name)
    return random.choice(books)

def get_random_chapter(version_name : str, book_name : str):
    chapters = get_chapters(version_name, book_name)
    return random.choice(chapters)

def get_random_verse(version_name : str, book_name : str, chapter_number : int):
    verses = get_verses(version_name, book_name, chapter_number)
    return random.choice(verses)

def get_random_verse_from_version(version_name : str):
    book = get_random_book(version_name)
    chapter = get_random_chapter(version_name, book.name)
    verse = get_random_verse(version_name, book.name, chapter.number)
    return verse
    

if __name__ == "__main__":
    v = get_random_verse_from_version("lsg")
    print(v)