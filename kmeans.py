import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from os.path import join, normpath, split
logs = []

with open(join(normpath(join(split(__file__)[0], "../logs")), "mean_logs.txt")) as f:
    j = 0
    for line in f.readlines():
        logs.append(float(line))
        j+=1


data = np.array([log for log in logs]).reshape(-1, 1)

k = 8
model = KMeans(n_clusters=k, n_init='auto', random_state=97)
model.fit(data)

labels = model.labels_
centroids = model.cluster_centers_.flatten()

# Индексы строк
indices = np.arange(len(data))

result_indices = {}

for cluster_id in range(k):
    # индексы точек, принадлежащих кластеру
    cluster_points_idx = np.where(labels == cluster_id)[0]

    
    # значения этих точек
    cluster_points = data[cluster_points_idx].flatten()
    
    # центроид
    centroid = centroids[cluster_id]
    
    # расстояния до центроида
    distances = np.abs(cluster_points - centroid)
    
    # сортировка по расстоянию
    sorted_idx = np.argsort(distances)
    
    # берём 10 ближайших
    top_10_idx = cluster_points_idx[sorted_idx[:10]]
    
    result_indices[cluster_id] = [top_10_idx, len(cluster_points_idx)]

# вывод
centers = []
for cluster_id, idxs in result_indices.items():
    print(f"Кластер {cluster_id}: Количество: {idxs[1]}, top 10: {idxs[0]}")
    centers.append(idxs[0][0])

centers.sort()
centers = [str(i) for i in centers]
print("./compile.sh \\{"+",".join(centers)+"\\} 10 mean_clusters")

print("../bin/run_hotspots ", end = "" )
for i in centers:
    print(f"../logs/mean_clusters{i[0][0]} 10 ", end="")

# ---- ВИЗУАЛИЗАЦИЯ ----
plt.figure(figsize=(10, 6))

plt.scatter(data.flatten(), indices, c=labels, s=20, cmap='tab10')

# Отметим центры кластеров линиями
for c in centroids:
    plt.axvline(c, color='red', linestyle='--', alpha=0.6)

plt.xlabel("Значение логов")
plt.ylabel("Порядковый номер строки")
plt.title("K-Means на 1D данных (ось Y — индекс элемента)")
plt.gca().invert_yaxis()  # Чтобы 0 был сверху (как в файле)
plt.show()
