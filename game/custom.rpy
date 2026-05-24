init python:
    def countdown(st, at, length=50.0):
        remaining = max(0.0, length - st)
        return Text("%.1f" % remaining, color="#ff4444", size=40, bold=True), 0.1

default quiz_score    = 0
default quiz_total    = 7
default boss_hp       = 3
default boss_attempts = 0
default fase1_benar   = 0
default fase2_benar   = 0
default fase3_benar   = 0