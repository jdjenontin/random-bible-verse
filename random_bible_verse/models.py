from pydantic import BaseModel, computed_field
from sqlmodel import Field, SQLModel, Relationship, Computed



class Version(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=None)
    name: str

    books : list["Book"] = Relationship(back_populates="version")

class Book(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=None)
    name: str
    version_id: int = Field(foreign_key="version.id")

    version: Version = Relationship(back_populates="books")
    chapters : list["Chapter"] = Relationship(back_populates="book")

class Chapter(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=None)
    number: int
    book_id: int = Field(foreign_key="book.id")

    book: Book = Relationship(back_populates="chapters")
    verses : list["Verse"] = Relationship(back_populates="chapter")

class Verse(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=None)
    number: int
    text: str
    chapter_id: int = Field(foreign_key="chapter.id")

    chapter: Chapter = Relationship(back_populates="verses")

class VerseDetails(BaseModel):
    version_name: str
    book_name: str
    chapter_number: int
    verse_number: int
    verse_text: str
    
    @computed_field
    def reference(self) -> str:
        return f"{self.book_name} {self.chapter_number}:{self.verse_number}, {self.version_name.upper()}"