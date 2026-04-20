# Flashing Guide / プログラムの書き込み手順

This guide explains how to transfer your edited `src/main.py` to the micro:bit.

編集した `src/main.py` を micro:bit 本体に書き込む手順を解説します。

---

## Step 1: Open the Official Editor / エディタを開く

* **Access the Editor**
    * Go to the **[micro:bit Python Editor](https://python.microbit.org/v/3)** in your web browser (Chrome or Edge recommended).
    * ブラウザ（Chrome または Edge 推奨）で [micro:bit Python エディタ](https://python.microbit.org/v/3) を開きます。

---

## Step 2: Load your src/main.py / ファイルを読み込む

* **Open File**
    * Click the **"Open"** (folder icon) in the editor.
    * エディタの「Open（フォルダアイコン）」をクリックします。

* **Import**
    * Drag and drop your edited **`src/main.py`** into the editor, or select it from your computer.
    * 編集した **`src/main.py`** を画面にドラッグ＆ドロップするか、ファイルを選択して読み込みます。

---

## Step 3: Connect micro:bit / 本体を接続する

* **USB Connection**
    * Connect your micro:bit to your computer using a USB cable.
    * micro:bit を USB ケーブルで PC に接続します。

* **Drive Recognition**
    * The micro:bit will appear as a USB drive named **"MICROBIT"**.
    * PC 上で **"MICROBIT"** という名前の USB ドライブとして認識されます。

---

## Step 4: Flash the Code / 書き込み

Choose one of the following methods to transfer your code.
以下のいずれかの方法でコードを転送します。

### Method A: Direct Flashing (Fastest) / 直接書き込み

* **Send to Device**
    * Click the **"Send to micro:bit"** button in the bottom left.
    * 画面左下の「Send to micro:bit」ボタンをクリックします。

* **Pairing**
    * Select your micro:bit in the browser's pop-up and click **"Connect"**.
    * ブラウザのポップアップで micro:bit を選択し、「接続」をクリックすると自動的に書き込みが始まります。

### Method B: Manual Transfer (.hex file) / 手動で転送

* **Download Hex**
    * Click the **"Download"** button (or "Save" -> "Download Hex").
    * 「Download」ボタン（または Save 内の Download Hex）をクリックします。

* **Copy to Drive**
    * Drag and drop the downloaded **`microbit.hex`** file directly into the **"MICROBIT"** drive.
    * 保存された **`.hex`** ファイルを、USB ドライブの **"MICROBIT"** へコピーします。

---

## Step 5: Verification / 完了の確認

* **Status LED**
    * The yellow LED on the back of the micro:bit will flash during the transfer.
    * 書き込み中、本体裏面の黄色い LED が点滅します。

* **Start-up Check**
    * Once finished, the micro:bit will restart automatically. 
    * 完了すると自動的に再起動します。
    * Press **Buttons A+B** to hear the start-up sound ("Do-Mi-So").
    * **AボタンとBボタンを同時押し**して、起動音が鳴れば成功です。

---

## Note / 注意事項

* **Memory Error**
    * If you encounter a "Memory Error," try clearing any unused files from the micro:bit or resetting the editor.
    * 「Memory Error」が出る場合は、古いファイルを削除するか、エディタをリセットして再度試してください。

---
Developed by **Kota Yoneda** Licensed under the MIT License.
