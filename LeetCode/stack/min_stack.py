"""
155. Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_list = []
        if len(self.min_list) > 0:
            self.min = self.min_list[-1]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if len(self.min_list) == 0:
            self.min = x
            self.min_list.append(x)

        if x < self.min:
            self.min = x
            self.min_list.append(x)

    def pop(self):
        """
        :rtype: None
        """
        popped = self.stack.pop()
        if popped == self.min:
            self.min_list.remove(popped)
            self.min = self.min_list[-1]

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min


if __name__ == "__main__":
    obj = MinStack()
    obj.push(1)
    obj.push(3)
    print("TOP: ", obj.top())
    print("MIN: ", obj.getMin())
    obj.push(-3)
    print("MIN: ", obj.getMin())
    print("TOP: ", obj.top())
    obj.pop()
    print("TOP: ", obj.top())
    print("MIN: ", obj.getMin())
