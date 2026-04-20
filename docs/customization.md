# CoShooter Customization Guide / 設定変更ガイド

You can customize **CoShooter** to match your clinical criteria or personal preferences.

CoShooterの警告の感度や音の設定は、`main.py` 内の数値を書き換えることで簡単に調整できます。

---

## 1. Adjusting the "Nitpicking" Level / 厳しさの調整

You can change the sensitivity by editing the following variables in `main.py`.

`main.py` の以下の変数を変更することで、デバイスの「厳しさ」を調整できます。

* **`SAFE_LIMIT_DEG`** (Default: `30.0`)
    * The angle (degrees) where the alert sound starts.
    * 警告音が鳴り始める角度です。数値を小さくするほど、わずかな「こね」に対しても指摘が始まります。

* **`DANGER_LIMIT_DEG`** (Default: `50.0`)
    * The angle where the sound reaches its highest pitch and fastest speed (The "Unacceptable" zone).
    * 警告音が最大（最高音・最速）になる「完全にアウト」な角度です。

---

## 2. Adjusting Sound (Pitch & Speed) / 音の高さと速さの調整

If the default sounds are too persistent or need more urgency, you can modify these values.

音の聞こえ方を調整したい場合は、以下の数値を変更してください。

### Pitch (Hz) / 音の高さ
* **`PITCH_START`** (Default: `440`): 
    * Frequency at the Safe Limit (Low pitch).
    * 指摘開始時の音の高さ（低音 A4）。
* **`PITCH_MAX`** (Default: `1500`): 
    * Frequency at the Danger Limit (High pitch).
    * 危険限界での音の高さ（高音）。

### Beep Interval (ms) / 音の間隔
* **`INTERVAL_MAX`** (Default: `500`): 
    * Wait time between beeps at the Safe Limit.
    * 指摘開始時のゆっくりとした間隔。
* **`INTERVAL_MIN`** (Default: `20`): 
    * Wait time between beeps at the Danger Limit.
    * 危険限界での激しく速い間隔（数値が小さいほど速くなります）。

---

## 3. Example Settings / 設定例

| Difficulty / 難易度 | SAFE_LIMIT | DANGER_LIMIT | Description / 説明 |
| :--- | :--- | :--- | :--- |
| **Strict (厳しめ)** | `25.0` | `35.0` | Very sensitive. Even minor prying is noticed. / わずかな動きも逃さず厳しく指摘。 |
| **Standard (標準)** | `30.0` | `50.0` | Recommended for initial training. / 初期トレーニングに推奨されるバランス。 |
| **Relaxed (緩め)** | `35.0` | `65.0` | Allows moderate tilting before loud alerts. / ある程度の倒し込みを許容。 |

---

## 4. How to Apply Changes / 設定変更の反映方法

1. **Edit `main.py`**
    * Open the file in your editor and update the values.
    * `main.py` をエディタで開き、各項目の数値を書き換えます。

2. **Flash the Code**
    * Transfer the updated `main.py` to your micro:bit.
    * 設定を反映させるため、書き換えた `main.py` を micro:bit 本体へ書き込みます。

3. **Verify**
    * Always test the behavior on a manikin after modification to ensure the "nitpicking" is appropriate.
    * 変更後は、トレーニングに使用する前に必ずマニキンで実際の挙動を確認し、指摘の強さが適切かチェックしてください。

---
Developed by **Kota Yoneda** Licensed under the MIT License.
