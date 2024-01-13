while True:
    Volume = input("Target Volume 값을 입력하세요(ml): ")
    Time = input("Dispensing Time 값을 입력하세요(sec): ")
    Viscosity = input("Viscosity 값을 입력하세요(mPa,cp): ")
    size = input("Hose size(inner) 값을 입력하세요(cm): ")
    length = input("Hose length 값을 입력하세요(m): ")

    try:
        # 사용자로부터 입력받은 값을 float으로 변환
        Volume_F = float(Volume)
        Time_F = float(Time)
        Viscosity_F = float(Viscosity)
        size_F = float(size)
        length_F = float(length)

        # 모든 입력이 정상적으로 이루어지면 무한 루프 종료
        break

    except ValueError:
        print("올바른 숫자를 입력하세요. 다시 시도해주세요.")

Flowrate = Volume_F / Time_F

flow = Flowrate / (3.14 / 4 * size_F**2)
ForceFeeding = Viscosity_F / 1000 * 3.14 * length_F * 2 * flow / 100
PressureFeeding = ForceFeeding / (3.14 / 4 * size_F**2)

print("Velocity of flow (V) : ",round(flow,3)," (cm/sec)")
print("Force of feeding (Ft) : ", round(ForceFeeding,3), " (kg)")
print("Pressure of feeding (Pt) : ", round(PressureFeeding,3), " (bar)")

