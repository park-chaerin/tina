while True:
    print("----Resin----")
    Volume = input("Target Volume 값을 입력하세요(ml): ")
    Time = input("Dispensing Time 값을 입력하세요(sec): ")
    Viscosity = input("Viscosity 값을 입력하세요(mPa,cp): ")
    size = input("Hose size(inner) 값을 입력하세요(cm): ")
    length = input("Hose length 값을 입력하세요(m): ")

    print("----Hardener----")
    Volume2 = input("Target Volume 값을 입력하세요(ml): ")
    Time2 = input("Dispensing Time 값을 입력하세요(sec): ")
    Viscosity2 = input("Viscosity 값을 입력하세요(mPa,cp): ")
    size2 = input("Hose size(inner) 값을 입력하세요(cm): ")
    length2 = input("Hose length 값을 입력하세요(m): ")

    try:
        # 사용자로부터 입력받은 값을 float으로 변환
        Volume_F = float(Volume)
        Time_F = float(Time)
        Viscosity_F = float(Viscosity)
        size_F = float(size)
        length_F = float(length)

        Volume_F2 = float(Volume2)
        Time_F2 = float(Time2)
        Viscosity_F2 = float(Viscosity2)
        size_F2 = float(size2)
        length_F2 = float(length2)

        # 모든 입력이 정상적으로 이루어지면 무한 루프 종료
        break

    except ValueError:
        print("올바른 숫자를 입력하세요. 다시 시도해주세요.")

Flowrate = Volume_F / Time_F
Flowrate2 = Volume_F2 / Time_F2

flow = Flowrate / (3.14 / 4 * size_F**2)
ForceFeeding = Viscosity_F / 1000 * 3.14 * length_F * 2 * flow / 100
PressureFeeding = ForceFeeding / (3.14 / 4 * size_F**2)

flow2 = Flowrate2 / (3.14 / 4 * size_F2**2)
ForceFeeding2 = Viscosity_F2 / 1000 * 3.14 * length_F2 * 2 * flow2 / 100
PressureFeeding2 = ForceFeeding2 / (3.14 / 4 * size_F2**2)

print("-----Resin-----")
print("Velocity of flow (V) : ",round(flow,3)," (cm/sec)")
print("Force of feeding (Ft) : ", round(ForceFeeding,3), " (kg)")
print("Pressure of feeding (Pt) : ", round(PressureFeeding,3), " (bar)")
print()
print("-----Hardener-----")
print("Velocity of flow (V) : ",round(flow2,3)," (cm/sec)")
print("Force of feeding (Ft) : ", round(ForceFeeding2,3), " (kg)")
print("Pressure of feeding (Pt) : ", round(PressureFeeding2,3), " (bar)")