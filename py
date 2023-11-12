import numpy as np
import matplotlib.pyplot as plt

def histogramHesapla(goruntu):
    # Görüntünün boyutlarını al
    yukseklik, genislik = goruntu.shape

    # Histogram için bir dizi oluştur
    histogram = np.zeros(256, dtype=int)

    # Görüntüyü dolaşarak histogramı hesapla
    for x in range(yukseklik):
        for y in range(genislik):
            pixel_degeri = goruntu[x, y]
            histogram[pixel_degeri]+=1

    return histogram

# Gri seviye bir örnek görüntü oluştur
goruntu = np.array([[40, 50, 60, 70, 80],
                  [90, 100, 110, 120, 130],
                  [140, 150, 160, 170, 180],
                  [190, 200, 210, 220, 230],
                  [240, 250, 0, 0, 0]], dtype=np.uint8)


# Histogramı hesapla
histogram = histogramHesapla(goruntu)

# Histogramı görselleştir
plt.bar(range(256), histogram)
plt.title("Gri Seviye Görüntü Histogramı")
plt.xlabel("Piksel Değeri")
plt.ylabel("Piksel Sayısı")
plt.show()
