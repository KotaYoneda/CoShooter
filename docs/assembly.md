# CoShooter Assembly Guide / 組み立てガイド

This guide explains how to set up **CoShooter** on a laryngoscope handle for optimal feedback.

CoShooterを喉頭鏡ハンドルにセットアップし、手技の精度を最大限に高めるためのガイドです。

---

## 1. Requirements / 準備するもの

* **micro:bit**
    * v2.0 or later recommended.
    * v2.0以降を推奨します。

* **Silicon Case**
    * Recommended for board protection and better grip.
    * 基板の保護とグリップ向上のため、装着を強く推奨します。

* **Battery pack**
    * AAA x 2.
    * 単4電池2本用。

* **Laryngoscope handle**
    * Compatible with training manikins.
    * 訓練用マネキンに対応したもの。

---

## 2. The "Thumb-Press" Style / 装着方法

CoShooter is designed to be held directly under your thumb. This ensures the most direct feedback and allows for quick setup.

CoShooterは、親指で直接押さえて保持するスタイルを推奨しています。準備が迅速に行えるだけでなく、手技のブレをダイレクトに感じ取ることができます。

* **Position / 位置**
    * Place the micro:bit on the **top head** of the laryngoscope handle.
    * micro:bitをハンドルの頭の部分（上端）に置きます。

* **Secure / 固定**
    * Firmly hold the micro:bit with your **left thumb** while grasping the handle.
    * ハンドルを握る際、左手の親指でmicro:bitを上からしっかり押さえてください。

* **Orientation / 向き**
    * The LED face should be **facing up (towards the ceiling)** when the handle is held correctly.
    * 正しくハンドルを保持したとき、micro:bitのLED面が**仰向け（天井向き）**になるように配置します。

* **Mechanism / 検知の仕組み**
    * The program detects when the micro:bit "lifts up" from its flat position.
    * プログラムは、水平な状態からmicro:bitが「起き上がる」動きを検知します。
    * As you "lever" (prying) the handle, the micro:bit's face will tilt toward you—this is what triggers the feedback.
    * ハンドルを前後に「こねる」と、micro:bitの顔が自分の方へ起き上がってきます。この動きが指摘の対象です。

---

## 3. Setup Steps / 手順

* **1. Flash the Code / 書き込み**
    * Transfer `src/main.py` to the micro:bit.
    * `src/main.py` をmicro:bitに書き込みます。

* **2. Protect the Board / 保護**
    * Put the micro:bit in a silicon case. This improves the grip under your thumb.
    * シリコンケースを装着します。親指での保持が安定します。

* **3. Connect Power & Start / 起動**
    * Plug in the battery pack. 
    * 電池を接続します。
    * **Press Buttons A+B** while the micro:bit is on a flat surface or in your hand to start the program (Hear "Do-Mi-So").
    * micro:bitが平らな場所にあるか、手に持っている状態で**AボタンとBボタンを同時押し**して開始します（「ド・ミ・ソ」と鳴ります）。

* **4. Hold it Ready / ホールド**
    * Once the program is running, place the micro:bit on the handle and secure it with your thumb.
    * プログラムが起動したら、micro:bitをハンドルに乗せ、親指でしっかりホールドして準備完了です。

---

## 4. Operation Check / 動作確認

* **The "Nitpicking" Test / 指摘動作の確認**
    * Purposefully tilt the handle back as if prying on teeth.
    * 意図的にハンドルを後方へ「こねる」ように倒してみます。

* **Feedback / フィードバック**
    * Verify that the **pitch and beep frequency increase** as the face of the micro:bit lifts toward you.
    * micro:bitの顔が自分の方へ起き上がってくるにつれて、警告音が高く・速くなることを確認してください。

---

## 5. Disclaimer / 免責事項

* **Simulation Use Only**
    * This device is for **simulation training only**. 
    * 本デバイスは**シミュレーション訓練専用**です。
* **No Clinical Use**
    * It must NEVER be used on human patients.
    * 実際の患者には絶対に使用しないでください。

---
Developed by **Kota Yoneda** Licensed under the MIT License.
