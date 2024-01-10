import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib.table import Table

import sys
sys.set_int_max_str_digits(0)


new_e_ls = []


################  Memory Efficient Method ##############
def memory_efficient_method(b_mem, e_mem, m_mem):
    cnt_mem = 0
    start = time.time()
    e_prime = 1
    c = 1
    # Create counter for count the number of each operation
    counter_mod = 0
    counter_multiplication = 0
    counter_sqrt = 0
    counter_subtraction = 0

    # Loop check id e_prime = e_mem + 1 then return

    while (e_prime != (e_mem + 1)):
        # print(f"e_prime = {e_prime}")
        c = np.mod(((np.mod(c, m_mem)) * np.mod(b_mem, m_mem)), m_mem)
        e_prime += 1
        counter_mod += 3
        counter_multiplication += 1
        cnt_mem += 1
    end = time.time()
    resTime = (end-start) * (10**3)  # time in ms
    counter_all = [counter_mod, counter_multiplication,
                   counter_sqrt, counter_subtraction]
    n_operation = sum(counter_all)

    return int(c), counter_all, n_operation, resTime


######################## Square And Multiply Algorithm ########################
def square_and_multiply_algorithm(b_sq_mul, e_sq_mul, m_sq_mul):

    # Convert from Decimal to binary.
    start = time.time()
    e_binary = bin(e_sq_mul)
    # print(e_binary)

    c = b_sq_mul
    #    power_of_c = 1

    counter_multiplication = 0
    counter_mod = 0
    counter_sqrt = 0
    counter_subtraction = 0

    for i in range(3, len(e_binary)):
        c = c ** 2
        #  Check condition If bit binary = 1
        if (e_binary[i] == "1"):
            #  Then multiply
            c *= b_sq_mul
            counter_multiplication += 1
        counter_mod += 1

    # print(f"C before mod : {c}")
    c = np.mod(c, m_sq_mul)
    end = time.time()

    resTime = (end-start) * (10**3)  # time in ms
    counter_all = [counter_mod, counter_multiplication,
                   counter_sqrt, counter_subtraction]
    n_operation = sum(counter_all)
    return int(c), counter_all, n_operation, resTime

#################### Exponent Modular ####################


def exponent_modular(b_ex, e_ex, m_ex):
    start = time.time()
    counter_mod = 0
    counter_multiplication = 0
    counter_sqrt = 0
    counter_subtraction = 0

    # Change from e -> (e mod (m-1))
    new_e_ex = np.mod(e_ex, (m_ex - 1))
    counter_subtraction += 1
    counter_mod += 1

    result_arr = memory_efficient_method(b_ex, new_e_ex, m_ex)

    end = time.time()
    resTime = (end - start) * (10**3)  # time in ms
    # Update counter after rern from square_and_multiply_algorithm method.
    counter_mod += result_arr[1][0]
    counter_multiplication += result_arr[1][1]
    counter_sqrt += result_arr[1][2]

    counter_all = [counter_mod, counter_multiplication,
                   counter_sqrt, counter_subtraction]
    n_operation = sum(counter_all)

    return result_arr[0], counter_all, n_operation, resTime


#################### Exponent Modular with Square and Multiply Algorithm #######################


def exponent_modular_with_square(b_sq_mul, e_sq_mul, m_sq_mul):
    # Create counter
    start = time.time()
    counter_mod = 0
    counter_multiplication = 0
    counter_sqrt = 0
    counter_subtraction = 0

    # Change from e -> (e mod (m-1))
    new_e_sq_mul = np.mod(e_sq_mul, (m_sq_mul - 1))
    new_e_ls.append(new_e_sq_mul)
    counter_subtraction += 1
    counter_mod += 1
    # print(f"new e value : {new_e_sq_mul}")
    result_arr = square_and_multiply_algorithm(
        b_sq_mul, new_e_sq_mul, m_sq_mul)

    end = time.time()
    # Update counter after return from square_and_multiply_algorithm method.
    counter_mod += result_arr[1][0]
    counter_multiplication += result_arr[1][1]
    counter_sqrt += result_arr[1][2]

    resTime = (end - start) * (10**3)  # time in ms
    counter_all = [counter_mod, counter_multiplication,
                   counter_sqrt, counter_subtraction]
    n_operation = sum(counter_all)

    return result_arr[0], counter_all, n_operation, resTime


# input type

w_type = int(input("what type of input: "))

# TODO : Latest Updated 3 / 12 / 66  change input and add method1 and method3 in graphs


