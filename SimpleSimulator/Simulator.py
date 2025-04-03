import sys

def prints(file):
    # file.write(f"{pc} {register_values['00000']} {register_values['00001']} {register_values['00010']} {register_values['00011']} {register_values['00100']} {register_values['00101']} {register_values['00110']} {register_values['00111']} {register_values['01000']} {register_values['01001']} {register_values['01010']} {register_values['01011']} {register_values['01100']} {register_values['01101']} {register_values['01110']} {register_values['01111']} {register_values['10000']} {register_values['10001']} {register_values['10010']} {register_values['10011']} {register_values['10100']} {register_values['10101']} {register_values['10110']} {register_values['10111']} {register_values['11000']} {register_values['11001']} {register_values['11010']} {register_values['11011']} {register_values['11100']} {register_values['11101']} {register_values['11110']} {register_values['11111']}\n")
    pc_bin = f'0b{bin(pc)[2:].zfill(32)}'
    
    
    reg_values = []
    for reg in register_values:
       
        value = register_values[reg]
        bin_value = f'0b{bin(value)[2:].zfill(32)}'
        reg_values.append(bin_value)
    
    
    file.write(f'{pc_bin} ' + ' '.join(reg_values) + '\n')


registers = {
    "00000": "zero",
    "00001": "ra",
    "00010": "sp",
    "00011": "gp",
    "00100": "tp",
    "00101": "t0",
    "00110": "t1",
    "00111": "t2",
    "01000": "s0",
    "01001": "s1",
    "01010": "a0",
    "01011": "a1",
    "01100": "a2",
    "01101": "a3",
    "01110": "a4",
    "01111": "a5",
    "10000": "a6",
    "10001": "a7",
    "10010": "s2",
    "10011": "s3",
    "10100": "s4",
    "10101": "s5",
    "10110": "s6",
    "10111": "s7",
    "11000": "s8",
    "11001": "s9",
    "11010": "s10",
    "11011": "s11",
    "11100": "t3",
    "11101": "t4",
    "11110": "t5",
    "11111": "t6"
}

memory = {
    0x00010000: 0,
    0x00010004: 0,
    0x00010008: 0,
    0x0001000C: 0,
    0x00010010: 0,
    0x00010014: 0,
    0x00010018: 0,
    0x0001001C: 0,
    0x00010020: 0,
    0x00010024: 0,
    0x00010028: 0,
    0x0001002C: 0,
    0x00010030: 0,
    0x00010034: 0,
    0x00010038: 0,
    0x0001003C: 0,
    0x00010040: 0,
    0x00010044: 0,
    0x00010048: 0,
    0x0001004C: 0,
    0x00010050: 0,
    0x00010054: 0,
    0x00010058: 0,
    0x0001005C: 0,
    0x00010060: 0,
    0x00010064: 0,
    0x00010068: 0,
    0x0001006C: 0,
    0x00010070: 0,
    0x00010074: 0,
    0x00010078: 0,
    0x0001007C: 0,
}

orignal={
    0x00010000: 0,
    0x00010004: 0,
    0x00010008: 0,
    0x0001000C: 0,
    0x00010010: 0,
    0x00010014: 0,
    0x00010018: 0,
    0x0001001C: 0,
    0x00010020: 0,
    0x00010024: 0,
    0x00010028: 0,
    0x0001002C: 0,
    0x00010030: 0,
    0x00010034: 0,
    0x00010038: 0,
    0x0001003C: 0,
    0x00010040: 0,
    0x00010044: 0,
    0x00010048: 0,
    0x0001004C: 0,
    0x00010050: 0,
    0x00010054: 0,
    0x00010058: 0,
    0x0001005C: 0,
    0x00010060: 0,
    0x00010064: 0,
    0x00010068: 0,
    0x0001006C: 0,
    0x00010070: 0,
    0x00010074: 0,
    0x00010078: 0,
    0x0001007C: 0,
}

register_values = {k: (0 if k != "00010" else 380) for k in registers.keys()}

register_values["00000"] = 0  

