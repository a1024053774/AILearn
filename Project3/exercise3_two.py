import numpy as np
import heapq


class State:
    def __init__(self, state, directionFlag=None, parent=None, g=0, f=None):
        self.state = state  # 此参数存储3×3阵列状态，用np.array实现
        self.direction = ['up', 'down', 'right', 'left']
        if directionFlag:
            self.direction.remove(directionFlag)
        # 记录生成此状态的移动方向，如果存在则删除该方向，避免来回反推
        self.parent = parent  # 记录父节点信息
        self.g = g  # A*算法新增：记录从初始状态到当前状态的实际步数
        self.f = f if f is not None else float('inf')  # A*算法新增： 初始化 f 值为正无穷，表示尚未计算

    def __lt__(self, other):  # A*算法新增：
        """
        实现小于操作符，使得 State 对象可以根据 f 值进行比较。
        这样它们就可以被正确地放入并从优先队列中取出。
        """
        return self.f < other.f

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

        if 'down' in self.direction and row < boarder:  # 在边界时无法再右移、下移
            s = self.state.copy()
            # 标志位symbol=0向下移动，产生新的状态节点，加入到subStates中
            temp = s.copy()
            s[row, col] = s[row + 1, col]
            s[row + 1, col] = temp[row, col]
            news = State(s, directionFlag='up', parent=self)
            subStates.append(news)

        if 'right' in self.direction and col < boarder:  # 在边界时无法再右移、下移
            s = self.state.copy()
            # 标志位symbol=0向右移动，产生新的状态节点，加入到subStates中
            temp = s.copy()
            s[row, col] = s[row, col + 1]
            s[row, col + 1] = temp[row, col]
            news = State(s, directionFlag='left', parent=self)
            subStates.append(news)
        return subStates

    # 任务2：设计启发式函数，返回一个函数值
    def heuristic(self):  # A*算法新增
        # 使用曼哈顿距离作为启发式函数
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.state[i, j] != 0:  # 忽略空白块
                    # 目标坐标
                    target_x, target_y = divmod(State.answer.flatten().tolist().index(self.state[i, j]), 3)
                    # 累加曼哈顿距离
                    distance += abs(target_x - i) + abs(target_y - j)
        return distance

    # 任务2结束

    # def BFS(self):
    #     openTable = []  # OPEN列表，存放状态的地方
    #     openTable.append(self)  # 将初始状态加入
    #     steps = 0  # 步骤
    #     if np.array_equal(s1.state, State.answer):
    #         return None, 0
    #     while len(openTable) > 0:
    #         n = openTable.pop(0)  # pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
    #         subStates = n.generateSubStates()
    #         steps += 1
    #         if steps > 100000:
    #             return None, 100000
    #         for subState in subStates:
    #             if np.array_equal(s1.state, subState):
    #                 return None, None
    #         # 查看子状态中有没有最终状态，如果有则输出之前的父状态到path中，输出steps
    #         path = []
    #         for subState in subStates:
    #             if np.array_equal(subState.state, State.answer):
    #                 while subState.parent:
    #                     path.append(subState.parent)
    #                     subState = subState.parent
    #                 path.reverse()
    #                 return path, steps  # 存在目标状态，则返回路径状态及步数
    #         # 将子状态添加到openTable中
    #         openTable.extend(subStates)
    #     else:
    #         return None, None

    # 修改BFS以跟踪探索的状态数
    def BFS(self):
        openTable = []  # OPEN列表，存放状态的地方
        openTable.append(self)  # 将初始状态加入
        steps = 0  # 步骤
        explored_states_count = 0  # 探索的状态数
        if np.array_equal(self.state, State.answer):
            return None, 0, explored_states_count
        while len(openTable) > 0:
            explored_states_count += 1  # 增加探索的状态数
            n = openTable.pop(0)
            subStates = n.generateSubStates()
            steps += 1
            if steps > 100000:
                return None, 100000, explored_states_count
            for subState in subStates:
                if np.array_equal(self.state, subState):
                    return None, None, explored_states_count
            path = []
            for subState in subStates:
                if np.array_equal(subState.state, State.answer):
                    while subState.parent:
                        path.append(subState.parent)
                        subState = subState.parent
                    path.reverse()
                    return path, steps, explored_states_count
            openTable.extend(subStates)
        else:
            return None, None, explored_states_count


