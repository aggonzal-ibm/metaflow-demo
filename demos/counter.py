from metaflow import FlowSpec, step

class CounterFlow(FlowSpec):
   

    @step
    def start(self):
        """Start of the flow"""
        self.count = 0
        print("The current count is %d" % self.count)
        self.next(self.add)
        
    @step
    def add(self):
        """Add one to the counter"""
      
        self.count += 1
        print("The current count is %d" % self.count)
        self.next(self.end)
       
        

    @step
    def end(self):
        """End of the flow"""
        self.count+=1
        print("The final count is %d" % self.count)

if __name__ == '__main__':
    CounterFlow()