def unsign(register_values):
    for reg in register_values:
        if register_values[reg] < 0:
            register_values[reg] = register_values[reg] + 2**32
        

#########################################################################################################
# R-Type processing
def r_type_processing(instruction, pc,file):
    funct7 = instruction[0:7]   
    rs2    = instruction[7:12]   
    rs1    = instruction[12:17]  
    funct3 = instruction[17:20]  
    rd     = instruction[20:25]  
    opcode = instruction[25:32]  

    if funct3 == "000" and funct7 == "0000000":
        op = "add"
    elif funct3 == "000" and funct7 == "0100000":
        op = "sub"
    elif funct3 == "010":
        op = "slt"
    elif funct3 == "101":
        op = "srl"
    elif funct3 == "110":
        op = "or"
    elif funct3 == "111":
        op = "and"
    else:
        op = None

    if op == "add":
        register_values[rd] = register_values[rs1] + register_values[rs2]
        pc += 4
    elif op == "sub":
        register_values[rd] = register_values[rs1] - register_values[rs2]
        pc += 4  
    elif op == "slt":
        register_values[rd] = 1 if register_values[rs1] < register_values[rs2] else 0
        pc += 4
    elif op == "srl":
        register_values[rd] = register_values[rs1] >> register_values[rs2]
        pc += 4
    elif op == "or":
        register_values[rd] = register_values[rs1] | register_values[rs2]
        pc += 4
    elif op == "and":
        register_values[rd] = register_values[rs1] & register_values[rs2]
        pc += 4

    # Ensure register zero always remains 0
    register_values["00000"] = 0
    unsign(register_values)
    # prints(file)
    return pc

#########################################################################################################
# I-Type processing 
I_op = {
    "0000011": "lw",
    "0010011": "addi",
    "1100111": "jalr"
}

def i_type_processing(instruction, pc,file):
    imm    = instruction[0:12]   # Bits 31-20 (Immediate)
    rs1    = instruction[12:17]  # Bits 19-15 (Source Register 1)
    funct3 = instruction[17:20]  # Bits 14-12 (Function Code)
    rd     = instruction[20:25]  
    opcode = instruction[25:32]  

    type = I_op[opcode]
    if type == "addi":
        imm_val = sign_extend(imm, 12)
        register_values[rd] = register_values[rs1] + imm_val
        pc += 4
    elif type == "lw":
        # lw handling - load word from memory
        imm_val = sign_extend(imm, 12)
        address = register_values[rs1] + imm_val
        # Check if address exists in memory, if not return 0
        if address in memory:
            register_values[rd] = memory[address]
        else:
            register_values[rd] = 0
        pc += 4
    elif type == "jalr":
        if rd != "00000":
            register_values[rd] = pc + 4
        imm_val = sign_extend(imm, 12)
        new_pc = (register_values[rs1] + imm_val) & ~1  # Clear LSB as per spec

        pc = new_pc
        


    register_values["00000"] = 0

    unsign(register_values)

    # prints(file)
    return pc

#########################################################################################################
# S-Type processing 
def s_type_processing(instruction, pc,file):
    imm_11_5 = instruction[0:7]      # imm[11:5] → bits 31-25
    rs2      = instruction[7:12]     # rs2 → bits 24-20
    rs1      = instruction[12:17]    # rs1 → bits 19-15
    funct3   = instruction[17:20]    # funct3 → bits 14-12
    imm_4_0  = instruction[20:25]    # imm[4:0] → bits 11-7
    opcode   = instruction[25:32]    # opcode → bits 6-0

    imm = imm_11_5 + imm_4_0
    imm_val = sign_extend(imm, 12)
    
    address = register_values[rs1] + imm_val
    
    if funct3 == "010":
        memory[address] = register_values[rs2]
    
    pc += 4
 
    unsign(register_values)
    # prints(file)

    return pc

