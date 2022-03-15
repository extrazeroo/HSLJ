import Utility
import DBBusiness

#判断优先行动方
def GetActiveRole():
    data = DBBusiness.GetRolesByCampFamilyRole()

    #暂时仅用个人速度作为优先行动判断条件
    l = []
    for i in data:
        l.append(i[7]) 
    cnt = Utility.GetRandomObjectListMaxPR(l)
    return data[cnt][0]

#判断被动接收方 （暂时现为个人）
def GetPassiveRole():
    data = DBBusiness.GetRolesByCampFamilyRole()

    #暂时仅用个人速度作为滞后行动判断条件
    l = []
    for i in data:
        l.append(i[7]) 
    cnt = Utility.GetRandomObjectListMinPR(l)
    return data[cnt][0]
