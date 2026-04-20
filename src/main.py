from microbit import accelerometer, button_a, button_b, display, Image, sleep
import music
import math

# ==========================================================
# 🛠️ SETTINGS - 臨床的境界線を設定してください / Clinical Thresholds
# ==========================================================
# 1. 警告（音）が鳴り始める「安全限界」の角度 (degree)
# 1. "Safe Limit" angle to start the alert sound (degrees)
# 設定例: 25.0 (厳しい), 30.0 (標準), 35.0 (緩い)
SAFE_LIMIT_DEG = 30.0

# 2. これを超えたら完全にアウトとする「危険限界」の角度 (degree)
# 2. "Danger Limit" angle for the maximum alert pitch (degrees)
# 設定例: 35.0 (厳しい), 50.0 (標準), 65.0 (緩い)
DANGER_LIMIT_DEG = 50.0

# 3. 音の高さの設定 (Hz) / Pitch Frequency Settings (Hz)
PITCH_START = 440   # 低音 (A4) / Low pitch at Safe Limit
PITCH_MAX = 1500    # 高音 / High pitch at Danger Limit

# 4. 音が鳴る間隔（頻度）の設定 (ms) / Beep Interval Settings (ms)
# 安全限界付近ではゆっくり、危険限界では速く鳴ります
# Slow at Safe Limit, fast at Danger Limit
INTERVAL_MAX = 500  # 最も遅い間隔 / Slowest beep
INTERVAL_MIN = 20   # 最も速い間隔 / Fastest beep
# ==========================================================

# Pre-calculate acceleration thresholds
SAFE_MG = 1000 * math.sin(math.radians(SAFE_LIMIT_DEG))
DANGER_MG = 1000 * math.sin(math.radians(DANGER_LIMIT_DEG))

active = False

while True:
    # Toggle active state with A+B press
    if button_a.is_pressed() and button_b.is_pressed():
        active = not active
        if active:
            music.play(['c4:1', 'e4:1', 'g4:1'], wait=True)
            display.show(Image.YES)
        else:
            music.play(['g4:1', 'e4:1', 'c4:1'], wait=True)
            display.clear()
            music.stop()
        
        while button_a.is_pressed() or button_b.is_pressed():
            sleep(10)

    if active:
        # Get current tilt on Y-axis
        val = accelerometer.get_y()

        if val > SAFE_MG:
            display.show(Image.NO)
            
            # Calculate tilt ratio (0.0 to 1.0)
            ratio = (val - SAFE_MG) / (DANGER_MG - SAFE_MG)
            ratio = max(0.0, min(ratio, 1.0))
            
            # Map ratio to Pitch
            p = int(PITCH_START + (ratio * (PITCH_MAX - PITCH_START)))
            
            # Map ratio to Interval (Beep speed)
            i = int(INTERVAL_MAX - (ratio * (INTERVAL_MAX - INTERVAL_MIN)))
            
            # Perform biofeedback beep
            # Sound length is half of the interval to create a 'pulsing' feel
            music.pitch(p, duration=int(i/2), wait=False)
            sleep(i) 
        else:
            display.show(Image.YES)
            music.stop()
            sleep(100)
    else:
        sleep(200)
