class MultilevelQueue:
    def __init__(self, levels):
        self.queues = [[] for _ in range(levels)]

    def add_process(self, level, process):
        if 0 <= level < len(self.queues):
            self.queues[level].append(process)

    def execute(self):
        for level in range(len(self.queues)):
            while self.queues[level]:
                process = self.queues[level].pop(0)
                print(process)

scheduler = MultilevelQueue(3)  #3 level
scheduler.add_process(0, "P1")
scheduler.add_process(1, "P2")
scheduler.add_process(2, "P3")
scheduler.add_process(0, "P4")
scheduler.execute()
