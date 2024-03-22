import numpy as np

class Percetron :
    def __init__(self, N, alpha) :
        self.w = np.random.randn(N+1) / np.sqrt(N) #w1, w1...
        self.alpha = alpha # Learning rate
        print("Percetron class produced.")
        
    def step(self, x) :
        if x > 0 :
            return 1
        else :
            return 0
        
    def fit(self, X, y, epochs = 10) :
        X = np.c_[X, np.ones(X.shape[0])]
        for epoch in range(epochs) : # 10 times loop
            for (x, target) in zip(X, y) : 
                p = self.step(np.dot(x, self.w))
                if p != target :
                    error = p - target
                    self.w += -self.alpha*error*x
                
    def predict(self, X) :
        X = np.atleast_2d(X)
        X = np.c_[X, np.ones(1)]
        p = self.step(np.dot(X, self.w))
        print(p)
        print('----------------------------------')
        
per = Percetron(2, 0.9)

X = np.array([[0,0], [0,1], [1,0], [1,1]])

Y = np.array([[0], [0], [0], [1]])

per.fit(X, Y)

x = np.array([0,0])
per.predict(x)

x = np.array([1,0])
per.predict(x)

x = np.array([0,1])
per.predict(x)

x = np.array([1,1])
per.predict(x)

