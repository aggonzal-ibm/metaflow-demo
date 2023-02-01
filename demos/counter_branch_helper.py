from metaflow import FlowSpec, step


class CounterBranchHelperFlow(FlowSpec):
    @step
    def start(self):
        self.creature = "dog"
        self.count = 0
        self.next(self.add_one, self.add_two)

    @step
    def add_one(self):
        self.increment = 1  # A
        self.count += self.increment
        self.next(self.join)

    @step
    def add_two(self):
        self.increment = 2  # A
        self.count += self.increment
        self.next(self.join)
        
    @step
    def join(self, inputs):
        self.count = max(inp.count for inp in inputs)
        print("count from add_one", inputs.add_one.count)
        print("count from add_two", inputs.add_two.count)
        self.merge_artifacts(inputs, exclude=['increment'])  # B
        self.next(self.end)
    
    
    @step
    def end(self):
        print("The creature is", self.creature)
        print("The final count", self.count)


if __name__ == '__main__':
    CounterBranchHelperFlow()

#A The value of increment diverges between the two branches
#B We must explicitly ignore the diverged artifact, since we are not handling it explicitly 