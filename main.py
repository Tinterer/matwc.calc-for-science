print('Добро пожаловать в калькулятор')

n1 = str(input('Напишите какими функциями хотите воспользоваться: арифметические вычисления/вычисления по формулам'))

if n1 == 'арифметические вычисления':
    change1 = str(input('Напишите ниже цифру арифметического действия, которое хотите выполнить:\n 1 - сложение \n 2 - вычитание \n 3 - умножение \n 4 - деление \n 5 - возведение в степень \n 6 - Вычисление корня степени'))

    if change1 == '1':
        print('Функция сложения')
        a = int(input('Введите первую переменную'))
        b = int(input('Введите вторую переменную'))
        print(a + b)

    if change1 == '2':
        print('Функция вычитания')
        a = int(input('Введите первую переменную'))
        b = int(input('Введите вторую переменную'))
        print(a - b)

    if change1 == '3':
        print('Функция умножения')
        a = int(input('Введите первую переменную'))
        b = int(input('Введите вторую переменную'))
        print(a * b)

    if change1 == '4':
        print('функция деления')
        a = int(input('Введите первую переменную'))
        b = int(input('Введите вторую переменную')) 
        print(a / b)

    if change1 == '5':
        print('Возведение в степень')
        a = int(input('Введите число'))
        i = int(input('Введите степень, в которую необходимо возвести число'))
        print(a ** i)  

    if change1 == '6':
        print('Вычислеие корня')
        a = int(input('Введите число'))
        i = int(input('Введите степень корня'))
        isqrt = 1 / i
        print(a ** isqrt)    

if n1 == 'вычисления по формулам':
    change2 = str(input('Введите один из доступных разделов: механика/электричество/термодинамика/перевод единиц'))

    if change2 == 'механика':
        mech1 = str(input('Выберите нужный раздел механики: 1 - кинематика \n 2 - динамика'))

        if mech1 == '1':
            d = str(input('выберите какое движение совершалось: 1 - равноускоренное \n 2 - равномерное'))

            if d == '1':
                mech2 = str(input('Из перечисленных величин выберите неизвестную величину: ускорение, время, начальная скорость, конечная скорость'))

                if mech2 == 'конечная скорость':
                    print('В случае, если какая-то величина неизвестна, то введите 0')
                    velocity = int(input('Введите начальную скорость: '))
                    square = int(input('Введите расстояние: '))
                    time = int(input('Введите время, за которое было совершено движение: '))
                    acceler = int(input('Введите ускорение(в случае свободного падения введите g): '))
                    at = acceler * time

                    if at > 0:
                        print(velocity + at)
                        print(' В данном случае используется формула нахождения скорости: Vк = V0 + at')

                    if acceler == 0:
                        s = 2 * square #это удвоенное расстояние
                        v0t = 2 * velocity * time #это удвоенное произведение начальной скорости и времени
                        t2 = time ** 2
                        differance = s - v0t

                        print( differance / t2)

                    if time == 0:
                        s = 2 * square
                        v0 = -2 * velocity
                        v02 = v0 ** 2
                        ass = 8 * acceler * square
                        summ = v02 + ass
                        sqrtsumm = summ ** 0.5
                        
                        t = v02 + sqrtsumm

                        v0t = v0 * t
                        at2 = a * t ** 2
                        at22 = at2 / 2

                        print(v0t + at22)

                if mech2 == 'расстояние':
                    print('В случае, если какая-то величина неизвестна, введите 0')
                    velocity = int(input('Введите начальную скорость'))
                    velocityend = int(input('Введите конечную скорость'))
                    time = int(input('Введите время, за которое было преодолено расстояние'))
                    acceler = int(input('Введите ускорениеЮ с которым двигалось тело'))

                    x = acceler * velocity * velocityend * time

                    if x != 0:
                        v0t = velocity * time
                        axt2 = acceler * time ** 2
                        axt22 = axt2 / 2
                        print(v0t + axt22)

                    if velocity == 0:
                        if velocityend == 0:
                            t = time ** 2
                            print(acceler * t / 2)

                        if velocityend > 0:
                            vet = velocityend * time
                            axt2 = acceler * time ** 2
                            axt22 = axt2 / 2
                            print(vet - axt22)

                    if time == 0:
                        v2 = velocityend ** 2
                        v02 = velocity ** 2
                        a2 = acceler * 2
                        v22 = v2 - v02
                        print(v22 / a2)

                    if acceler == 0:
                        v0v = velocity + velocityend
                        v0v2 = v0v / 2
                        print(v0v2 * 2)

                if mech2 == 'время':
                    print('Если величина неизвестна, то введите 0')
                    square = int(input('Введите расстояние, пройденное за этот промежуток времени'))
                    velocity = int(input('Введите начальную скорость'))
                    velocityend = int(input('Введите конечную скорость'))
                    acceler = float(input('Введите ускорение'))

                    x = acceler * velocityend * velocity * square

                    if x != 0:
                        v02 = velocity ** 2
                        s2 = 2 * square
                        z = -velocity + v02 + s2
                        print(z / acceler)

                        

<html>
    <head>
        <link rel="stylesheet" href="style.css">
        <meta charset="utf-8">
        <meta name="author" content="Матвей Теслов">
        <meta name="description" content="Калькулятор Матвея">
        <title>clc.m2</title>
    </head>
    <body>

        <header>
            <h1>calculatorm</h1>
        </header>

        <ul id='ulhornavbar'><span>
            <li id="lihornavbar" class="active"><a href="index.html" title="Главная страница">Главная</a></li>
            <li id="lihornavbar"><a href="maths/index.html" title="Раздел математики">Математика</a></li>
            <li id="lihornavbar"><a href="physics/index.html" title="Раздел физики">Физика</a></li>
            <li id="lihornavbar"><a href="utilits/index.html" title="Раздел Польши">Другое</a></li>
        </ul></span>

        <main>
            <article>
                <header id="lastnews">
                    <h3>
                        Последние новости о калькуляторе CLC m2
                    </h3>
                </header>
                <p>
                    &nbsp;&nbsp;&nbsp;&nbsp;
                </p>
            </article>

        </main>

        <div id="footer">
            clc.m2.v2.1
        </div>

    </body>
</html>                        