import re
import os

class PidiEngine:
    def __init__(self):
        self.memory = {}
        self.running = True

    def execute(self, code):
        try:
            pattern = r'("[^"]*"|[a-zA-Z_]\w*|\d+|\+|\-|\*|\/|\=|\(|\)|E_BE_SAME|JOIN_AM|MINUS_AM|TIMES_AM|SHARE_AM|SUPPOSE|SOTEY|DAT_ME|TALK_AM|ASK_AM|FINISH|NO_BE_SAME|PASS_AM|UNDER_AM|WAKA_ROUND|CHOP_AM|GET_OUT|LISTEN_AM|FIX_AM|TEST_AM|NA_SO|NO_BE_SO|MUMU_ERROR|SENSE_AM|NETWORK_AM|KPA_AM|BOLA_AM|TIGHT_AM|LOOSE_AM|WETIN_BE|WHO_BE|HOW_FAR|DIVE_IN|JUMP_OUT|SHARP_SHARP|SOFT_SOFT|KOLO_AM|CHILL_AM|VEX_AM|JOY_AM|LOAD_AM|SEND_AM|CATCH_AM|THROW_AM|TRY_YOUR_BEST|IF_E_BAD|ALWAYS_DO|STANDBY|SHUTDOWN|RESTART|OBEY_AM|DISOBEY_AM|SABI_AM|FORGET_AM|GIVE_AM|TAKE_AM|DOUBT_AM|TRUST_AM|CHECK_AM|WAIT_AM|GO_SLOW|RUN_FAST|LEVEL_UP|GROUND_AM|SKY_AM|FIRE_AM|WATER_AM|BREEZE_AM)'
            tokens = re.findall(pattern, code)

            i = 0
            while i < len(tokens) and self.running:
                token = tokens[i]

                if token == 'DAT_ME':
                    var_name = tokens[i+1]
                    if tokens[i+2] == '=':
                        if i + 5 < len(tokens) and tokens[i+4] in ['JOIN_AM', 'MINUS_AM', 'TIMES_AM', 'SHARE_AM']:
                            v1 = int(self.memory.get(tokens[i+3], tokens[i+3]))
                            v2 = int(self.memory.get(tokens[i+5], tokens[i+5]))
                            op = tokens[i+4]
                            if op == 'JOIN_AM': self.memory[var_name] = v1 + v2
                            elif op == 'MINUS_AM': self.memory[var_name] = v1 - v2
                            elif op == 'TIMES_AM': self.memory[var_name] = v1 * v2
                            elif op == 'SHARE_AM': self.memory[var_name] = v1 // v2
                            i += 6
                        else:
                            val = tokens[i+3]
                            self.memory[var_name] = val.replace('"', '') if val.startswith('"') else int(val)
                            i += 4
                    continue

                elif token == 'TALK_AM':
                    target = tokens[i+1]
                    print(str(self.memory.get(target, target)).replace('"', ''))
                    i += 2
                    continue

                elif token == 'FINISH':
                    self.running = False
                    break

                i += 1
        except Exception:
            print("MUMU_ERROR: Something spoil!")

# This part tells Python to find your .pidi file and run it
if __name__ == "__main__":
    engine = PidiEngine()
    # Replace 'myscript.pidi' with whatever you name your PidiLang file
    if os.path.exists('myscript.pidi'):
        with open('myscript.pidi', 'r') as f:
            engine.execute(f.read())
    else:
        print("MUMU_ERROR: No .pidi file found!")
