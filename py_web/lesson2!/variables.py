class vegetable:
    name:str = ""
    color:str = ""
    leavesDiscription:str = ""
    steamDiscription:str = ""
    flowersDiscription:str = ""
    colories:int = 0
    count:int = 0
    numOfFlowers:int = 0
    protein:float = 0
    tallow:float = 0
    carbohydrate:float = 0
    hasLeaves:bool = False
    hasSteam:bool = False
    hasFlowers:bool = False
    averageNumOfFlowers:float = 0
    averageNumOfhasLeaves:float = 0
    
# for k in vegetable.__dict__:
#     print(k,":",type(k))
print(vegetable.__dict__)