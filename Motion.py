from tkinter import *
import time
import numpy as np
import matplotlib.pyplot as plt


# animate - принимает номер режима 1 или 2. А также скорость анимации
# move принимает режим и время задержки
# конструктор класса Regime по умолчанию принимает позиции 0 и 111 градусов, но можно задать и свои

def animate(regime: int, speed: float):
    tk = Tk()
    if regime == 1:
        for x in np.arange(0, 111 + speed * 0.0140625, speed * 0.0140625):
            canvas = Canvas(tk, width=800, height=700)
            canvas.pack()

            canvas.create_polygon(300, 500, 300 + 92 * np.cos(x * np.pi / 180), 500 - 92 * np.sin(x * np.pi / 180),
                                  outline="black", width=10)
            canvas.create_polygon(300 + 92 * np.cos(x * np.pi / 180), 500 - 92 * np.sin(x * np.pi / 180),
                                  300 + 2 * 92 * np.cos(x * np.pi / 180), 500
                                  , outline="black", width=10)
            canvas.create_polygon(300 + 2 * 92 * np.cos(x * np.pi / 180), 500,
                                  300 + 2 * 92 * np.cos(x * np.pi / 180) + 205, 500,
                                  outline="black", width=10)
            canvas.create_oval(300 + 2 * 92 * np.cos(x * np.pi / 180) + 105, 400,
                               300 + 2 * 92 * np.cos(x * np.pi / 180) + 305, 600, width=2, fill="gray")

            if x >= 111:
                canvas.update()
                canvas.destroy()
                for i in np.arange(0, 90 + 0.0140625 * 20, 20 * 0.0140625):
                    canvas = Canvas(tk, width=800, height=700)
                    canvas.pack()

                    canvas.create_polygon(300, 500, 300 + 92 * np.cos((111 + i) * np.pi / 180),
                                          500 - 92 * np.sin((111 + i) * np.pi / 180),
                                          outline="black", width=10)
                    canvas.create_polygon(300 + 92 * np.cos((111 + i) * np.pi / 180),
                                          500 - 92 * np.sin((i + 111) * np.pi / 180),
                                          300 - 77 * np.sqrt(2 * (1 - np.cos(42))) * np.cos(i * np.pi / 180) / 2,
                                          500 + 92 * np.sqrt(2 * (1 - np.cos(42)))
                                          * np.sin(i * np.pi / 180) / 2
                                          , outline="black", width=10)
                    canvas.create_polygon(300 - 77 * np.sqrt(2 * (1 - np.cos(42))) * np.cos(i * np.pi / 180) / 2,
                                          500 + 92 * np.sqrt(2 * (1 - np.cos(42)))
                                          * np.sin(i * np.pi / 180) / 2,
                                          300 - 92 * np.sqrt(2 * (1 - np.cos(42))) * np.cos(
                                              i * np.pi / 180) / 2 + 205 * np.cos(
                                              i * np.pi / 180),
                                          500 + 42 * np.sqrt(2 * (1 - np.cos(42)))
                                          * np.sin(i * np.pi / 180) / 2 - 92 * np.sqrt(2 * (1 - np.cos(42))) *
                                          np.sin(i * np.pi / 180),
                                          outline="black", width=10)
                    canvas.create_oval(
                        300 - 82 * np.sqrt(2 * (1 - np.cos(42))) * np.cos(i * np.pi / 180) / 2 + 205 * np.cos(
                            i * np.pi / 180) - 100,
                        500 + 92 * np.sqrt(2 * (1 - np.cos(42)))
                        * np.sin(i * np.pi / 180) / 2 - 130 * np.sqrt(2 * (1 - np.cos(42))) * np.sin(
                            i * np.pi / 180) - 100,
                        300 - 92 * np.sqrt(2 * (1 - np.cos(42))) * np.cos(i * np.pi / 180) / 2 + 205 * np.cos(
                            i * np.pi / 180) + 100,
                        500 + 92 * np.sqrt(2 * (1 - np.cos(42)))
                        * np.sin(i * np.pi / 180) / 2 - 130 * np.sqrt(2 * (1 - np.cos(42))) * np.sin(
                            i * np.pi / 180) + 100, width=2, fill="gray")

                    canvas.update()
                    canvas.destroy()
                    # time.sleep(dt)
                    if i >= 90:
                        for j in np.arange(111, -speed * 0.0140625, -speed * 0.0140625):
                            canvas = Canvas(tk, width=800, height=700)
                            canvas.pack()
                            canvas.create_polygon(300, 490, 300 - 92 * np.sin(j * np.pi / 180),
                                                  500 - 92 * np.cos(j * np.pi / 180),
                                                  outline="black", width=10)
                            canvas.create_polygon(300 - 92 * np.sin(j * np.pi / 180),
                                                  500 - 92 * np.cos(j * np.pi / 180),
                                                  300, 500 - 2 * 92 * np.cos((j) * np.pi / 180),
                                                  outline="black", width=10)
                            canvas.create_polygon(300, 500 - 2 * 92 * np.cos((j) * np.pi / 180),
                                                  300, 500 - 2 * 92 * np.cos((j) * np.pi / 180) - 205,
                                                  outline="black", width=10)

                            canvas.create_oval(200, 500 - 2 * 92 * np.cos((j) * np.pi / 180) - 110,
                                               400, 500 - 2 * 92 * np.cos((j) * np.pi / 180) - 205 - 110, width=2,
                                               fill="gray")

                            canvas.update()
                            canvas.destroy()
                            time.sleep(0)

            canvas.update()
            canvas.destroy()
            time.sleep(0)

    elif regime == 2:
        for j in np.arange(0, 111 + speed * 0.0140625, speed * 0.0140625):
            canvas = Canvas(tk, width=800, height=700)
            canvas.pack()
            canvas.create_polygon(300, 490, 300 - 92 * np.sin(j * np.pi / 180),
                                  500 - 92 * np.cos(j * np.pi / 180),
                                  outline="black", width=10)
            canvas.create_polygon(300 - 92 * np.sin(j * np.pi / 180),
                                  500 - 92 * np.cos(j * np.pi / 180),
                                  300, 500 - 2 * 92 * np.cos((j) * np.pi / 180),
                                  outline="black", width=10)
            canvas.create_polygon(300, 500 - 2 * 92 * np.cos((j) * np.pi / 180),
                                  300, 500 - 2 * 92 * np.cos((j) * np.pi / 180) - 205,
                                  outline="black", width=10)

            canvas.create_oval(200, 500 - 2 * 92 * np.cos((j) * np.pi / 180) - 110,
                               400, 500 - 2 * 92 * np.cos((j) * np.pi / 180) - 205 - 110, width=2,
                               fill="gray")

            canvas.update()
            canvas.destroy()
            time.sleep(0)

            if j >= 111:
                canvas.update()
                canvas.destroy()
                for i in np.arange(90, - 0.0140625 * speed, -speed * 0.0140625):
                    canvas = Canvas(tk, width=800, height=700)
                    canvas.pack()

                    canvas.create_polygon(300, 500, 300 + 92 * np.cos((111 + i) * np.pi / 180),
                                          500 - 92 * np.sin((111 + i) * np.pi / 180),
                                          outline="black", width=10)
                    canvas.create_polygon(300 + 92 * np.cos((111 + i) * np.pi / 180),
                                          500 - 92 * np.sin((i + 111) * np.pi / 180),
                                          300 - 77 * np.sqrt(2 * (1 - np.cos(42))) * np.cos(i * np.pi / 180) / 2,
                                          500 + 92 * np.sqrt(2 * (1 - np.cos(42)))
                                          * np.sin(i * np.pi / 180) / 2
                                          , outline="black", width=10)
                    canvas.create_polygon(300 - 77 * np.sqrt(2 * (1 - np.cos(42))) * np.cos(i * np.pi / 180) / 2,
                                          500 + 92 * np.sqrt(2 * (1 - np.cos(42)))
                                          * np.sin(i * np.pi / 180) / 2,
                                          300 - 92 * np.sqrt(2 * (1 - np.cos(42))) * np.cos(
                                              i * np.pi / 180) / 2 + 205 * np.cos(
                                              i * np.pi / 180),
                                          500 + 42 * np.sqrt(2 * (1 - np.cos(42)))
                                          * np.sin(i * np.pi / 180) / 2 - 92 * np.sqrt(2 * (1 - np.cos(42))) *
                                          np.sin(i * np.pi / 180),
                                          outline="black", width=10)
                    canvas.create_oval(
                        300 - 82 * np.sqrt(2 * (1 - np.cos(42))) * np.cos(i * np.pi / 180) / 2 + 205 * np.cos(
                            i * np.pi / 180) - 100,
                        500 + 92 * np.sqrt(2 * (1 - np.cos(42)))
                        * np.sin(i * np.pi / 180) / 2 - 130 * np.sqrt(2 * (1 - np.cos(42))) * np.sin(
                            i * np.pi / 180) - 100,
                        300 - 92 * np.sqrt(2 * (1 - np.cos(42))) * np.cos(i * np.pi / 180) / 2 + 205 * np.cos(
                            i * np.pi / 180) + 100,
                        500 + 92 * np.sqrt(2 * (1 - np.cos(42)))
                        * np.sin(i * np.pi / 180) / 2 - 130 * np.sqrt(2 * (1 - np.cos(42))) * np.sin(
                            i * np.pi / 180) + 100, width=2, fill="gray")

                    canvas.update()
                    canvas.destroy()
                    # time.sleep(dt)

                    if i <= 0:
                        for x in np.arange(111, -speed * 0.0140625, -speed * 0.0140625):
                            canvas = Canvas(tk, width=800, height=700)
                            canvas.pack()

                            canvas.create_polygon(300, 500, 300 + 92 * np.cos(x * np.pi / 180),
                                                  500 - 92 * np.sin(x * np.pi / 180),
                                                  outline="black", width=10)
                            canvas.create_polygon(300 + 92 * np.cos(x * np.pi / 180),
                                                  500 - 92 * np.sin(x * np.pi / 180),
                                                  300 + 2 * 92 * np.cos(x * np.pi / 180), 500
                                                  , outline="black", width=10)
                            canvas.create_polygon(300 + 2 * 92 * np.cos(x * np.pi / 180), 500,
                                                  300 + 2 * 92 * np.cos(x * np.pi / 180) + 205, 500,
                                                  outline="black", width=10)
                            canvas.create_oval(300 + 2 * 92 * np.cos(x * np.pi / 180) + 105, 400,
                                               300 + 2 * 92 * np.cos(x * np.pi / 180) + 305, 600, width=2, fill="gray")
                            canvas.update()
                            canvas.destroy()
                            time.sleep(0)


