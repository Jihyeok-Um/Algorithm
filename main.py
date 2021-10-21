import sys
treeList = []
treeDic = {}
input = sys.stdin.readline
while (True):
    tree = input().rstrip()
    if not tree:
        break
    treeList.append(tree)
    treeDic[tree] = 0

for i in range(len(treeList)):
    treeDic[treeList[i]] += 1

sortedTreeDic = sorted(treeDic.items())
for i in range(len(sortedTreeDic)):
    print("%s %.4f" % (sortedTreeDic[i][0], (sortedTreeDic[i][1]/len(treeList))*100))