################  TYPE 1 --> M = NOT PRIME & E > M #############
# 1.1
type1B = 14
type1E = [37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
          79, 83, 89, 97, 101, 103, 107, 109, 113, 127]
type1M = 22

# 1.2
type2B = 42
type2E = [83, 89, 97, 101, 103, 107, 109, 113, 127, 131,
          137, 139, 149, 151, 157, 163, 167, 173, 179, 181]
type2M = 76

# 1.3
type3B = 95
type3M = 144
type3E = [149, 151, 157, 163, 167, 173, 179, 181, 191,
          193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251]

# 1.4
type4B = 156
type4M = 322
type4E = [331, 337, 347, 349, 353, 359, 367,
          373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443]

# 1.5
type5B = 221
type5M = 566
type5E = [571, 577, 587, 593, 599, 601, 607, 613, 617,
          619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683]

# TODO : Latest Updated 3 / 12 / 66 use only type 2 method.
################  TYPE 2 --> M = NOT PRIME  #############
# 2.1
type6B = 31334
type6M = 200029
type6E = [202067, 202087, 218627, 221471,
          230999, 242773, 247249, 259517, 260527, 281249, 290597, 291509, 293827, 299771, 319591, 320041, 336689, 352483, 355573, 372121]
# type6E = np.arange(type6M, type6M + (20 * 100), 20)

# 2.2
type7B = 516
type7M = 5557
type7E = [5639, 6053, 6673, 7207, 7853, 8231, 8941, 9133, 9463, 10037,
          11161, 12781, 13553, 13963, 14591, 15061, 15823, 16883, 17449, 18587]
# type7E = np.arange(type7M, type7M + (414 * 100), 414)

# 2.3
type8B = 5112
type8M = 21599
type8E = [100003, 100019, 100043, 100049, 100057, 100069, 100103, 100109, 100129,
          100151, 100153, 100169, 100183, 100189, 100193, 100207, 100213, 100237, 100267, 100271]
# type8E = np.arange(type8M, type8M + (6 * 100), 6)

# 2.4
type9B = 94
type9M = 281
type9E = [409, 463, 541, 599, 607, 653, 661, 727, 739, 797,
          811, 859, 863, 877, 941, 1009, 1087, 1153, 1291, 1511]
# type9E = np.arange(type9M, type9M + (58 * 100), 58)

# 2.5
type10B = 6203
type10M = 72217
type10E = [500009, 500029, 500041, 500057, 500069, 500083, 500107, 500111, 500113,
           500119, 500153, 500167, 500173, 500177, 500179, 500197, 500209, 500231, 500233, 500237]


#####################################################################

inputB = [type1B, type2B, type3B, type4B, type5B,
          type6B, type7B, type8B, type9B, type10B]
inputM = [type1M, type2M, type3M, type4M, type5M,
          type6M, type7M, type8M, type9M, type10M]
inputE = [type1E, type2E, type3E, type4E, type5E,
          type6E, type7E, type8E, type9E, type10E]
# 2 4 5 6 7 9 10 --> Can't use data table
# 1 3 8 --> Useable  (5 is maybe useable)
resMemoryEffMethod = []
resSquareAndMulMethod = []
resExponentModularMethod = []
resExponentModularWithSquareMethod = []

timeMemoryEffMethod = []
timeSquareAndMulMethod = []
timeExponentModularMethod = []
timeExponentModularWithSquareMethod = []

n_loop = 100

############################################################
#  For calculating result
for i in range(len(type7E)):
    for j in range(n_loop):
        # resMemoryEffMethod.append(
        #     memory_efficient_method(inputB[w_type-1], inputE[w_type-1][i], inputM[w_type-1])[0])
        # resSquareAndMulMethod.append(
        #     square_and_multiply_algorithm(inputB[w_type-1], inputE[w_type-1][i], inputM[w_type-1])[0])
        # resExponentModularMethod.append(
        #     exponent_modular(inputB[w_type-1], inputE[w_type-1][i], inputM[w_type-1])[0])
        # resExponentModularWithSquareMethod.append(
        #     exponent_modular_with_square(inputB[w_type-1], inputE[w_type-1][i], inputM[w_type-1])[0])
        resMemoryEffMethod.append(
            memory_efficient_method(inputB[w_type-1], inputE[w_type-1][i], inputM[w_type-1])[3])
        resSquareAndMulMethod.append(
            square_and_multiply_algorithm(inputB[w_type-1], inputE[w_type-1][i], inputM[w_type-1])[3])
        resExponentModularMethod.append(
            exponent_modular(inputB[w_type-1], inputE[w_type-1][i], inputM[w_type-1])[3])
        resExponentModularWithSquareMethod.append(
            exponent_modular_with_square(inputB[w_type-1], inputE[w_type-1][i], inputM[w_type-1])[3])
    # print(f"avg of time Memory Eff : {timeMemoryEffMethod}")
    ############## time average to plotting graph ###############
    # timeMemoryEffMethod.append(sum(resMemoryEffMethod)/(n_loop))
    # timeSquareAndMulMethod.append(sum(resSquareAndMulMethod)/(n_loop))
    # timeExponentModularMethod.append(sum(resExponentModularMethod)/(n_loop))
    # timeExponentModularWithSquareMethod.append(sum(resExponentModularWithSquareMethod)/(n_loop))
    ############## time minimum to plotting graph ###############
    timeMemoryEffMethod.append(min(resMemoryEffMethod))
    timeSquareAndMulMethod.append(min(resSquareAndMulMethod))
    timeExponentModularMethod.append(min(resExponentModularMethod))
    timeExponentModularWithSquareMethod.append(
        min(resExponentModularWithSquareMethod))
    resMemoryEffMethod = []
    resSquareAndMulMethod = []
    resExponentModularMethod = []
    resExponentModularWithSquareMethod = []