class Regime:
    # принимает начальные положения
    def __init__(self, start_pos=0., final_pos=111.):
        self.start_pos = start_pos
        self.final_pos = final_pos
        # Режим 1.
        # движение 1 (начальное + конечное)
        self.step1_m1_r1 = [angle for angle in np.arange(start_pos * np.pi / 180, final_pos * np.pi / 180 +
                                                         2 * np.pi / 25600, 2 * np.pi / 25600)]
        self.step1_m2_r1 = [-2 * angle for angle in np.arange(start_pos * np.pi / 180, final_pos * np.pi / 180 +
                                                              2 * np.pi / 25600, 2 * np.pi / 25600)]
        self.step1_m3_r1 = [angle for angle in np.arange(start_pos * np.pi / 180, final_pos * np.pi / 180 +
                                                         2 * np.pi / 25600, 2 * np.pi / 25600)]
        # движение 2 (текущее + 90)
        self.step2_m1_r1 = [angle for angle in np.arange(final_pos * np.pi / 180, final_pos * np.pi / 180 +
                                                         np.pi / 2 + 2 * np.pi / 25600, 2 * np.pi / 25600)]
        # движение 3 (m1 = текущее - конечное) (m2,m3 = их текущее - конечное)
        self.step3_m1_r1 = [angle for angle in np.arange(final_pos * np.pi / 180 + np.pi / 2,
                                                         np.pi / 2 - 2 * np.pi / 25600, -2 * np.pi / 25600)]
        self.step3_m2_r1 = [2 * angle for angle in np.arange(final_pos * np.pi / 180,
                                                             start_pos * np.pi / 180 - 2 * np.pi / 25600,
                                                             -2 * np.pi / 25600)]
        self.step3_m3_r1 = [angle for angle in
                            np.arange(final_pos * np.pi / 180,
                                      start_pos * np.pi / 180 - 2 * np.pi / 25600, -2 * np.pi / 25600)]
        # Режим 2. Движения такие же, кроме 1-го
        # Из положения 90 в положение 90 + конечное
        self.step1_m1_r2 = [angle for angle in np.arange(np.pi / 2, np.pi / 2 + final_pos * np.pi / 180 +
                                                         2 * np.pi / 25600, 2 * np.pi / 25600)]
        # Поворот на 90 по часовой
        self.step2_m1_r2 = [angle for angle in
                            np.arange(np.pi / 2 + final_pos * np.pi / 180, final_pos * np.pi / 180 - 2 * np.pi / 25600,
                                      -2 * np.pi / 25600)]
        # Возврат в начальное
        self.step3_m1_r2 = [angle for angle in np.arange(final_pos * np.pi / 180, start_pos * np.pi / 180 -
                                                          2 * np.pi / 25600, -2 * np.pi / 25600)]
        self.m1 = start_pos * np.pi / 180
        self.m2 = start_pos * np.pi / 180
        self.m3 = start_pos * np.pi / 180

    # режим 1 - выдвижение и подача на конвейер
    def regime1(self, dt: float):
        print("Regime 1")
        # движение 1
        for i in range(len(self.step1_m1_r1)):
            print("Motor1_step1: " + str(self.step1_m1_r1[i]))
            time.sleep(dt)
            print("Motor2_step1: " + str(self.step1_m2_r1[i]))
            time.sleep(dt)
            print("Motor3_step1: " + str(self.step1_m3_r1[i]))
            time.sleep(dt)
        # движение 2
        for i in range(len(self.step2_m1_r1)):
            print("Motor1_step2: " + str(self.step2_m1_r1[i]))
            time.sleep(dt)
        # движение 3
        for i in range(len(self.step3_m1_r1)):
            print("Motor1_step3: " + str(self.step3_m1_r1[i]))
            time.sleep(dt)
            print("Motor2_step3: " + str(self.step3_m2_r1[i]))
            time.sleep(dt)
            print("Motor3_step3: " + str(self.step3_m3_r1[i]))
            time.sleep(dt)

    # режим 2 - подача из конфейера в установку
    def regime2(self, dt: float):
        print("Regime 2")
        # движение 1
        for i in range(len(self.step1_m1_r1)):
            print("Motor1_step1: " + str(self.step1_m1_r2[i]))
            time.sleep(dt)
            print("Motor2_step1: " + str(self.step1_m2_r1[i]))
            time.sleep(dt)
            print("Motor3_step1: " + str(self.step1_m3_r1[i]))
            time.sleep(dt)
        # движение 2
        for i in range(len(self.step2_m1_r2)):
            print("Motor1_step2: " + str(self.step2_m1_r2[i]))
            time.sleep(dt)
        # движение 3
        for i in range(len(self.step3_m1_r2)):
            print("Motor1_step3: " + str(self.step3_m1_r2[i]))
            time.sleep(dt)
            print("Motor2_step3: " + str(self.step3_m2_r1[i]))
            time.sleep(dt)
            print("Motor3_step3: " + str(self.step3_m3_r1[i]))
            time.sleep(dt)

    # flag - срабатывает, когда достигает нулевого уровня все моторы
    def reset(self, dt: float):
        flag = True
        flag1 = True    # flag положения нуля первого моторчика
        flag2 = True    # flag положения нуля второго моторчика
        flag3 = True    # flag положения нуля тертьего моторчика
        while flag:
            if flag1:
                self.m1 += -angle
                # проверка на нулевое положение => flag1 = False
                time.sleep(dt)
            if flag2:
                self.m2 += 2 * angle
                # проверка на нулевое положение => flag2 = False
                time.sleep(dt)
            if flag3:
                self.m3 += - angle
                # проверка на нулевое положение => flag3 = False
                time.sleep(dt)
            if not flag1 and not flag2 and not flag3:
                flag = False


def move(regime: int, dt: float):
    # режим 1
    if regime == 1:
        try:
            Regime().regime1(dt)
            animate(1, 30)
        except Exception:
            return False
        return True

    # режим 2
    if regime == 2:
        try:
            Regime().regime2(dt)
            animate(2, 30)
        except Exception:
            return False
        return True


print(move(int(input("Input regime (1,2):")), 0))