#########################################################################################################
# B-Type processing 
B_f3_reversed = {
    "000": "beq",
    "001": "bne"
}
def b_type_processing(instruction, pc,file):
    imm_12   = instruction[0]       
    imm_10_5 = instruction[1:7]     
    rs2      = instruction[7:12]   
    rs1      = instruction[12:17]  
    funct3   = instruction[17:20]   
    imm_4_1  = instruction[20:24]   
    imm_11   = instruction[24]      
    opcode   = instruction[25:32]   

    full_imm = imm_12 + imm_11 + imm_10_5 + imm_4_1 + "0"  
    imm_val = sign_extend(full_imm, 13)

    rs1_key = rs1  
    rs2_key = rs2

    branch_type = B_f3_reversed.get(funct3, None)
    if branch_type == "beq":
        if register_values[rs1_key] == register_values[rs2_key]:
            pc += imm_val
        else:
            pc += 4
    elif branch_type == "bne":
        if register_values[rs1_key] != register_values[rs2_key]:
            pc += imm_val
        else:
            pc += 4
    else:
        pc += 4
    
    # prints(file)
    return pc

#########################################################################################################
# J-Type processing 
def j_type_processing(instruction, pc,file):

    imm_20    = instruction[0]      
    imm_10_1  = instruction[1:11]   
    imm_11    = instruction[11]     
    imm_19_12 = instruction[12:20]  
    rd        = instruction[20:25] 
    opcode    = instruction[25:32]  

    full_imm = imm_20 + imm_19_12 + imm_11 + imm_10_1 + "0"  # LSB is 0
    imm_val = sign_extend(full_imm, 21)  # 21-bit immediate


    register_values[rd] = pc + 4
    pc = pc + imm_val


    register_values["00000"] = 0
    unsign(register_values)
    
    return pc

#########################################################################################################
def sign_extend(value, bits):
    if value[0] == '1':  
        return int(value, 2) - (1 << bits)
    return int(value, 2)

#########################################################################################################
def identify_type(instruction):

    opcode = instruction[25:32]  
    if opcode in ["0110011", "0111011"]:  
        return "R"
    elif opcode in ["0000011", "0010011", "1100111"]:  
        return "I"
    elif opcode in ["0100011"]:  
        return "S"
    elif opcode in ["1100011"]: 
        return "B"
    elif opcode in ["1101111"]:  
        return "J"
    else:
        return None

#########################################################################################################
def take_input(filename):
    with open(filename, 'r') as file:
        instructions = [line.strip() for line in file.readlines()]
    return instructions

#########################################################################################################

pc = 0
instructions = take_input(sys.argv[1])  
# instructions = take_input("input.txt")

file = open(sys.argv[2], "w")
# file = open("output.txt", "w")
while instructions[pc // 4] != "00000000000000000000000001100011":
    instruction = instructions[pc // 4]
    inst_type = identify_type(instruction)
    if inst_type == "R":
        pc = r_type_processing(instruction, pc,file)
    elif inst_type == "I":
        pc = i_type_processing(instruction, pc,file)
    elif inst_type == "S":
        pc = s_type_processing(instruction, pc,file)
    elif inst_type == "B":
        pc = b_type_processing(instruction, pc,file)
    elif inst_type == "J":
        pc = j_type_processing(instruction, pc,file)
    else:
        print("Unknown instruction type")
        break
    prints(file)

instruction = instructions[pc // 4]
inst_type = identify_type(instruction)
if inst_type == "R":
    pc = r_type_processing(instruction, pc,file)
elif inst_type == "I":
    pc = i_type_processing(instruction, pc,file)
elif inst_type == "S":
    pc = s_type_processing(instruction, pc,file)
elif inst_type == "B":
    pc = b_type_processing(instruction, pc,file)
elif inst_type == "J":
    pc = j_type_processing(instruction, pc,file)
prints(file)


# for i in memory:
#     if memory[i] != 0:
#         file.write(f"0x000{hex(i)[2:].upper()}:{memory[i]}\n")
for i in orignal:
    file.write(f"0x000{hex(i)[2:].upper()}:0b{bin(memory[i])[2:].zfill(32)}\n")
file.close()

#check jalr,sw,lw

