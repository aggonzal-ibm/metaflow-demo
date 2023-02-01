from metaflow import FlowSpec, step

class CounterBranchFlow(FlowSpec):
    @step
    def start(self):
        self.creature = "dog"
        self.count = 0
        self.next(self.add_one, self.add_two) #A

    @step
    def add_one(self):
        self.count += 1
        self.next(self.join)

    @step
    def add_two(self):
        self.count += 2
        self.next(self.join)

    @step
    def join(self, inputs): #B
        self.count = max(inp.count for inp in inputs) #C
        print("count from add_one", inputs.add_one.count) #D
        print("count from add_two", inputs.add_two.count) #D
        self.creature = inputs[0].creature #E
        self.next(self.end)

    @step
    def end(self):
        print("The creature is", self.creature)
        print("The final count is", self.count)

if __name__ == '__main__':
    CounterBranchFlow()
#A A static branch is defined by giving all outbound steps as arguments to self.next
#B A join step is defined by an extra inputs argument to step
#C We take the maximum of two counts by iterating over inputs
#D We can also print out values from specific named branches
#E To re-assign unmodified artifacts, we can just refer to the first branch by index