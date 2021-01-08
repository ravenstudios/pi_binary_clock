import RPi.GPIO as GPIO
import time, datetime



DATA = 11
CLOCK = 13
LATCH = 15

GPIO.setwarnings(False)
GPIO.setmode (GPIO.BOARD)
GPIO.setup(DATA, GPIO.OUT)
GPIO.setup(CLOCK, GPIO.OUT)
GPIO.setup(LATCH, GPIO.OUT)

tenth_hours = [255, 239, 247]
hours = [255, 239, 247, 486, 251, 490, 498, 739, 253, 492]

tenth_mins = [255, 239, 247, 486, 251, 490]
mins = [255, 239, 247, 486, 251, 490, 498, 739, 253, 492]

tenth_seconds = [255, 239, 247, 486, 251, 490]
seconds = [255, 239, 247, 486, 251, 490, 498, 739, 253, 492]

def shift_out(*values):
        bits = {"0": False, "1": True}
        # if self.invert:
        #     bits = {"1": False, "0": True}


        GPIO.output(LATCH, 0)
        for val in reversed(values):
            for bit in '{0:08b}'.format(val):
                GPIO.output(CLOCK, 0)
                GPIO.output(DATA, int(bit))
                GPIO.output(CLOCK, 1)
        GPIO.output(LATCH, 1)








while 1:


    now = datetime.datetime.now()
    # print(now)
    th = int(now.strftime("%H")) // 10
    h = int(now.strftime("%H")) % 10
    tm = int(now.strftime("%M")) // 10
    m = int(now.strftime("%M")) % 10
    ts = int(now.strftime("%S")) // 10
    s = int(now.strftime("%S")) % 10



    shift_out(2, tenth_hours[th])
    shift_out(4, hours[h])
    shift_out(8, tenth_mins[tm])
    shift_out(16, mins[m])
    shift_out(32, tenth_seconds[ts])
    shift_out(1, seconds[s])
