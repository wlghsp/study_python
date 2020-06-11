from sklearn.datasets import make_blobs

X,y = make_blobs(n_samples=150,     # make_blobs 무작위 데이터 생성
                 n_features=2,
                 centers=3,
                 cluster_std=0.5,
                 shuffle=True,
                 random_state=0)
import matplotlib.pyplot as plt

plt.scatter(X[:,0],
            X[:,1],
            c='white',
            marker='o',
            edgecolors='black',
            s=50)


from sklearn.cluster import KMeans

distortions = []
for i in range(1,11):
    km = KMeans(n_clusters=i,               # 기본 설정
                init='k-means++',      # k평균 알고리즘 설정.
                n_init=10,
                max_iter=300,   #최대 몇번 반복
                random_state=0)
    km.fit(X)
    distortions.append(km.inertia_)

y_km = km.fit_predict(X)   #군집분석 알고리즘에 의한 예측 클래스 레이블

print('왜곡: %.2f' % km.inertia_)

plt.plot(range(1,11), distortions, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Distortion')
plt.tight_layout()
plt.show()
