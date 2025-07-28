import json
from sqlmodel import Session

from random_bible_verse.models import Version, Book, Chapter, Verse
from random_bible_verse.db import engine, create_db_tables


def load_bible_from_json(version_name: str):
    with open(f"data/{version_name}.json") as f:
        data: dict = json.load(f)
        version = Version(name=version_name)

        for book_name, book_data in data.items():
            book = Book(name=book_name, version=version)
            version.books.append(book)

            for chapter_number, chapter_data in book_data.items():
                chapter = Chapter(number=chapter_number, book=book)
                book.chapters.append(chapter)

                for verse_number, verse_text in chapter_data.items():
                    verse = Verse(number=verse_number, text=verse_text, chapter=chapter)
                    chapter.verses.append(verse)

        with Session(engine) as session:
            session.add(version)
            session.commit()
            session.refresh(version)
            return version


if __name__ == "__main__":
    create_db_tables()
    load_bible_from_json("kjv")
    load_bible_from_json("lsg")