x_e = inputE[w_type-1]
x_log = np.log(inputE[w_type-1])

t = inputE[w_type-1]

###########################################################

# Show c value
print("(Method: b | e | m |  --> time)")
for i in range(0, len(type7E)):
    print(
        f"Memory Efficient Method : {inputB[w_type-1]} | {inputE[w_type-1][i]} | {inputM[w_type-1]} |  --> {timeMemoryEffMethod[i]}")
    print(
        f"Sqrt And Mul Method : {inputB[w_type-1]} | {inputE[w_type-1][i]} | {inputM[w_type-1]} |  --> {timeSquareAndMulMethod[i]}")
    print(
        f"Expo Mod Method : {inputB[w_type-1]} | {inputE[w_type-1][i]} | {inputM[w_type-1]} |  --> {timeExponentModularMethod[i]}")
    print(
        f"Expo Mod W/ Sqrt : {inputB[w_type-1]} | {inputE[w_type-1][i]}  | {inputM[w_type-1]}| --> {timeExponentModularWithSquareMethod[i]}")


############################# PLOT ALL METHODS ##########################
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))
########################## PLOTTING E GRAPH ###########################
ax1.set_title(
    "All Methods", fontsize=10)
ax1.set_xlabel("e value", fontsize=10)

ax1.set_ylabel(
    f"Computation time in ms [ b = {inputB[w_type-1]} | m = {inputM[w_type-1]} ] ", fontsize=10)


ax1.plot(x_e, timeMemoryEffMethod, '--',
         color="red", label="Memory Efficient", marker="o")

# m, b = np.polyfit(x_e, timeMemoryEffMethod, 1)
# ax1.plot(x_e, m*x_e+b,
#          label="Memory Efficient Method", color="red")


ax1.plot(x_e, timeSquareAndMulMethod, ':',
         color="blue", label="Exponentiation by Squaring", marker="+")
# m, b = np.polyfit(x_e, timeSquareAndMulMethod, 1)
# ax1.plot(x_e, m*x_e+b,
#          label="Square And Multiply Algorithm", color="blue")


ax1.plot(x_e, timeExponentModularMethod, '-.',
         color="orange", label="Exponentiation And Modular", marker="d")
# m, b = np.polyfit(x_e, timeExponentModularMethod, 1)
# ax1.plot(x_e, m*x_e+b,
#          label="Exponential And Modular Method", color="orange")


ax1.plot(x_e, timeExponentModularWithSquareMethod,
         color="green", label="Modulo the exponent with Exponentiation by squaring", marker="x")
# m, b = np.polyfit(x_e, timeExponentModularWithSquareMethod, 1)
# ax1.plot(x_e, m*x_e+b,
#          label="Exponential And Modular With Square Method", color="green")


for i in range(0, len(t)):

    ax1.annotate(f"e = {x_e[i]}",
                 (x_e[i], timeMemoryEffMethod[i]), fontsize=7)

    ax1.annotate(f"e = {x_e[i]}", (x_e[i],
                 timeSquareAndMulMethod[i]), fontsize=7)

    ax1.annotate(f"e = {x_e[i]}",
                 (x_e[i], timeExponentModularMethod[i]), fontsize=7)

    ax1.annotate(f"e = {x_e[i]}", (x_e[i],
                 timeExponentModularWithSquareMethod[i]), fontsize=7)

