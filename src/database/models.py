from sqlalchemy import ForeignKey, Enum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.ext.asyncio import AsyncAttrs

class Base(DeclarativeBase, AsyncAttrs):
    pass

class Task(Base):
    __tablename__ = "tasks"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    is_practical: Mapped[bool] = mapped_column(default=False)
    answers = relationship('Answer', backref='task')
    
class Answer(Base):
    __tablename__ = "answers"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    task_id: Mapped[int] = mapped_column(ForeignKey("tasks.id"))
    desc: Mapped[str] = mapped_column()
    is_correct: Mapped[bool] = mapped_column()
    