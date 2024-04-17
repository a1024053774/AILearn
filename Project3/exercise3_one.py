import numpy as np

class State:
    def __init__(self, state, directionFlag=None, parent=None):
        self.state = state #此参数存储3×3阵列状态，用np.array实现
        self.direction = ['up', 'down', 'right', 'left']
        if directionFlag:
            self.direction.remove(directionFlag)
        # 记录生成此状态的移动方向，如果存在则删除该方向，避免来回反推
        self.parent = parent #记录父节点信息

    def showInfo(self):
        for i in range(3):
            for j in range(3):
                print(self.state[i, j], end='  ')
            print("\n")
        print('->')
        return

    def getEmptyPos(self):
        postion = np.where(self.state == self.symbol)
        return postion

    def generateSubStates(self):  # 产生子节点
        if not self.direction:
            return []
        subStates = []
        boarder = len(self.state) - 1
        # the maximum of the x,y
        row, col = self.getEmptyPos()
        if 'left' in self.direction and col > 0:  # 向左移动
            s = self.state.copy()
            # 标志位symbol=0向左移动，产生新的状态节点，加入到subStates中
            temp = s.copy()
            s[row, col] = s[row, col - 1]
            s[row, col - 1] = temp[row, col]
            news = State(s, directionFlag='right', parent=self)
            subStates.append(news)

        if 'up' in self.direction and row > 0:
            s = self.state.copy()
            # 标志位symbol=0向上移动，产生新的状态节点，加入到subStates中
            temp = s.copy()
            s[row, col] = s[row - 1, col]
            s[row - 1, col] = temp[row, col]
            news = State(s, directionFlag='down', parent=self)
            subStates.append(news)

        if 'down' in self.direction and row < boarder:  #在最大边界时无法再右移或下移
            s = self.state.copy()
            # 标志位symbol=0向下移动，产生新的状态节点，加入到subStates中
            temp = s.copy()
            s[row, col] = s[row + 1, col]
            s[row + 1, col] = temp[row, col]
            news = State(s, directionFlag='up', parent=self)
            subStates.append(news)
####任务1 参照以上代码，增加标志位右移产生新状态节点的代码

        if 'right' in self.direction and col < boarder:  # 向右移动
            s = self.state.copy()
            temp = s[row, col + 1]
            s[row, col + 1] = self.symbol
            s[row, col] = temp
            news = State(s, directionFlag='left', parent=self)
            subStates.append(news)

####任务1结束############## 
        return subStates

#BFS广度优先搜索算法
    def BFS(self):
        openTable = []  # OPEN列表，存放状态的地方
        openTable.append(self)  # 将初始状态加入
        steps = 0  # 步骤
        while len(openTable) > 0:
            n = openTable.pop(0)  # pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
            subStates = n.generateSubStates()
            steps += 1
            if steps > 100000:
                return None, 100000
            for subState in subStates:
                if np.array_equal(s1.state, subState):
                    return None, None
            # 查看子状态中有没有最终状态，如果有则输出之前的父状态到path中，输出steps
            path = []
            for subState in subStates:
                if np.array_equal(subState.state, State.answer):
                    while subState.parent:
                        path.append(subState.parent)
                        subState = subState.parent
                    path.reverse()
                    return path, steps#存在目标状态，则返回路径状态及步数
            # 将子状态添加到openTable中
            openTable.extend(subStates)
        else:
            return None, None

####任务2 参照广度优先搜索算法代码，编写深度优先搜索算法
    # def DFS(self):
    def DFS(self, visited=None, path=None, steps=0):
        if visited is None:
            visited = []
        if path is None:
            path = []

        visited.append(self.state.tobytes())  # 将状态转换为字节串以便存储
        steps += 1
        if steps > 100000:
            return None, 100000

        if np.array_equal(self.state, State.answer):
            return path, steps

        subStates = self.generateSubStates()
        for subState in subStates:
            if subState.state.tobytes() not in visited:
                path.append(subState)
                result_path, result_steps = subState.DFS(visited, path, steps)
                if result_path is not None:
                    return result_path, result_steps
                path.pop()  # 回溯
        return None, None


####任务2 ################

State.symbol = 0
State.answer = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])
s1 = State(np.array([[0, 1, 3], [8, 2, 4], [7, 6, 5]]))
path, steps = s1.BFS()
if path:  # 找到解决方案时，输出路径
    for node in path:
        node.showInfo()        # 打印从初始状态到最终状态的中间路径
    print(State.answer)
    print(f'广度优先搜索算法解决了！搜索步数为{steps}步！')
else:
    print(f'初始状态{s1.state}未能找到解决方案！已尝试步数{steps}')

####任务3 添加相应的代码，以比较BFS和DFS两种算法################
if __name__ == "__main__":
    initial_state = np.array([[0, 1, 3], [8, 2, 4], [7, 6, 5]])
    s1 = State(initial_state)

    print("开始广度优先搜索(BFS)...")
    path, steps = s1.BFS()
    if path:  # 找到解决方案时，输出路径
        print(f'BFS解决了！搜索步数为{steps}步！')
    else:
        print(f'初始状态{s1.state}未能找到解决方案！已尝试步数{steps}')

    print("\n开始深度优先搜索(DFS)...")
    path, steps = s1.DFS()
    if path is not None:  # 找到解决方案时，输出路径
        print(f'DFS解决了！搜索步数为{steps}步！')
    else:
        print(f'初始状态{s1.state}未能找到解决方案！已尝试步数{steps}')
####任务3结束################