# plt.yticks(np.arange(0, 10, 0.01))
ax1.grid()
ax1.legend(fontsize=10)

########################## PLOTTING LOG(E) GRAPH ###########################
ax2.set_xscale("log")
ax2.set_title(
    "All Methods", fontsize=10)
ax2.set_xlabel("ln(e) value", fontsize=10)

ax2.plot(x_log, timeMemoryEffMethod, '--',
         color="red", label="Memory Efficient", marker="o")
# m, b = np.polyfit(x_e, timeMemoryEffMethod, 1)
# ax2.plot(x_log, m*x_e+b,
#          label="Memory Efficient Method", color="red")

ax2.plot(x_log, timeSquareAndMulMethod, ':',
         color="blue", label="Exponentiation by Squaring", marker="+")
# m, b = np.polyfit(x_e, timeSquareAndMulMethod, 1)
# ax2.plot(x_log, m*x_e+b,
#          label="Square And Multiply Algorithm", color="blue")

ax2.plot(x_log, timeExponentModularMethod, '-.',
         color="orange", label="Exponentiation And Modular", marker="d")
# m, b = np.polyfit(x_e, timeExponentModularMethod, 1)
# ax2.plot(x_log, m*x_e+b,
#          label="Exponential And Modular Method", color="orange")

ax2.plot(x_log, timeExponentModularWithSquareMethod,
         color="green", label="Modulo the exponent with Exponentiation by squaring", marker="x")
# m, b = np.polyfit(x_e, timeExponentModularWithSquareMethod, 1)
# ax2.plot(x_log, m*x_e+b,
#          label="Exponential And Modular With Square Method", color="green")


# for i in range(0, len(t), 10):

#     ax2.annotate(f"log(e) = {round(x_log[i], 2)}",
#                  (x_log[i], timeMemoryEffMethod[i]), fontsize=7)

#     ax2.annotate(f"log(e) = {round(x_log[i], 2)}", (x_log[i],
#                  timeSquareAndMulMethod[i]), fontsize=7)

#     ax2.annotate(f"log(e) = {round(x_log[i], 2)}",
#                  (x_log[i], timeExponentModularMethod[i]), fontsize=7)

#     ax2.annotate(f"log(e) = {round(x_log[i], 2)}", (x_log[i],
#                  timeExponentModularWithSquareMethod[i]), fontsize=7)
ax2.legend(fontsize=10)
# plt.yticks(np.arange(0, timeMemoryEffMethod[-1], timeMemoryEffMethod[-1]/10))
# plt.ylim(0, timeMemoryEffMethod[0])
ax2.grid()


############################# PLOT ONLY METHOD 2 AND 4 ##########################
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))
########################## PLOTTING E GRAPH ###########################
ax1.set_title(
    "Exponentiation by Squaring Method and \n Modulo the exponent with Exponentiation by squaring Method", fontsize=10)
ax1.set_xlabel("e value", fontsize=10)

ax1.set_ylabel(
    f"Computation time in ms [ b = {inputB[w_type-1]} | m = {inputM[w_type-1]} ] ", fontsize=10)

ax1.plot(x_e, timeSquareAndMulMethod, ':',
         color="blue", label="Exponentiation by Squaring", marker="+")
# m, b = np.polyfit(x_e, timeSquareAndMulMethod, 1)
# ax1.plot(x_e, m*x_e+b,
#          label="Square And Multiply Algorithm", color="orange")

ax1.plot(x_e, timeExponentModularWithSquareMethod,
         color="green", label="Modulo the exponent with Exponentiation by squaring", marker="x")
# m, b = np.polyfit(x_e, timeExponentModularWithSquareMethod, 1)
# ax1.plot(x_e, m*x_e+b,
#          label="Exponential And Modular With Square Method", color="green")


for i in range(0, len(t)):
    ax1.annotate(f"e = {x_e[i]}",
                 (x_e[i], timeSquareAndMulMethod[i]), fontsize=7)
    ax1.annotate(f"e = {x_e[i]}", (x_e[i],
                 timeExponentModularWithSquareMethod[i]), fontsize=7)
ax1.grid()
ax1.legend(fontsize=10)

########################## PLOTTING LOG(E) GRAPH ###########################
ax2.set_xscale("log")
ax2.set_title(
    "Exponentiation by Squaring Method and \n Modulo the exponent with Exponentiation by squaring Method", fontsize=10)
ax2.set_xlabel("ln(e) value", fontsize=10)
ax2.plot(x_log, timeSquareAndMulMethod, ':',
         color="blue", label="Exponentiation by Squaring", marker="+")
