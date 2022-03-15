import Utility
import DBBusiness

#判断游戏是否结束
def IsGameOver(roleType):
    data = DBBusiness.GetRoles()

    #判断生存者是否唯一
    l = []
    for i in data:
        if i[2] > 0:
            l.append(i[2]) 
    
    if l.__len__ == 1:
        return True
    else:
        return False