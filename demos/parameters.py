from metaflow import FlowSpec, step, Parameter

class ParameterFlow(FlowSpec):
    """A flow that takes a parameter"""

    # The parameter is defined as a class variable
    # with a default value
    animal = Parameter('creature', help="Specify a creature", required=True)
    count = Parameter('count', help="Numbers of creatures", default=1)
    ratio = Parameter('ratio', help="Ratio of creatures between 0.0  and 1.0", type=float)

    @step
    def start(self):
        print(self.animal, "is a sttring of", len(self.animal), "characters")
        print(self.count, "is an integer of value", self.count)
        print(self.ratio, "is a float of value", self.ratio)
        self.next(self.end)
        

    @step
    def end(self):
        """End of the flow"""
        print("done")
        
if __name__ == '__main__':
    ParameterFlow()