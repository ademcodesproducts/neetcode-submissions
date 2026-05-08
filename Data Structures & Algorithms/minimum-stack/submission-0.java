class MinStack {

    private Stack<Integer> stk;

    public MinStack() {
        this.stk = new Stack<>();
    }
    
    public void push(int val) {
        stk.push(val);
    }
    
    public void pop() {
        stk.pop();
    }
    
    public int top() {
        return stk.peek();
    }
    
    public int getMin() {

        Stack<Integer> minStk = new Stack<>();
        int minimum = stk.peek();

        while (!stk.isEmpty()) {

            if (minimum > stk.peek()) {
                minimum = stk.peek();
            } 
            minStk.push(stk.pop());
        }

        while (!minStk.isEmpty()) {
            stk.push(minStk.pop());
        }

        return minimum;
    }
}
