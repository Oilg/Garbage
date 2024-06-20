from fastapi import FastAPI
import uvicorn
from fastapi.routing import APIRouter
from sqlalchemy import Column, Boolean, String
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
import settings
from sqlalchemy.dialects.postgresql import UUID
import uuid
import re
from fastapi import HTTPException
from pydantic import BaseModel
from pydantic import validator

engine = create_async_engine(settings.DATABASE_URL, future=True, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    is_active = Column(Boolean(), default=True)


class UserDAL:
    """Data Access Layer for operating user info"""

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_user(
            self, name: str, last_name: str, address: str, phone: str, email: str
    ) -> User:
        new_user = User(
            name=name,
            last_name=last_name,
            address=address,
            phone=phone,
            email=email,
        )
        self.db_session.add(new_user)
        await self.db_session.flush()
        return new_user


LETTER_MATCH_PATTERN = re.compile(r"[a-яА-Яa-zA-Z\-]+$")


class TunedModel(BaseModel):
    class Config:
        """tells pydantic to convert even non dict obj to json"""

        orm_mode = True


class ShowUser(TunedModel):
    user_id: uuid.UUID
    name: str
    last_name: str
    address: str
    phone: str
    email: str
    is_active: bool


class UserCreate(BaseModel):
    name: str
    last_name: str
    address: str
    phone: str
    email: str

    @validator("name")
    def validate_name(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(
                status_code=422, detail="Name should contains only letters"
            )
        return value

    @validator("last_name")
    def validate_surname(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(
                status_code=422, detail="Last name should contains only letters"
            )
        return value


app = FastAPI(title="Garbage")

user_router = APIRouter()


async def _create_new_user(body: UserCreate) -> ShowUser:
    async with async_session() as session:
        async with session.begin():
            user_dal = UserDAL(session)
            user = await user_dal.create_user(
                name=body.name,
                last_name=body.last_name,
                address=body.address,
                phone=body.phone,
                email=body.email,
            )
            return ShowUser(
                user_id=user.user_id,
                name=body.name,
                last_name=body.last_name,
                address=body.address,
                phone=body.phone,
                email=body.email,
                is_active=user.is_active
            )


@user_router.post("/", response_model=ShowUser)
async def create_user(body: UserCreate) -> ShowUser:
    return await _create_new_user(body)


# create the instance for the routes
main_api_router = APIRouter()

main_api_router.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(main_api_router)

if __name__ == "__main__":
    # run app on the host and port
    uvicorn.run(app, host="0.0.0.0", port=8000)
