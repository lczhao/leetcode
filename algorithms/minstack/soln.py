class MinStack:
   
    def __init__(self):
        self.stack = [];
        self.minValues = [];
    
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x);
        if self.minValues == []:
            self.minValues.append(x);
        else:
            if self.minValues[-1] >= x:
                self.minValues.append(x);
        return;
        
    # @return nothing
    def pop(self):
        s = self.stack.pop();
        if s == self.minValues[-1]:
            self.minValues.pop();
            
    # @return an integer
    def top(self):
        return self.stack[-1];
    # @return an integer
    def getMin(self):
        return self.minValues[-1];