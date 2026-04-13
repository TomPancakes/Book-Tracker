#BOOK TRACKER APP W/ DATABASE INTEGRATION


#Import libraries
import sqlalchemy as sa


#Set up Database
engine = sa.create_engine("sqlite:///books.db")
connection = engine.connect()

metadata = sa.MetaData()

books_table = sa.Table(
    "books",
    metadata,
    #columns go here
    sa.Column('id', sa.Integer, primary_key=True, autoincrement=True), #PrimaryKey is UNIQUE identifier. 
    sa.Column('title', sa.String), #Frieren
    sa.Column('score', sa.Integer), #86
    sa.Column('status', sa.String), #READING, PAUSED, DROPPED, COMPLETED

)

