class Multiset:
    def add(self, setA, element):
        sA = list(setA)
        sA.append(element)
        sA.sort()
        result = '{'+str(setA)[1:-1]+ '} +' +str(element) + ' ={' +str(sA)[1:-1]+'}'
        return result

    def remove_occ(self, setA, element):
        sA = list(setA)
        while element in setA: setA.remove(element)
        result = '{'+str(sA)[1:-1]+ '} /' +str(element) + ' ={' +str(setA)[1:-1]+'}'
        return result

    def multiplicity(self, setA, element):
        c = setA.count(element)
        result = 'm({'+str(setA)[1:-1]+ '} , ' +str(element) + ') = '+str(c)
        return result

    def union(self , setA , setB):
        newL = list()
        largeL = list(set(setA).union(set(setB)))
        for i in set(largeL):
            if i in setA and i in setB:
                countA = setA.count(i)
                countB = setB.count(i)
                for j in range(max([countA , countB])):
                    newL.append(i)
        
            elif i in setA and i not in setB:
                for j in range(setA.count(i)):
                    newL.append(i)
            
            elif i not in setA and i in setB:
                for j in range(setB.count(i)):
                    newL.append(i)
                
        result = '{' + str(setA)[1:-1] + '} U {' + str(setB)[1:-1] +'} = {' + str(newL)[1:-1] + '}'
        return result

    def intersection(self , setA , setB):
        newL = list()
        largeL = list(set(setA).intersection(set(setB)))
        for i in largeL:
            mini = setA.count(i) if setA.count(i) < setB.count(i) else setB.count(i)
            for j in range(mini):
                newL.append(i)
        result = '{' + str(setA)[1:-1] + '} ∩ {' + str(setB)[1:-1] +'} = {' + str(newL)[1:-1] + '}'
        return result

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
        result = '{' + str(setA)[1:-1] + '} - {' + str(setB)[1:-1] +'} = {' + str(newL)[1:-1] + '}'
        return result

if __name__ == "__main__":
    obj = Multiset()
    print(obj.add([1,2,3],1)) 
    print(obj.remove_occ([1,2,2,3,3],3)) 
    print(obj.multiplicity([1,2,2,3,3],3)) 
    print(obj.union([1,2],[1, 2, 2, 3])) 
    print(obj.intersection([1, 1, 2, 2, 3],[2, 2, 2, 3, 4]))
    print(obj.difference([1, 1, 1, 2, 2, 3],[1, 2, 2, 2]))
