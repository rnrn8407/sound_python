import numpy as np  # 数値計算用
import matplotlib.pyplot as plt  # グラフ描画用
from scipy.io.wavfile import write  # WAVファイル書き込み用

rate = 44100  # サンプリングレート
duration = 5  # 秒
f_start = 220  # 初期周波数
f_end = 880   # 最終周波数

t = np.linspace(0, duration, int(rate * duration), endpoint=False)  # 時間軸配列（0～5秒）
x_norm = t / duration  # 時間を0～1に正規化

# 半円弧型
y1 = np.sqrt(1 - (x_norm - 1)**2)  # y = sqrt(1 - (x-1)^2)
freqs1 = f_start + (f_end - f_start) * y1  # 周波数配列1

# y=xで線対称なカーブ
y2 = 1 - np.sqrt(1 - x_norm**2)  # y = 1 - sqrt(1 - x^2)
freqs2 = f_start + (f_end - f_start) * y2  # 周波数配列2

# 直線型
y3 = x_norm  # y = x
freqs3 = f_start + (f_end - f_start) * y3  # 周波数配列3

# サイン波生成（半円弧型）
phase1 = 2 * np.pi * np.cumsum(freqs1) / rate
data1 = 0.5 * np.sin(phase1)
data1_int16 = np.int16(data1 * 32767)
write("semicircle_freq.wav", rate, data1_int16)  # WAVファイルとして保存

# サイン波生成（線対称型）
phase2 = 2 * np.pi * np.cumsum(freqs2) / rate
data2 = 0.5 * np.sin(phase2)
data2_int16 = np.int16(data2 * 32767)
write("semicircle_freq_symmetric.wav", rate, data2_int16)  # WAVファイルとして保存

# サイン波生成（直線型）
phase3 = 2 * np.pi * np.cumsum(freqs3) / rate
data3 = 0.5 * np.sin(phase3)
data3_int16 = np.int16(data3 * 32767)
write("linear_freq.wav", rate, data3_int16)  # WAVファイルとして保存

# グラフ描画
plt.figure(figsize=(8,4))
plt.plot(t, freqs1, label="y = sqrt(1-(x-1)^2)")  # 半円弧型
plt.plot(t, freqs2, label="y = 1 - sqrt(1-x^2)")  # 線対称型
plt.plot(t, freqs3, label="y = x")  # 直線型
plt.xlabel("Time [s]")
plt.ylabel("Frequency [Hz]")
plt.title("Frequency vs Time (semicircle, symmetric, linear)")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()