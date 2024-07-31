from sqlmodel import Session, select

from random_bible_verse.models import Version, Book, Chapter, Verse, VerseDetails
from random_bible_verse.db import engine
import random

def get_versions():
    """Get available versions"""
    with Session(engine) as session:
        statement = select(Version)
        versions = session.exec(statement).all()
        return versions

def get_version(version_name : str) -> Version:
    """Get a version by name

    Args:
        version_name (str): The name of the bible version (ex : KJV/LSG)

    Returns:
        Version: The correspondin version
    """
    with Session(engine) as session:
        statement = select(Version).where(Version.name == version_name)
        version = session.exec(statement).first()
        return version
    

def get_books(version_name : str) -> list[Book]:
    """Get books of a version

    Args:
        version_name (str): The name of the bible version

    Raises:
        ValueError: If the version is not found

    Returns:
        list[Book]: List of books
    """

    version = get_version(version_name)
    if not version:
        raise ValueError(f"Version {version_name} not found")
    
    with Session(engine) as session:
        statement = select(Book).where(Book.version_id == version.id)
        books = session.exec(statement).all()
        return books
    
def get_book(version_name : str, book_name : str) -> Book:
    """Get a book by name and version

    Args:
        version_name (str): The name of the version
        book_name (str): The name of the book

    Raises:
        ValueError: If the version or the book is not found

    Returns:
        Book: The book
    """

    version = get_version(version_name)
    if not version:
        raise ValueError(f"Version {version_name} not found")
    
    with Session(engine) as session:
        statement = select(Book).where(Book.version_id == version.id).where(Book.name == book_name)
        book = session.exec(statement).first()
        return book

def get_chapters(version_name : str, book_name : str) -> list[Chapter]:
    """Get chapters of a book

    Args:
        version_name (str): The name of the version
        book_name (str): The name of the book

    Raises:
        ValueError: If the book is not found

    Returns:
        list[Chapter]: List of chapters
    """

    book = get_book(version_name, book_name)
    if not book:
        raise ValueError(f"Book {book_name} not found in version {version_name}")
    
    with Session(engine) as session:
        statement = select(Chapter).where(Chapter.book_id == book.id)
        chapters = session.exec(statement).all()
        return chapters

def get_chapter(version_name : str, book_name : str, chapter_number : int) -> Chapter:
    """Get a chapter by number, book and version

    Args:
        version_name (str): The name of the version
        book_name (str): The name of the book
        chapter_number (int): The number of the chapter

    Raises:
        ValueError: If the chapter is not found

    Returns:
        Chapter: The chapter
    """

    book = get_book(version_name, book_name)
    if not book:
        raise ValueError(f"Book {book_name} not found in version {version_name}")
    
    with Session(engine) as session:
        statement = select(Chapter).where(Chapter.book_id == book.id).where(Chapter.number == chapter_number)
        chapter = session.exec(statement).first()
        return chapter
    
def get_verses(version_name : str, book_name : str, chapter_number : int) -> list[VerseDetails]:
    """Get verses of a chapter

    Args:
        version_name (str): The name of the version
        book_name (str): The name of the book
        chapter_number (int): The number of the chapter

    Raises:
        ValueError: If the chapter is not found

    Returns:
        list[VerseDetails]: List of verses
    """

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
    
def get_verse(version_name : str, book_name : str, chapter_number : int, verse_number : int) -> VerseDetails:
    """Get a verse by number, chapter, book and version

    Args:
        version_name (str): The name of the version
        book_name (str): The name of the book
        chapter_number (int): The number of the chapter
        verse_number (int): The number of the verse

    Raises:
        ValueError: If the verse is not found

    Returns:
        VerseDetails: The verse
    """

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
    

def get_random_book(version_name : str) -> Book:
    """Get a random book from a version

    Args:
        version_name (str): The name of the version

    Returns:
        Book: The random book
    """

    pass

def get_random_chapter(version_name : str, book_name : str) -> Chapter:
    """Get a random chapter from a book

    Args:
        version_name (str): The name of the version
        book_name (str): The name of the book

    Returns:
        Chapter: The random chapter
    """

    pass

def get_random_verse(version_name : str, book_name : str, chapter_number : int) -> VerseDetails:
    """Get a random verse from a chapter

    Args:
        version_name (str): The name of the version
        book_name (str): The name of the book
        chapter_number (int): The number of the chapter

    Returns:
        VerseDetails: The random verse
    """

    pass

def get_random_verse_from_version(version_name : str) -> VerseDetails:
    """Get a random verse from a version

    Args:
        version_name (str): The name of the version

    Returns:
        VerseDetails: The random verse
    """
    
    pass
    
