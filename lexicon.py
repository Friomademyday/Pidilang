import re

class PidiEngine:
    def __init__(self):
        self.memory = {}
        self.running = True

    def run(self, code):
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

                elif token == 'ASK_AM':
                    var_target = tokens[i+1]
                    prompt_text = tokens[i+2]
                    try:
                        user_response = input(prompt_text.replace('"', '') + " ")
                        if user_response.isdigit():
                            self.memory[var_target] = int(user_response)
                        else:
                            self.memory[var_target] = user_response
                    except EOFError:
                        print("MUMU_ERROR: Input take too long!")
                        self.memory[var_target] = 0
                    i += 3
                    continue

                elif token == 'TRY_YOUR_BEST':
                    i += 1
                    continue

                elif token == 'IF_E_BAD':
                    d = 0
                    while i < len(tokens):
                        if tokens[i] == '(': d += 1
                        elif tokens[i] == ')':
                            d -= 1
                            if d == 0: break
                        i += 1
                    i += 1
                    continue

                elif token == 'SUPPOSE':
                    v1 = self.memory.get(tokens[i+2], tokens[i+2])
                    op = tokens[i+3]
                    v2 = self.memory.get(tokens[i+4], tokens[i+4])
                    v1 = int(v1) if str(v1).isdigit() else v1
                    v2 = int(v2) if str(v2).isdigit() else v2
                    met = False
                    if op == 'E_BE_SAME': met = (v1 == v2)
                    elif op == 'NO_BE_SAME': met = (v1 != v2)
                    elif op == 'PASS_AM': met = (v1 > v2)
                    elif op == 'UNDER_AM': met = (v1 < v2)
                    if met:
                        i += 6
                    else:
                        d = 0
                        while i < len(tokens):
                            if tokens[i] == '(': d += 1
                            elif tokens[i] == ')':
                                d -= 1
                                if d == 0: break
                            i += 1
                        i += 1
                    continue

                elif token == 'FINISH':
                    print("Pidi Engine Logout. No Wahala.")
                    self.running = False
                    break

                i += 1
        except Exception as e:
            print(f"MUMU_ERROR: {e}")

engine = PidiEngine()

engine.run('TRY_YOUR_BEST TALK_AM "Checking system..."')
engine.run('DAT_ME secret = 1234')
engine.run('DAT_ME attempt = 1234')

engine.run('SUPPOSE ( attempt E_BE_SAME secret ) TALK_AM "Correct! Door open."')
engine.run('SUPPOSE ( attempt NO_BE_SAME secret ) TALK_AM "Wrong! Alarm de ring!"')

engine.run('FINISH')
