import numpy as np

class Perceptron:
    def __init__(self, N, alpha):
        self.w = np.random.randn(N+1) / np.sqrt(N)  # 가중치 초기화
        self.alpha = alpha  # 학습률
        print("Perceptron class produced.")

    def step(self, x):
        if x > 0:
            return 1
        else:
            return 0

    def fit(self, X, y, epochs=10):
        X = np.c_[X, np.ones(X.shape[0])]  # 편향을 위한 열 추가
        for epoch in range(epochs):  # epoch 횟수만큼 반복
            for (x, target) in zip(X, y):
                p = self.step(np.dot(x, self.w))
                if p != target:
                    error = p - target
                    self.w += -self.alpha * error * x  # 가중치 업데이트

    def predict(self, X):
        X = np.atleast_2d(X)
        X = np.c_[X, np.ones(X.shape[0])]  # 편향을 위한 열 추가
        p = self.step(np.dot(X, self.w))
        print(p)
        print('----------------------------------')

# XOR 연산을 위한 입력과 출력 데이터
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
Y = np.array([[0], [1], [1], [0]])

per = Perceptron(2, 0.9)

# 퍼셉트론 학습
per.fit(X, Y)

# 학습된 퍼셉트론으로 XOR 연산 예측
for x in X:
    per.predict(x)