# m, b = np.polyfit(x_e, timeSquareAndMulMethod, 1)
# ax2.plot(x_log, m*x_e+b,
#          label="Square And Multiply Algorithm", color="orange")

ax2.plot(x_log, timeExponentModularWithSquareMethod,
         color="green", label="Modulo the exponent with Exponentiation by squaring", marker="x")
# m, b = np.polyfit(x_e, timeExponentModularWithSquareMethod, 1)
# ax2.plot(x_log, m*x_e+b,
#          label="Exponential And Modular With Square Method", color="green")


# for i in range(0, len(t), 10):
#     ax2.annotate(f"log(e) = {round(x_log[i], 2)}",
#                  (x_log[i], timeSquareAndMulMethod[i]), fontsize=7)
#     ax2.annotate(f"log(e) = {round(x_log[i], 2)}", (x_log[i],
#                  timeExponentModularWithSquareMethod[i]), fontsize=7)
ax2.grid()
ax2.legend(fontsize=10)

# plt.legend(fontsize=15)
# plt.yticks(np.arange(0, timeSquareAndMulMethod[-1], timeSquareAndMulMethod[-1]/100))


# ############# TODO: Plot the data graph ####################
# columns = ('Square and Multiply Algorithm',
#            'Exponential And Modular With Square Method')
# rows = [f'e = {(inputE[w_type-1])[i]}' for i in (range(len(inputE[w_type-1])))]

# # Data for the table
# data = [
#     ['', columns[0], columns[1]],
#     [rows[0], f"{resMemoryEffMethod[0]:.4f}", f"{resSquareAndMulMethod[0]:.4f}",
#         f"{resExponentModularMethod[0]:.4f}", f"{resExponentModularWithSquareMethod[0]:.4f}"],
#     [rows[1], f"{resMemoryEffMethod[1]:.4f}", f"{resSquareAndMulMethod[1]:.4f}",
#         f"{resExponentModularMethod[1]:.4f}", f"{resExponentModularWithSquareMethod[1]:.4f}"],
#     [rows[2], f"{resMemoryEffMethod[2]:.4f}", f"{resSquareAndMulMethod[2]:.4f}",
#         f"{resExponentModularMethod[2]:.4f}", f"{resExponentModularWithSquareMethod[2]:.4f}"],
#     [rows[3], f"{resMemoryEffMethod[3]:.4f}", f"{resSquareAndMulMethod[3]:.4f}",
#         f"{resExponentModularMethod[3]:.4f}", f"{resExponentModularWithSquareMethod[3]:.4f}"],
#     [rows[4], f"{resMemoryEffMethod[4]:.4f}", f"{resSquareAndMulMethod[4]:.4f}",
#         f"{resExponentModularMethod[4]:.4f}", f"{resExponentModularWithSquareMethod[4]:.4f}"],
#     [rows[5], f"{resMemoryEffMethod[5]:.4f}", f"{resSquareAndMulMethod[5]:.4f}",
#         f"{resExponentModularMethod[5]:.4f}", f"{resExponentModularWithSquareMethod[5]:.4f}"],
#     [rows[6], f"{resMemoryEffMethod[6]:.4f}", f"{resSquareAndMulMethod[6]:.4f}",
#         f"{resExponentModularMethod[6]:.4f}", f"{resExponentModularWithSquareMethod[6]:.4f}"],
#     [rows[7], f"{resMemoryEffMethod[7]:.4f}", f"{resSquareAndMulMethod[7]:.4f}",
#         f"{resExponentModularMethod[7]:.4f}", f"{resExponentModularWithSquareMethod[7]:.4f}"],
#     [rows[8], f"{resMemoryEffMethod[8]:.4f}", f"{resSquareAndMulMethod[8]:.4f}",
#         f"{resExponentModularMethod[8]:.4f}", f"{resExponentModularWithSquareMethod[8]:.4f}"],
#     [rows[9], f"{resMemoryEffMethod[9]:.4f}", f"{resSquareAndMulMethod[9]:.4f}",
#         f"{resExponentModularMethod[9]:.4f}", f"{resExponentModularWithSquareMethod[9]:.4f}"],

# ]


# # Create a figure and axis
# fig, ax = plt.subplots()

# # Create a table
# table = ax.table(cellText=data, loc='center', cellLoc='center')

# # Style the table
# table.auto_set_font_size(False)
# table.set_fontsize(11)
# table.scale(1, 1.5)  # Adjust the table size
# ax.set_title(f"Computataion time in ms | Input type = {w_type}.")

# # Remove axis labels and ticks
# ax.axis('off')

# # Display the table
plt.show()
