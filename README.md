# Frequency Curve Sound Generator

このリポジトリは、3種類の異なる周波数変化（半円弧型、線対称型、直線型）に基づくサイン波音声（WAVファイル）を生成し、それぞれの周波数変化をグラフで比較するPythonスクリプトを提供します。

## 特徴

- **半円弧型**: `y = sqrt(1 - (x-1)^2)`
- **線対称型**: `y = 1 - sqrt(1 - x^2)`
- **直線型**: `y = x`
- それぞれのカーブに基づく音声（WAVファイル）を生成
- 3つのカーブを重ねたグラフを描画

## 必要なライブラリ

- numpy
- matplotlib
- scipy

インストール例:
```bash
pip install numpy matplotlib scipy