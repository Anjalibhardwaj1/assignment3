class Multiset:
    def add(self, setA, element):
        newL = list(setA)
        newL.append(element)
        newL.sort()
        res = '{'+str(setA)[1:-1]+ '} +' +str(element) + ' = {' +str(newL)[1:-1]+'}'
        return res

    def remove_occ(self, setA, element):
        newL = list(setA)
        while element in setA: setA.remove(element)
        res = '{'+str(newL)[1:-1]+ '} /' +str(element) + ' ={' +str(setA)[1:-1]+'}'
        return res

    def multiplicity(self, setA, element):
        c = setA.count(element)
        res = 'm({'+str(setA)[1:-1]+ '} , ' +str(element) + ') = '+str(c)
        return res

    def union(self , setA , setB):
        c = list()
        newL = list(set(setA).union(set(setB)))
        for i in set(newL):
            if i in setA and i in setB:
                countA = setA.count(i)
                countB = setB.count(i)
                for j in range(max([countA , countB])):
                    c.append(i)
        
            elif i in setA and i not in setB:
                for j in range(setA.count(i)):
                    c.append(i)
            
            elif i not in setA and i in setB:
                for j in range(setB.count(i)):
                    c.append(i)
                
        res = '{' + str(setA)[1:-1] + '} U {' + str(setB)[1:-1] +'} = {' + str(c)[1:-1] + '}'
        return res

    def intersection(self , setA , setB):
        c = list()
        newL = list(set(setA).intersection(set(setB)))
        for i in newL:
            mini = setA.count(i) if setA.count(i) < setB.count(i) else setB.count(i)
            for j in range(mini):
                c.append(i)
        res = '{' + str(setA)[1:-1] + '} ∩ {' + str(setB)[1:-1] +'} = {' + str(c)[1:-1] + '}'
        return res

    def difference(self , setA , setB):
        newL = list()
        for i in set(setA):
            if i not in setB:
                for j in range(setA.count(i)):
                    newL.append(i)
            else:
                a_b = setA.count(i)-setB.count(i)
                for x in range(a_b):
                    newL.append(i)
        res = '{' + str(setA)[1:-1] + '} - {' + str(setB)[1:-1] +'} = {' + str(newL)[1:-1] + '}'
        return res

if __name__ == "__main__":
    obj = Multiset()
    print(obj.add([1,2,3],1)) 
    print(obj.remove_occ([1,1,2,3],1)) 
    print(obj.multiplicity([1,1,1,2,2,3],1)) 
    print(obj.union([1,2],[2, 2, 3])) 
    print(obj.intersection([1, 1, 2, 2, 3],[2, 2, 2, 3, 4]))
    print(obj.difference([1, 1, 1, 2, 2, 3],[1, 2, 2, 2]))