class AStarSolver:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.open_table = []
        self.closed_table = set()

        heapq.heappush(self.open_table, (initial_state.heuristic(), initial_state))

        # 任务1 上行语句的作用是：
        # 将初始状态和其启发式函数值推入优先队列（open_table）。
        # 这里，启发式函数值作为元组的第一个元素，
        # 确保了状态会根据其启发式函数值的大小被排序。
        # 优先队列（最小堆）将确保具有最小启发式函数值的状态首先被取出处理。

    # def solve(self):
    #     steps = 0
    #     while self.open_table:
    #         _, current = heapq.heappop(self.open_table)
    #
    #         # 任务1 注释上面那行语句的作用是：
    #         # 从优先队列（open_table）中弹出具有最小启发式函数值的状态。
    #         # _是一个占位符，用于接收元组中的启发式函数值
    #         # 因为我们只关心状态本身，而不是它的启发式函数值。
    #         # ______________________________________________________
    #
    #         steps += 1  # 步数加1
    #
    #         if np.array_equal(current.state, State.answer):
    #             path = []
    #             while current.parent:
    #                 path.append(current)
    #                 current = current.parent
    #             path.reverse()
    #             return path, steps  # 返回路径及搜索步数
    #         self.closed_table.add(current)
    #
    #         for subState in current.generateSubStates():
    #             if subState in self.closed_table:
    #                 continue
    #             g = current.g + 1
    #             f = g + subState.heuristic()
    #             subState.g = g
    #             subState.parent = current
    #             heapq.heappush(self.open_table, (f, subState))
    #
    #             # 任务1 上行语句的作用是：
    #             # 将一个新的或更新后的子状态及其启发式函数值f推入优先队列。
    #             # f是根据子状态的启发式函数值
    #             # 和从初始状态到该子状态的已知最小成本g计算得到的。
    #             # 确保了搜索优先考虑成本较低和启发式估计较优的路径。
    #             # ______________________________________________________
    #         if steps > 10000:
    #             return None, None

    # 修改solve以跟踪探索的状态数
    def solve(self):
        steps = 0
        explored_states_count = 0  # 探索的状态数
        while self.open_table:
            explored_states_count += 1  # 增加探索的状态数
            _, current = heapq.heappop(self.open_table)
            steps += 1

            if np.array_equal(current.state, State.answer):
                path = []
                while current.parent:
                    path.append(current)
                    current = current.parent
                path.reverse()
                return path, steps, explored_states_count
            self.closed_table.add(current)

            for subState in current.generateSubStates():
                if subState in self.closed_table:
                    continue
                g = current.g + 1
                f = g + subState.heuristic()
                subState.g = g
                subState.parent = current
                heapq.heappush(self.open_table, (f, subState))
            if steps > 10000:
                return None, None, explored_states_count


State.symbol = 0
State.answer = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])
s1 = State(np.array([[1, 2, 8], [4, 0, 3], [7, 6, 5]]))
# path, steps = s1.BFS()
path, steps, bfs_explored = s1.BFS()  # 接收三个返回值
if steps == 0:
    print(f"s1就是目标状态!")
elif path:  # 找到解决方案时，输出路径
    for node in path:
        node.showInfo()  # 打印从初始状态到最终状态的中间路径
    print(State.answer)
    print(f'广度优先搜索解决了！步数为{steps}步！')
else:
    print(f'初始状态{s1.state}未能找到解决方案！已尝试步数{steps}')

astar_solver = AStarSolver(s1)
# astar_path, astar_steps = astar_solver.solve()

# 修改后的代码
astar_path, astar_steps, astar_explored = astar_solver.solve()  # 接收三个返回值

if astar_path:
    print("\nA*算法的解决方案:")
    for node in astar_path:
        node.showInfo()
    print(f'A*算法使用了搜索步数为 {astar_steps}步.')
elif astar_steps == 0:
    print(f"s1就是目标状态!")
else:
    print(f'初始状态{s1.state}未能找到解决方案！')


# if __name__ == "__main__":
#     initial_state = np.array([[0, 1, 3], [8, 2, 4], [7, 6, 5]])
#     s1 = State(initial_state)
#
#     print("开始广度优先搜索(BFS)...")
#     bfs_path, bfs_steps, bfs_explored = s1.BFS()
#     if bfs_path:
#         print(f'BFS解决了！搜索步数为{bfs_steps}步，探索了{bfs_explored}个状态。')
#     else:
#         print(f'BFS未能找到解决方案！已尝试步数{bfs_steps}，探索了{bfs_explored}个状态。')
#
#     print("\n开始A*算法...")
#     astar_solver = AStarSolver(s1)
#     astar_path, astar_steps, astar_explored = astar_solver.solve()
#     if astar_path:
#         print(f'A*算法解决了！搜索步数为{astar_steps}步，探索了{astar_explored}个状态。')
#     else:
#         print(f'A*算法未能找到解决方案！已尝试步数{astar_steps}，探索了{astar_explored}个状态。')


class BFSSolver:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.open_table = []  # 用列表来实现队列，用于存放待探索的状态
        self.closed_table = set()  # 用于存放已探索的状态

    def solve(self):
        self.open_table.append(self.initial_state)
        explored_states_count = 0

        while self.open_table:
            current_state = self.open_table.pop(0)  # 从队列中弹出第一个元素
            explored_states_count += 1

            if np.array_equal(current_state.state, State.answer):
                # 找到解决方案
                path = []
                while current_state.parent:
                    path.append(current_state)
                    current_state = current_state.parent
                path.reverse()
                return path, len(path), explored_states_count

            self.closed_table.add(current_state)

            for subState in current_state.generateSubStates():
                if subState not in self.closed_table and subState not in self.open_table:
                    self.open_table.append(subState)

        return None, None, explored_states_count

if __name__ == "__main__":
    initial_state = np.array([[2, 8, 3], [1, 6, 4], [7, 0, 5]])
    s1 = State(initial_state)

    bfs_solver = BFSSolver(s1)
    bfs_path, bfs_steps, bfs_explored = bfs_solver.solve()

    if bfs_path:
        print("BFS算法的解决方案:")
        for node in bfs_path:
            node.showInfo()
        print(f'BFS算法使用了搜索步数为 {bfs_steps}步，探索了{bfs_explored}个状态。')
    else:
        print("BFS算法未能找到解决方案。")
