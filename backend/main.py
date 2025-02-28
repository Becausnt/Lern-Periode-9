from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import Response, status
from pydantic import BaseModel  
import json
from math import log

# vars --- replace with db later on
base_exp = 50
growth_rate = 1.35

class GoalData(BaseModel):
    name: str
    description: str
    hours_spent: float

class UserData(BaseModel):
    name: str
    bio: str
    exp: int
    total_hours:float
    def add_exp(exp_to_add: int):
        self.exp += exp_to_add
    @property
    def level(self):
        return log(1 + (self.exp * (growth_rate - 1)) / base_exp) / log(growth_rate)

# Database
user_db = {}
goal_db = {}

# utility functions
def format_goal_response(goal: GoalData, goal_id: int) -> str:
        response_data = f'"{goal_id}": {goal_db[goal_id].model_dump_json()}'
        response_data = '{' + response_data + '}'
        return response_data
def format_user_response(goal: UserData, user_id: int) -> str:
        response_data = f'"{user_id}": {user_db[user_id].model_dump_json()}'
        response_data = '{' + response_data + '}'
        return response_data

# Example data
example_user = UserData(name="Becausnt", bio="Nah.", exp=100, total_hours=2)
user_db[0] = example_user
example_goal = GoalData(name="Learn to draw", description="Sketch, whatever", hours_spent=0)
goal_db[0] = example_goal

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hosted with FastAPI"}

# ------------------------------- GOALS ------------------------------------
# ---------- CREATE -------------
@app.post("/goals")
async def post_goal(goal: GoalData):

    last_key = int(list(goal_db)[len(list(goal_db)) -1])
    goal_db[int(last_key) + 1] = goal
    response_data = format_goal_response(goal_db[last_key + 1], last_key + 1)

    return Response(content=response_data, status_code=status.HTTP_201_CREATED, media_type='application/json')


# ---------- READ -------------
@app.get("/goals")
async def read_goals():
    return goal_db

@app.get("/goals/{goal_id}")
async def read_goal(goal_id: int):
    return goal_db[goal_id]


# ---------- UPDATE -------------
@app.put("/goals/{goal_id}")
async def put_goal(goal: GoalData, goal_id: int):
    try:
        goal_db[goal_id] = goal

        response_data = format_goal_response(goal_db[goal_id], goal_id)

        return Response(content=response_data, status_code=200)
    except:
        return HTTPException(detail="Invalid id or data", status_code=400)

@app.put("/goals/{goal_id}/{hours_to_add}")
async def put_goal(goal_id: int, hours_to_add: float):
    try:
        goal_id = int(goal_id)
        hours_to_add = float(hours_to_add)

        goal_db[goal_id].hours_spent += hours_to_add

        response_data = format_goal_response(goal_db[goal_id], goal_id)

        return Response(content=response_data, status_code=200)
    except:
        return HTTPException(detail=f"Invalid id '{goal_id}'(int) or hours '{hours_to_add}'(float)", status_code=400)


# ---------- DELETE -------------
@app.delete("/goals/{goal_id}")
async def delete_goal(goal_id: int):
    if goal_id not in goal_db:
        return HTTPException(status_code=404, detail="Goal not found")
        
    goal_id = int(goal_id)
    del goal_db[goal_id]
    return Response(content='{"msg": "Delete successful"}', status_code=200)



# ------------------------------- USER ------------------------------------
# ---------- CREATE -------------
@app.post("/users")
async def create_user(user: UserData):
    last_key = int(list(user_db)[len(list(user_db)) -1])
    user_db[int(last_key) + 1] = user
    response_data = format_user_response(user_db[last_key + 1], last_key + 1)

    return Response(content=response_data, status_code=201, media_type='application/json')
# ---------- READ -------------
@app.get("/users")
async def get_users():
    return user_db

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return Response(content=user_db[user_id].model_dump_json(), status_code=200)

# ---------- UPDATE -------------
@app.put("/users/{user_id}")
async def update_user(user: UserData, user_id: int):
    try:
        user_db[user_id] = user

        response_data = format_user_response(user_db[user_id], user_id)

        return Response(content=response_data, status_code=200)
    except:
        return HTTPException(detail="Invalid id or data", status_code=400)
    
@app.put("/users/{user_id}/{hours_to_add}")
async def put_user(user_id: int, hours_to_add: float):
    try:
        user_id = int(user_id)
        hours_to_add = float(hours_to_add)

        user_db[user_id].total_hours += hours_to_add

        response_data = format_user_response(user_db[user_id], user_id)

        return Response(content=response_data, status_code=200)
    except:
        return HTTPException(detail=f"Invalid id '{user_id}'(int) or hours '{hours_to_add}'(float)", status_code=400)

# ---------- DELETE -------------
@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    if user_id not in user_db:
        return HTTPException(status_code=404, detail="Uesr not found")
        
    user_id = int(user_id)
    del user_db[user_id]
    return Response(content='{"msg": "Delete successful"}', status_code=200)


# TODO
## track hours spent on goal
