import sqlalchemy

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, sqlalchemy.Identity(), nullable=False, primary_key=True),
    sqlalchemy.Column("first_name", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("last_name", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("address", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("phone", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("email", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("is_active", sqlalchemy.Boolean, default=True),
)