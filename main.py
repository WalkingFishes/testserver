from fastapi import FastAPI

app = FastAPI()

class Golfer:
	def __init__(self, golferId, lastName, firstName, winnings):
		self.golferId = golferId
		self.lastName = lastName
		self.firstName = firstName
		self.winnings = winnings

Golfers = [
	Golfer(1, "DeChambeau", "Bryson", 225000),
	Golfer(2, "Woods", "Tiger", 217750),
	Golfer(3, "Thomas", "Justin", 177900),
]

class User:
	def __init__(self, userId, name, golferIds):
		self.userId = userId
		self.name = name
		self.golferIds = golferIds

Users = [
	User(1, "karl1", [0,1]),
	User(2, "George 2", [0,2])
]

@app.get("/")
async def root():
	return {"message": "Hello World2"}

@app.get("/golfers")
async def read_golfers():
	return {"users": Golfers}

@app.get("/users")
async def read_users():
	return {"users": Users}

@app.get("/users/{user_id}")
async def read_user(user_id: int):
	golfers = []
	for x in Users[user_id].golferIds:
		golfers.append(Golfers[x])
	return {"user": Users[user_id], "golfers": golfers}
