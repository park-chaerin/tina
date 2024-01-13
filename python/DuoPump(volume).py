#PRO DUO PUMP SPEED CALCULATION

while True:

    amount = input("Target Amount 값을 입력하세요(ml): ")
    time = input("Dispensing Time 값을 입력하세요(sec): ")
    print("----Resin----")
    viscosity = input("Viscosity 값을 입력하세요(mPa,cp): ")
    density = input("Density 값을 입력하세요(cm): ")
    ratio = input("Mixing Ratio 값을 입력하세요(Volume): ")
    print("----Hardner----")
    viscosity2 = input("Viscosity 값을 입력하세요(mPa,cp): ")
    density2 = input("Density 값을 입력하세요(cm): ")
    ratio2 = input("Mixing Ratio 값을 입력하세요(Volume): ")

    try:
        # 사용자로부터 입력받은 값을 float으로 변환
        amountF = float(amount)
        timeF = float(time)
        viscosityF = float(viscosity)
        densityF = float(density)
        ratioF = float(ratio)

        viscosityF2 = float(viscosity2)
        densityF2 = float(density2)
        ratioF2 = float(ratio2)

        # 모든 입력이 정상적으로 이루어지면 무한 루프 종료
        break

    except ValueError:
        print("올바른 숫자를 입력하세요. 다시 시도해주세요.")

Flowrate = amountF / timeF

DosingAmount = amountF * ratioF / (ratioF + ratioF2)
DosingAmount2 = amountF * ratioF2 / (ratioF + ratioF2)
