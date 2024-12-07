from sqlmodel import SQLModel, Field
from datetime import datetime


class VerificationTokenModel(SQLModel, table=True):
    __tablename__ = "verification_token"

    identifier: str = Field(nullable=False, primary_key=True)
    expires: datetime = Field(nullable=False)
    token: str = Field(nullable=False, primary_key=True)
    # __table_args__ = (
    #     # Ensure composite primary key
    #     {"primary_key": ("identifier", "token")},
    # )
